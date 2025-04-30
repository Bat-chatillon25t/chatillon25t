__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from collections.abc import Generator
from flow_kit.tools.env_vars import get_env_var_value as get_env_var_value
from tg_api_clients import artifacts, execution, health, platform, q_gates, releases, report_mgmt, reporting, test_infrastructure, user_mgmt

ENV_VAR_DEFAULT_AUTH_KEY: str
ENV_VAR_DEFAULT_PROJECT_ID: str
ENV_VAR_DEFAULT_URL: str

class TestGuideConnectionError(Exception):
    """Exception that is raised, when test.guide access is not possible."""

class TestGuideConfig:
    """Dataclass for config of test.guide-access."""
    def __init__(self, url: str, project_id: int, auth_key: str) -> None: ...
    def __hash__(self): ...
    def __eq__(self, other) -> bool: ...
    @property
    def project_id(self) -> int:
        """Returns the test.guide projectId."""
    @property
    def url(self) -> str:
        """Returns the test.guide url."""
    def check_server_health(self) -> None:
        """Check if test.guide instance is live and ready."""
    def get_health_api(self) -> Generator[health.HealthApi, None, None]:
        """Get health API instance."""
    def get_user_mgmt_api(self) -> Generator[user_mgmt.UserApi, None, None]:
        """Get user management API instance."""
    def get_artifacts_api(self) -> Generator[artifacts.ArtifactsApi, None, None]:
        """Get artifacts API instance."""
    def get_execution_tasks_api(self) -> Generator[execution.ExecutionTasksApi, None, None]:
        """Get execution tasks API instance."""
    def get_playbooks_api(self) -> Generator[execution.PlaybooksApi, None, None]:
        """Get playbooks API instance."""
    def get_playbook_folders_api(self) -> Generator[execution.PlaybookFoldersApi, None, None]:
        """Get playbook folders API instance."""
    def get_qgates_api(self) -> Generator[q_gates.QgatesApi, None, None]:
        """Get q-gates API instance."""
    def get_releases_api(self) -> Generator[releases.ReleasesApi, None, None]:
        """Get releases API instance."""
    def get_report_api(self) -> Generator[report_mgmt.ReportApi, None, None]:
        """Get report API instance."""
    def get_testcase_api(self) -> Generator[report_mgmt.TestcaseApi, None, None]:
        """Get testcase API instance."""
    def get_export_api(self) -> Generator[report_mgmt.ExportApi, None, None]:
        """Get export API instance."""
    def get_statistic_api(self) -> Generator[report_mgmt.StatisticApi, None, None]:
        """Get statistic API instance."""
    def get_atx_api(self) -> Generator[report_mgmt.AtxApi, None, None]:
        """Get statistic API instance."""
    def get_reporting_api(self) -> Generator[reporting.ReportingApi, None, None]:
        """Get reporting API instance."""
    def get_platform_api(self) -> Generator[platform.PlatformApi, None, None]:
        """Get platform API instance."""
    def get_test_resources_api(self) -> Generator[test_infrastructure.TestResourcesApi, None, None]:
        """Get test resource API instance."""
    def get_test_resource_machines_api(self) -> Generator[test_infrastructure.TestResourceMachinesApi, None, None]:
        """Get test resource machine API instance."""
    def get_custom_attributes_api(self) -> Generator[test_infrastructure.CustomAttributesApi, None, None]:
        """Get custom attributes API instance."""
    def get_custom_attribute_entries_api(self) -> Generator[test_infrastructure.CustomAttributeEntriesApi, None, None]:
        """Get custom attribute entries API instance."""

class TestGuideConfigInitError(Exception):
    """Exception that is raised if default config could not be initialized."""
    def __init__(self, exception: Exception) -> None: ...

class DefaultTestGuideConfig:
    """Class that creates and holds a default test.guide config."""
    @classmethod
    def get(cls) -> TestGuideConfig:
        """Get instance of the default config."""
    @classmethod
    def reset(cls) -> None:
        """Reset class."""