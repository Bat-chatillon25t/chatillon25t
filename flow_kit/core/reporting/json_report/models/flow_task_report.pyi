__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from flow_kit.core.reporting.json_report.models.flow_task_report_block import FlowTaskReportBlock as FlowTaskReportBlock
from flow_kit.core.reporting.json_report.models.flow_task_report_summary import FlowTaskReportSummary as FlowTaskReportSummary
from pydantic import BaseModel
from typing import Any

class FlowTaskReport(BaseModel):
    """Model class for REST-API representation of a flow task report.

    This and other model classes generate a json report which can be uploaded as is to the test.guide REST-API.
    """
    blocks: list[FlowTaskReportBlock]
    summary: FlowTaskReportSummary
    model_config: Incomplete
    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias."""
    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """