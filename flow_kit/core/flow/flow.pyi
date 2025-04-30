__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.request_counter_utils import sum_request_counters as sum_request_counters
from flow_kit.core.block.tool_id import ToolId as ToolId
from flow_kit.core.flow.alias_mapping import AliasMapping as AliasMapping
from flow_kit.core.flow.block_dependencies import BlockDependencies as BlockDependencies
from flow_kit.core.flow.flow_block_container import FlowBlockContainer as FlowBlockContainer
from flow_kit.core.flow.flow_parameter import FlowParameterCollection as FlowParameterCollection
from flow_kit.core.flow.parameter_mapping_set import ParameterMappingSet as ParameterMappingSet
from flow_kit.core.flow.result_mapping import ResultMapping as ResultMapping

class Flow:
    """Object describing a flow with flow blocks, aliases, dependencies and parameters."""
    is_alias_present: Incomplete
    get_identifier_by_alias: Incomplete
    get_parameters_by_block_identifier: Incomplete
    get_all_block_identifier_from_parameter_mapping_set: Incomplete
    get_flow_blocks: Incomplete
    get_block_by_identifier: Incomplete
    has_id: Incomplete
    get_dependencies: Incomplete
    def __init__(self, flow_block_container: FlowBlockContainer, parameter_mapping_set: ParameterMappingSet, alias_mapping: AliasMapping, block_dependencies: BlockDependencies, flow_parameters: FlowParameterCollection) -> None: ...
    def get_flow_parameters(self) -> FlowParameterCollection:
        """Returns the FlowParameterCollection."""
    def get_flow_block_by_alias(self, alias: str) -> FlowBlock:
        """Returns flow block object for given alias."""
    def get_result_mapping(self) -> ResultMapping:
        """Returns a ResultMapping for all FlowBlocks contains in the FlowBlockContainer."""
    def get_block_representation(self, block: FlowBlock) -> str:
        """Get user readable representation for a block."""
    def get_alias_mapping(self) -> AliasMapping:
        """Get AliasMapping of this flow."""
    def copy(self) -> Flow:
        """Creates a new Flow object from this Flow object."""
    def get_request_counters(self) -> dict[ToolId, int]:
        """Get summed request counters of all blocks of the flow."""