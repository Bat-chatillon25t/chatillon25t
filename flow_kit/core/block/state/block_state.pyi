__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from enum import Enum

class BlockState(Enum):
    """Possible states of a block."""
    ABORTED = ...
    FINISHED = ...
    SKIPPED = ...
    INIT = ...
    READY = ...
    RUNNING = ...
    def is_final_state(self) -> bool:
        """Tells if this state has no more events to interact with."""
    def is_failed_final_state(self) -> bool:
        """Some error or unexpected happend to result in this end state."""
    def is_successful_final_state(self) -> bool:
        """All works fine and the block has finished his work."""

SUCCESSFUL_FINAL_STATES: Incomplete
FAILED_FINAL_STATES: Incomplete
FINAL_STATES: Incomplete