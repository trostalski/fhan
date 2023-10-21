"""
Generated class for Person. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Link(BaseModel):
    """Link to a resource that concerns the same actual person.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference target: The resource to which this actual person is associated
    :param str assurance: level1 | level2 | level3 | level4
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        target: "Reference" = None,
        assurance: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.target = target
        self.assurance = assurance

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Person":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Person(DomainResource):
    """Demographics and administrative information about a person independent of a specific health-related context.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: A human identifier for this person
    :param HumanName name: A name associated with the person
    :param ContactPoint telecom: A contact detail for the person
    :param str gender: male | female | other | unknown
    :param str birthDate: The date on which the person was born
    :param Address address: One or more addresses for the person
    :param Attachment photo: Image of the person
    :param Reference managingOrganization: The organization that is the custodian of the person record
    :param bool active: This person's record is in active use
    :param Link link: Link to a resource that concerns the same actual person
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "name": {"class_name": "HumanName", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
        "photo": {"class_name": "Attachment", "is_contained": False},
        "managingOrganization": {"class_name": "Reference", "is_contained": False},
        "link": {"class_name": "Link", "is_contained": True},
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
        name: list["HumanName"] = None,
        telecom: list["ContactPoint"] = None,
        gender: "str" = None,
        birthDate: "str" = None,
        address: list["Address"] = None,
        photo: "Attachment" = None,
        managingOrganization: "Reference" = None,
        active: "bool" = None,
        link: list["Link"] = None,
    ):
        self.resourceType = resourceType or "Person"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.name = name or []
        self.telecom = telecom or []
        self.gender = gender
        self.birthDate = birthDate
        self.address = address or []
        self.photo = photo
        self.managingOrganization = managingOrganization
        self.active = active
        self.link = link or []

    @classmethod
    def from_dict(cls, data: dict) -> "Person":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Person":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
