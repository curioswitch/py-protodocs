from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ZERO: _ClassVar[TestEnum]
    ONE: _ClassVar[TestEnum]
    TWO: _ClassVar[TestEnum]
ZERO: TestEnum
ONE: TestEnum
TWO: TestEnum

class TestMessage(_message.Message):
    __slots__ = ("bool", "int32", "int64", "uint32", "uint64", "sint32", "sint64", "fixed32", "fixed64", "float", "double", "string", "bytes", "test_enum", "nested", "strings", "map", "self")
    class Nested(_message.Message):
        __slots__ = ("string",)
        STRING_FIELD_NUMBER: _ClassVar[int]
        string: str
        def __init__(self, string: _Optional[str] = ...) -> None: ...
    class MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BOOL_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_NUMBER: _ClassVar[int]
    SINT32_FIELD_NUMBER: _ClassVar[int]
    SINT64_FIELD_NUMBER: _ClassVar[int]
    FIXED32_FIELD_NUMBER: _ClassVar[int]
    FIXED64_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    TEST_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    int32: int
    int64: int
    uint32: int
    uint64: int
    sint32: int
    sint64: int
    fixed32: int
    fixed64: int
    float: float
    double: float
    string: str
    bytes: bytes
    test_enum: TestEnum
    nested: TestMessage.Nested
    strings: _containers.RepeatedScalarFieldContainer[str]
    map: _containers.ScalarMap[str, int]
    self: TestMessage
    def __init__(self_, bool: _Optional[bool] = ..., int32: _Optional[int] = ..., int64: _Optional[int] = ..., uint32: _Optional[int] = ..., uint64: _Optional[int] = ..., sint32: _Optional[int] = ..., sint64: _Optional[int] = ..., fixed32: _Optional[int] = ..., fixed64: _Optional[int] = ..., float: _Optional[float] = ..., double: _Optional[float] = ..., string: _Optional[str] = ..., bytes: _Optional[bytes] = ..., test_enum: _Optional[_Union[TestEnum, str]] = ..., nested: _Optional[_Union[TestMessage.Nested, _Mapping]] = ..., strings: _Optional[_Iterable[str]] = ..., map: _Optional[_Mapping[str, int]] = ..., self: _Optional[_Union[TestMessage, _Mapping]] = ...) -> None: ...

