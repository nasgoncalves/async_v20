from collections import namedtuple
from functools import wraps

from .helpers import assign_descriptors
from .helpers import create_signature
from .helpers import async_flatten_dict
from .helpers import flatten_dict
import pandas as pd


# Small metaclass that simply returns
# any value passed to it though the slice syntax
# This is done purely as documentation.
class JSONArray(type):
    def __getitem__(cls, value):
        return value


# This array class indicates to the reader of code that
# this particular JSON value is expected to be an Array
class Array(metaclass=JSONArray):
    pass


class ORM(type):
    _arg_lookup = {}

    def __new__(mcs, *args, **kwargs):
        class_obj = super().__new__(mcs, *args, **kwargs)
        class_obj = assign_descriptors(class_obj)
        init_sig = create_signature(class_obj._schema)
        class_obj.template = dict.fromkeys(flatten_dict(class_obj._schema))

        def auto_assign(init):

            @wraps(init)
            def wrapper(self, *args, **kwargs):
                # Encapsulates the idea of an argument
                argument = namedtuple('argument', ['name', 'value', 'annotation'])
                kwargs = {key.lower(): value for key, value in kwargs.items()}
                bound = init_sig.bind(*args, **kwargs)
                bound.apply_defaults()
                bound = bound.arguments.items()
                annotations = (schema_value.typ for schema_value in self._schema.values())
                arguments = [argument(name_value[0], name_value[1], typ)
                             for name_value, typ
                             in (zip(bound, annotations)) if name_value[1]]

                self._fields = []  # Would normally place this is the class. Didn't segment instance attrs though
                for argument in arguments:
                    self._fields.append(argument.name)
                    if isinstance(argument.annotation, ORM):
                        setattr(self, argument.name, argument.annotation(argument.value))
                    else:
                        setattr(self, argument.name, argument.value)

            wrapper.__signature__ = init_sig
            return wrapper

        class_obj.__init__ = auto_assign(class_obj.__init__)
        return class_obj


class Model(metaclass=ORM):
    _schema = {}

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return self.__class__.__name__

    # Recursion might be an issue
    async def json_dict(self):
        async def get_object_fields(attr):
            attr = getattr(self, attr)
            if isinstance(attr, Model):
                attr = await attr.json_dict()
            return str(attr)

        return {attr: await get_object_fields(attr) for attr in self._fields}

    async def data(self):
        return await async_flatten_dict(await self.json_dict())

    async def series(self):
        return pd.Series(self.template.update(await self.data()))
