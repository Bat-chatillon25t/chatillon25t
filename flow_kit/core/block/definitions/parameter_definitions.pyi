__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from flow_kit.core.block.exceptions import UnresolvedParameterValueError as UnresolvedParameterValueError
from typing import Any

ParameterKey = str

@dataclass(frozen=True)
class ParameterDefinition:
    """Definition of a parameter for a FlowBlock."""
    key: ParameterKey = field(hash=True)
    value_type: type = field(hash=True)
    description: str = field(default='', hash=False)
    optional: bool = field(default=False, hash=True)
    default_value: Any = field(default=None, hash=False)

class BlockParameter(ABC, metaclass=abc.ABCMeta):
    """Abstract parameter value for a FlowBlock."""
    @property
    @abstractmethod
    def parameter_key(self) -> ParameterKey: ...
    @property
    @abstractmethod
    def value(self) -> Any: ...
    @property
    @abstractmethod
    def resolution_error(self) -> str | None: ...
    @abstractmethod
    def has_error_while_resolution(self) -> bool:
        """True if parameter resolution for this BlockParameter resulted in error."""

class ResolvedBlockParameter(BlockParameter):
    """Successfully resolved parameter value for a FlowBlock."""
    def __init__(self, parameter_key: ParameterKey, value: Any) -> None: ...
    @property
    def parameter_key(self) -> ParameterKey: ...
    @property
    def value(self) -> Any: ...
    @property
    def resolution_error(self) -> str | None: ...
    def has_error_while_resolution(self) -> bool:
        """True if parameter resolution for this BlockParameter resulted in error."""

class ErrorBlockParameter(BlockParameter):
    """Parameter value for parameters where resolution resulted in an error."""
    @property
    def parameter_key(self) -> ParameterKey: ...
    def __init__(self, parameter_key: ParameterKey, resolution_error: str) -> None: ...
    @property
    def value(self) -> Any: ...
    @property
    def resolution_error(self) -> str: ...
    def has_error_while_resolution(self) -> bool:
        """True if parameter resolution for this BlockParameter resulted in error."""