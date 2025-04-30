__copyright__ = 'Copyright © by tracetronic GmbH, Dresden'
__license__ = (
    "This file is distributed as an integral part of tracetronic's software products "
    'and may only be used in connection with and pursuant to the terms and conditions '
    'of a valid tracetronic software product license.'
)


import abc
from abc import ABC, abstractmethod
from atlassian import Jira
from collections.abc import Generator
from dataclasses import dataclass
from typing import Any, Self

class JiraConnectionError(Exception):
    """Exception that is raised, when jira access is not possible."""

class JiraAuth(ABC, metaclass=abc.ABCMeta):
    """Interface for different jira authentication objects."""
    @abstractmethod
    def as_argument_dict(self) -> dict[str, Any]:
        """Transform auth object into dict which can be used as keyword parameters to initialize atlassian.Jira."""

@dataclass
class BasicAuth(JiraAuth):
    """Authenticate with username and password."""
    username: str
    password: str
    def as_argument_dict(self) -> dict[str, str]: ...

@dataclass
class ApiTokenAuth(JiraAuth):
    """Authenticate with username and api token."""
    username: str
    api_token: str
    def as_argument_dict(self) -> dict[str, str]: ...

@dataclass
class AccessTokenAuth(JiraAuth):
    """Authenticate with access token."""
    access_token: str
    def as_argument_dict(self) -> dict[str, str]: ...

@dataclass
class OAuth(JiraAuth):
    """Authenticate with username and api token."""
    access_token: str
    access_token_secret: str
    consumer_key: str
    key_cert: str
    def as_argument_dict(self) -> dict[str, dict[str, str]]: ...

class JiraConfig:
    """Dataclass for config of jira-access."""
    def __init__(self, url: str, auth_info: JiraAuth) -> None: ...
    @classmethod
    def with_token(cls, url: str, token: str) -> Self:
        """Creates config with the given url and token."""
    @classmethod
    def with_username_and_password(cls, url: str, username: str, password: str) -> Self:
        """Creates config with the given username and password."""
    @property
    def url(self) -> str:
        """Returns base url."""
    def __hash__(self): ...
    def __eq__(self, other) -> bool: ...
    def get_jira_instance(self) -> Generator[Jira, None, None]:
        """Initialize jira-instance and test connection."""