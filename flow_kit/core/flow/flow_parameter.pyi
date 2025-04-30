__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from dataclasses import dataclass
from flow_kit.core.block.definitions.type_check import TypeCheck as TypeCheck
from flow_kit.core.flow.exceptions import FlowParameterAlreadyPresentError as FlowParameterAlreadyPresentError, FlowParameterNotFoundError as FlowParameterNotFoundError, FlowParameterNotSuppliedError as FlowParameterNotSuppliedError
from typing import Any, Self

@dataclass
class FlowParameterDefinition:
    """Class for describing a parameter of a flow."""
    key: str
    value_type: type

@dataclass
class FlowParameter:
    """Dataclass modelling a concrete parameter value."""
    key: str
    value: Any

class FlowParameterCollection:
    """Container class for holding multiple flow parameters."""
    def __init__(self, definitions: list[FlowParameterDefinition]) -> None: ...
    def supply(self, parameter: FlowParameter) -> None:
        """Supply a parameter value."""
    def has_definition(self, key: str) -> bool:
        """True if parameter with given key is present."""
    def get_definition(self, key: str) -> FlowParameterDefinition:
        """Get value for an existing parameter."""
    def get_definitions(self) -> list[FlowParameterDefinition]:
        """Get all FlowParameter."""
    def get_value(self, key: str) -> Any:
        """Get value for flow parameter."""
    def copy(self) -> FlowParameterCollection:
        """Copies this FlowParameterCollection without supplied values."""

class FlowParameterBuilder:
    """Builder class for FlowParameterCollection."""
    def __init__(self) -> None: ...
    def add_definition(self, par_def: FlowParameterDefinition) -> Self:
        """Add a definition.

        If the key of the definition is already in use with the same value type, nothing will happen.
        If the key of the definition is already in use with another value type, an exception will be raised.
        """
    def build(self) -> FlowParameterCollection:
        """Build the FlowParameterCollection."""