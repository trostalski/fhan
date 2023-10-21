"""
Generated class for EnrollmentResponse. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class EnrollmentResponse(DomainResource):
    """This resource provides enrollment and plan details from the processing of an EnrollmentRequest resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier
    :param str status: active | cancelled | draft | entered-in-error
    :param Reference request: Claim reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str created: Creation date
    :param Reference organization: Insurer
    :param Reference requestProvider: Responsible practitioner
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "organization": {"class_name": "Reference", "is_contained": False},
        "requestProvider": {"class_name": "Reference", "is_contained": False},
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
        identifier: list["Identifier"] = None,
        status: "str" = None,
        request: "Reference" = None,
        outcome: "str" = None,
        disposition: "str" = None,
        created: "str" = None,
        organization: "Reference" = None,
        requestProvider: "Reference" = None,
    ):
        self.resourceType = resourceType or "EnrollmentResponse"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.request = request
        self.outcome = outcome
        self.disposition = disposition
        self.created = created
        self.organization = organization
        self.requestProvider = requestProvider

    @classmethod
    def from_dict(cls, data: dict) -> "EnrollmentResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "EnrollmentResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
