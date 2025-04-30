__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from pathlib import PurePath

class PathHelper:
    """Utility class to hold helper methods for path handling."""
    LONG_PATH_PREFIX: str
    LONG_UNC_PATH_PREFIX: str
    @classmethod
    def extend_path(cls, path: PurePath) -> PurePath:
        """Extends pathes with headers to be interpreted as a long Windows path.

        It returns a Path object of the same as was passed into the function.
        """
    @classmethod
    def remove_long_path_prefix(cls, path: PurePath) -> PurePath:
        """Removes an existing prefix for long pathes from a given path.

        It returns a Path object of the same as was passed into the function.
        """