"""
Generated class for OrganizationAffiliation. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class OrganizationAffiliation(DomainResource):
    """Defines an affiliation/assotiation/relationship between 2 distinct oganizations, that is not a part-of relationship/sub-division relationship.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifiers that are specific to this role
    :param bool active: Whether this organization affiliation record is in active use
    :param Period period: The period during which the participatingOrganization is affiliated with the primary organization
    :param Reference organization: Organization where the role is available
    :param Reference participatingOrganization: Organization that provides/performs the role (e.g. providing services or is a member of)
    :param Reference network: Health insurance provider network in which the participatingOrganization provides the role's services (if defined) at the indicated locations (if defined)
    :param CodeableConcept code: Definition of the role the participatingOrganization plays
    :param CodeableConcept specialty: Specific specialty of the participatingOrganization in the context of the role
    :param Reference location: The location(s) at which the role occurs
    :param Reference healthcareService: Healthcare services provided through the role
    :param ContactPoint telecom: Contact details at the participatingOrganization relevant to this Affiliation
    :param Reference endpoint: Technical endpoints providing access to services operated for this role
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "organization": {"class_name": "Reference", "is_contained": False},
        "participatingOrganization": {"class_name": "Reference", "is_contained": False},
        "network": {"class_name": "Reference", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "specialty": {"class_name": "CodeableConcept", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "healthcareService": {"class_name": "Reference", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
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
        period: "Period" = None,
        organization: "Reference" = None,
        participatingOrganization: "Reference" = None,
        network: list["Reference"] = None,
        code: list["CodeableConcept"] = None,
        specialty: list["CodeableConcept"] = None,
        location: list["Reference"] = None,
        healthcareService: list["Reference"] = None,
        telecom: list["ContactPoint"] = None,
        endpoint: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "OrganizationAffiliation"
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
        self.period = period
        self.organization = organization
        self.participatingOrganization = participatingOrganization
        self.network = network or []
        self.code = code or []
        self.specialty = specialty or []
        self.location = location or []
        self.healthcareService = healthcareService or []
        self.telecom = telecom or []
        self.endpoint = endpoint or []

    @classmethod
    def from_dict(cls, data: dict) -> "OrganizationAffiliation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "OrganizationAffiliation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
