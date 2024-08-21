# https://www.hl7.org/fhir/valueset-issue-type.html


class BaseException(Exception):
    """Base exception class."""


class RequestException(BaseException):
    """Raised when an error is returned from the server."""


class OperationOutcomeException(BaseException):
    """Raised when an OperationOutcome error is returned from the server."""


class NotFoundException(BaseException):
    """Raised when a resource is not found."""

    # add message to the exception


class AuthenticationException(BaseException):
    """Raised when client is not authenticated."""


class FhirContextException(BaseException):
    """Raised when the required FHIR context is not known."""


class UnknownSearchParameterException(BaseException):
    """Raised when a search parameter is not known."""


class InvalidFhirPathException(BaseException):
    """Raised when a FHIRPath expression is not valid."""
