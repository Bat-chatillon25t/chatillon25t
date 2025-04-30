__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit import Flow as Flow
from flow_kit.core.execution_engine.execution_engine import ExecutionEngine as ExecutionEngine
from flow_kit.core.flow.exceptions import FlowAbortedError as FlowAbortedError
from flow_kit.core.reporting.reporting_engine import FlowResult as FlowResult, ReportingEngine as ReportingEngine
from flow_kit.core.validation.exceptions import StaticFlowValidationError as StaticFlowValidationError
from flow_kit.core.visualization.flow_plotter import FlowPlotter as FlowPlotter

def main(flow: Flow, *, validate: bool = True, execute: bool = False, visualize: bool = False) -> None:
    """Main function for running flow kit flows.

    :param flow: flow to run
    :param validate: flag to validate the flow
    :param execute: flag to execute the flow (will also validate)
    :param visualize: flag to visualize the flow as puml file
    """