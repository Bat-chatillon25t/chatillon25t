__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


class FlowSecretKeeper:
    """Class to clean strings of secrets that should not be revealed."""
    RELEVANT_PREFIX: str
    REPLACEMENT_VALUE: str
    def __init__(self) -> None: ...
    def tidy_up(self, in_value: str) -> str:
        """Remove protected values from string."""
    @classmethod
    def get_instance(cls) -> FlowSecretKeeper: ...
    @classmethod
    def reset(cls) -> None: ...