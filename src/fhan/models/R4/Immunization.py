"""
Generated class for Immunization. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Performer(BaseModel):
    """Indicates who performed the immunization event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: What type of performance was done
    :param Reference actor: Individual or organization who was performing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        function: "CodeableConcept" = None,
        actor: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function
        self.actor = actor

    @classmethod
    def from_dict(cls, data: dict) -> "Immunization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Immunization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Education(BaseModel):
    """Educational material presented to the patient (or guardian) at the time of vaccine administration.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str documentType: Educational material document identifier
    :param str reference: Educational material reference pointer
    :param str publicationDate: Educational material publication date
    :param str presentationDate: Educational material presentation date
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        documentType: "str" = None,
        reference: "str" = None,
        publicationDate: "str" = None,
        presentationDate: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.documentType = documentType
        self.reference = reference
        self.publicationDate = publicationDate
        self.presentationDate = presentationDate

    @classmethod
    def from_dict(cls, data: dict) -> "Immunization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Immunization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Reaction(BaseModel):
    """Categorical data indicating that an adverse event is associated in time to an immunization.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When reaction started
    :param Reference detail: Additional information on reaction
    :param bool reported: Indicates self-reported reaction
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "detail": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        date: "str" = None,
        detail: "Reference" = None,
        reported: "bool" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.date = date
        self.detail = detail
        self.reported = reported

    @classmethod
    def from_dict(cls, data: dict) -> "Immunization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Immunization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ProtocolApplied(BaseModel):
    """The protocol (set of recommendations) being followed by the provider who administered the dose.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str series: Name of vaccine series
    :param Reference authority: Who is responsible for publishing the recommendations
    :param CodeableConcept targetDisease: Vaccine preventatable disease being targetted
    :param int doseNumberPositiveInt: Dose number within series
    :param str doseNumberString: Dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    :param str seriesDosesString: Recommended number of doses for immunity
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "authority": {"class_name": "Reference", "is_contained": False},
        "targetDisease": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        series: "str" = None,
        authority: "Reference" = None,
        targetDisease: list["CodeableConcept"] = None,
        doseNumberPositiveInt: "int" = None,
        doseNumberString: "str" = None,
        seriesDosesPositiveInt: "int" = None,
        seriesDosesString: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.series = series
        self.authority = authority
        self.targetDisease = targetDisease or []
        self.doseNumberPositiveInt = doseNumberPositiveInt
        self.doseNumberString = doseNumberString
        self.seriesDosesPositiveInt = seriesDosesPositiveInt
        self.seriesDosesString = seriesDosesString

    @classmethod
    def from_dict(cls, data: dict) -> "Immunization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Immunization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Immunization(DomainResource):
    """Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: completed | entered-in-error | not-done
    :param CodeableConcept statusReason: Reason not done
    :param CodeableConcept vaccineCode: Vaccine product administered
    :param Reference patient: Who was immunized
    :param Reference encounter: Encounter immunization was part of
    :param str occurrenceDateTime: Vaccine administration date
    :param str occurrenceString: Vaccine administration date
    :param str recorded: When the immunization was first captured in the subject's record
    :param bool primarySource: Indicates context the data was recorded in
    :param CodeableConcept reportOrigin: Indicates the source of a secondarily reported record
    :param Reference location: Where immunization occurred
    :param Reference manufacturer: Vaccine manufacturer
    :param str lotNumber: Vaccine lot number
    :param str expirationDate: Vaccine expiration date
    :param CodeableConcept site: Body site vaccine  was administered
    :param CodeableConcept route: How vaccine entered body
    :param Quantity doseQuantity: Amount of vaccine administered
    :param Performer performer: Who performed event
    :param Annotation note: Additional immunization notes
    :param CodeableConcept reasonCode: Why immunization occurred
    :param Reference reasonReference: Why immunization occurred
    :param bool isSubpotent: Dose potency
    :param CodeableConcept subpotentReason: Reason for being subpotent
    :param Education education: Educational material presented to patient
    :param CodeableConcept programEligibility: Patient eligibility for a vaccination program
    :param CodeableConcept fundingSource: Funding source for the vaccine
    :param Reaction reaction: Details of a reaction that follows immunization
    :param ProtocolApplied protocolApplied: Protocol followed by the provider
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        "vaccineCode": {"class_name": "CodeableConcept", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "reportOrigin": {"class_name": "CodeableConcept", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        "site": {"class_name": "CodeableConcept", "is_contained": False},
        "route": {"class_name": "CodeableConcept", "is_contained": False},
        "doseQuantity": {"class_name": "Quantity", "is_contained": False},
        "performer": {"class_name": "Performer", "is_contained": True},
        "note": {"class_name": "Annotation", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "subpotentReason": {"class_name": "CodeableConcept", "is_contained": False},
        "education": {"class_name": "Education", "is_contained": True},
        "programEligibility": {"class_name": "CodeableConcept", "is_contained": False},
        "fundingSource": {"class_name": "CodeableConcept", "is_contained": False},
        "reaction": {"class_name": "Reaction", "is_contained": True},
        "protocolApplied": {"class_name": "ProtocolApplied", "is_contained": True},
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
        statusReason: "CodeableConcept" = None,
        vaccineCode: "CodeableConcept" = None,
        patient: "Reference" = None,
        encounter: "Reference" = None,
        occurrenceDateTime: "str" = None,
        occurrenceString: "str" = None,
        recorded: "str" = None,
        primarySource: "bool" = None,
        reportOrigin: "CodeableConcept" = None,
        location: "Reference" = None,
        manufacturer: "Reference" = None,
        lotNumber: "str" = None,
        expirationDate: "str" = None,
        site: "CodeableConcept" = None,
        route: "CodeableConcept" = None,
        doseQuantity: "Quantity" = None,
        performer: list["Performer"] = None,
        note: list["Annotation"] = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        isSubpotent: "bool" = None,
        subpotentReason: list["CodeableConcept"] = None,
        education: list["Education"] = None,
        programEligibility: list["CodeableConcept"] = None,
        fundingSource: "CodeableConcept" = None,
        reaction: list["Reaction"] = None,
        protocolApplied: list["ProtocolApplied"] = None,
    ):
        self.resourceType = resourceType or "Immunization"
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
        self.statusReason = statusReason
        self.vaccineCode = vaccineCode
        self.patient = patient
        self.encounter = encounter
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrenceString = occurrenceString
        self.recorded = recorded
        self.primarySource = primarySource
        self.reportOrigin = reportOrigin
        self.location = location
        self.manufacturer = manufacturer
        self.lotNumber = lotNumber
        self.expirationDate = expirationDate
        self.site = site
        self.route = route
        self.doseQuantity = doseQuantity
        self.performer = performer or []
        self.note = note or []
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.isSubpotent = isSubpotent
        self.subpotentReason = subpotentReason or []
        self.education = education or []
        self.programEligibility = programEligibility or []
        self.fundingSource = fundingSource
        self.reaction = reaction or []
        self.protocolApplied = protocolApplied or []

    @classmethod
    def from_dict(cls, data: dict) -> "Immunization":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Immunization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
