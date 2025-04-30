__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.executable_block import ExecutableBlock as ExecutableBlock
from flow_kit.core.block.human_friendly_block import HumanFriendlyBlock as HumanFriendlyBlock
from flow_kit.core.block.parametrized_block import ParameterizedBlock as ParameterizedBlock
from flow_kit.core.block.stateable_block import StateableBlock as StateableBlock
from flow_kit.core.reporting.json_report.models.flow_task_report_block_interaction import FlowTaskReportBlockInteraction as FlowTaskReportBlockInteraction
from flow_kit.core.validation.validation_problem import ValidationProblem as ValidationProblem
from typing import Self

class FlowBlock(ParameterizedBlock, StateableBlock, ExecutableBlock, HumanFriendlyBlock, ABC, metaclass=abc.ABCMeta):
    """Generic block for flow steps."""
    def __init__(self) -> None: ...
    def get_identifier(self) -> BlockIdentifier:
        """Get BlockIdentifier."""
    def get_summary(self) -> str:
        """Get summary for simple reporting."""
    def validate(self) -> list[ValidationProblem]:
        """Validates an instantiated block."""
    def copy(self) -> Self:
        """Creates a copy of this FlowBlock with a reset execution state."""
    def get_interactions(self) -> list[FlowTaskReportBlockInteraction]:
        """Overwrite this method to provide block specific interactions."""