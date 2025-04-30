__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.tools.file_operation.file_path_checks import FilePathChecks as FilePathChecks
from flow_kit.tools.file_operation.path_helper import PathHelper as PathHelper
from flow_kit.tools.test_guide.test_guide_block import TestGuideBlock as TestGuideBlock

class DownloadReport(TestGuideBlock):
    """test.guide ReportingApi: Download result of report generation."""
    PAR__TASK_ID: str
    PAR__TARGET_PATH: str
    PAR__ALLOW_OVERWRITE: str
    def get_result_definition(self) -> ResultDefinition: ...