__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.tools.test_guide.test_guide_block import TestGuideBlock as TestGuideBlock

class DeleteCustomAttribute(TestGuideBlock):
    """test.guide Test_InfrastructureApi: Delete the custom attribute for the given ID.

    All associated custom attribute entries should be explicitly deleted.
    """
    PAR__CUSTOM_ATTRIBUTE_ID: str
    PAR__DELETE_ALL_ENTRIES: str
    def get_result_definition(self) -> ResultDefinition: ...