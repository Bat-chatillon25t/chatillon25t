__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC
from flow_kit.core.reporting.formatting.char_box import CharBox as CharBox
from flow_kit.core.reporting.formatting.indenter import Indenter as Indenter

class ReportItemBase(ABC, metaclass=abc.ABCMeta):
    """Abstract base class for items that should be reported."""
    def __init__(self) -> None: ...
    def get_lines_of_text(self, indent_level: int = 0, width: int = 200) -> list[str]:
        """Get lines of text for report of this item."""