__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.execution_info import ExecutionInfo as ExecutionInfo
from flow_kit.core.reporting.flow_secret_keeper import FlowSecretKeeper as FlowSecretKeeper
from flow_kit.core.reporting.report_item_base import ReportItemBase as ReportItemBase

class ReportResult(ReportItemBase):
    """Class for reporting of parameters."""
    def __init__(self, result_definition: ResultDefinition, execution_result: ExecutionInfo | None) -> None: ...
    @property
    def value_type(self) -> str:
        """Returns type name of the value of result definition."""
    @property
    def result_error(self) -> str:
        """Returns representation of error."""
    @property
    def result_value(self) -> str:
        """Returns representation of result value."""