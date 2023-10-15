class BaseException(Exception):
    """Base exception class."""


class AuthenticationError(BaseException):
    """Raised when client is not authenticated."""


class FhirContextException(BaseException):
    """Raised when the required FHIR context is not known."""


class UnknownSearchParameterException(BaseException):
    """Raised when a search parameter is not known."""
