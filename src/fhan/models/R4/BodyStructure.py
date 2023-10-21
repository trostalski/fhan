"""
Generated class for BodyStructure. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class BodyStructure(DomainResource):
    """Record details about an anatomical structure.  This resource may be used when a coded concept does not provide the necessary detail needed for the use case.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Bodystructure identifier
    :param bool active: Whether this record is in active use
    :param CodeableConcept morphology: Kind of Structure
    :param CodeableConcept location: Body site
    :param CodeableConcept locationQualifier: Body site modifier
    :param str description: Text description
    :param Attachment image: Attached images
    :param Reference patient: Who this is about
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "morphology": {"class_name": "CodeableConcept", "is_contained": False},
        "location": {"class_name": "CodeableConcept", "is_contained": False},
        "locationQualifier": {"class_name": "CodeableConcept", "is_contained": False},
        "image": {"class_name": "Attachment", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
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
        active: "bool" = None,
        morphology: "CodeableConcept" = None,
        location: "CodeableConcept" = None,
        locationQualifier: list["CodeableConcept"] = None,
        description: "str" = None,
        image: list["Attachment"] = None,
        patient: "Reference" = None,
    ):
        self.resourceType = resourceType or "BodyStructure"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.active = active
        self.morphology = morphology
        self.location = location
        self.locationQualifier = locationQualifier or []
        self.description = description
        self.image = image or []
        self.patient = patient

    @classmethod
    def from_dict(cls, data: dict) -> "BodyStructure":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "BodyStructure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
