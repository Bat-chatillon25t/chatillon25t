__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import ast
from _typeshed import Incomplete, TraceFunction as TraceFunction
from dataclasses import dataclass
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.flow.flow import FlowBlock as FlowBlock
from flow_kit.core.flow.flow_builder import _ParameterMappingTemplate
from flow_kit.core.flow.parameter_mapping import ParameterMapping as ParameterMapping
from pathlib import Path
from types import FrameType
from typing import Any, ClassVar

@dataclass
class CodePosition:
    file_path: Path
    line_start: int
    column_start: int
    line_end: int | None
    column_end: int | None
    @property
    def line_start_zero_count(self) -> int:
        """Starting line of position for internal uses (counting start at line 0)."""
    @property
    def line_end_zero_count(self) -> int | None:
        """Ending line of position for internal uses (counting start at line 0)."""

@dataclass(frozen=True)
class ElementReference:
    """Reference of an element of a flow."""
    element_name: ClassVar[str]

@dataclass(frozen=True)
class FlowBlockReference(ElementReference):
    """Reference of a flow block."""
    block_identifier: BlockIdentifier
    element_name = ...

@dataclass(frozen=True)
class ParameterMappingReference(ElementReference):
    """Reference of a parameter mapping for a flow block."""
    block_identifier: BlockIdentifier
    parameter_key: str
    element_name = ...

class AddBlockWithCallFrameWrapper:
    """Wraps a PyFrameObject of an add_block_with call."""
    def __init__(self, frame) -> None: ...
    def get_block_object(self) -> FlowBlock:
        """Returns block object of add_block_with call."""
    def get_parameter_mappings(self) -> list[ParameterMapping | _ParameterMappingTemplate]:
        """Returns parameter_mappings object of add_block_with call."""
    def get_function_name(self) -> str:
        """Returns short function name."""
    def get_qualified_function_name(self) -> str:
        """Returns qualified function name."""
    def get_calling_file_path(self) -> Path:
        """Returns file path of file which does the call."""
    def get_calling_file_line_number(self) -> int:
        """Returns line number in calling file for the call."""

class FlowBuilderTrace:
    """Trace with references of flow elements defined in a flow builder."""
    def __init__(self) -> None: ...
    def add_reference_to_code_entry_for_flow_block(self, flow_block_reference: FlowBlockReference, code_position: CodePosition) -> None:
        """Add trace entry for a flow block.

        :param flow_block_reference: reference for flow block
        :param code_position: position of code definition
        :return:
        """
    def add_reference_to_code_entry_for_parameter_mapping(self, parameter_mapping_reference: ParameterMappingReference, code_position: CodePosition) -> None:
        """Add trace entry for a parameter mapping.

        :param parameter_mapping_reference: reference for parameter mapping
        :param code_position: position of code definition
        :return:
        """
    def get_error_message_with_code_snippet_for_reference(self, reference: ElementReference) -> str | None:
        """Returns a code snippet for the given flow element reference.

        :param reference: Flow element reference to get a code snippet for.
        :return:
        """

class FlowBuilderTracing:
    """Collects position locations of calls to the FlowBuilder."""
    instance: FlowBuilderTracing | None
    @classmethod
    def enable_tracing(cls) -> None:
        """Enables tracing by creating a FlowBuilderTracing instance."""
    original_trace_callback: TraceFunction | None
    flow_builder_trace: Incomplete
    def __init__(self) -> None: ...
    def get_definition_file_ast(self, definition_file_path: Path) -> ast.AST:
        """Returns abstract syntax tree for the given definition file."""
    @staticmethod
    def trace_function(frame: FrameType, event: str, arg: Any) -> None:
        """Wrapping trace function which calls previous trace function and trace function for flow builder tracing."""
    @staticmethod
    def trace_add_block_with_calls(frame: FrameType, event: str) -> None:
        """Trace function to find and log calls to FlowBuilder.add_block_with."""
    @staticmethod
    def add_reference_to_code_link_for_flow_block(add_block_call_ast_node: ast.Call, definition_file_path: Path, frame_wrapper: AddBlockWithCallFrameWrapper, tracing_instance: FlowBuilderTracing) -> None: ...
    @staticmethod
    def add_reference_to_code_links_for_parameter_mappings(block_definition_ast_node: ast.Call, definition_file_path: Path, frame_wrapper: AddBlockWithCallFrameWrapper, tracing_instance: FlowBuilderTracing) -> None: ...
    def add_reference_to_code_link(self, reference: ElementReference, code_position: CodePosition) -> None:
        """Add trace information for a flow block instantiation.

        :param reference: Identification of the element in the flow
        :param code_position: Position inside the code
        :return:
        """
    @classmethod
    def get_flow_builder_trace(cls) -> FlowBuilderTrace | None:
        """Returns trace with references to code links for this flow builder tracing.

        :return: flow builder references.
        """
    @classmethod
    def start_tracing(cls) -> None:
        """Start tracing by registering trace function."""
    @classmethod
    def stop_tracing(cls) -> None:
        """Stop tracing by unregistering trace function."""

class _FunctionVisitor(ast.NodeVisitor):
    def __init__(self, line_number: int, function_name: str) -> None: ...
    def visit_Call(self, node: ast.Call) -> None: ...
    @property
    def matching_node(self) -> ast.Call | None: ...