__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit import Flow as Flow
from flow_kit.core.flow.flow_builder_tracing import FlowBlockReference as FlowBlockReference, ParameterMappingReference as ParameterMappingReference
from flow_kit.core.validation.exceptions import MissingParameterMappingError as MissingParameterMappingError, ParameterMappingValidationError as ParameterMappingValidationError, StaticFlowValidationError as StaticFlowValidationError, UnknownBlockIdentifierError as UnknownBlockIdentifierError, UnknownParameterKeyError as UnknownParameterKeyError
from flow_kit.core.validation.validation_problem import ValidationProblem as ValidationProblem

class StaticFlowValidator:
    """Class for static checking of flow."""
    @classmethod
    def get_validation_problems(cls, flow: Flow) -> list[ValidationProblem]:
        """Returns all static validation problems found in the given flow."""
    @classmethod
    def validate_flow(cls, flow: Flow) -> None:
        """Validates a flow and throws an exception if an error occurs."""