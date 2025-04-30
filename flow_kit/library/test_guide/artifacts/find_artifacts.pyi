__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.tools.test_guide.test_guide_block import TestGuideBlock as TestGuideBlock

class FindArtifacts(TestGuideBlock):
    """test.guide ArtifactsApi: Find artifacts."""
    PAR__DEPOSITORY_ID: str
    PAR__ARTIFACT_ID: str
    PAR__START_DATE: str
    PAR__END_DATE: str
    PAR__LAST_ACCESS_START_DATE: str
    PAR__LAST_ACCESS_END_DATE: str
    PAR__FILE_NAME: str
    PAR__EXTENSION: str
    PAR__ATTRIBUTES: str
    PAR__HASH: str
    PAR__SHARED: str
    PAR__SHARE_ID: str
    PAR__LOCKED: str
    PAR__OFFSET: str
    PAR__LIMIT: str
    PAR__MIN_FILE_SIZE: str
    PAR__MAX_FILE_SIZE: str
    def get_result_definition(self) -> ResultDefinition: ...