__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.execution_engine.block_executor import BlockExecutor as BlockExecutor
from flow_kit.core.execution_engine.engine_states import EngineStates as EngineStates
from flow_kit.core.flow.flow import Flow as Flow
from flow_kit.core.validation.exceptions import StaticFlowValidationError as StaticFlowValidationError
from flow_kit.core.validation.static_flow_validator import StaticFlowValidator as StaticFlowValidator

class ExecutionEngine:
    """execution engine for FlowBlocks."""
    def __init__(self, flow: Flow) -> None: ...
    def get_state(self) -> EngineStates:
        """Get current state of ExecutionEngine."""
    def validate(self) -> None:
        """Validate flow."""
    def execute(self) -> None:
        """Run ExecutionEngine."""
    def is_finished(self) -> bool:
        """True if Queue with BlockIdentifier for execution is empty."""