# This file is from https://github.com/python/typeshed as of commit sha b6d28acb2368cdd8c87554e01e22e134061997d6
# Copyright github.com/python/typeshed project contributors

import abc
import collections
import sys
from collections.abc import Iterable
from typing import TYPE_CHECKING as TYPE_CHECKING  # noqa: Y022,Y027,Y039
from typing import Any
from typing import AsyncContextManager as AsyncContextManager
from typing import AsyncGenerator as AsyncGenerator
from typing import AsyncIterable as AsyncIterable
from typing import AsyncIterator as AsyncIterator
from typing import Awaitable as Awaitable
from typing import Callable
from typing import ChainMap as ChainMap
from typing import ClassVar as ClassVar
from typing import ContextManager as ContextManager
from typing import Coroutine as Coroutine
from typing import Counter as Counter
from typing import DefaultDict as DefaultDict
from typing import Deque as Deque
from typing import Mapping
from typing import NewType as NewType
from typing import NoReturn as NoReturn
from typing import Sequence
from typing import Text as Text
from typing import Type as Type
from typing import TypeVar, _Alias
from typing import overload as overload
from typing import type_check_only

import _typeshed
from _collections_abc import dict_items, dict_keys, dict_values
from _typeshed import IdentityFunction

__all__ = [
    "ClassVar",
    "Concatenate",
    "Final",
    "LiteralString",
    "ParamSpec",
    "ParamSpecArgs",
    "ParamSpecKwargs",
    "Self",
    "Type",
    "TypeVarTuple",
    "Unpack",
    "Awaitable",
    "AsyncIterator",
    "AsyncIterable",
    "Coroutine",
    "AsyncGenerator",
    "AsyncContextManager",
    "ChainMap",
    "ContextManager",
    "Counter",
    "Deque",
    "DefaultDict",
    "NamedTuple",
    "OrderedDict",
    "TypedDict",
    "SupportsIndex",
    "Annotated",
    "assert_never",
    "assert_type",
    "dataclass_transform",
    "final",
    "IntVar",
    "is_typeddict",
    "Literal",
    "NewType",
    "overload",
    "Protocol",
    "reveal_type",
    "runtime",
    "runtime_checkable",
    "Text",
    "TypeAlias",
    "TypeGuard",
    "TYPE_CHECKING",
    "Never",
    "NoReturn",
    "Required",
    "NotRequired",
    "clear_overloads",
    "get_args",
    "get_origin",
    "get_overloads",
    "get_type_hints",
]

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])
_TC = TypeVar("_TC", bound=Type[object])

# unfortunately we have to duplicate this class definition from typing.pyi or we break pytype
class _SpecialForm:
    def __getitem__(self, parameters: Any) -> object: ...
    if sys.version_info >= (3, 10):
        def __or__(self, other: Any) -> _SpecialForm: ...
        def __ror__(self, other: Any) -> _SpecialForm: ...

# Do not import (and re-export) Protocol or runtime_checkable from
# typing module because type checkers need to be able to distinguish
# typing.Protocol and typing_extensions.Protocol so they can properly
# warn users about potential runtime exceptions when using typing.Protocol
# on older versions of Python.
Protocol: _SpecialForm = ...

def runtime_checkable(cls: _TC) -> _TC: ...

# This alias for above is kept here for backwards compatibility.
runtime = runtime_checkable
Final: _SpecialForm

def final(f: _F) -> _F: ...

Literal: _SpecialForm

def IntVar(name: str) -> Any: ...  # returns a new TypeVar

# Internal mypy fallback type for all typed dicts (does not exist at runtime)
# N.B. Keep this mostly in sync with typing._TypedDict/mypy_extensions._TypedDict
@type_check_only
class _TypedDict(Mapping[str, object], metaclass=abc.ABCMeta):
    __required_keys__: ClassVar[frozenset[str]]
    __optional_keys__: ClassVar[frozenset[str]]
    __total__: ClassVar[bool]
    def copy(self: _typeshed.Self) -> _typeshed.Self: ...
    # Using Never so that only calls using mypy plugin hook that specialize the signature
    # can go through.
    def setdefault(self, k: Never, default: object) -> object: ...
    # Mypy plugin hook for 'pop' expects that 'default' has a type variable type.
    def pop(
        self, k: Never, default: _T = ...
    ) -> object: ...  # pyright: ignore[reportInvalidTypeVarUse]
    def update(self: _T, __m: _T) -> None: ...
    def items(self) -> dict_items[str, object]: ...
    def keys(self) -> dict_keys[str, object]: ...
    def values(self) -> dict_values[str, object]: ...
    def __delitem__(self, k: Never) -> None: ...
    if sys.version_info >= (3, 9):
        def __or__(self: _typeshed.Self, __value: _typeshed.Self) -> _typeshed.Self: ...
        def __ior__(
            self: _typeshed.Self, __value: _typeshed.Self
        ) -> _typeshed.Self: ...

