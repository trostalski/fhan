"""
Generated class for MedicationDispense. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Dosage import *
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
class MedicationDispense:
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
    :param Reference basedOn: Plan that is fulfilled by this dispense
    :param Reference partOf: Event that dispense is part of
    :param str status: preparation | in-progress | cancelled | on-hold | completed | entered-in-error | stopped | declined | unknown
    :param CodeableReference notPerformedReason: Why a dispense was not performed
    :param str statusChanged: When the status changed
    :param CodeableConcept category: Type of medication dispense
    :param CodeableReference medication: What medication was supplied
    :param Reference subject: Who the dispense is for
    :param Reference encounter: Encounter associated with event
    :param Reference supportingInformation: Information that supports the dispensing of the medication
    :param BackboneElement performer: Who performed event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Who performed the dispense and what they did
    :param Reference actor: Individual who was performing
    :param Reference location: Where the dispense occurred
    :param Reference authorizingPrescription: Medication order that authorizes the dispense
    :param CodeableConcept type: Trial fill, partial fill, emergency fill, etc
    :param Quantity quantity: Amount dispensed
    :param Quantity daysSupply: Amount of medication expressed as a timing amount
    :param str recorded: When the recording of the dispense started
    :param str whenPrepared: When product was packaged and reviewed
    :param str whenHandedOver: When product was given out
    :param Reference destination: Where the medication was/will be sent
    :param Reference receiver: Who collected the medication or where the medication was delivered
    :param Annotation note: Information about the dispense
    :param str renderedDosageInstruction: Full representation of the dosage instructions
    :param Dosage dosageInstruction: How the medication is to be used by the patient or administered by the caregiver
    :param BackboneElement substitution: Whether a substitution was performed on the dispense
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool wasSubstituted: Whether a substitution was or was not performed on the dispense
    :param CodeableConcept type: Code signifying whether a different drug was dispensed from what was prescribed
    :param CodeableConcept reason: Why was substitution made
    :param Reference responsibleParty: Who is responsible for the substitution
    :param Reference eventHistory: A list of relevant lifecycle events
    
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
    
    partOf: "Reference" = None
    
    status: str = None
    
    notPerformedReason: "CodeableReference" = None
    
    statusChanged: str = None
    
    category: "CodeableConcept" = None
    
    medication: "CodeableReference" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    location: "Reference" = None
    
    authorizingPrescription: "Reference" = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    daysSupply: "Quantity" = None
    
    recorded: str = None
    
    whenPrepared: str = None
    
    whenHandedOver: str = None
    
    destination: "Reference" = None
    
    receiver: "Reference" = None
    
    note: "Annotation" = None
    
    renderedDosageInstruction: str = None
    
    dosageInstruction: "Dosage" = None
    
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    wasSubstituted: bool = None
    
    type: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    responsibleParty: "Reference" = None
    
    eventHistory: "Reference" = None
    