__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from typing import Any

class JiraIssueFields:
    """Container for all fields of a Jira issue."""
    def __init__(self, dict_of_fields: dict[str, Any]) -> None: ...
    def keys(self) -> set[str]:
        """Returns dict of all available field keys."""
    def __getitem__(self, key: str) -> Any: ...
    def as_dict(self) -> dict[str, Any]: ...