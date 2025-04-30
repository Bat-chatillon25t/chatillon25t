__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.tools.jira.jira_api import JiraApi as JiraApi
from flow_kit.tools.jira.jira_block import JiraBlock as JiraBlock
from flow_kit.tools.jira.jira_issue import JiraIssue as JiraIssue

class JiraJql(JiraBlock):
    """Search jira issues by JQL."""
    PAR__JQL: str
    def get_action_parameter_definitions(self) -> set[ParameterDefinition]: ...
    def get_result_definition(self) -> ResultDefinition: ...