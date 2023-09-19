"""
Generated class for MedicationRequest. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Duration import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Meta import *


@dataclass
class MedicationRequest:
    """
    An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
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
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    intent: str = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    reportedboolean: bool = None
    
    reportedboolean: "Reference" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    medicationCodeableConcept: "Reference" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    performer: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    recorder: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    courseOfTherapyType: "CodeableConcept" = None
    
    insurance: "Reference" = None
    
    note: "Annotation" = None
    
    dosageInstruction: "Dosage" = None
    
    dispenseRequest: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    initialFill: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    quantity: "Quantity" = None
    
    duration: "Duration" = None
    
    dispenseInterval: "Duration" = None
    
    validityPeriod: "Period" = None
    
    numberOfRepeatsAllowed: int = None
    
    quantity: "Quantity" = None
    
    expectedSupplyDuration: "Duration" = None
    
    performer: "Reference" = None
    
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    allowedboolean: bool = None
    
    allowedboolean: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    priorPrescription: "Reference" = None
    
    detectedIssue: "Reference" = None
    
    eventHistory: "Reference" = None
    