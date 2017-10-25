import inspect

import pytest
from async_v20 import endpoints
from async_v20 import interface
from async_v20.client import OandaClient
from async_v20.definitions.types import Account
from async_v20.definitions.types import AccountID
from async_v20.definitions.types import InstrumentName
from async_v20.definitions.types import StopLossOrderRequest
from async_v20.definitions.types import TradeSpecifier
from async_v20.definitions.types import TransactionID
from async_v20.endpoints import POSTOrders
from async_v20.endpoints.annotations import Instruments, LastTransactionID
from async_v20.interface.helpers import _arguments
from async_v20.interface.helpers import _create_request_params
from async_v20.interface.helpers import create_annotation_lookup
from async_v20.interface.helpers import create_body
from async_v20.interface.helpers import make_args_optional
from hypothesis.strategies import text, sampled_from

from .helpers import order_dict
from ..data.json_data import GETAccountID_response

client_attrs = [getattr(OandaClient, attr) for attr in dir(OandaClient)]
client_methods = list(filter(lambda x: hasattr(x, 'endpoint'), client_attrs))


@pytest.fixture
def stop_loss_order():
    order = StopLossOrderRequest(trade_id=1234, price=0.8)
    yield order
    del order


@pytest.fixture
def client():
    client = OandaClient(token='test_token', rest_host=None, stream_host=None)
    client.default_parameters.update({AccountID: 123456789,
                                      # Instruments: 'AUD_USD,EUR_USD',
                                      # InstrumentName: 'AUD_USD',
                                      LastTransactionID: 0,
                                      # TradeSpecifier: '@test_trade_specifier',
                                      TransactionID: 0
                                      })
    yield client
    del client


@pytest.mark.parametrize('method', client_methods)
def test_make_args_optional(method):
    """Ensure that all arguments passed to endpoint's are optional
    """
    result = make_args_optional(inspect.signature(method))

    def check_valid_param(param):
        if param.default != inspect._empty:
            return True
        else:
            print(param)

    assert all(map(check_valid_param, result.parameters.values()))


text_gen = text()
client_signatures = [inspect.signature(method) for method in client_methods]


def bound_args(sig):
    args = [text_gen.example() for _ in range(len(sig.parameters.keys()))]
    bound = sig.bind(*args)
    return sig, bound.arguments, args


annotation_lookup_arguments = [bound_args(sig) for sig in client_signatures]


@pytest.mark.asyncio
@pytest.mark.parametrize('signature, bound_arguments, args', annotation_lookup_arguments)
async def test_create_annotation_lookup(signature, bound_arguments, args):
    """Ensure that the annotation lookup dictionary is built correctly"""
    result = create_annotation_lookup(signature, bound_arguments)
    annotations = [param.annotation for param in signature.parameters.values()]
    correct = zip(annotations, args)
    assert all(map(lambda x: result[x[0]] == x[1], correct))


param_locations = ['header', 'path', 'query']
location = sampled_from(param_locations)
test_arguments_arguments = [(getattr(endpoints, cls), location.example()) for cls in endpoints.__all__]


@pytest.mark.parametrize('endpoint, param_location', test_arguments_arguments)
def test_arguments(endpoint, param_location):
    result = _arguments(endpoint, param_location)
    correct = list(filter(lambda x: x['located'] == param_location, endpoint.parameters))
    assert len(list(result)) == len(list(correct))


test_arguments_arguments = [(getattr(endpoints, cls), location.example(),) for cls in endpoints.__all__]


@pytest.mark.parametrize('interface_method', [method for cls in (getattr(interface, cls) for cls in interface.__all__)
                                              for method in cls.__dict__.values() if hasattr(method, 'endpoint')])
@pytest.mark.asyncio
async def test_create_request_params(client, interface_method):
    endpoint = interface_method.endpoint
    sig = interface_method.__signature__
    print(interface_method.__name__)
    args = tuple(range(len(sig.parameters)))
    arguments = create_annotation_lookup(sig, sig.bind(*args).arguments)
    print('arguments', arguments)
    for location in param_locations:
        result = await _create_request_params(client, endpoint, arguments, location)
        print(result)


@pytest.mark.asyncio
async def test_request_body_is_constructed_correctly(stop_loss_order):
    result = create_body(POSTOrders.request_schema,
                         {'irrelevant': stop_loss_order, 'test': Account(), 'arg': 'random_string'})
    print(result)
    assert result == {'order': {'tradeID': 1234, 'price': '0.8', 'type': 'STOP_LOSS', 'timeInForce': 'GTC',
                                'triggerCondition': 'DEFAULT'}}


@pytest.mark.asyncio
async def test_objects_can_be_converted_between_Model_object_and_json():
    account = Account(**GETAccountID_response['account'])
    response_json_account = GETAccountID_response['account']
    account_to_json = account.json_dict()

    response_json_account = order_dict(response_json_account)
    account_to_json = order_dict(account_to_json)
    print('SERVER DATA')
    print(response_json_account)
    print('ASYNC_20 DATA')
    print(account_to_json)
    assert response_json_account == account_to_json
