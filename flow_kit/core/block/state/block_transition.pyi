__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from dataclasses import dataclass
from flow_kit.core.block.state.block_event import BlockEvent as BlockEvent
from flow_kit.core.block.state.block_state import BlockState as BlockState

@dataclass(frozen=True, eq=True)
class BlockTransition:
    """Represents the change from one state(:py:class:`BlockState`) to another.

    Transitions occur in response to specific events(:py:class:`BlockEvent`).
    """
    event: BlockEvent
    from_state: BlockState
    to_state: BlockState