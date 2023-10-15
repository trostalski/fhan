"""
Generated class for OperationOutcome. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Issue(BaseModel):
    """An error, warning, or information message that results from a system action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str severity: fatal | error | warning | information
    :param str code: Error or warning code
    :param CodeableConcept details: Additional details about the error
    :param str diagnostics: Additional diagnostic information about the issue
    :param str location: Deprecated: Path of element(s) related to issue
    :param str expression: FHIRPath of element(s) related to issue
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "details": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        severity: "str" = None,
        code: "str" = None,
        details: "CodeableConcept" = None,
        diagnostics: "str" = None,
        location: list["str"] = None,
        expression: list["str"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.severity = severity
        self.code = code
        self.details = details
        self.diagnostics = diagnostics
        self.location = location or []
        self.expression = expression or []

    @classmethod
    def from_dict(cls, data: dict) -> "OperationOutcome":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OperationOutcome":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class OperationOutcome(DomainResource):
    """A collection of error, warning, or information messages that result from a system action.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Issue issue: A single issue associated with the action
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "issue": {"class_name": "Issue", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        issue: list["Issue"] = None,
    ):
        self.resourceType = resourceType or "OperationOutcome"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.issue = issue or []

    @classmethod
    def from_dict(cls, data: dict) -> "OperationOutcome":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OperationOutcome":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
