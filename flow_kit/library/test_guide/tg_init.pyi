__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.tools.env_vars import get_env_var_value as get_env_var_value
from flow_kit.tools.test_guide.test_guide_config import ENV_VAR_DEFAULT_AUTH_KEY as ENV_VAR_DEFAULT_AUTH_KEY, ENV_VAR_DEFAULT_PROJECT_ID as ENV_VAR_DEFAULT_PROJECT_ID, ENV_VAR_DEFAULT_URL as ENV_VAR_DEFAULT_URL, TestGuideConfig as TestGuideConfig

class TGInit(FlowBlock):
    """Block to initialize connection to test.guide."""
    PAR__URL: str
    PAR__PROJECT_ID: str
    PAR__ENV_AUTH_KEY: str
    def get_parameter_definitions(self) -> set[ParameterDefinition]:
        """Get parameter definitions for this block."""
    def get_result_definition(self) -> ResultDefinition:
        """This block will return a TestGuideConfig object."""