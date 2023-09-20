"""
Generated class for MedicationDispense. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Dosage import *
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
    """ Indicates who or what performed the event.
    :param BackboneElement performer: Who performed event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Who performed the dispense and what they did
    :param Reference actor: Individual who was performing
    """
    performer: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
@dataclass
class substitution(Element):
    """ Indicates whether or not substitution was made as part of the dispense.  In some cases, substitution will be expected but does not happen, in other cases substitution is not expected but does happen.  This block explains what substitution did or did not happen and why.  If nothing is specified, substitution was not done.
    :param BackboneElement substitution: Whether a substitution was performed on the dispense
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool wasSubstituted: Whether a substitution was or was not performed on the dispense
    :param CodeableConcept type: Code signifying whether a different drug was dispensed from what was prescribed
    :param CodeableConcept reason: Why was substitution made
    :param Reference responsibleParty: Who is responsible for the substitution
    """
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    wasSubstituted: bool = None
    
    type: "CodeableConcept" = None
    
    reason: list["CodeableConcept"] = None
    
    responsibleParty: list["Reference"] = None
    


@dataclass
class MedicationDispense(ModelBase):
    """ Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a description of the medication product (supply) provided and the instructions for administering the medication.  The medication dispense is the result of a pharmacy system responding to a medication order.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param Reference partOf: Event that dispense is part of
    :param str status: preparation | in-progress | cancelled | on-hold | completed | entered-in-error | stopped | declined | unknown
    :param CodeableConcept statusReasonCodeableConcept: Why a dispense was not performed
    :param Reference statusReasonCodeableConcept: Why a dispense was not performed
    :param CodeableConcept category: Type of medication dispense
    :param CodeableConcept medicationCodeableConcept: What medication was supplied
    :param Reference medicationCodeableConcept: What medication was supplied
    :param Reference subject: Who the dispense is for
    :param Reference context: Encounter / Episode associated with event
    :param Reference supportingInformation: Information that supports the dispensing of the medication
    :param BackboneElement performer: Who performed event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Who performed the dispense and what they did
    :param Reference actor: Individual who was performing
    :param Reference location: Where the dispense occurred
    :param Reference authorizingPrescription: Medication order that authorizes the dispense
    :param CodeableConcept type: Trial fill, partial fill, emergency fill, etc.
    :param Quantity quantity: Amount dispensed
    :param Quantity daysSupply: Amount of medication expressed as a timing amount
    :param str whenPrepared: When product was packaged and reviewed
    :param str whenHandedOver: When product was given out
    :param Reference destination: Where the medication was sent
    :param Reference receiver: Who collected the medication
    :param Annotation note: Information about the dispense
    :param Dosage dosageInstruction: How the medication is to be used by the patient or administered by the caregiver
    :param BackboneElement substitution: Whether a substitution was performed on the dispense
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool wasSubstituted: Whether a substitution was or was not performed on the dispense
    :param CodeableConcept type: Code signifying whether a different drug was dispensed from what was prescribed
    :param CodeableConcept reason: Why was substitution made
    :param Reference responsibleParty: Who is responsible for the substitution
    :param Reference detectedIssue: Clinical issue with action
    :param Reference eventHistory: A list of relevant lifecycle events
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
    
    partOf: list["Reference"] = None
    
    status: str = None
    
    statusReasonCodeableConcept: "CodeableConcept" = None
    
    statusReasonCodeableConcept: "Reference" = None
    
    category: "CodeableConcept" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    medicationCodeableConcept: "Reference" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    supportingInformation: list["Reference"] = None
    
    performer: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    location: "Reference" = None
    
    authorizingPrescription: list["Reference"] = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    daysSupply: "Quantity" = None
    
    whenPrepared: str = None
    
    whenHandedOver: str = None
    
    destination: "Reference" = None
    
    receiver: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    dosageInstruction: list["Dosage"] = None
    
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    wasSubstituted: bool = None
    
    type: "CodeableConcept" = None
    
    reason: list["CodeableConcept"] = None
    
    responsibleParty: list["Reference"] = None
    
    detectedIssue: list["Reference"] = None
    
    eventHistory: list["Reference"] = None
    