class BaseException(Exception):
    """Base exception class."""


class AuthenticationError(BaseException):
    """Raised when client is not authenticated."""
