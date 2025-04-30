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
from flow_kit.tools.jira.jira_config import JiraConfig as JiraConfig

class MissingJiraAuthentificationError(Exception):
    """Exception that is raised, if authentification for JiraConfig is missing."""

class JiraInit(FlowBlock):
    """Block to test connection to jira and create jira config object for dependend blocks."""
    PAR__URL: str
    PAR__ENV_KEY_USER: str
    PAR__ENV_KEY_PASSWORD: str
    PAR__ENV_KEY_TOKEN: str
    def get_parameter_definitions(self) -> set[ParameterDefinition]: ...
    def get_result_definition(self) -> ResultDefinition: ...