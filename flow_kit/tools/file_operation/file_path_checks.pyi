__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.tools.file_operation.path_helper import PathHelper as PathHelper
from pathlib import Path

class FilePathChecks:
    """Checks for validity of file pathes."""
    @staticmethod
    def target_path_check(target_path: Path, allow_overwrite: bool) -> None:
        """Checks that the given target_path can be used as a target_path for file operations."""