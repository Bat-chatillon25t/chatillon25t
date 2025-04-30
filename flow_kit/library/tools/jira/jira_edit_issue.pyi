__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.reporting.interactions import Interaction as Interaction
from flow_kit.core.reporting.json_report.models.flow_task_report_block_interaction import FlowTaskReportBlockInteraction as FlowTaskReportBlockInteraction
from flow_kit.tools.jira.jira_api import JiraApi as JiraApi
from flow_kit.tools.jira.jira_block import JiraBlock as JiraBlock
from flow_kit.tools.jira.jira_config import JiraConfig as JiraConfig
from flow_kit.tools.jira.jira_issue_fields import JiraIssueFields as JiraIssueFields

class JiraEditIssue(JiraBlock):
    """Edit fields of jira issue."""
    PAR__ISSUE_KEY: str
    PAR__FIELDS: str
    def get_action_parameter_definitions(self) -> set[ParameterDefinition]: ...
    def get_result_definition(self) -> ResultDefinition: ...
    def get_interactions(self) -> list[FlowTaskReportBlockInteraction]: ...