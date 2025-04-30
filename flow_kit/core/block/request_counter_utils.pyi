__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.tool_id import ToolId as ToolId

def sum_request_counters(*counters: dict[ToolId, int]) -> dict[ToolId, int]:
    """Function to sum up multiple requests counters."""