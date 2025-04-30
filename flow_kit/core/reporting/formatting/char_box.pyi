__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


class CharBox:
    """Class for adding a box to a list of lines."""
    def __init__(self, content: list[str], width: int = 0, min_max_width: tuple[int, int] = (60, 120)) -> None: ...
    @classmethod
    def len_border(cls) -> int:
        """Get total count of chars for border in a content line."""
    def get_lines(self) -> list[str]:
        """Return lines with decorating border."""