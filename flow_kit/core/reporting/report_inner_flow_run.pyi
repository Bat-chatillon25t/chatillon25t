__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import dataclasses
from flow_kit import Flow as Flow
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.reporting.report_flow_block import ReportFlowBlock as ReportFlowBlock

@dataclasses.dataclass
class ReportInnerFlowRun:
    """Class for reporting of inner flow runs."""
    result: BlockState
    flow: Flow
    label: str | None = ...
    report_blocks: list[ReportFlowBlock] = dataclasses.field(default_factory=list)