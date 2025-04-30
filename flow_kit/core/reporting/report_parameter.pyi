__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import BlockParameter as BlockParameter, ParameterDefinition as ParameterDefinition
from flow_kit.core.reporting.flow_secret_keeper import FlowSecretKeeper as FlowSecretKeeper
from flow_kit.core.reporting.report_item_base import ReportItemBase as ReportItemBase

class ReportParameter(ReportItemBase):
    """Class for reporting of parameters."""
    def __init__(self, parameter_definition: ParameterDefinition, block_parameter: BlockParameter | None) -> None: ...
    @property
    def parameter_key(self) -> str:
        """Get key of parameter."""
    @property
    def value_type(self) -> str:
        """Get name of value_type of parameter."""
    @property
    def resolved_text_repr_of_value(self) -> str:
        """Get resolved value text representation of parameter."""
    @property
    def resolved_value(self) -> str | None:
        """Get resolved value of parameter."""
    @property
    def has_error_while_resolution(self) -> bool:
        """True if error occurred in parameter resolution."""