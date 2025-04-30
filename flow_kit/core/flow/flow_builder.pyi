__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from dataclasses import dataclass
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.flow.alias_mapping import AliasMapping as AliasMapping
from flow_kit.core.flow.block_dependencies import BlockDependenciesBuilder as BlockDependenciesBuilder, BlockDependency as BlockDependency
from flow_kit.core.flow.flow import Flow as Flow
from flow_kit.core.flow.flow_block_container import FlowBlockContainer as FlowBlockContainer
from flow_kit.core.flow.flow_builder_tracing import FlowBuilderTracing as FlowBuilderTracing, ParameterMappingReference as ParameterMappingReference
from flow_kit.core.flow.flow_parameter import FlowParameterBuilder as FlowParameterBuilder, FlowParameterDefinition as FlowParameterDefinition
from flow_kit.core.flow.parameter_mapping import BatchItemMapping as BatchItemMapping, ExecutionResultMapping as ExecutionResultMapping, FlowParameterMapping as FlowParameterMapping, ParameterMapping as ParameterMapping, StaticValueMapping as StaticValueMapping, UserExpressionResultMapping as UserExpressionResultMapping
from flow_kit.core.flow.parameter_mapping_set import ParameterMappingSet as ParameterMappingSet
from flow_kit.core.validation.exceptions import ParameterMappingValidationError as ParameterMappingValidationError
from typing import Any, Self

class UnsupportetItemTypeError(Exception):
    """Exception that is raised, when item of unknown type should be added to a flow."""

@dataclass
class _ParameterMappingTemplate(ABC, metaclass=abc.ABCMeta):
    """Baseclass fo parameter mapping templates to allow them to be defined without block."""
    parameter_key: str
    @abstractmethod
    def build(self, block: FlowBlock) -> ParameterMapping:
        """Get parameter mapping for concrete block."""
    def get_required_blocks(self) -> list[FlowBlock]:
        """Get required flow blocks."""
    def get_required_flow_parameters(self, block: FlowBlock) -> list[FlowParameterDefinition]:
        """Get required flow parameters."""

@dataclass
class _StaticValueMappingTemplate(_ParameterMappingTemplate):
    """Template for StaticValueMapping."""
    value: Any
    def build(self, block: FlowBlock) -> ParameterMapping:
        """Get StaticValueMapping for block."""

@dataclass
class _BlockResultMappingTemplate(_ParameterMappingTemplate):
    """Template for ExecutionResultMapping."""
    result_block: FlowBlock
    def build(self, block: FlowBlock) -> ParameterMapping:
        """Get ExecutionResultMapping for block."""
    def get_required_blocks(self) -> list[FlowBlock]:
        """Get required flow blocks."""

@dataclass
class _UserExpressionResultMappingTemplate(_ParameterMappingTemplate):
    """Template for UserExpressionResultMapping."""
    expression: str
    def build(self, block: FlowBlock) -> ParameterMapping:
        """Get UserExpressionResultMapping for block."""

@dataclass
class _FlowParameterMappingTemplate(_ParameterMappingTemplate):
    """Template for FlowParameterMapping."""
    parameter_name: str
    def build(self, block: FlowBlock) -> ParameterMapping: ...
    def get_required_flow_parameters(self, block: FlowBlock) -> list[FlowParameterDefinition]:
        """Get required flow parameters."""

@dataclass
class _BatchItemMappingTemplate(_ParameterMappingTemplate):
    """Template for BatchItemMapping."""
    def build(self, block: FlowBlock) -> ParameterMapping: ...
    def get_required_flow_parameters(self, block: FlowBlock) -> list[FlowParameterDefinition]: ...

class Assign:
    """Builder class for creating ParameterMappingTemplate."""
    key: Incomplete
    def __init__(self, key: str) -> None: ...
    def to_static_value(self, value: Any) -> _StaticValueMappingTemplate:
        """Get template for StaticValueMapping."""
    def to_user_expression(self, expression: str) -> _UserExpressionResultMappingTemplate:
        """Get template for UserExpressionResultMapping."""
    def to_block_result(self, result_block: FlowBlock) -> _BlockResultMappingTemplate:
        """Get template for ExecutionResultMapping."""
    def to_batch_item(self):
        """Get template for BatchItemMapping."""
    def to_flow_parameter(self, param: str):
        """Get template for FlowParameterMapping."""

class FlowBuilder:
    """Builder class with fluent api for flow definition."""
    def __init__(self) -> None: ...
    def add(self, item: FlowBlock | ParameterMapping | BlockDependency) -> Self:
        """Add an item to the flow."""
    def add_block_with(self, block: FlowBlock, *parameter_mappings: ParameterMapping | _ParameterMappingTemplate, required_blocks: list[FlowBlock | str] | None = None, result_alias: str = '') -> Self:
        """Add block to flow with its links."""
    def add_block(self, block: FlowBlock) -> Self:
        """Add block to flow.

        Hint: Use assignment expression to access this block in further steps:
        .add_block(my_block := FlowBlock())
        """
    def add_alias(self, alias: str, block: FlowBlock | BlockIdentifier) -> Self:
        """Add alias definition to the flow."""
    def add_parameter_mapping(self, parameter_mapping: ParameterMapping) -> Self:
        """Add parameter mapping to the flow."""
    def add_dependency(self, dependency: BlockDependency) -> Self:
        """Add dependency to ths flow."""
    def build(self) -> Flow:
        """Return created flow object."""

class FlowBuilderError(Exception):
    """Exception that is raised if a check inside the flow builder fails."""