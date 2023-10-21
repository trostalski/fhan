"""
Generated class for Organization. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Contact(BaseModel):
    """Contact for the organization for a certain purpose.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: A name associated with the contact
    :param ContactPoint telecom: Contact details (telephone, email, etc.)  for a contact
    :param Address address: Visiting or postal addresses for the contact
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "purpose": {"class_name": "CodeableConcept", "is_contained": False},
        "name": {"class_name": "HumanName", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        purpose: "CodeableConcept" = None,
        name: "HumanName" = None,
        telecom: list["ContactPoint"] = None,
        address: "Address" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.purpose = purpose
        self.name = name
        self.telecom = telecom or []
        self.address = address

    @classmethod
    def from_dict(cls, data: dict) -> "Organization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Organization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Organization(DomainResource):
    """A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifies this organization  across multiple systems
    :param bool active: Whether the organization's record is still in active use
    :param CodeableConcept type: Kind of organization
    :param str name: Name used for the organization
    :param str alias: A list of alternate names that the organization is known as, or was known as in the past
    :param ContactPoint telecom: A contact detail for the organization
    :param Address address: An address for the organization
    :param Reference partOf: The organization of which this organization forms a part
    :param Contact contact: Contact for the organization for a certain purpose
    :param Reference endpoint: Technical endpoints providing access to services operated for the organization
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "address": {"class_name": "Address", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "contact": {"class_name": "Contact", "is_contained": True},
        "endpoint": {"class_name": "Reference", "is_contained": False},
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
        type: list["CodeableConcept"] = None,
        name: "str" = None,
        alias: list["str"] = None,
        telecom: list["ContactPoint"] = None,
        address: list["Address"] = None,
        partOf: "Reference" = None,
        contact: list["Contact"] = None,
        endpoint: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "Organization"
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
        self.type = type or []
        self.name = name
        self.alias = alias or []
        self.telecom = telecom or []
        self.address = address or []
        self.partOf = partOf
        self.contact = contact or []
        self.endpoint = endpoint or []

    @classmethod
    def from_dict(cls, data: dict) -> "Organization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Organization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
