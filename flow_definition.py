# noqa: INP001

__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = '''
MIT License

Copyright (c) by tracetronic GmbH, Dresden

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next paragraph) shall be included in all copies or
 substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from flow_kit import Assign, Flow, FlowBuilder
from flow_kit.library.control_flow import ConditionalSkip
from flow_kit.library.test_guide.reporting import RetrieveAllTemplates, StartReportGeneration
from flow_kit.library.trigger import ReleaseStateChangedTrigger
from flow_kit.library.user_code import GenericUserCode
from tg_api_clients.reporting import AbstractReportData, GenerationDataType, ReleaseReportData, Template

TEMPLATE_NAME = 'Default Test Summary Report'


def get_id_of_template_with_name(template_list: list[Template]) -> int:
    """Get id of template with given name."""
    for template in template_list:
        if template.label == TEMPLATE_NAME:
            template_id = template.template_id
            if template_id:
                return template_id

    raise LookupError


def calc_export_request(release_id: int) -> AbstractReportData:
    """Create data object for export request."""
    return ReleaseReportData(d_type=GenerationDataType.RELEASE, release_id=release_id)  # type: ignore[call-arg]


def get_flow() -> Flow:
    """Define the flow to be executed."""
    return (
        FlowBuilder()
        .add_block_with(
            trigger_block := ReleaseStateChangedTrigger().with_label('trigger: release state changed'),
            result_alias='trigger_payload',
        )
        .add_block_with(
            skip_condition_block := ConditionalSkip().with_label('skip if not LOCKED'),
            Assign(ConditionalSkip.PAR__SKIP).to_user_expression('trigger_payload.new_state != "LOCKED"'),
            required_blocks=[trigger_block],
        )
        .add_block_with(
            template_list_block := RetrieveAllTemplates().with_label('get all defined report templates'),
            # required_blocks=... not necessary, because Assign().to_block_result() adds the given block automatically
        )
        .add_block_with(
            template_id_block := GenericUserCode(get_id_of_template_with_name).with_label('find template id'),
            Assign('template_list').to_block_result(template_list_block),
            # required_blocks=... not necessary, because Assign().to_block_result() adds the given block automatically
        )
        .add_block_with(
            export_request_block := GenericUserCode(calc_export_request).with_label('calculate export request'),
            Assign('release_id').to_user_expression('trigger_payload.release_id'),
            required_blocks=[trigger_block, skip_condition_block],
        )
        .add_block_with(
            StartReportGeneration().with_label('start report generation'),
            Assign(StartReportGeneration.PAR__REPORT_DATA).to_block_result(export_request_block),
            Assign(StartReportGeneration.PAR__TEMPLATE_ID).to_block_result(template_id_block),
            # required_blocks=... not necessary, because Assign().to_block_result() adds the given block automatically
        )
        .build()
    )
