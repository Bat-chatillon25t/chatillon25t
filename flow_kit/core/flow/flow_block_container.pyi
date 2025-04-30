__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.flow.exceptions import BlockIdentifierNotUniqueError as BlockIdentifierNotUniqueError

class FlowBlockContainer:
    """Container for FlowBlocks."""
    def __init__(self, flow_blocks: list[FlowBlock]) -> None: ...
    def get_block_by_identifier(self, identifier: BlockIdentifier) -> FlowBlock:
        """Get block by identifier."""
    def has_id(self, identifier: BlockIdentifier) -> bool:
        """True if identifier is present."""
    def get_flow_blocks(self) -> list[FlowBlock]:
        """Get all contained FlowBlocks."""
    def copy(self) -> FlowBlockContainer:
        """Creates a copy of this FlowBlockContainer while creating copies of all contained FlowBlocks."""