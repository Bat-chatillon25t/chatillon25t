__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC
from collections.abc import Callable as Callable
from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.function_parser import FunctionParser as FunctionParser
from flow_kit.core.block.tool_id import ToolId as ToolId
from flow_kit.core.execution_engine.http_client_send_hook_callback import CallbackAlreadyRegisteredError as CallbackAlreadyRegisteredError, HttpClientSendEventInfo as HttpClientSendEventInfo, HttpClientSendHookCallback as HttpClientSendHookCallback

class UserCodeBlockBase(FlowBlock, ABC, metaclass=abc.ABCMeta):
    """Block that calculates parameter and result definition by given typing of a user_function."""
    def __init__(self, user_function: Callable, required_args: str = '', ignored_args: str = '') -> None: ...
    def get_parameter_definitions(self) -> set[ParameterDefinition]: ...
    def get_result_definition(self) -> ResultDefinition: ...