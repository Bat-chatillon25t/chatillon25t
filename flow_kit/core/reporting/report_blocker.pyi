__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.reporting.report_item_base import ReportItemBase as ReportItemBase

class ReportBlocker(ReportItemBase):
    """Class for reporting unfulfilled dependency."""
    def __init__(self, block: FlowBlock) -> None: ...