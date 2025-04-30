__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC, abstractmethod
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.definitions.type_check import TypeCheck as TypeCheck
from flow_kit.core.block.exceptions import AlreadyExecutedError as AlreadyExecutedError, BlockNotExecutedError as BlockNotExecutedError, ValueTypeMismatchError as ValueTypeMismatchError
from flow_kit.core.block.execution_info import ExecutionInfo as ExecutionInfo, TypeErrorExecutionInfo as TypeErrorExecutionInfo, UncaughtErrorExecutionInfo as UncaughtErrorExecutionInfo
from flow_kit.core.block.request_counter_utils import sum_request_counters as sum_request_counters
from flow_kit.core.block.tool_id import ToolId as ToolId
from flow_kit.core.reporting.report_inner_flow_run import ReportInnerFlowRun as ReportInnerFlowRun

class ExecutableBlock(ABC, metaclass=abc.ABCMeta):
    """Provides the possibility to execute a block and query the resulting result or errors."""
    def __init__(self) -> None: ...
    def execute(self) -> ExecutionInfo:
        """Runs this block and produces a result or at least do some work."""
    def was_executed(self) -> bool:
        """Returns if Block was executed."""
    def get_execution_info(self) -> ExecutionInfo:
        """Returns the ExecutionInfo if block was executed already.

        To ensure that an ExectionInfo is available, check was_executed() first.
        """
    @abstractmethod
    def get_result_definition(self) -> ResultDefinition:
        """Returns the result_definition for this block."""
    def get_inner_flows(self) -> list[ReportInnerFlowRun] | None:
        """Return the inner flows of this block.

        Implement this method to report inner flows of a block.
        """
    def increase_request_counter(self, tool_id: ToolId) -> None:
        """Increase the request counter for the given tool."""
    def get_request_counters(self) -> dict[ToolId, int]:
        """Get the requests this block executed."""