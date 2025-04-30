__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from collections.abc import Callable as Callable
from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.exceptions import MissingParameterTypingError as MissingParameterTypingError, MissingRequiredParameterError as MissingRequiredParameterError, MissingReturnTypingError as MissingReturnTypingError

class FunctionParser:
    """Class to parse definition of parameters and return value from function."""
    def __init__(self, func: Callable, required_args: str = '', ignored_args: str = 'self') -> None:
        """Constructor.

        :param func: function to parse.
        :param required_args: arguments of this function that must be defined.
        :param ignored_args: arguments of this function that should not be included in parameter_definitions.
        """
    @staticmethod
    def extract_nested_type(type_annotation: type) -> type:
        """Extract type from Container types like Optional and Annotated."""
    def get_parameter_definitions(self) -> list[ParameterDefinition]:
        """Returns set of ParameterDefinition-objects."""
    def get_result_definition(self) -> ResultDefinition:
        """Returns ResultDefinition-object."""