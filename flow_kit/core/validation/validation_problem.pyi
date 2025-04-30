__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from dataclasses import dataclass
from flow_kit.core.flow.flow_builder_tracing import ElementReference as ElementReference, FlowBuilderTracing as FlowBuilderTracing

@dataclass
class ValidationProblem:
    """Container class for a problem found during static flow validation."""
    error: Exception
    location_reference: ElementReference | None = ...
    def get_representation(self) -> str:
        """Summarize this problem for logging."""