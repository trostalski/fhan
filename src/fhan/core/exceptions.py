# https://www.hl7.org/fhir/valueset-issue-type.html


class BaseException(Exception):
    """Base exception class."""


class OperationOutcomeException(BaseException):
    """Raised when an OperationOutcome error is returned from the server."""


class NotFoundException(BaseException):
    """Raised when a resource is not found."""


class AuthenticationException(BaseException):
    """Raised when client is not authenticated."""


class FhirContextException(BaseException):
    """Raised when the required FHIR context is not known."""


class UnknownSearchParameterException(BaseException):
    """Raised when a search parameter is not known."""


class InvalidFhirPathException(BaseException):
    """Raised when a FHIRPath expression is not valid."""
