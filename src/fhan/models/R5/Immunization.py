"""
Generated class for Immunization. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Immunization:
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
    :param Reference basedOn: Authority that the immunization event is based on
    :param str status: completed | entered-in-error | not-done
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept vaccineCode: Vaccine administered
    :param CodeableReference administeredProduct: Product that was administered
    :param CodeableReference manufacturer: Vaccine manufacturer
    :param str lotNumber: Vaccine lot number
    :param str expirationDate: Vaccine expiration date
    :param Reference patient: Who was immunized
    :param Reference encounter: Encounter immunization was part of
    :param Reference supportingInformation: Additional information in support of the immunization
    :param str occurrencedateTime: Vaccine administration date
    :param str occurrencedateTime: Vaccine administration date
    :param bool primarySource: Indicates context the data was captured in
    :param CodeableReference informationSource: Indicates the source of a  reported record
    :param Reference location: Where immunization occurred
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
    :param CodeableReference reason: Why immunization occurred
    :param bool isSubpotent: Dose potency
    :param CodeableConcept subpotentReason: Reason for being subpotent
    :param BackboneElement programEligibility: Patient eligibility for a specific vaccination program
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept program: The program that eligibility is declared for
    :param CodeableConcept programStatus: The patient's eligibility status for the program
    :param CodeableConcept fundingSource: Funding source for the vaccine
    :param BackboneElement reaction: Details of a reaction that follows immunization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When reaction started
    :param CodeableReference manifestation: Additional information on reaction
    :param bool reported: Indicates self-reported reaction
    :param BackboneElement protocolApplied: Protocol followed by the provider
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str series: Name of vaccine series
    :param Reference authority: Who is responsible for publishing the recommendations
    :param CodeableConcept targetDisease: Vaccine preventatable disease being targeted
    :param str doseNumber: Dose number within series
    :param str seriesDoses: Recommended number of doses for immunity
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    basedOn: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    vaccineCode: "CodeableConcept" = None
    
    administeredProduct: "CodeableReference" = None
    
    manufacturer: "CodeableReference" = None
    
    lotNumber: str = None
    
    expirationDate: str = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: str = None
    
    primarySource: bool = None
    
    informationSource: "CodeableReference" = None
    
    location: "Reference" = None
    
    site: "CodeableConcept" = None
    
    route: "CodeableConcept" = None
    
    doseQuantity: "Quantity" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    note: "Annotation" = None
    
    reason: "CodeableReference" = None
    
    isSubpotent: bool = None
    
    subpotentReason: "CodeableConcept" = None
    
    programEligibility: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    program: "CodeableConcept" = None
    
    programStatus: "CodeableConcept" = None
    
    fundingSource: "CodeableConcept" = None
    
    reaction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    date: str = None
    
    manifestation: "CodeableReference" = None
    
    reported: bool = None
    
    protocolApplied: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    series: str = None
    
    authority: "Reference" = None
    
    targetDisease: "CodeableConcept" = None
    
    doseNumber: str = None
    
    seriesDoses: str = None
    