# TypedDict is a (non-subscriptable) special form.
TypedDict: object

OrderedDict = _Alias()

def get_type_hints(
    obj: Callable[..., Any],
    globalns: dict[str, Any] | None = ...,
    localns: dict[str, Any] | None = ...,
    include_extras: bool = ...,
) -> dict[str, Any]: ...
def get_args(tp: Any) -> tuple[Any, ...]: ...
def get_origin(tp: Any) -> Any | None: ...

Annotated: _SpecialForm
_AnnotatedAlias: Any  # undocumented

@runtime_checkable
class SupportsIndex(Protocol, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __index__(self) -> int: ...

# New things in 3.10
if sys.version_info >= (3, 10):
    from typing import Concatenate as Concatenate
    from typing import ParamSpec as ParamSpec
    from typing import ParamSpecArgs as ParamSpecArgs
    from typing import ParamSpecKwargs as ParamSpecKwargs
    from typing import TypeAlias as TypeAlias
    from typing import TypeGuard as TypeGuard
    from typing import is_typeddict as is_typeddict
else:
    class ParamSpecArgs:
        __origin__: ParamSpec
        def __init__(self, origin: ParamSpec) -> None: ...

    class ParamSpecKwargs:
        __origin__: ParamSpec
        def __init__(self, origin: ParamSpec) -> None: ...

    class ParamSpec:
        __name__: str
        __bound__: type[Any] | None
        __covariant__: bool
        __contravariant__: bool
        def __init__(
            self,
            name: str,
            *,
            bound: None | type[Any] | str = ...,
            contravariant: bool = ...,
            covariant: bool = ...,
        ) -> None: ...
        @property
        def args(self) -> ParamSpecArgs: ...
        @property
        def kwargs(self) -> ParamSpecKwargs: ...
    Concatenate: _SpecialForm
    TypeAlias: _SpecialForm
    TypeGuard: _SpecialForm
    def is_typeddict(tp: object) -> bool: ...

# New things in 3.11
# NamedTuples are not new, but the ability to create generic NamedTuples is new in 3.11
if sys.version_info >= (3, 11):
    from typing import LiteralString as LiteralString
    from typing import NamedTuple as NamedTuple
    from typing import Never as Never
    from typing import NotRequired as NotRequired
    from typing import Required as Required
    from typing import Self as Self
    from typing import TypeVarTuple as TypeVarTuple
    from typing import Unpack as Unpack
    from typing import assert_never as assert_never
    from typing import assert_type as assert_type
    from typing import clear_overloads as clear_overloads
    from typing import dataclass_transform as dataclass_transform
    from typing import get_overloads as get_overloads
    from typing import reveal_type as reveal_type
else:
    Self: _SpecialForm
    Never: _SpecialForm = ...
    def reveal_type(__obj: _T) -> _T: ...
    def assert_never(__arg: Never) -> Never: ...
    def assert_type(__val: _T, __typ: Any) -> _T: ...
    def clear_overloads() -> None: ...
    def get_overloads(
        func: Callable[..., object]
    ) -> Sequence[Callable[..., object]]: ...

    Required: _SpecialForm
    NotRequired: _SpecialForm
    LiteralString: _SpecialForm
    Unpack: _SpecialForm

    @final
    class TypeVarTuple:
        __name__: str
        def __init__(self, name: str) -> None: ...
        def __iter__(self) -> Any: ...  # Unpack[Self]

    def dataclass_transform(
        *,
        eq_default: bool = ...,
        order_default: bool = ...,
        kw_only_default: bool = ...,
        field_specifiers: tuple[type[Any] | Callable[..., Any], ...] = ...,
        **kwargs: object,
    ) -> IdentityFunction: ...

    class NamedTuple(tuple[Any, ...]):
        if sys.version_info < (3, 8):
            _field_types: collections.OrderedDict[str, type]
        elif sys.version_info < (3, 9):
            _field_types: dict[str, type]
        _field_defaults: dict[str, Any]
        _fields: tuple[str, ...]
        _source: str
        @overload
        def __init__(
            self, typename: str, fields: Iterable[tuple[str, Any]] = ...
        ) -> None: ...
        @overload
        def __init__(
            self, typename: str, fields: None = ..., **kwargs: Any
        ) -> None: ...
        @classmethod
        def _make(
            cls: type[_typeshed.Self], iterable: Iterable[Any]
        ) -> _typeshed.Self: ...
        if sys.version_info >= (3, 8):
            def _asdict(self) -> dict[str, Any]: ...
        else:
            def _asdict(self) -> collections.OrderedDict[str, Any]: ...

        def _replace(self: _typeshed.Self, **kwargs: Any) -> _typeshed.Self: ...
