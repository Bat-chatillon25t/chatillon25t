__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC, abstractmethod
from flow_kit.core.block.definitions.parameter_definitions import BlockParameter as BlockParameter, ParameterDefinition as ParameterDefinition, ParameterKey as ParameterKey
from flow_kit.core.block.exceptions import ParameterDefinitionNotPresentError as ParameterDefinitionNotPresentError, ParameterNotSuppliedError as ParameterNotSuppliedError
from typing import Any

class ParameterizedBlock(ABC, metaclass=abc.ABCMeta):
    """Parametrization for a flow block."""
    def __init__(self) -> None: ...
    def supply(self, parameter: BlockParameter) -> None:
        """Set parameter to this flow step. Overwrites existing parameters with same key."""
    @abstractmethod
    def get_parameter_definitions(self) -> set[ParameterDefinition]:
        """Get the definition for parameterization of the block."""
    def get_parameter_definition_for_parameter_key(self, parameter_key: ParameterKey) -> ParameterDefinition:
        """Returns the ParameterDefinition with a given ParameterKey."""
    def is_fully_supplied(self) -> bool:
        """Returns True, if values for all required parameters are provided."""
    def has_parameters_with_resolution_error(self) -> bool:
        """Returns True, if any supplied parameter has a resolution error."""
    def get_parameter(self, key: str) -> BlockParameter | None:
        """Get the parameter object for given key."""
    def get_parameter_value(self, key: str) -> Any:
        """Get the value of the parameter object for given key."""