class ExtendedTestMessage(_message.Message):
    __slots__ = ("bool", "int32", "int64", "uint32", "uint64", "sint32", "sint64", "fixed32", "fixed64", "float", "double", "string", "bytes", "test_enum", "nested", "complex_other_message", "strings", "nesteds", "selves", "string_to_int_map", "int_to_string_map", "message_map", "self_map", "self", "nested_self", "nested_nested_self")
    class Nested(_message.Message):
        __slots__ = ("string",)
        STRING_FIELD_NUMBER: _ClassVar[int]
        string: str
        def __init__(self, string: _Optional[str] = ...) -> None: ...
    class NestedSelf(_message.Message):
        __slots__ = ("self",)
        SELF_FIELD_NUMBER: _ClassVar[int]
        self: ExtendedTestMessage
        def __init__(self_, self: _Optional[_Union[ExtendedTestMessage, _Mapping]] = ...) -> None: ...
    class NestedNestedSelf(_message.Message):
        __slots__ = ("nested_self",)
        NESTED_SELF_FIELD_NUMBER: _ClassVar[int]
        nested_self: ExtendedTestMessage.NestedSelf
        def __init__(self, nested_self: _Optional[_Union[ExtendedTestMessage.NestedSelf, _Mapping]] = ...) -> None: ...
    class StringToIntMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    class IntToStringMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    class MessageMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExtendedTestMessage.Nested
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ExtendedTestMessage.Nested, _Mapping]] = ...) -> None: ...
    class SelfMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExtendedTestMessage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ExtendedTestMessage, _Mapping]] = ...) -> None: ...
    BOOL_FIELD_NUMBER: _ClassVar[int]
    INT32_FIELD_NUMBER: _ClassVar[int]
    INT64_FIELD_NUMBER: _ClassVar[int]
    UINT32_FIELD_NUMBER: _ClassVar[int]
    UINT64_FIELD_NUMBER: _ClassVar[int]
    SINT32_FIELD_NUMBER: _ClassVar[int]
    SINT64_FIELD_NUMBER: _ClassVar[int]
    FIXED32_FIELD_NUMBER: _ClassVar[int]
    FIXED64_FIELD_NUMBER: _ClassVar[int]
    FLOAT_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    TEST_ENUM_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    COMPLEX_OTHER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STRINGS_FIELD_NUMBER: _ClassVar[int]
    NESTEDS_FIELD_NUMBER: _ClassVar[int]
    SELVES_FIELD_NUMBER: _ClassVar[int]
    STRING_TO_INT_MAP_FIELD_NUMBER: _ClassVar[int]
    INT_TO_STRING_MAP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_MAP_FIELD_NUMBER: _ClassVar[int]
    SELF_MAP_FIELD_NUMBER: _ClassVar[int]
    SELF_FIELD_NUMBER: _ClassVar[int]
    NESTED_SELF_FIELD_NUMBER: _ClassVar[int]
    NESTED_NESTED_SELF_FIELD_NUMBER: _ClassVar[int]
    bool: bool
    int32: int
    int64: int
    uint32: int
    uint64: int
    sint32: int
    sint64: int
    fixed32: int
    fixed64: int
    float: float
    double: float
    string: str
    bytes: bytes
    test_enum: TestEnum
    nested: ExtendedTestMessage.Nested
    complex_other_message: TestMessage
    strings: _containers.RepeatedScalarFieldContainer[str]
    nesteds: _containers.RepeatedCompositeFieldContainer[ExtendedTestMessage.Nested]
    selves: _containers.RepeatedCompositeFieldContainer[ExtendedTestMessage]
    string_to_int_map: _containers.ScalarMap[str, int]
    int_to_string_map: _containers.ScalarMap[int, str]
    message_map: _containers.MessageMap[str, ExtendedTestMessage.Nested]
    self_map: _containers.MessageMap[str, ExtendedTestMessage]
    self: ExtendedTestMessage
    nested_self: ExtendedTestMessage.NestedSelf
    nested_nested_self: ExtendedTestMessage.NestedNestedSelf
    def __init__(self_, bool: _Optional[bool] = ..., int32: _Optional[int] = ..., int64: _Optional[int] = ..., uint32: _Optional[int] = ..., uint64: _Optional[int] = ..., sint32: _Optional[int] = ..., sint64: _Optional[int] = ..., fixed32: _Optional[int] = ..., fixed64: _Optional[int] = ..., float: _Optional[float] = ..., double: _Optional[float] = ..., string: _Optional[str] = ..., bytes: _Optional[bytes] = ..., test_enum: _Optional[_Union[TestEnum, str]] = ..., nested: _Optional[_Union[ExtendedTestMessage.Nested, _Mapping]] = ..., complex_other_message: _Optional[_Union[TestMessage, _Mapping]] = ..., strings: _Optional[_Iterable[str]] = ..., nesteds: _Optional[_Iterable[_Union[ExtendedTestMessage.Nested, _Mapping]]] = ..., selves: _Optional[_Iterable[_Union[ExtendedTestMessage, _Mapping]]] = ..., string_to_int_map: _Optional[_Mapping[str, int]] = ..., int_to_string_map: _Optional[_Mapping[int, str]] = ..., message_map: _Optional[_Mapping[str, ExtendedTestMessage.Nested]] = ..., self_map: _Optional[_Mapping[str, ExtendedTestMessage]] = ..., self: _Optional[_Union[ExtendedTestMessage, _Mapping]] = ..., nested_self: _Optional[_Union[ExtendedTestMessage.NestedSelf, _Mapping]] = ..., nested_nested_self: _Optional[_Union[ExtendedTestMessage.NestedNestedSelf, _Mapping]] = ...) -> None: ...
