from .decorators import endpoint, shortcut
from ..definitions.types import ClientExtensions
from ..definitions.types import ClientID
from ..definitions.types import DateTime
from ..definitions.types import InstrumentName
from ..definitions.types import LimitOrderRequest
from ..definitions.types import MarketIfTouchedOrderRequest
from ..definitions.types import MarketOrderRequest
from ..definitions.types import OrderID
from ..definitions.types import OrderPositionFill
from ..definitions.types import OrderRequest
from ..definitions.types import OrderSpecifier
from ..definitions.types import OrderStateFilter
from ..definitions.types import OrderTriggerCondition
from ..definitions.types import OrderType
from ..definitions.types import PriceValue
from ..definitions.types import StopLossDetails
from ..definitions.types import StopLossOrderRequest
from ..definitions.types import StopOrderRequest
from ..definitions.types import TakeProfitDetails
from ..definitions.types import TakeProfitOrderRequest
from ..definitions.types import TimeInForce
from ..definitions.types import TradeID
from ..definitions.types import TrailingStopLossDetails
from ..definitions.types import TrailingStopLossOrderRequest
from ..definitions.types import DecimalNumber
from ..endpoints.annotations import Count
from ..endpoints.annotations import Ids
from ..endpoints.annotations import TradeClientExtensions
from ..endpoints.order import *

__all__ = ['OrderInterface']


