__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.reporting.json_report.models.flow_task_report_block_error import FlowTaskReportBlockError as FlowTaskReportBlockError
from flow_kit.core.reporting.json_report.models.flow_task_report_block_inner_flow import FlowTaskReportBlockInnerFlow as FlowTaskReportBlockInnerFlow
from flow_kit.core.reporting.json_report.models.flow_task_report_block_interaction import FlowTaskReportBlockInteraction as FlowTaskReportBlockInteraction
from flow_kit.core.reporting.json_report.models.flow_task_report_block_parameter import FlowTaskReportBlockParameter as FlowTaskReportBlockParameter
from flow_kit.core.reporting.json_report.models.flow_task_report_block_result import FlowTaskReportBlockResult as FlowTaskReportBlockResult
from flow_kit.core.reporting.json_report.models.flow_task_report_block_state import FlowTaskReportBlockState as FlowTaskReportBlockState
from pydantic import BaseModel, StrictStr as StrictStr
from typing import Any

class FlowTaskReportBlock(BaseModel):
    """Model class for REST-API representation of a flow task report block."""
    label: StrictStr | None
    result_alias: StrictStr | None
    block_type: StrictStr | None
    block_state: FlowTaskReportBlockState
    block_identifier: StrictStr | None
    required_blocks: list[StrictStr]
    parameters: list[FlowTaskReportBlockParameter]
    result: FlowTaskReportBlockResult
    inner_flows: list[FlowTaskReportBlockInnerFlow] | None
    error: FlowTaskReportBlockError | None
    interactions: list[FlowTaskReportBlockInteraction]
    def block_state_validate_enum(cls, value: str) -> str | None:
        """Validates the enum."""
    model_config: Incomplete
    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """