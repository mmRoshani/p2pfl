"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
compile command:
python -m grpc_tools.protoc -I=p2pfl/proto --python_out=p2pfl/proto --grpc_python_out=p2pfl/proto p2pfl/proto/node.proto --mypy_out=p2pfl/proto
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int
    CMD_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    source: builtins.str
    ttl: builtins.int
    hash: builtins.int
    cmd: builtins.str
    @property
    def args(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    round: builtins.int
    def __init__(
        self,
        *,
        source: builtins.str = ...,
        ttl: builtins.int = ...,
        hash: builtins.int = ...,
        cmd: builtins.str = ...,
        args: collections.abc.Iterable[builtins.str] | None = ...,
        round: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_round", b"_round", "round", b"round"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_round", b"_round", "args", b"args", "cmd", b"cmd", "hash", b"hash", "round", b"round", "source", b"source", "ttl", b"ttl"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_round", b"_round"]) -> typing_extensions.Literal["round"] | None: ...

global___Message = Message

@typing_extensions.final
class Weights(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_FIELD_NUMBER: builtins.int
    ROUND_FIELD_NUMBER: builtins.int
    WEIGHTS_FIELD_NUMBER: builtins.int
    CONTRIBUTORS_FIELD_NUMBER: builtins.int
    WEIGHT_FIELD_NUMBER: builtins.int
    CMD_FIELD_NUMBER: builtins.int
    source: builtins.str
    round: builtins.int
    weights: builtins.bytes
    @property
    def contributors(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    weight: builtins.int
    cmd: builtins.str
    def __init__(
        self,
        *,
        source: builtins.str = ...,
        round: builtins.int = ...,
        weights: builtins.bytes = ...,
        contributors: collections.abc.Iterable[builtins.str] | None = ...,
        weight: builtins.int = ...,
        cmd: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cmd", b"cmd", "contributors", b"contributors", "round", b"round", "source", b"source", "weight", b"weight", "weights", b"weights"]) -> None: ...

global___Weights = Weights

@typing_extensions.final
class HandShakeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADDR_FIELD_NUMBER: builtins.int
    addr: builtins.str
    def __init__(
        self,
        *,
        addr: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["addr", b"addr"]) -> None: ...

global___HandShakeRequest = HandShakeRequest

@typing_extensions.final
class ResponseMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERROR_FIELD_NUMBER: builtins.int
    error: builtins.str
    def __init__(
        self,
        *,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_error", b"_error", "error", b"error"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_error", b"_error"]) -> typing_extensions.Literal["error"] | None: ...

global___ResponseMessage = ResponseMessage
