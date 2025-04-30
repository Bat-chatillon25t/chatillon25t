__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.flow.block_dependencies import BlockDependency as BlockDependency
from flow_kit.core.flow.flow import Flow as Flow
from flow_kit.core.flow.parameter_mapping import ExecutionResultMapping as ExecutionResultMapping

STATE_COLOR_MAP: Incomplete

class PumlPrintable(ABC, metaclass=abc.ABCMeta):
    """Abstract class for all wrapper classes to generate a plant uml representation for a object."""
    @staticmethod
    def convert_to_puml_id(block_id: BlockIdentifier) -> str:
        """Converts a Blockidentifier into an valid plant uml identifier."""
    @abstractmethod
    def get_puml(self) -> str:
        """Returns the plant uml text."""

class FlowNode(PumlPrintable):
    """Dataobject representing a node in flow visualization."""
    def __init__(self, block: FlowBlock) -> None: ...
    def get_puml(self) -> str:
        """Get plantuml code."""

class FlowLink(PumlPrintable):
    """Dataobject representing a link in flow visualization."""
    def __init__(self, dependency: BlockDependency, *, with_data_flow: bool = False) -> None: ...
    def get_puml(self) -> str:
        """Get plantuml code."""

class FlowPlotter:
    """Class to visualize a flow."""
    def __init__(self, flow: Flow) -> None: ...
    def get_puml_code(self) -> str:
        """Get plantuml code."""