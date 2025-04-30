__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


from flow_kit.core.block.definitions.parameter_definitions import ParameterDefinition as ParameterDefinition
from flow_kit.core.block.definitions.result_definitions import ResultDefinition as ResultDefinition
from flow_kit.core.reporting.interactions import Interaction as Interaction
from flow_kit.core.reporting.json_report.models.flow_task_report_block_interaction import FlowTaskReportBlockInteraction as FlowTaskReportBlockInteraction
from flow_kit.tools.test_guide.test_guide_block import TestGuideBlock as TestGuideBlock

class PerformPlanAction(TestGuideBlock):
    """test.guide Q_GatesApi: Perform an action on a Q-gate plan."""
    PAR__PLAN_KEY: str
    PAR__PLAN_ACTION: str
    def get_result_definition(self) -> ResultDefinition: ...
    def get_interactions(self) -> list[FlowTaskReportBlockInteraction]: ...