"""
Generated class for CareTeam. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Participant(BaseModel):
    """Identifies all people and organizations who are expected to be involved in the care team.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Type of involvement
    :param Reference member: Who is involved
    :param Reference onBehalfOf: Organization of the practitioner
    :param Period period: Time period of participant
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "member": {"class_name": "Reference", "is_contained": False},
        "onBehalfOf": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        role: list["CodeableConcept"] = None,
        member: "Reference" = None,
        onBehalfOf: "Reference" = None,
        period: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role or []
        self.member = member
        self.onBehalfOf = onBehalfOf
        self.period = period

    @classmethod
    def from_dict(cls, data: dict) -> "CareTeam":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CareTeam":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CareTeam(DomainResource):
    """The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this team
    :param str status: proposed | active | suspended | inactive | entered-in-error
    :param CodeableConcept category: Type of team
    :param str name: Name of the team, such as crisis assessment team
    :param Reference subject: Who care team is for
    :param Reference encounter: Encounter created as part of
    :param Period period: Time period team covers
    :param Participant participant: Members of the team
    :param CodeableConcept reasonCode: Why the care team exists
    :param Reference reasonReference: Why the care team exists
    :param Reference managingOrganization: Organization responsible for the care team
    :param ContactPoint telecom: A contact detail for the care team (that applies to all members)
    :param Annotation note: Comments made about the CareTeam
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "period": {"class_name": "Period", "is_contained": False},
        "participant": {"class_name": "Participant", "is_contained": True},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "managingOrganization": {"class_name": "Reference", "is_contained": False},
        "telecom": {"class_name": "ContactPoint", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
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
        category: list["CodeableConcept"] = None,
        name: "str" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        period: "Period" = None,
        participant: list["Participant"] = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        managingOrganization: list["Reference"] = None,
        telecom: list["ContactPoint"] = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "CareTeam"
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
        self.category = category or []
        self.name = name
        self.subject = subject
        self.encounter = encounter
        self.period = period
        self.participant = participant or []
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.managingOrganization = managingOrganization or []
        self.telecom = telecom or []
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "CareTeam":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CareTeam":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
