__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr
from typing import Any

class FlowRequestCounter(BaseModel):
    """Model class for REST-API representation of a flow request counter."""
    tool: StrictStr
    number_of_requests: StrictInt
    def tool_validate_enum(cls, value):
        """Validates the enum."""
    model_config: Incomplete
    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """