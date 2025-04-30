__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


class BlockIdentifier:
    """Identifier for a block."""
    def __init__(self) -> None: ...
    def __eq__(self, other: object) -> bool:
        """Compares this Identifier with one other object."""
    def __hash__(self) -> int:
        """Returns the hash of the object."""