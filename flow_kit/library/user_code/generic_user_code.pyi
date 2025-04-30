__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from collections.abc import Callable as Callable
from flow_kit.core.block.user_code_block_base import UserCodeBlockBase as UserCodeBlockBase

class GenericUserCode(UserCodeBlockBase):
    """Block that calculates any data by executing user code.

    The user code must be provided as a callable to the Block.
    This callable must have type hints for all arguments and for the return value.
    Based on this type hints the parameter definition and the result definition will be determined automatically.
    Arguments with default value will be treated as optional.
    The docstring will although be parsed to get description for the block and its parameters and return values.


    Example:
    # define the user code function
    def my_user_code(text: str, max_len: int = 100) -> str:
        '''Shorten long strings.

        :param text: Input string.
        :param max_len: Maximum length of output string.
        :return: Copy of input string with max length.
        '''
        if len(text) > max_len:
            return text[:max_len]
        else:
            return text

    # use user code block in a flow
    flow = (
        FlowBuilder()
        .add_block_with(
            GenericUserCode(my_user_code),
            WithStaticValueMapping('text', 'abc'),
            WithStaticValueMapping('max_len', 2),
        )
        .build()
    )
    """
    def __init__(self, user_function: Callable) -> None: ...