__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.execution_info import ExecutionInfo as ExecutionInfo
from flow_kit.core.flow.alias_mapping import AliasMapping as AliasMapping
from flow_kit.core.flow.exceptions import ResultNotPresentError as ResultNotPresentError
from typing import Any

class ResultMapping:
    """Contains the relation between the identifier and the result of a block."""
    def __init__(self, mapping: dict[BlockIdentifier, ExecutionInfo], alias_mapping: AliasMapping) -> None: ...
    def get_result_by_identifier(self, identifier: BlockIdentifier) -> ExecutionInfo:
        """Returns the block result for the given block identifier."""
    def get_result_value_by_alias(self, alias: str) -> Any:
        """Returns value of block result for given alias."""