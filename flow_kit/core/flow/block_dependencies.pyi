__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from dataclasses import dataclass
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.flow.exceptions import CyclicDependencyError as CyclicDependencyError
from typing import Self

@dataclass(frozen=True, eq=True)
class BlockDependency:
    """Presents the dependency of one block on another."""
    dependent: BlockIdentifier
    required: BlockIdentifier
    def __init__(self, *, dependent: BlockIdentifier | FlowBlock, required: BlockIdentifier | FlowBlock) -> None: ...

class BlockDependencies:
    """Manage dependencies between flow blocks."""
    def __init__(self, dependencies: dict[BlockIdentifier, set[BlockDependency]]) -> None: ...
    def get_block_dependencies(self, dependent_identifier: BlockIdentifier) -> set[BlockDependency]:
        """Returns all dependencies for a block with the given ID."""

class BlockDependenciesBuilder:
    """Builder for a :py:class:`BlockDependencies`."""
    def __init__(self) -> None: ...
    def add_dependency(self, dependency: BlockDependency) -> Self:
        """Adds a dependency of a block."""
    def build(self) -> BlockDependencies:
        """Builds the :py:class:`BlockTransitionSet`."""