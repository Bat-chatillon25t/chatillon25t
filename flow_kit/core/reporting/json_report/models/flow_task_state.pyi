__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from enum import Enum

class FlowTaskState(str, Enum):
    """Model class for REST-API representation of a flow task state."""
    RETAINED = 'RETAINED'
    WAITING = 'WAITING'
    RUNNING = 'RUNNING'
    FINISHED = 'FINISHED'
    SKIPPED = 'SKIPPED'
    ABORTED = 'ABORTED'