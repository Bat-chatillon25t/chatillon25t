__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.tools.file_operation.path_helper import PathHelper as PathHelper

class CreateDirectory(FlowBlock):
    """Creates directory under the given path."""
    PAR__TARGET_PATH: str
    def get_parameter_definitions(self) -> set[ParameterDefinition]:
        """Get the definition for parameterization of the block."""
    def get_result_definition(self) -> ResultDefinition:
        """Returns the result_definition for this block."""