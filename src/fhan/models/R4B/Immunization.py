"""
Generated class for Immunization. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Immunization:
    """
    Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
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
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    note: "Annotation" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    isSubpotent: bool = None
    
    subpotentReason: "CodeableConcept" = None
    
    education: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    documentType: str = None
    
    reference: str = None
    
    publicationDate: str = None
    
    presentationDate: str = None
    
    programEligibility: "CodeableConcept" = None
    
    fundingSource: "CodeableConcept" = None
    
    reaction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    date: str = None
    
    detail: "Reference" = None
    
    reported: bool = None
    
    protocolApplied: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    series: str = None
    
    authority: "Reference" = None
    
    targetDisease: "CodeableConcept" = None
    
    doseNumberpositiveInt: int = None
    
    doseNumberpositiveInt: str = None
    
    seriesDosespositiveInt: int = None
    
    seriesDosespositiveInt: str = None
    