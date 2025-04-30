__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from collections.abc import Callable as Callable
from flow_kit.core.block.user_code_block_base import UserCodeBlockBase as UserCodeBlockBase
from flow_kit.tools.ecu_test.object_api import ObjectApi as ObjectApi

class ObjectApiUserCode(UserCodeBlockBase):
    """Run custom code with ecu.test ObjectApi.

    Given function must have an argument api which will be the ObjectApiClient.
    All other arguments and the return value must have type hints.

    This block expects a running instance of ecu.test and does not start or stop ecu.test automatically.
    """
    def __init__(self, user_function: Callable) -> None: ...