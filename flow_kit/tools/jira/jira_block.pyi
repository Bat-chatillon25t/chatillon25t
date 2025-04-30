__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC, abstractmethod
from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.tool_id import ToolId as ToolId
from flow_kit.tools.jira.jira_api import JiraApi as JiraApi
from flow_kit.tools.jira.jira_config import JiraConfig as JiraConfig

class JiraBlock(FlowBlock, ABC, metaclass=abc.ABCMeta):
    """Abstract base class for all blocks that need to interact with jira."""
    PAR__JIRA_CONFIG: str
    @abstractmethod
    def get_action_parameter_definitions(self) -> set[ParameterDefinition]:
        """Get parameter definitions for implemented jira action."""
    def get_parameter_definitions(self) -> set[ParameterDefinition]: ...