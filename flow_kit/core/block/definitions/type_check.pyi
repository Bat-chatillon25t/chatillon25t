__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from flow_kit.core.block.exceptions import InvalidValueTypeError as InvalidValueTypeError, TypeDefinitionMismatchError as TypeDefinitionMismatchError, ValueTypeMismatchError as ValueTypeMismatchError
from typing import ClassVar

class TypeCheck:
    """Helper class to check types and values."""
    TYPE_ARG_COUNT: ClassVar[dict[type, int]]
    ALLOWED_TYPES_FROM_TYPING_MODULE: Incomplete
    @classmethod
    def ensure_valid_type(cls, type_value: type | None) -> None:
        """Checks that the given type_value is valid for use in the flow.kit."""
    @classmethod
    def match_type(cls, expected_type_value, type_value_to_check) -> None:
        """Check that the type_value_to_check matches the expected_type_value.

        This means that the type_value_to_check equals the expected_type_value or is a subclass is a subclass of it.
        """
    @classmethod
    def match_value(cls, type_value, value) -> None:
        """Check that the given value is of type type_value."""
    @classmethod
    def get_display_name_for_type(cls, python_type: type | None) -> str:
        """Gives a printable name for the python type."""
    @classmethod
    def get_annotation_string_for_type(cls, value_type_class: type | None) -> str:
        """Get string for type annotation to allowed types in flow.kit."""