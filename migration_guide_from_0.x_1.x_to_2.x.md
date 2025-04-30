# Migration guide from version 0.x and 1.x to version 2.x

To streamline our wording `process` got renamed to `flow`. This includes classes, parameters and files. 

This makes the following changes to existing `process_definition.py` files necessary:
* Change filename of `process_definition.py` to `flow_definition.py`.
* Change function name `get_process()` to `get_flow()`.
* In imports and usage change the following class names:
  * `Process` -> `Flow`
  * `ProcessBuilder` -> `FlowBuilder`
* If you use BatchProcessing, the following changes are necessary:
  * `Assign.to_process_parameter` -> `Assing.to_flow_parameter`
  * If you used the argument `process` as keyword argument, when creating a BatchProcessingBlock instance:
    * `BatchProcessing(process=<...>, out_block=<...>) `-> `BatchProcessing(flow=<...>, out_block=<...>)`
