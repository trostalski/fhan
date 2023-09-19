"""
Generated class for Dosage. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Element import *
from fhan.models.R4B.Timing import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Ratio import *


@dataclass
class Dosage:
    """
    Base StructureDefinition for Dosage Type: Indicates how the medication is/was taken or should be taken by the patient.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    text: str = None
    
    additionalInstruction: "CodeableConcept" = None
    
    patientInstruction: str = None
    
    timing: "Timing" = None
    
    asNeededboolean: bool = None
    
    asNeededboolean: "CodeableConcept" = None
    
    site: "CodeableConcept" = None
    
    route: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    doseAndRate: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    doseRange: "Range" = None
    
    doseRange: "Quantity" = None
    
    rateRatio: "Ratio" = None
    
    rateRatio: "Range" = None
    
    rateRatio: "Quantity" = None
    
    maxDosePerPeriod: "Ratio" = None
    
    maxDosePerAdministration: "Quantity" = None
    
    maxDosePerLifetime: "Quantity" = None
    