__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


class Indenter:
    """Class to indent a list of lines."""
    def __init__(self, content: list[str], indent_count: int = 4, indent_char: str = ' ') -> None: ...
    def get_lines(self) -> list[str]:
        """Return lines with decorating border."""