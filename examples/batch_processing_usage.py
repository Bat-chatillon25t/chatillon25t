"""BatchProcessing is a FlowBlock that applies a defined flow to each item of an input list/batch.

The BatchProcessing block returns a list containing the out_block results for the flow runs of all items of the
input list.

In order to use the BatchProcessing block a flow and an out_block need to be specified. The specification for both
elements in described in more detail below:
- flow: Flow is the sub-flow which is run one time for every item of the parameter "list" of the
           BatchProcessing block. The inner blocks of this sub-flow need to be defined the same way as overall
           flows of the flow-kit are defined.

- out_block: The out_block defines the block from which the result values are taken for the output of the
             BatchProcessing block. It must be a block contained in the sub-flow given by the flow defined
             in the constructor of BatchProcessing.

Connection of the parameters in the defined sub-flow with the flow containing this block:
Values from the containing flow you want to use in the flow contained in the BatchProcessing block need to be
passed as parameters into the BatchProcessing block. There are two ways values can be passed into the contained
flow of a BatchProcessing block:
- Parameter LIST: This parameter takes a list of items. The sub-flow of the BatchProcessing block is run one time
                  for every item of this list. The specific item for the run can be assigned to parameters of the
                  contained flow by assigning it with "Assign('<name>').to_batch_item()" .
- User-defined flow parameters: User-defined flow parameters are values whose values are available in all
                                   runs of the sub-flow inside the BatchProcessing block. Any number of
                                   user-defined flow parameters can be used for a BatchProcessing block.
                                   User-defined flow parameters are defined by assigning a value to a parameter
                                   with a user-defined name for the flow parameter on the instance of the
                                   BatchProcessing, e.g. Assign('<my_defined_parameter>').to_block_result(...).
"""

__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)

import logging

from flow_kit import Assign, Flow, FlowBuilder
from flow_kit.core import app
from flow_kit.library.control_flow import BatchProcessing
from flow_kit.library.user_code import GenericUserCode


def _produce_list() -> list[int]:
    """User defined function that produces a list of items.

    For each item of the produced list the inner flow will be executed once.
    """
    return [1, 2, 3]


def _produce_power() -> int:
    """User defined function that produces a fixed value.

    This value will be available to all executions of the inner flow.
    """
    return 2


def _process_list_item(number: int, power: int) -> int:
    """User defined function that processes a single item of a list.

    This function is called in each execution of the inner flow.
    """
    return number**power


def _consume_result_list(param: list[int]) -> None:
    """User defined function that consumes a list of processed items.

    This function is called with the list of the results of all executions of the inner flow of the BatchProcessing.
    """
    print(f'Consumed list {param}')  # noqa: T201


# fmt: off

def get_flow() -> Flow:
    """Define the flow to be executed."""
    return (

        # FlowBuilder for overall flow.
        FlowBuilder()

        # Add block that uses user function to produce a list of items.
        .add_block_with(list_producer_block := GenericUserCode(_produce_list).with_label('produce list'))

        # Add block that uses user function to produce a value.
        .add_block_with(power_producer_block := GenericUserCode(_produce_power).with_label('produce power'))

        # Add BatchProcess block that executes an inner flow to all items of a list.
        .add_block_with(
            batch_processing := BatchProcessing(  # type: ignore[abstract]

                ########################################################################################################
                # define the INNER FLOW also with the FlowBuilder                                                #
                FlowBuilder()

                # add a block to the inner flow
                .add_block_with(
                    flow_block := GenericUserCode(_process_list_item).with_label('CALCULATE POWER OF ITEMS'),

                    # link parameter number to one item of the list, which changes in each iteration
                    # this determines the value_type of the parameter PAR_LIST of the BatchProcessing block
                    Assign('number').to_batch_item(),

                    # link parameter power to parameter called var_power, which is constant in all iterations
                    # this adds a parameter called var_power to the BatchProcessing block and determines its value_type
                    Assign('power').to_flow_parameter('var_power'),
                ).build(),
                # end of the inner flow                                                                             #
                ########################################################################################################

                # define the block that marks the "end" of the inner flow, which contains the result items
                out_block=flow_block,

            ).with_label('Calculate power of each element.'),

            ############################################################################################################
            # Link the defined ports in the outer flow as with a normal block                                       #

            # PAR__LIST must always be present. Value type is determined by assignment to_batch_item() in inner flow.
            Assign(BatchProcessing.PAR__LIST).to_block_result(list_producer_block),

            # var_power must be present because it is defined via .to_flow_parameter('var_power') in inner flow.
            Assign('var_power').to_block_result(power_producer_block),

            # Multiple other flow parameters can be added here, if they are defined in inner flow.               #
            # Assign(...).to_....                                                                                      #
            ############################################################################################################
        )

        # Add a block that consumes the list of all results which are calculated by the BatchProcessing block.
        .add_block_with(
            GenericUserCode(_consume_result_list).with_label('consume result list'),

            # Block result of BatchProcessing is a list of all results of the defined out_block of inner flow.
            Assign('param').to_block_result(batch_processing),

        )
    ).build()

# fmt: on


# Run this file to execute the sample flow and see the result
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.main(get_flow(), execute=True)
