__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit import Flow as Flow
from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.state.block_event import BlockEvent as BlockEvent
from flow_kit.core.block.state.block_state import BlockState as BlockState
from flow_kit.core.execution_engine.execution_engine import ExecutionEngine as ExecutionEngine
from flow_kit.core.flow.exceptions import FlowParameterNotFoundError as FlowParameterNotFoundError, InnerFlowOutBlockAbortedError as InnerFlowOutBlockAbortedError
from flow_kit.core.flow.flow_builder_tracing import FlowBlockReference as FlowBlockReference
from flow_kit.core.flow.flow_parameter import FlowParameter as FlowParameter, FlowParameterCollection as FlowParameterCollection
from flow_kit.core.flow.parameter_mapping import BatchItemMapping as BatchItemMapping
from flow_kit.core.reporting.report_inner_flow_run import ReportInnerFlowRun as ReportInnerFlowRun
from flow_kit.core.validation.exceptions import MissingBatchMappingError as MissingBatchMappingError
from flow_kit.core.validation.static_flow_validator import StaticFlowValidator as StaticFlowValidator
from flow_kit.core.validation.validation_problem import ValidationProblem as ValidationProblem

class BatchProcessing(FlowBlock):
    """Special FlowBlock that applies a defined sub-flow to each element of a stack."""
    PAR__LIST: str
    def __init__(self, flow: Flow, *, out_block: FlowBlock) -> None:
        """Creates a BatchProcessing block.

        :param flow: Inner flow that is repeated for each item of the given batch.
        :param out_block: Block that is part of the inner flow.
            The result values of all iterations of this block
            will be returned as result value of the BatchProcess block.
            Even if no result must be processed after the batch processing, this block must be given to
            determine the state after execution.
        """
    def get_inner_flows(self) -> list[ReportInnerFlowRun]:
        """Return the inner flow runs.

        :return: list of inner flow reports
        """
    def get_parameter_definitions(self) -> set[ParameterDefinition]:
        """Returns parameter definition as collection of requested flow parameters and the batch to work on.

        The needed parameters are given by the flow parameters of the inner flow.
        """
    def get_result_definition(self) -> ResultDefinition:
        """Returns result definition as list of results of the defined out_block.

        The result value type will be a list of the result value type of the out_block.
        """
    def validate(self) -> list[ValidationProblem]:
        """Validates the sub-flow which is defined in this block."""