from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Payment(_message.Message):
    __slots__ = ("id", "amount", "payment_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    amount: float
    payment_id: str
    def __init__(self, id: _Optional[int] = ..., amount: _Optional[float] = ..., payment_id: _Optional[str] = ...) -> None: ...

class ProcessPaymentRequest(_message.Message):
    __slots__ = ("order_id",)
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: int
    def __init__(self, order_id: _Optional[int] = ...) -> None: ...

class ProcessPaymentResponse(_message.Message):
    __slots__ = ("payment",)
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    payment: Payment
    def __init__(self, payment: _Optional[_Union[Payment, _Mapping]] = ...) -> None: ...

class GetPaymentByOrderIdRequest(_message.Message):
    __slots__ = ("order_id",)
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: int
    def __init__(self, order_id: _Optional[int] = ...) -> None: ...

class GetPaymentByOrderIdResponse(_message.Message):
    __slots__ = ("payment",)
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    payment: Payment
    def __init__(self, payment: _Optional[_Union[Payment, _Mapping]] = ...) -> None: ...