class OrderInterface(object):
    @endpoint(POSTOrders)
    def post_order(self, order_request: OrderRequest = ...):
        """
        Post an OrderRequest.

        Args:

            order_request: :class:`~async_v20.definitions.types.OrderRequest`
                or a class derived from OrderRequest

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        pass

    @shortcut
    def create_order(self, instrument: InstrumentName, units: DecimalNumber, type: OrderType = 'MARKET',
                     trade_id: TradeID = ..., price: PriceValue = ..., client_trade_id: ClientID = ...,
                     time_in_force: TimeInForce = ..., gtd_time: DateTime =  ...,
                     trigger_condition: OrderTriggerCondition = ..., client_extensions: ClientExtensions = ...,
                     distance: PriceValue = ..., price_bound: PriceValue = ...,
                     position_fill: OrderPositionFill = ..., take_profit_on_fill: TakeProfitDetails = ...,
                     stop_loss_on_fill: StopLossDetails = ...,
                     trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                     trade_client_extensions: ClientExtensions = ...):
        """
        create an OrderRequest

        Args:

            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
            price: :class:`~async_v20.definitions.primitives.PriceValue`
            type: :class:`~async_v20.definitions.primitives.OrderType`
            client_trade_id: :class:`~async_v20.definitions.primitives.ClientID`
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
            distance: :class:`~async_v20.definitions.primitives.PriceValue`
            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
            units: :class:`~async_v20.definitions.primitives.Unit`
            price_bound: :class:`~async_v20.definitions.primitives.PriceValue`
            position_fill: :class:`~async_v20.definitions.primitives.OrderPositionFill`
            take_profit_on_fill: :class:`~async_v20.definitions.types.TakeProfitDetails`
            stop_loss_on_fill: :class:`~async_v20.definitions.types.StopLossDetails`
            trailing_stop_loss_on_fill: :class:`~async_v20.definitions.types.TrailingStopLossDetails`
            trade_client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.post_order(
            order_request=OrderRequest(
                instrument=instrument, units=units, type=type, trade_id=trade_id, price=price,
                client_trade_id=client_trade_id, time_in_force=time_in_force, gtd_time=gtd_time,
                trigger_condition=trigger_condition, client_extensions=client_extensions,
                distance=distance, price_bound=price_bound, position_fill=position_fill,
                take_profit_on_fill=take_profit_on_fill, stop_loss_on_fill=stop_loss_on_fill,
                trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                trade_client_extensions=trade_client_extensions))

    @endpoint(GETOrders)
    def list_orders(self,
                    ids: Ids = ...,
                    state: OrderStateFilter = ...,
                    instrument: InstrumentName = ...,
                    count: Count = ...,
                    before_id: OrderID = ...):
        """
        Get a list of Orders for an Account

        Args:

            ids: :class:`~async_v20.endpoints.annotations.Ids`
                list of Order IDs to retrieve
            state: :class:`~async_v20.definitions.primitives.OrderStateFilter`
                The state to filter the requested Orders by
            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                The instrument to filter the requested orders by
            count: :class:`~async_v20.endpoints.annotations.Count`
                The maximum number of Orders to return
            before_id: :class:`~async_v20.definitions.primitives.OrderID`
                The maximum Order ID to return. If not provided the most recent
                Orders in the Account are returned

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (orders= :class:`~async_v20.definitions.types.ArrayOrder`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

        """
        pass

    @endpoint(GETPendingOrders)
    def list_pending_orders(self):
        """
        List all pending Orders

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (orders= :class:`~async_v20.definitions.types.ArrayOrder`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

        """
        pass

    @endpoint(GETOrderSpecifier)
    def get_order(self, order_specifier: OrderSpecifier = ...):
        """
        Get details for a single Order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The Order Specifier

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (order= :class:`~async_v20.definitions.types.Order`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

        """
        pass

    @endpoint(PUTOrderSpecifier)
    def replace_order(self,
                      order_specifier: OrderSpecifier = ...,
                      order_request: OrderRequest = ...):
        """
        Replace an Order  by simultaneously cancelling it and
        creating a replacement Order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The Order Specifier
            order_request: :class:`~async_v20.definitions.types.OrderRequest`
                Specification of the replacing Order

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                replacingOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        pass

    @endpoint(PUTOrderSpecifierCancel)
    def cancel_order(self, order_specifier: OrderSpecifier = ...):
        """
        Cancel a pending Order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The Order Specifier

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.OrderCancelRejectTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        pass

    @endpoint(PUTClientExtensions)
    def set_client_extensions(self,
                              order_specifier: OrderSpecifier = ...,
                              client_extensions: ClientExtensions = ...,
                              trade_client_extensions: TradeClientExtensions = ...):
        """
        Update the Client Extensions for an Order . Do not set,
        modify, or delete clientExtensions if your account is associated with
        MT4.

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The Order Specifier
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The Client Extensions to update for the Order. Do not set,
                modify, or delete clientExtensions if your account is
                associated with MT4.
            trade_client_extensions: :class:`~async_v20.endpoints.annotations.TradeClientExtensions`
                The Client Extensions to update for the Trade created when the
                Order is filled. Do not set, modify, or delete clientExtensions
                if your account is associated with MT4.

        Returns:

            status [200]
                :class:`~async_v20.interface.response.Response`
                (orderClientExtensionsModifyTransaction=
                :class:`~async_v20.definitions.types.OrderClientExtensionsModifyTransaction`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderClientExtensionsModifyRejectTransaction=
                :class:`~async_v20.definitions.types.OrderClientExtensionsModifyRejectTransaction`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderClientExtensionsModifyRejectTransaction=
                :class:`~async_v20.definitions.types.OrderClientExtensionsModifyRejectTransaction`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        pass

    @shortcut
    def market_order(self, instrument: InstrumentName, units: DecimalNumber,
                     time_in_force: TimeInForce = 'FOK', price_bound: PriceValue = ...,
                     position_fill: OrderPositionFill = 'DEFAULT', client_extensions: ClientExtensions = ...,
                     take_profit_on_fill: TakeProfitDetails = ..., stop_loss_on_fill: StopLossDetails = ...,
                     trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                     trade_client_extensions: ClientExtensions = ...):
        """
        Create a Market Order Request

        Args:

            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                The Market Order's Instrument.
            units: :class:`~async_v20.definitions.primitives.Unit`
                The quantity requested to be filled by the Market Order. A posititive number of units
                results in a long Order, and a negative number of units results in a short Order.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the Market Order.
                Restricted to FOK or IOC for a MarketOrder.
            price_bound: :class:`~async_v20.definitions.primitives.PriceValue`
                The worst price that the client is willing to have the Market Order filled at.
            position_fill: :class:`~async_v20.definitions.primitives.OrderPositionFill`
                Specification of how Positions in the Account
                are modified when the Order is filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.
            take_profit_on_fill: :class:`~async_v20.definitions.types.TakeProfitDetails`
                TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
                a client. This may happen when an Order
                is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
                modified directly through the Trade.
            stop_loss_on_fill: :class:`~async_v20.definitions.types.StopLossDetails`
                StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
                client. This may happen when an Order
                is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
                directly through the Trade.
            trailing_stop_loss_on_fill: :class:`~async_v20.definitions.types.TrailingStopLossDetails`
                TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
                created on behalf of a client. This may happen when an Order is
                filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
                Order is modified directly through the Trade.
            trade_client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                Client Extensions to add to the Trade created when the Order is filled (if such a
                Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
                MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.post_order(
            order_request=MarketOrderRequest(
                instrument=instrument, units=units, time_in_force=time_in_force,
                price_bound=price_bound, position_fill=position_fill,
                client_extensions=client_extensions,
                take_profit_on_fill=take_profit_on_fill,
                stop_loss_on_fill=stop_loss_on_fill,
                trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                trade_client_extensions=trade_client_extensions
            ))

    @shortcut
    def limit_order(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                    time_in_force: TimeInForce = 'GTC', gtd_time: DateTime =  ...,
                    position_fill: OrderPositionFill = 'DEFAULT', trigger_condition: OrderTriggerCondition = 'DEFAULT',
                    client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                    stop_loss_on_fill: StopLossDetails = ...,
                    trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                    trade_client_extensions: ClientExtensions = ...):
        """
        Create a Limit Order

        Args:

            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                The Limit Order's Instrument.
            units: :class:`~async_v20.definitions.primitives.Unit`
                The quantity requested to be filled by the Limit Order. A posititive number of units
                results in a long Order, and a negative number of units results in a short Order.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the Limit Order. The Limit Order will only be
                filled by a market price that is equal to or better than this price.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the Limit Order.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the Limit Order will
                be cancelled if its timeInForce is "GTD".
            position_fill: :class:`~async_v20.definitions.primitives.OrderPositionFill`
                Specification of how Positions in the Account
                are modified when the Order is filled.
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.
            take_profit_on_fill: :class:`~async_v20.definitions.types.TakeProfitDetails`
                TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
                a client. This may happen when an Order
                is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
                modified directly through the Trade.
            stop_loss_on_fill: :class:`~async_v20.definitions.types.StopLossDetails`
                StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
                client. This may happen when an Order
                is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
                directly through the Trade.
            trailing_stop_loss_on_fill: :class:`~async_v20.definitions.types.TrailingStopLossDetails`
                TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
                created on behalf of a client. This may happen when an Order is
                filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
                Order is modified directly through the Trade.
            trade_client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                Client Extensions to add to the Trade created when the Order is filled (if such a
                Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
                MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.post_order(
            order_request=LimitOrderRequest(
                instrument=instrument, units=units, price=price,
                time_in_force=time_in_force, gtd_time=gtd_time,
                position_fill=position_fill,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions,
                take_profit_on_fill=take_profit_on_fill,
                stop_loss_on_fill=stop_loss_on_fill,
                trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                trade_client_extensions=trade_client_extensions
            ))

    @shortcut
    def limit_replace_order(self,
                            order_specifier: OrderSpecifier, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                            time_in_force: TimeInForce = 'GTC', gtd_time: DateTime =  ...,
                            position_fill: OrderPositionFill = 'DEFAULT',
                            trigger_condition: OrderTriggerCondition = 'DEFAULT',
                            client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                            stop_loss_on_fill: StopLossDetails = ...,
                            trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                            trade_client_extensions: ClientExtensions = ...):
        """
        Replace a pending Limit Order

        Args:
            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The ID of the Limit Order to replace
            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                The Limit Order's Instrument.
            units: :class:`~async_v20.definitions.primitives.Unit`
                The quantity requested to be filled by the Limit Order. A posititive number of units
                results in a long Order, and a negative number of units results in a short Order.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the Limit Order. The Limit Order will only be
                filled by a market price that is equal to or better than this price.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the Limit Order.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the Limit Order will
                be cancelled if its timeInForce is "GTD".
            position_fill: :class:`~async_v20.definitions.primitives.OrderPositionFill`
                Specification of how Positions in the Account
                are modified when the Order is filled.
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.
            take_profit_on_fill: :class:`~async_v20.definitions.types.TakeProfitDetails`
                TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
                a client. This may happen when an Order
                is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
                modified directly through the Trade.
            stop_loss_on_fill: :class:`~async_v20.definitions.types.StopLossDetails`
                StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
                client. This may happen when an Order
                is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
                directly through the Trade.
            trailing_stop_loss_on_fill: :class:`~async_v20.definitions.types.TrailingStopLossDetails`
                TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
                created on behalf of a client. This may happen when an Order is
                filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
                Order is modified directly through the Trade.
            trade_client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                Client Extensions to add to the Trade created when the Order is filled (if such a
                Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
                MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                replacingOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.replace_order(
            order_specifier=order_specifier,
            order_request=LimitOrderRequest(
                instrument=instrument, units=units, price=price,
                time_in_force=time_in_force, gtd_time=gtd_time, position_fill=position_fill,
                trigger_condition=trigger_condition, client_extensions=client_extensions,
                take_profit_on_fill=take_profit_on_fill,
                stop_loss_on_fill=stop_loss_on_fill,
                trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                trade_client_extensions=trade_client_extensions
            ))

    @shortcut
    def stop_order(self, trade_id: TradeID, price: PriceValue,
                   client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime =  ...,
                   trigger_condition: OrderTriggerCondition = 'DEFAULT', client_extensions: ClientExtensions = ...):
        """
        Create a Stop Order

        Args:

            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The ID of the Trade to close when the price threshold is breached.
            client_trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The client ID of the Trade to be closed when the price threshold is breached.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the StopLoss Order. The associated Trade will be
                closed by a market price that is equal to or worse than this threshold.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the StopLoss Order. Restricted
                to "GTC", "GFD" and "GTD" for StopLoss Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the StopLoss Order will
                be cancelled if its timeInForce is "GTD".
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.post_order(
            order_request=StopLossOrderRequest(
                trade_id=trade_id, price=price, client_trade_id=client_trade_id,
                time_in_force=time_in_force, gtd_time=gtd_time,
                trigger_condition=trigger_condition, client_extensions=client_extensions
            ))

    @shortcut
    def stop_replace_order(self,
                           order_specifier: OrderSpecifier,
                           instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                           price_bound: PriceValue = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime =  ...,
                           position_fill: OrderPositionFill = 'DEFAULT',
                           trigger_condition: OrderTriggerCondition = 'DEFAULT',
                           client_extensions: ClientExtensions = ..., take_profit_on_fill: TakeProfitDetails = ...,
                           stop_loss_on_fill: StopLossDetails = ...,
                           trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                           trade_client_extensions: ClientExtensions = ...):
        """
        Replace a pending Stop Order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The ID of the Stop Order to replace
            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                The Stop Order's Instrument.
            units: :class:`~async_v20.definitions.primitives.Unit`
                The quantity requested to be filled by the Stop Order. A posititive number of units
                results in a long Order, and a negative number of units results in a short Order.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the Stop Order. The Stop Order will only be
                filled by a market price that is equal to or worse than this price.
            price_bound: :class:`~async_v20.definitions.primitives.PriceValue`
                The worst market price that may be used to fill this Stop Order. If the market gaps and
                crosses through both the price and the priceBound, the Stop Order will be cancelled instead of being filled.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the Stop Order.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the Stop Order will
                be cancelled if its timeInForce is "GTD".
            position_fill: :class:`~async_v20.definitions.primitives.OrderPositionFill`
                Specification of how Positions in the Account
                are modified when the Order is filled.
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.
            take_profit_on_fill: :class:`~async_v20.definitions.types.TakeProfitDetails`
                TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
                a client. This may happen when an Order
                is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
                modified directly through the Trade.
            stop_loss_on_fill: :class:`~async_v20.definitions.types.StopLossDetails`
                StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
                client. This may happen when an Order
                is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
                directly through the Trade.
            trailing_stop_loss_on_fill: :class:`~async_v20.definitions.types.TrailingStopLossDetails`
                TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
                created on behalf of a client. This may happen when an Order is
                filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
                Order is modified directly through the Trade.
            trade_client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                Client Extensions to add to the Trade created when the Order is filled (if such a
                Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
                MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                replacingOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        return self.replace_order(
            order_specifier=order_specifier,
            order_request=StopOrderRequest(
                instrument=instrument, units=units, price=price,
                price_bound=price_bound, time_in_force=time_in_force,
                gtd_time=gtd_time, position_fill=position_fill,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions,
                take_profit_on_fill=take_profit_on_fill,
                stop_loss_on_fill=stop_loss_on_fill,
                trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                trade_client_extensions=trade_client_extensions
            ))

    @shortcut
    def market_if_touched_order(self, instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                                price_bound: PriceValue = ...,
                                time_in_force: TimeInForce = 'GTC', gtd_time: DateTime =  ...,
                                position_fill: OrderPositionFill = 'DEFAULT',
                                trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                client_extensions: ClientExtensions = ...,
                                take_profit_on_fill: TakeProfitDetails = ...,
                                stop_loss_on_fill: StopLossDetails = ...,
                                trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                                trade_client_extensions: ClientExtensions = ...):
        """
        Create a market if touched order

        Args:

            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                The MarketIfTouched Order's Instrument.
            units: :class:`~async_v20.definitions.primitives.Unit`
                The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
                results in a long Order, and a negative number of units results in a short Order.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
                filled by a market price that crosses this price from the direction of the market price
                at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's
                price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
            price_bound: :class:`~async_v20.definitions.primitives.PriceValue`
                The worst market price that may be used to fill this MarketIfTouched Order.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the MarketIfTouched Order. Restricted
                to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the MarketIfTouched Order will
                be cancelled if its timeInForce is "GTD".
            position_fill: :class:`~async_v20.definitions.primitives.OrderPositionFill`
                Specification of how Positions in the Account
                are modified when the Order is filled.
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.
            take_profit_on_fill: :class:`~async_v20.definitions.types.TakeProfitDetails`
                TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
                a client. This may happen when an Order
                is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
                modified directly through the Trade.
            stop_loss_on_fill: :class:`~async_v20.definitions.types.StopLossDetails`
                StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
                client. This may happen when an Order
                is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
                directly through the Trade.
            trailing_stop_loss_on_fill: :class:`~async_v20.definitions.types.TrailingStopLossDetails`
                TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
                created on behalf of a client. This may happen when an Order is
                filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
                Order is modified directly through the Trade.
            trade_client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                Client Extensions to add to the Trade created when the Order is filled (if such a
                Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
                MT4.


        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.post_order(
            order_request=MarketIfTouchedOrderRequest(
                instrument=instrument, units=units, price=price,
                price_bound=price_bound, time_in_force=time_in_force,
                gtd_time=gtd_time, position_fill=position_fill,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions,
                take_profit_on_fill=take_profit_on_fill,
                stop_loss_on_fill=stop_loss_on_fill,
                trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                trade_client_extensions=trade_client_extensions
            ))

    @shortcut
    def market_if_touched_replace_order(self,
                                        order_specifier: OrderSpecifier,
                                        instrument: InstrumentName, units: DecimalNumber, price: PriceValue,
                                        price_bound: PriceValue = ...,
                                        time_in_force: TimeInForce = 'GTC', gtd_time: DateTime =  ...,
                                        position_fill: OrderPositionFill = 'DEFAULT',
                                        trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                        client_extensions: ClientExtensions = ...,
                                        take_profit_on_fill: TakeProfitDetails = ...,
                                        stop_loss_on_fill: StopLossDetails = ...,
                                        trailing_stop_loss_on_fill: TrailingStopLossDetails = ...,
                                        trade_client_extensions: ClientExtensions = ...
                                        ):
        """
        Replace a pending market if touched order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The ID of the MarketIfTouched Order to replace
            instrument: :class:`~async_v20.definitions.primitives.InstrumentName`
                The MarketIfTouched Order's Instrument.
            units: :class:`~async_v20.definitions.primitives.Unit`
                The quantity requested to be filled by the MarketIfTouched Order. A posititive number of units
                results in a long Order, and a negative number of units results in a short Order.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the MarketIfTouched Order. The MarketIfTouched Order will only be
                filled by a market price that crosses this price from the direction of the market price
                at the time when the Order was created (the initialMarketPrice). Depending on the value of the Order's
                price and initialMarketPrice, the MarketIfTouchedOrder will behave like a Limit or a Stop Order.
            price_bound: :class:`~async_v20.definitions.primitives.PriceValue`
                The worst market price that may be used to fill this MarketIfTouched Order.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the MarketIfTouched Order. Restricted
                to "GTC", "GFD" and "GTD" for MarketIfTouched Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the MarketIfTouched Order will
                be cancelled if its timeInForce is "GTD".
            position_fill: :class:`~async_v20.definitions.primitives.OrderPositionFill`
                Specification of how Positions in the Account
                are modified when the Order is filled.
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.
            take_profit_on_fill: :class:`~async_v20.definitions.types.TakeProfitDetails`
                TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of
                a client. This may happen when an Order
                is filled that opens a Trade requiring a Take Profit, or when a Trade's dependent Take Profit Order is
                modified directly through the Trade.
            stop_loss_on_fill: :class:`~async_v20.definitions.types.StopLossDetails`
                StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a
                client. This may happen when an Order
                is filled that opens a Trade requiring a Stop Loss, or when a Trade's dependent Stop Loss Order is modified
                directly through the Trade.
            trailing_stop_loss_on_fill: :class:`~async_v20.definitions.types.TrailingStopLossDetails`
                TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be
                created on behalf of a client. This may happen when an Order is
                filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade's dependent Trailing Stop Loss
                Order is modified directly through the Trade.
            trade_client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                Client Extensions to add to the Trade created when the Order is filled (if such a
                Trade is created). Do not set, modify, or delete tradeClientExtensions if your account is associated with
                MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                replacingOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        return self.replace_order(
            order_specifier=order_specifier,
            order_request=MarketIfTouchedOrderRequest(
                instrument=instrument, units=units,
                price=price, price_bound=price_bound,
                time_in_force=time_in_force,
                gtd_time=gtd_time,
                position_fill=position_fill,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions,
                take_profit_on_fill=take_profit_on_fill,
                stop_loss_on_fill=stop_loss_on_fill,
                trailing_stop_loss_on_fill=trailing_stop_loss_on_fill,
                trade_client_extensions=trade_client_extensions)
        )

    @shortcut
    def take_profit_order(self, trade_id: TradeID, price: PriceValue,
                          client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC',
                          gtd_time: DateTime =  ...,
                          trigger_condition: OrderTriggerCondition = 'DEFAULT',
                          client_extensions: ClientExtensions = ...):
        """
        Create a take profit order

        Args:

            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The ID of the Trade to close when the price threshold is breached.
            client_trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The client ID of the Trade to be closed when the price threshold is breached.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the TakeProfit Order. The associated Trade will be
                closed by a market price that is equal to or better than this threshold.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the TakeProfit Order. Restricted
                to "GTC", "GFD" and "GTD" for TakeProfit Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the TakeProfit Order will
                be cancelled if its timeInForce is "GTD".
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        return self.post_order(
            order_request=TakeProfitOrderRequest(
                trade_id=trade_id, price=price, client_trade_id=client_trade_id,
                time_in_force=time_in_force, gtd_time=gtd_time,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions
            ))

    @shortcut
    def take_profit_replace_order(self,
                                  order_specifier: OrderSpecifier,
                                  trade_id: TradeID, price: PriceValue,
                                  client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC',
                                  gtd_time: DateTime =  ...,
                                  trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                  client_extensions: ClientExtensions = ...
                                  ):
        """
        Replace a pending take profit order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The ID of the Take Profit Order to replace
            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The ID of the Trade to close when the price threshold is breached.
            client_trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The client ID of the Trade to be closed when the price threshold is breached.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the TakeProfit Order. The associated Trade will be
                closed by a market price that is equal to or better than this threshold.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the TakeProfit Order. Restricted
                to "GTC", "GFD" and "GTD" for TakeProfit Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the TakeProfit Order will
                be cancelled if its timeInForce is "GTD".
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.


        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                replacingOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.replace_order(
            order_specifier=order_specifier,
            order_request=TakeProfitOrderRequest(
                trade_id=trade_id, price=price,
                client_trade_id=client_trade_id,
                time_in_force=time_in_force, gtd_time=gtd_time,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions)
        )

    @shortcut
    def stop_loss_order(self, trade_id: TradeID, price: PriceValue,
                        client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC', gtd_time: DateTime =  ...,
                        trigger_condition: OrderTriggerCondition = 'DEFAULT',
                        client_extensions: ClientExtensions = ...):
        """
        Create a Stop Loss Order

        Args:

            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The ID of the Trade to close when the price threshold is breached.
            client_trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The client ID of the Trade to be closed when the price threshold is breached.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the StopLoss Order. The associated Trade will be
                closed by a market price that is equal to or worse than this threshold.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the StopLoss Order. Restricted
                to "GTC", "GFD" and "GTD" for StopLoss Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the StopLoss Order will
                be cancelled if its timeInForce is "GTD".
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.post_order(
            order_request=StopLossOrderRequest(
                trade_id=trade_id, price=price, client_trade_id=client_trade_id,
                time_in_force=time_in_force, gtd_time=gtd_time,
                trigger_condition=trigger_condition, client_extensions=client_extensions
            ))

    @shortcut
    def stop_loss_replace_order(self, order_specifier: OrderSpecifier,
                                trade_id: TradeID, price: PriceValue,
                                client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC',
                                gtd_time: DateTime =  ...,
                                trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                client_extensions: ClientExtensions = ...):
        """
        Replace a pending Stop Loss Order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The ID of the Stop Loss Order to replace
            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The ID of the Trade to close when the price threshold is breached.
            client_trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The client ID of the Trade to be closed when the price threshold is breached.
            price: :class:`~async_v20.definitions.primitives.PriceValue`
                The price threshold specified for the StopLoss Order. The associated Trade will be
                closed by a market price that is equal to or worse than this threshold.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the StopLoss Order. Restricted
                to "GTC", "GFD" and "GTD" for StopLoss Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the StopLoss Order will
                be cancelled if its timeInForce is "GTD".
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.

        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                replacingOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

        """
        return self.replace_order(
            order_specifier=order_specifier,
            order_request=StopLossOrderRequest(
                trade_id=trade_id, price=price,
                client_trade_id=client_trade_id,
                time_in_force=time_in_force, gtd_time=gtd_time,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions
            ))

    @shortcut
    def trailing_stop_loss_order(self, trade_id: TradeID, distance: PriceValue,
                                 client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC',
                                 gtd_time: DateTime =  ...,
                                 trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                 client_extensions: ClientExtensions = ...):
        """
        Create a Trailing Stop Loss Order

        Args:

            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The ID of the Trade to close when the price threshold is breached.
            client_trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The client ID of the Trade to be closed when the price threshold is breached.
            distance: :class:`~async_v20.definitions.primitives.PriceValue`
                The price distance specified for the TrailingStopLoss Order.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the TrailingStopLoss Order. Restricted
                to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the StopLoss Order will
                be cancelled if its timeInForce is "GTD".
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.


        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.post_order(
            order_request=TrailingStopLossOrderRequest(
                trade_id=trade_id, distance=distance,
                client_trade_id=client_trade_id,
                time_in_force=time_in_force,
                gtd_time=gtd_time,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions
            ))

    @shortcut
    def trailing_stop_loss_replace_order(self, order_specifier: OrderSpecifier,
                                         trade_id: TradeID, distance: PriceValue,
                                         client_trade_id: ClientID = ..., time_in_force: TimeInForce = 'GTC',
                                         gtd_time: DateTime =  ...,
                                         trigger_condition: OrderTriggerCondition = 'DEFAULT',
                                         client_extensions: ClientExtensions = ...):
        """
        Replace a pending Trailing Stop Loss Order

        Args:

            order_specifier: :class:`~async_v20.definitions.primitives.OrderSpecifier`
                The ID of the Take Profit Order to replace
            trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The ID of the Trade to close when the price threshold is breached.
            client_trade_id: :class:`~async_v20.definitions.primitives.TradeID`
                The client ID of the Trade to be closed when the price threshold is breached.
            distance: :class:`~async_v20.definitions.primitives.PriceValue`
                The price distance specified for the TrailingStopLoss Order.
            time_in_force: :class:`~async_v20.definitions.primitives.TimeInForce`
                The time-in-force requested for the TrailingStopLoss Order. Restricted
                to "GTC", "GFD" and "GTD" for TrailingStopLoss Orders.
            gtd_time: :class:`~async_v20.definitions.primitives.DateTime`
                The date/time when the StopLoss Order will
                be cancelled if its timeInForce is "GTD".
            trigger_condition: :class:`~async_v20.definitions.primitives.OrderTriggerCondition`
                Specification of what component of a price should be used
                for comparison when determining if the Order should be filled.
            client_extensions: :class:`~async_v20.definitions.types.ClientExtensions`
                The client extensions to add to the Order. Do not set,
                modify, or delete clientExtensions if your account is associated with MT4.


        Returns:

            status [201]
                :class:`~async_v20.interface.response.Response`
                (orderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                orderCreateTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderFillTransaction= :class:`~async_v20.definitions.types.OrderFillTransaction`,
                orderReissueTransaction= :class:`~async_v20.definitions.types.Transaction`,
                orderReissueRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                replacingOrderCancelTransaction= :class:`~async_v20.definitions.types.OrderCancelTransaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`)

            status [400]
                :class:`~async_v20.interface.response.Response`
                (orderRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)

            status [401]
                :class:`~async_v20.interface.response.Response`
                (orderCancelRejectTransaction= :class:`~async_v20.definitions.types.Transaction`,
                relatedTransactionIDs= :class:`~async_v20.definitions.types.ArrayTransactionID`,
                lastTransactionID= :class:`~async_v20.definitions.primitives.TransactionID`,
                errorCode= :class:`~builtins.str`,
                errorMessage= :class:`~builtins.str`)
        """
        return self.replace_order(
            order_specifier=order_specifier,
            order_request=TrailingStopLossOrderRequest(
                trade_id=trade_id, distance=distance,
                client_trade_id=client_trade_id,
                time_in_force=time_in_force,
                gtd_time=gtd_time,
                trigger_condition=trigger_condition,
                client_extensions=client_extensions
            ))
