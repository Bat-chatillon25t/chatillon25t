__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from dataclasses import dataclass

@dataclass
class ResultDefinition:
    """Definition of the result of a FlowBlock."""
    value_type: type | None
    description: str = ...