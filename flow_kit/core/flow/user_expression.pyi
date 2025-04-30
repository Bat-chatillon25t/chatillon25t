__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.flow.exceptions import UserExpressionResolutionError as UserExpressionResolutionError, UserExpressionSyntaxError as UserExpressionSyntaxError
from typing import Any

def get_safe_builtins() -> dict:
    """Returns dict with builtins that could be used in user expression code."""

class UserExpression:
    """Class to hold a user defined expression."""
    def __init__(self, expression: str) -> None: ...
    def check_syntax(self) -> None:
        """Check for syntax errors in expression."""
    def get_expression(self) -> str:
        """Return expression.."""
    def replace_alias(self, old: str, new: str) -> None:
        """Replaces alias."""
    def resolve(self, alias_to_result_value: dict[str, Any]) -> Any:
        """Resolve expression with given result mappings."""
    def get_identifiers(self) -> set[str]:
        """Return all used identifiers."""