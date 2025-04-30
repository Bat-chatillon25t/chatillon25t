__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from enum import Enum
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.block.tool_id import ToolId as ToolId
from flow_kit.core.flow.flow import Flow as Flow
from flow_kit.core.reporting.json_report.models.flow_request_counter import FlowRequestCounter as FlowRequestCounter
from flow_kit.core.reporting.json_report.models.flow_task_report import FlowTaskReport as FlowTaskReport
from flow_kit.core.reporting.json_report.models.flow_task_report_summary_flow_source import FlowTaskReportSummaryFlowSource as FlowTaskReportSummaryFlowSource
from flow_kit.core.reporting.json_report.models.flow_task_state import FlowTaskState as FlowTaskState
from flow_kit.core.reporting.report_flow_block import ReportFlowBlock as ReportFlowBlock
from flow_kit.core.validation.exceptions import StaticFlowValidationError as StaticFlowValidationError

FlowReport = str
REPORT_PATH: Incomplete

class FlowResult(Enum):
    """Possible flow results."""
    ABORTED = 0
    SKIPPED = 1
    FINISHED = 2

class ReportingEngine:
    """Reporting engine for flows."""
    def __init__(self, flow: Flow) -> None: ...
    def get_report_for_block(self, flow_block: FlowBlock) -> ReportFlowBlock:
        """Get report for given block."""
    def get_text_report_for_block(self, flow_block: FlowBlock, indent_level: int, width: int = 200) -> list[str]:
        """Get text report for given block."""
    def get_overall_text_report(self) -> FlowReport:
        """Get generated overall report."""
    def get_overall_result(self) -> FlowResult | None:
        """Get the aggregated overall result of the flow."""
    def create_json_report(self, e: StaticFlowValidationError | None = None) -> None:
        """Create the report as JSON file report.json in working directory."""