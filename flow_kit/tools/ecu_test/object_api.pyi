__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import psutil
import re
from dataclasses import dataclass

class EcuTestIsNotRunningError(Exception):
    """Exception that is raised if ecu.test is not running."""
class MissingApiClientDirInEcuTestInstallationError(Exception):
    """Exception that is raised if ApiClient dir cannot be found in ecu.test-installation."""
class UnsupportedPlatformError(Exception):
    """Exception that is raised on unsupported platforms."""

@dataclass
class SearchCriteria:
    """Dataclass to define search criteria for process."""
    name: re.Pattern
    cmdline: re.Pattern
    def get_attr_names(self) -> list[str]:
        """Returns used attribute names."""
    def match_process(self, process: psutil.Process) -> bool:
        """Returns true if all criterias match for this process."""

class ObjectApi:
    """Helper class to get access to the object api of ecu.test."""
    @classmethod
    def get_instance(cls) -> ApiClient:
        """Get instance of object api."""
    @classmethod
    def get_ecu_test_executable_currently_running(cls) -> str:
        """Get executable path of currently running ecu.test process."""
    @staticmethod
    def get_api_client_dir_from_ecu_test_exe(path_ecu_test_exe: str) -> str:
        """Get path to api client from path to ecu.test executable."""