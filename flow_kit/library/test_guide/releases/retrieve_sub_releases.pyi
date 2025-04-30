__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.tools.test_guide.test_guide_block import TestGuideBlock as TestGuideBlock

class RetrieveSubReleases(TestGuideBlock):
    """test.guide ReleasesApi: Retrieve a releases direct sub releases (child releases)."""
    PAR__RELEASE_ID: str
    PAR__QUERY_PARAMETERS: str
    PAR__OFFSET: str
    PAR__LIMIT: str
    PAR__SORT: str
    PAR__DIR: str
    def get_result_definition(self) -> ResultDefinition: ...