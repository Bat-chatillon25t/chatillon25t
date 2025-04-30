__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.tools.ecu_test.object_api import ObjectApi as ObjectApi

class GlobalConstantNameIsNotAStringError(Exception):
    """Exception that is raised if name of global constant is not a string."""
class GlobalConstantValueExpressionIsNotAStringError(Exception):
    """Exception that is raised if value expression of global constant is not a string."""

class CreateGcdFile(FlowBlock):
    """Create a global constants file.

    This block expects a running instance of ecu.test and does not start or stop ecu.test automatically.
    """
    PAR__GCD_PATH: str
    PAR__CONSTANTS: str
    PAR__ALLOW_OVERWRITE: str
    def get_parameter_definitions(self) -> set[ParameterDefinition]: ...
    def get_result_definition(self) -> ResultDefinition: ...