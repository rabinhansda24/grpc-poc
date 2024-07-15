from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ("id", "product", "amount", "payment_status")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    product: str
    amount: float
    payment_status: bool
    def __init__(self, id: _Optional[int] = ..., product: _Optional[str] = ..., amount: _Optional[float] = ..., payment_status: bool = ...) -> None: ...

class CreateOrder(_message.Message):
    __slots__ = ("product", "amount")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    product: str
    amount: float
    def __init__(self, product: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...

class UpdateOrder(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class GetOrderByIdRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetOrderByIdResponse(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class CreateOrderRequest(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: CreateOrder
    def __init__(self, order: _Optional[_Union[CreateOrder, _Mapping]] = ...) -> None: ...

class CreateOrderResponse(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class UpdateOrderRequest(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class UpdateOrderResponse(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: Order
    def __init__(self, order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...
