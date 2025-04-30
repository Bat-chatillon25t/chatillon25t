# noqa: INP001

__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)

import logging
import platform
import sys
from argparse import ArgumentParser
from pathlib import Path

from flow_kit.core.flow.flow_builder_tracing import FlowBuilderTracing
from flow_kit.core.validation.exceptions import StaticFlowValidationError
from flow_kit.core.validation.validation_problem import ValidationProblem

try:
    import flow_definition
except ImportError:
    logging.exception(
        'Unable to import flow_definition. If you just updated your flow.kit, '
        'you may need to migrate following the migration guide found in docs/migration_guide_from_0.x_1.x_to_2.x.md.',
    )
    raise
from flow_kit.core.app import main


def _get_argument_parser() -> ArgumentParser:
    argument_parser = ArgumentParser(
        prog='flow-kit',
        description='Workflow automation with flow.kit',
        epilog='Automotive DevOps Platform by tracetronic',
    )
    argument_parser.add_argument('--validate', action='store_true')
    argument_parser.add_argument('--execute', action='store_true')
    argument_parser.add_argument('--visualize', action='store_true')

    return argument_parser


def _setup_logging() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def _get_version() -> str:
    version_file = Path(__file__).parent / 'version.txt'
    if version_file.is_file():
        return version_file.read_text().strip()
    return '[ STARTED FROM SOURCE ]'


def _log_system_information() -> None:
    logging.info(f'{platform.system() = }')
    logging.info(f'{platform.version() = }')
    logging.info(f'{platform.machine() = }')
    logging.info(f'{sys.version = }')


def _log_and_exit_for_own_exceptions(flow_builder_exception: Exception) -> None:
    if hasattr(flow_builder_exception, 'location_reference'):
        logging.exception(
            msg=StaticFlowValidationError([ValidationProblem(flow_builder_exception)]),
            exc_info=logging.getLogger().isEnabledFor(logging.DEBUG),
        )
        sys.exit(1)


if __name__ == '__main__':
    _setup_logging()

    argument_parser = _get_argument_parser()
    logging.info(f'Starting {argument_parser.prog}')
    logging.info(f'Version: {_get_version()}')
    _log_system_information()

    args = argument_parser.parse_args()
    flag_validate = args.validate
    flag_execute = args.execute
    flag_visualize = args.visualize

    logging.info(f'Loading flow from {flow_definition.__file__}')
    FlowBuilderTracing.enable_tracing()
    try:
        flow = flow_definition.get_flow()
    except Exception as exception:
        _log_and_exit_for_own_exceptions(exception)
        raise

    main(flow, validate=flag_validate, execute=flag_execute, visualize=flag_visualize)
