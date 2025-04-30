__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC, abstractmethod
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.definitions.parameter_definitions import BlockParameter as BlockParameter, ErrorBlockParameter as ErrorBlockParameter, ParameterDefinition as ParameterDefinition, ParameterKey as ParameterKey, ResolvedBlockParameter as ResolvedBlockParameter
from flow_kit.core.block.definitions.type_check import TypeCheck as TypeCheck
from flow_kit.core.block.exceptions import ValueTypeMismatchError as ValueTypeMismatchError
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.flow.exceptions import ReservedFlowParameterNameError as ReservedFlowParameterNameError, ResultNotPresentError as ResultNotPresentError, UnknownAliasError as UnknownAliasError, UserExpressionResolutionError as UserExpressionResolutionError
from flow_kit.core.flow.flow_parameter import FlowParameterCollection as FlowParameterCollection
from flow_kit.core.flow.result_mapping import ResultMapping as ResultMapping
from flow_kit.core.flow.user_expression import UserExpression as UserExpression
from typing import Any, ClassVar

class ParameterMapping(ABC, metaclass=abc.ABCMeta):
    """Abstract class for a mapping of a FlowBlock's ParameterDefinition to a value."""
    def __init__(self, block: FlowBlock, parameter_key: str) -> None: ...
    @property
    def block_identifier(self) -> BlockIdentifier:
        """Returns the block identifier this mapping is meant for."""
    @property
    def parameter_key(self) -> ParameterKey:
        """Returns the parameter key this mapping is meant for."""
    @property
    def parameter_definition(self) -> ParameterDefinition:
        """Retuns the full definition for the parameter."""
    def resolve(self, result_mapping: ResultMapping, flow_parameters: FlowParameterCollection) -> BlockParameter:
        """Resolve the mapping to a concrete value given the context of the flow."""
    @abstractmethod
    def validate(self) -> None:
        """Validate settings of this parameter mapping."""

class StaticValueMapping(ParameterMapping):
    """Mapping referencing a given static value."""
    def __init__(self, block: FlowBlock, parameter_key: str, value: Any) -> None: ...
    def validate(self) -> None:
        """Check if type of given static value is correct."""

class ExecutionResultMapping(ParameterMapping):
    """Mapping referencing the result of another block as a value."""
    def __init__(self, block: FlowBlock, parameter_key: str, result_block: FlowBlock) -> None: ...
    def get_result_block_identifier(self) -> BlockIdentifier:
        """Returns linked block_identifier."""
    def validate(self) -> None:
        """Check if value types match."""

class UserExpressionResultMapping(ParameterMapping):
    """Mapping referencing user defined expression to combine results of other blocks."""
    def __init__(self, block: FlowBlock, parameter_key: str, expression: str) -> None: ...
    def validate(self) -> None:
        """Check syntax of expression."""

class FlowParameterMapping(ParameterMapping):
    """Mapping referencing parameters of a flow."""
    REGISTERED_SPECIFIC_FLOW_PARAMETER_MAPPINGS: ClassVar[dict[str, type['FlowParameterMapping']]]
    def __init__(self, block: FlowBlock, parameter_key: str, flow_parameter_name: str) -> None: ...
    def validate(self) -> None:
        """No special validation here."""
    @classmethod
    def get_reserved_flow_parameter_name(cls) -> str | None:
        """Returns the reserved flow_parameter_name for this FlowParameterMapping."""
    @classmethod
    def register_specific_flow_parameter_mapping(cls, flow_parameter_mapping_class: type['FlowParameterMapping']) -> None:
        """Registers a special type of FlowParameterMapping."""

class BatchItemMapping(FlowParameterMapping):
    """Mapping referencing items of the batch within a batch processing sub-flow."""
    @classmethod
    def get_reserved_flow_parameter_name(cls) -> str:
        """Returns the reserved flow_parameter_name for this FlowParameterMapping."""
    def __init__(self, block: FlowBlock, parameter_key: str) -> None: ...