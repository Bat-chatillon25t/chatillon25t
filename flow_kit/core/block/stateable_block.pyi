__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from flow_kit.core.block.state.block_event import BlockEvent as BlockEvent
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.block.state.block_state_graph import BlockStateGraphBuilder as BlockStateGraphBuilder
from flow_kit.core.block.state.block_transition import BlockTransition as BlockTransition

FLOW_BLOCK_STATE_GRAPH: Incomplete

class StateableBlock:
    """Block which runs through different states(:py:class:`BlockState`).

    on the basis of different events( :py:class:`BlockEvent`).
    """
    def __init__(self, current_state: BlockState = ...) -> None: ...
    def get_state(self) -> BlockState:
        """Gives the actual state of the block.

        :return: Actual state.
        """
    def handle_event(self, event: BlockEvent) -> None:
        """Method to trigger state changes based on Events.

        :param event: see :py:class:`BlockEvent`.
        """