__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterKey as ParameterKey
from typing import Any

class AlreadyExecutedError(Exception):
    """Exception thrown when trying to execute a block that has already been executed once."""
class BlockNotExecutedError(Exception):
    """Exception that is thrown if a method asserts block to be already executed."""
class BlockTransitionConflictError(Exception):
    """Exception that is thrown if a transition conflicts with another transition in the set."""
class ComplexGraphError(Exception):
    """Exception that is thrown if the state graph is getting more complex than it should be at start."""
class UnresolvedParameterValueError(Exception):
    """Is raised, when resolved_value is requested before it is resolved."""

class ParameterDefinitionNotPresentError(Exception):
    """Raised if no ParameterDefinition for a given ParameterKey is present."""
    parameter_key: str
    def __init__(self, parameter_key: ParameterKey) -> None: ...

class ParameterNotSuppliedError(Exception):
    """Raised if no parameter is supplied for a ParameterDefinition that is not optional."""
class ValueTypeError(Exception):
    """Base Exception for ValueTypeErrors."""
class ValueTypeMismatchError(ValueTypeError):
    """Exception that is raised, when trying to match a value with the wrong type."""
class InvalidValueTypeError(ValueTypeError):
    """Raised if a given type cannot be used as a type for the value."""
class TypeDefinitionMismatchError(Exception):
    """Raised, when type of the value of ParameterDefinition and linked ResultDefinition do not match."""
class MissingParameterTypingError(Exception):
    """Exception that is raised, when typing is missing for parameter in user code function."""
class MissingReturnTypingError(Exception):
    """Exception that is raised, when typing is missing for return value in user code function."""
class MissingRequiredParameterError(Exception):
    """Exception that is raised, when required parameter is not found in user code function."""

def short_repr_for_error_message(object_to_print: Any, max_length: int = 20) -> str:
    """Gives a short representation of the object to use in an exception message."""