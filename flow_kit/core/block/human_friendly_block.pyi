__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from typing import Self

class HumanFriendlyBlock:
    """Human friendly properties of a block."""
    def __init__(self) -> None: ...
    def set_label(self, name: str) -> None:
        """Set friendly name for this block."""
    def with_label(self, name: str) -> Self:
        """Set friendly name for this block."""
    def get_label(self) -> str:
        """Get friendly name for this block."""