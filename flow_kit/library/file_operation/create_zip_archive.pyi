__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.block.flow_block import FlowBlock as FlowBlock
from flow_kit.core.block.parametrized_block import ParameterDefinition as ParameterDefinition
from flow_kit.tools.file_operation.path_helper import PathHelper as PathHelper

class CreateZipArchive(FlowBlock):
    """Creates a Zip archive of all files inside a given folder."""
    ARCHIVE_EXTENSION: str
    PAR__CONTENT_FOLDER_PATH: str
    PAR__TARGET_PATH: str
    PAR__ALLOW_OVERWRITE: str
    def get_result_definition(self) -> ResultDefinition:
        """Returns the result_definition for this block."""
    def get_parameter_definitions(self) -> set[ParameterDefinition]:
        """Get the definition for parameterization of the block."""