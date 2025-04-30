__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.tools import env_vars as env_vars

class TimeControlledTrigger(FlowBlock):
    """Block that provides payload of a time controlled trigger."""
    def get_parameter_definitions(self) -> set[ParameterDefinition]:
        """Get parameter definitions for this block."""
    def get_result_definition(self) -> ResultDefinition:
        """This block will return the TimeTriggerPayload."""