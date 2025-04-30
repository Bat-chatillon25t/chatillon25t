__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from collections.abc import Callable as Callable
from dataclasses import dataclass

class CallbackAlreadyRegisteredError(Exception):
    """Exception raised if a callback was already added."""

@dataclass
class HttpClientSendEventInfo:
    """Object containing information for a http.client.send event."""
    valid_http_request_line: bool
    host: str | None
    full_message: str

class HttpClientSendHookCallback:
    """Class to hold an audit hook during execution time of a flow."""
    def __init__(self) -> None: ...
    def add_callback_function(self, callback_function: Callable[[HttpClientSendEventInfo], None]) -> None:
        """Adds a function to callback on an audit hook event."""
    def remove_callback_function(self) -> None:
        """Removes the set callback function."""
    @classmethod
    def get_instance(cls) -> HttpClientSendHookCallback: ...