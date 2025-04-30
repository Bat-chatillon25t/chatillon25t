__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


class MissingEnvVarError(Exception):
    """Exception that is raised, if a requested env var is not set."""

def get_env_var_value(env_var_name: str) -> str:
    """Get value of an environment variable or raise an exception if not set."""