__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.tools.jira.jira_config import JiraConfig as JiraConfig
from flow_kit.tools.jira.jira_issue import JiraIssue as JiraIssue
from flow_kit.tools.jira.jira_issue_fields import JiraIssueFields as JiraIssueFields

class JiraApi:
    """Wrapper for 3rd-party jira lib to set typing for code generation."""
    def __init__(self, jira_config: JiraConfig) -> None: ...
    def get_issue(self, issue_key: str) -> JiraIssue:
        """Get issue from jira.

        :param issue_key: Key of jira issue.
        :return: Jira issue.
        """
    def add_issue_comment(self, issue_key: str, message: str) -> None:
        """Adds a comment to a jira issue.

        :param issue_key: Key of the issue.
        :param message: Message for the comment.
        """
    def assign_issue(self, issue_key: str, user: str) -> None:
        """Assign jira issue to user.

        :param issue_key: Key of the jira issue.
        :param user: AccountId of the user. Use empty string for unassigned.
        """
    def issue_transition(self, issue_key: str, status: str) -> None:
        """Transition jira issue to given state.

        :param issue_key: Key of the jira issue.
        :param status: Target state.
        """
    def jql(self, jql: str) -> list[JiraIssue]:
        """Search jira issues by JQL.

        :param jql: JQL to search issues.
        :return: list of jira issues.
        """
    def edit_issue(self, issue_key: str, fields: JiraIssueFields) -> None:
        """Edit fields of jira issue.

        :param issue_key: Key of the jira issue.
        :param fields: Fields to update.
        """