__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import datetime
from abc import ABC
from flow_kit.core.block.exceptions import ValueTypeMismatchError as ValueTypeMismatchError
from typing import Any

class ExecutionInfo(ABC):
    """Abstract class for all information that was created by one execution of a block."""
    is_error: bool
    def __init__(self, value: Any, start_time: datetime.datetime, end_time: datetime.datetime) -> None: ...
    def get_result_value(self) -> Any:
        """Get value of result."""
    def is_error_result(self) -> bool:
        """Tell if the block was interrupted by e.g. an error."""
    def get_error(self) -> Exception:
        """Returns an exception which was caught while executing."""
    def get_execution_time(self) -> datetime.timedelta:
        """Returns duration of block execution."""

class UncaughtErrorExecutionInfo(ExecutionInfo):
    """ExecutionInfo which captured any exception when a block is aborted by an uncaught exception."""
    is_error: bool
    def __init__(self, exception: Exception, start_time: datetime.datetime, end_time: datetime.datetime) -> None: ...
    def get_error(self) -> Exception:
        """Returns the caught Exception."""

class TypeErrorExecutionInfo(ExecutionInfo):
    """Result which is given, when result of a block does not match result_definition."""
    is_error: bool
    def __init__(self, type_error: ValueTypeMismatchError, start_time: datetime.datetime, end_time: datetime.datetime) -> None: ...
    def get_error(self) -> ValueTypeMismatchError:
        """Returns the ValueTypeMismatchError."""