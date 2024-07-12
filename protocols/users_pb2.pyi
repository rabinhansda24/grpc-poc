from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUser(_message.Message):
    __slots__ = ("name", "email")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class UserResponse(_message.Message):
    __slots__ = ("id", "name", "email")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class GetUsersRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetUsersResponse(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[UserResponse]
    def __init__(self, users: _Optional[_Iterable[_Union[UserResponse, _Mapping]]] = ...) -> None: ...

class GetUserByIdRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class GetUserByIdResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: UserResponse
    def __init__(self, user: _Optional[_Union[UserResponse, _Mapping]] = ...) -> None: ...
