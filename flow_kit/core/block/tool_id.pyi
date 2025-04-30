__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from enum import Enum

class ToolId(Enum):
    """Tool identifier for a request during block execution."""
    TESTGUIDE = 'TESTGUIDE'
    GENERIC = 'GENERIC'
    JIRA = 'JIRA'