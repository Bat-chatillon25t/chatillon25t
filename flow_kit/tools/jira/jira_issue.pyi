__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.tools.jira.jira_issue_fields import JiraIssueFields as JiraIssueFields
from typing import Any

class InvalidIssueResponseError(Exception):
    """Raised when api response cannot be converted into an issue."""
    def __init__(self, missing_field: str | None = None) -> None: ...

class JiraIssue:
    """Wrapper object for Jira issues."""
    def __init__(self, properties: dict[str, Any]) -> None: ...
    @property
    def key(self) -> str:
        """Unique key of the issue."""
    @property
    def summary(self) -> str:
        """Convienence method to access 'summary' field of the issue."""
    @property
    def description(self) -> str:
        """Convienence method to access 'description' field of the issue."""
    def get_fields(self) -> JiraIssueFields:
        """Returns Accessable for the fields of the issue."""