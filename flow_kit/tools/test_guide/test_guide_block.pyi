__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC
from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.tool_id import ToolId as ToolId
from flow_kit.tools.test_guide.test_guide_config import DefaultTestGuideConfig as DefaultTestGuideConfig, TestGuideConfig as TestGuideConfig
from functools import cached_property as cached_property

class TestGuideBlock(FlowBlock, ABC, metaclass=abc.ABCMeta):
    """Abstract base class for all blocks that need to interact with test.guide."""
    PAR__TG_CONFIG: str
    def get_parameter_definitions(self) -> set[ParameterDefinition]: ...
    @cached_property
    def tg_config(self) -> TestGuideConfig: ...

class TgConfigParameterDefinition(ParameterDefinition):
    """Special parameter definition for TestGuideConfig."""
    @property
    def default_value(self) -> TestGuideConfig:
        """Implement default value as property."""
    @default_value.setter
    def default_value(self, _: TestGuideConfig) -> None:
        """Setter must be implemented because default_value is field of a dataclass in base ParameterDefinition."""