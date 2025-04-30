__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.flow.exceptions import AliasNameFormatError as AliasNameFormatError, ForbiddenAliasNameError as ForbiddenAliasNameError, UnknownAliasError as UnknownAliasError
from flow_kit.core.flow.user_expression import get_safe_builtins as get_safe_builtins

class AliasMapping:
    """Implementation of a mapping of aliases for BlockIdentifiers."""
    ALIAS_PATTERN: Incomplete
    def __init__(self, mappings: dict[str, BlockIdentifier]) -> None: ...
    def is_alias_present(self, alias: str) -> bool:
        """True if alias is already present in this flow."""
    def get_identifier_by_alias(self, alias: str) -> BlockIdentifier:
        """Returns block identifier for given alias."""
    @classmethod
    def match_alias_pattern(cls, alias: str) -> None:
        """Raise exception on wrong format."""
    @staticmethod
    def check_alias_shadows_builtin(alias: str) -> None:
        """Warns if alias name shadows python builtin name."""
    def get_alias(self, block: FlowBlock) -> str | None:
        """Returns the alias for a block."""