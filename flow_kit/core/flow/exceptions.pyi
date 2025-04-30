__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.flow.parameter_mapping import FlowParameterMapping as FlowParameterMapping

class AliasNameFormatError(Exception):
    """Exception that is raised, on setting alias with wrong name format."""
class ForbiddenAliasNameError(Exception):
    """Exception that is raised, when builtin names are used as alias."""
class UnknownAliasError(Exception):
    """Exception that is raised, when requesting an alias that is not present."""
class CyclicDependencyError(Exception):
    """Exception that is raised, when a circular dependency of blocks is detected."""

class BlockIdentifierNotUniqueError(Exception):
    """Exception that is raised when a block is used more than once."""
    def __init__(self, block_identifier: BlockIdentifier) -> None: ...

class ResultNotPresentError(Exception):
    """Error that no result is registered for the given identifier in the ResultMapping."""
class UserExpressionSyntaxError(Exception):
    """Exception that is raised on SyntaxError in user defined expression."""
class UserExpressionResolutionError(Exception):
    """Exception that is raised if resolving a user expression results in an exception."""
class FlowAbortedError(Exception):
    """Exception that is raised, if a flow got aborted, when a flow block got aborted."""
class FlowParameterNotFoundError(Exception):
    """Exception that is raised, if a flow parameter is requested, that was not created before."""
class FlowParameterAlreadyPresentError(Exception):
    """Exception that is raised, if a flow parameter with a key is created, that is already present."""
class FlowParameterNotSuppliedError(Exception):
    """Exception that is raised, if a flow parameter value for a key is requested, that is not supplied."""

class ReservedFlowParameterNameError(Exception):
    """Exception that is raised, if a reserved flow_parameter_name is used in a FlowParameterMapping."""
    def __init__(self, flow_parameter_mapping_type: type['FlowParameterMapping']) -> None: ...

class InnerFlowOutBlockAbortedError(Exception):
    """Exception that is raised, if the out_blocks of the inner flow of a block are ABORTED."""