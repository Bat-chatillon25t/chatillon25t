__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from dataclasses import dataclass
from flow_kit.core.block.exceptions import BlockTransitionConflictError as BlockTransitionConflictError
from flow_kit.core.block.state.block_event import BlockEvent as BlockEvent
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.block.state.block_transition import BlockTransition as BlockTransition
from typing import Self

class BlockStateGraph:
    """Graph which represants the state flow of a flow block."""
    @dataclass(frozen=True, eq=True)
    class TransitionCondition:
        """Allows grouping the transactions according to their prerequisite and result."""
        event: BlockEvent
        from_state: BlockState
    def __init__(self, transitions: set[BlockTransition]) -> None: ...
    def get_next_state(self, event: BlockEvent, actual_state: BlockState) -> BlockState | None:
        """Returns the next state for a given event and an actual state if there is one transition.

        :param event: Event that triggers the transition.
        :param actual_state: Actual status at the time of the event.
        :return: The state which results from the event or None if no transition is known.
        """
    def __len__(self) -> int:
        """Number of all known transitions."""

class BlockStateGraphBuilder:
    """Builder for a :py:class:`BlockTransitionSet`."""
    def __init__(self) -> None: ...
    def add_transition(self, transition: BlockTransition) -> Self:
        """Adds a transition to the set."""
    def build(self) -> BlockStateGraph:
        """Builds the :py:class:`BlockTransitionSet`."""