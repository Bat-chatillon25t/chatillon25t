__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from _typeshed import Incomplete
from pydantic import BaseModel, StrictStr as StrictStr
from typing import Any

class FlowTaskReportBlockInteraction(BaseModel):
    """Model class for REST-API representation of an interactions of a block to be displayed as hyperlink."""
    url: StrictStr
    text: StrictStr
    interaction: StrictStr | None
    target_type: StrictStr | None
    def interaction_validate_enum(cls, value):
        """Validates the enum."""
    def target_type_validate_enum(cls, value):
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