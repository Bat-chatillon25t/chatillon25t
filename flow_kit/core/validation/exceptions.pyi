__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from flow_kit.core.block.definitions.block_identifier import BlockIdentifier as BlockIdentifier
from flow_kit.core.flow.flow_builder_tracing import ElementReference as ElementReference, ParameterMappingReference as ParameterMappingReference
from flow_kit.core.flow.parameter_mapping import ParameterMapping as ParameterMapping
from flow_kit.core.validation.validation_problem import ValidationProblem as ValidationProblem

class CodeDefinitionLocalizableError(Exception):
    """Exception including a location reference to get reference to the code definition."""
    location_reference: ElementReference | None
    def __init__(self, message: str, location_reference: ElementReference | None = None) -> None: ...

class UnknownBlockIdentifierError(CodeDefinitionLocalizableError):
    """Exception that is raised, when an unknown BlockIdentifier is used."""
    def __init__(self, block_identifier: BlockIdentifier, location_reference: ElementReference | None = None) -> None: ...

class UnknownParameterKeyError(CodeDefinitionLocalizableError):
    """Exception that is raised, if block does not define a parameter with requested key."""
    def __init__(self, mapping: ParameterMapping, block_desc: str, location_reference: ElementReference | None = None) -> None: ...

class MissingParameterMappingError(CodeDefinitionLocalizableError):
    """Exception that is raised, if not all non-optional parameters have mappings defined."""
    def __init__(self, block_desc: str, missing_parameter_keys: set[str], location_reference: ElementReference | None = None) -> None: ...

class ParameterMappingValidationError(CodeDefinitionLocalizableError):
    """Exception raised, if the validation of a parameter mapping fails. Wraps the originally occurred exception."""
    exception: Incomplete
    __traceback__: Incomplete
    def __init__(self, exception: Exception, location_reference: ParameterMappingReference | None = None) -> None: ...

class StaticFlowValidationError(Exception):
    """Exception that is raised if any errors occur during static flow validation."""
    problems: Incomplete
    def __init__(self, problems: list[ValidationProblem]) -> None: ...

class MissingBatchMappingError(CodeDefinitionLocalizableError):
    """Exception that is rasied, when BatchProcessing is defined without usage of the batch item."""
    def __init__(self, location_reference: ElementReference | None = None) -> None: ...