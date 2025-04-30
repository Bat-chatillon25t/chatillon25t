__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from enum import Enum

class FlowTaskReportBlockState(str, Enum):
    """FlowTaskReportBlockState."""
    ABORTED = 'ABORTED'
    FINISHED = 'FINISHED'
    SKIPPED = 'SKIPPED'
    INIT = 'INIT'
    READY = 'READY'
    RUNNING = 'RUNNING'