__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.tools.test_guide.test_guide_block import TestGuideBlock as TestGuideBlock

class ProjectFilterTestCaseExecutions(TestGuideBlock):
    """test.guide Report_MgmtApi: Get test case executions of the specified project filter."""
    PAR__FILTER_ID: str
    PAR__OFFSET: str
    PAR__LIMIT: str
    def get_result_definition(self) -> ResultDefinition: ...