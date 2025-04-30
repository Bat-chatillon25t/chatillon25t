__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from collections.abc import Iterable
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.flow.parameter_mapping import ParameterMapping as ParameterMapping

class ParameterMappingSet:
    """Collects a set parameter mappings for flow blocks."""
    def __init__(self, mappings: Iterable[ParameterMapping]) -> None: ...
    def get_parameters_by_block_identifier(self, block_identifier: BlockIdentifier) -> set[ParameterMapping]:
        """Get all parameters for block with identifier."""
    def get_all_block_identifier(self) -> set[BlockIdentifier]:
        """Get all block identifier for which paramter mappings are present."""