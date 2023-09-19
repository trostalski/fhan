"""
Generated class for MedicationDispense. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Meta import *


@dataclass
class MedicationDispense:
    """
    Indicates that a medication product is to be or has been dispensed for a named person/patient.  This includes a description of the medication product (supply) provided and the instructions for administering the medication.  The medication dispense is the result of a pharmacy system responding to a medication order.
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
    
    partOf: "Reference" = None
    
    status: str = None
    
    statusReasonCodeableConcept: "CodeableConcept" = None
    
    statusReasonCodeableConcept: "Reference" = None
    
    category: "CodeableConcept" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    medicationCodeableConcept: "Reference" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
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
    
    whenPrepared: str = None
    
    whenHandedOver: str = None
    
    destination: "Reference" = None
    
    receiver: "Reference" = None
    
    note: "Annotation" = None
    
    dosageInstruction: "Dosage" = None
    
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    wasSubstituted: bool = None
    
    type: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    responsibleParty: "Reference" = None
    
    detectedIssue: "Reference" = None
    
    eventHistory: "Reference" = None
    