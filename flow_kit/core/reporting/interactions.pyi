__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import dataclasses
from flow_kit.core.reporting.json_report.models.flow_task_report_block_interaction import FlowTaskReportBlockInteraction as FlowTaskReportBlockInteraction
from flow_kit.tools.jira.jira_config import JiraConfig as JiraConfig
from flow_kit.tools.test_guide.test_guide_config import TestGuideConfig as TestGuideConfig
from flow_kit.tools.url_builder import build_url as build_url
from typing import Self

@dataclasses.dataclass
class Interaction:
    """Base class for fluent API to create FlowTaskReportBlockInteraction."""
    url: str | None = ...
    text: str | None = ...
    action: str = ...
    target_type: str = ...
    @property
    def create(self) -> Self:
        """Set action type to CREATE."""
    @property
    def link(self) -> Self:
        """Set action type to LINK."""
    @property
    def update(self) -> Self:
        """Set action type to UPDATE."""
    @property
    def user(self) -> Self:
        """Set action type to USER."""
    def release(self, tg_config: TestGuideConfig, release_id: int) -> Self:
        """Interaction with a release."""
    def artifact(self, tg_config: TestGuideConfig, artifact_id: str) -> Self:
        """Interaction with an artifact."""
    def execution_task(self, tg_config: TestGuideConfig, task_id: int) -> Self:
        """Interaction with an execution task."""
    def playbook(self, tg_config: TestGuideConfig, playbook_id: int) -> Self:
        """Interaction with a playbook."""
    def qgate_plan(self, tg_config: TestGuideConfig, plan_key: str) -> Self:
        """Interaction with a q-gate plan."""
    def tce(self, tg_config: TestGuideConfig, tce_id: int) -> Self:
        """Interaction with a test case execution."""
    def review(self, tg_config: TestGuideConfig, tce_id: int, review_id: int) -> Self:
        """Interaction with a review."""
    def atx(self, tg_config: TestGuideConfig, atx_id: int) -> Self:
        """Interaction with an atx report."""
    def jira_issue(self, jira_config: JiraConfig, issue_key: str) -> Self:
        """Interaction with a jira issue."""
    def test_resource(self, tg_config: TestGuideConfig, test_resource_id: str) -> Self:
        """Interaction with a test resource."""
    def test_resource_machine(self, tg_config: TestGuideConfig, test_resource_machine_id: str) -> Self:
        """Interaction with a test resource machine."""
    def generic(self, url: str, text: str) -> Self:
        """Generic specification of an interaction directly providing url and text."""
    def build(self) -> FlowTaskReportBlockInteraction:
        """Create FlowTaskReportBlockInteraction."""