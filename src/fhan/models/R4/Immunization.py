"""
Generated class for Immunization. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class performer(Element):
    """ Indicates who performed the immunization event.
    :param BackboneElement performer: Who performed event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: What type of performance was done
    :param Reference actor: Individual or organization who was performing
    """
    performer: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
@dataclass
class education(Element):
    """ Educational material presented to the patient (or guardian) at the time of vaccine administration.
    :param BackboneElement education: Educational material presented to patient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str documentType: Educational material document identifier
    :param str reference: Educational material reference pointer
    :param str publicationDate: Educational material publication date
    :param str presentationDate: Educational material presentation date
    """
    education: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    documentType: str = None
    
    reference: str = None
    
    publicationDate: str = None
    
    presentationDate: str = None
    
@dataclass
class reaction(Element):
    """ Categorical data indicating that an adverse event is associated in time to an immunization.
    :param BackboneElement reaction: Details of a reaction that follows immunization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When reaction started
    :param Reference detail: Additional information on reaction
    :param bool reported: Indicates self-reported reaction
    """
    reaction: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    date: str = None
    
    detail: "Reference" = None
    
    reported: bool = None
    
@dataclass
class protocolApplied(Element):
    """ The protocol (set of recommendations) being followed by the provider who administered the dose.
    :param BackboneElement protocolApplied: Protocol followed by the provider
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str series: Name of vaccine series
    :param Reference authority: Who is responsible for publishing the recommendations
    :param CodeableConcept targetDisease: Vaccine preventatable disease being targetted
    :param int doseNumberpositiveInt: Dose number within series
    :param str doseNumberpositiveInt: Dose number within series
    :param int seriesDosespositiveInt: Recommended number of doses for immunity
    :param str seriesDosespositiveInt: Recommended number of doses for immunity
    """
    protocolApplied: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    series: str = None
    
    authority: "Reference" = None
    
    targetDisease: list["CodeableConcept"] = None
    
    doseNumberpositiveInt: int = None
    
    doseNumberpositiveInt: str = None
    
    seriesDosespositiveInt: int = None
    
    seriesDosespositiveInt: str = None
    


@dataclass
class Immunization(ModelBase):
    """ Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
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
    :param str occurrencedateTime: Vaccine administration date
    :param str occurrencedateTime: Vaccine administration date
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
    :param BackboneElement performer: Who performed event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: What type of performance was done
    :param Reference actor: Individual or organization who was performing
    :param Annotation note: Additional immunization notes
    :param CodeableConcept reasonCode: Why immunization occurred
    :param Reference reasonReference: Why immunization occurred
    :param bool isSubpotent: Dose potency
    :param CodeableConcept subpotentReason: Reason for being subpotent
    :param BackboneElement education: Educational material presented to patient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str documentType: Educational material document identifier
    :param str reference: Educational material reference pointer
    :param str publicationDate: Educational material publication date
    :param str presentationDate: Educational material presentation date
    :param CodeableConcept programEligibility: Patient eligibility for a vaccination program
    :param CodeableConcept fundingSource: Funding source for the vaccine
    :param BackboneElement reaction: Details of a reaction that follows immunization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When reaction started
    :param Reference detail: Additional information on reaction
    :param bool reported: Indicates self-reported reaction
    :param BackboneElement protocolApplied: Protocol followed by the provider
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str series: Name of vaccine series
    :param Reference authority: Who is responsible for publishing the recommendations
    :param CodeableConcept targetDisease: Vaccine preventatable disease being targetted
    :param int doseNumberpositiveInt: Dose number within series
    :param str doseNumberpositiveInt: Dose number within series
    :param int seriesDosespositiveInt: Recommended number of doses for immunity
    :param str seriesDosespositiveInt: Recommended number of doses for immunity
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    vaccineCode: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: str = None
    
    recorded: str = None
    
    primarySource: bool = None
    
    reportOrigin: "CodeableConcept" = None
    
    location: "Reference" = None
    
    manufacturer: "Reference" = None
    
    lotNumber: str = None
    
    expirationDate: str = None
    
    site: "CodeableConcept" = None
    
    route: "CodeableConcept" = None
    
    doseQuantity: "Quantity" = None
    
    performer: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    note: list["Annotation"] = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    isSubpotent: bool = None
    
    subpotentReason: list["CodeableConcept"] = None
    
    education: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    documentType: str = None
    
    reference: str = None
    
    publicationDate: str = None
    
    presentationDate: str = None
    
    programEligibility: list["CodeableConcept"] = None
    
    fundingSource: "CodeableConcept" = None
    
    reaction: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    date: str = None
    
    detail: "Reference" = None
    
    reported: bool = None
    
    protocolApplied: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    series: str = None
    
    authority: "Reference" = None
    
    targetDisease: list["CodeableConcept"] = None
    
    doseNumberpositiveInt: int = None
    
    doseNumberpositiveInt: str = None
    
    seriesDosespositiveInt: int = None
    
    seriesDosespositiveInt: str = None
    