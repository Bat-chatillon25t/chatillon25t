__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.reporting.json_report.models.flow_task_report_block import FlowTaskReportBlock as FlowTaskReportBlock
from flow_kit.core.reporting.json_report.models.flow_task_report_block_error import FlowTaskReportBlockError as FlowTaskReportBlockError
from flow_kit.core.reporting.json_report.models.flow_task_report_block_inner_flow import FlowTaskReportBlockInnerFlow as FlowTaskReportBlockInnerFlow
from flow_kit.core.reporting.json_report.models.flow_task_report_block_parameter import FlowTaskReportBlockParameter as FlowTaskReportBlockParameter
from flow_kit.core.reporting.json_report.models.flow_task_report_block_state import FlowTaskReportBlockState as FlowTaskReportBlockState
from flow_kit.core.reporting.report_blocker import ReportBlocker as ReportBlocker
from flow_kit.core.reporting.report_inner_flow_run import ReportInnerFlowRun as ReportInnerFlowRun
from flow_kit.core.reporting.report_item_base import ReportItemBase as ReportItemBase
from flow_kit.core.reporting.report_parameter import ReportParameter as ReportParameter
from flow_kit.core.reporting.report_result import ReportResult as ReportResult

class ReportFlowBlock(ReportItemBase):
    """Class for reporting of flow blocks."""
    def __init__(self, flow_block: FlowBlock, alias: str | None, dependent_on: list[FlowBlock]) -> None: ...
    @property
    def label(self) -> str:
        """Get label of flow block."""
    @property
    def state(self) -> FlowTaskReportBlockState:
        """Get state of flow block."""
    @property
    def alias(self) -> str | None:
        """Get alias of flow block."""
    @property
    def block(self) -> str:
        """Get type of block."""
    @property
    def execution_time(self) -> int | None:
        """Get execution time in ms."""
    def get_flow_task_report_block(self) -> FlowTaskReportBlock:
        """Create flow task report block object for json representation of report."""