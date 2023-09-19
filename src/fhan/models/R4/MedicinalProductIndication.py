"""
Generated class for MedicinalProductIndication. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Population import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductIndication:
    """
    Indication for the Medicinal Product.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    subject: "Reference" = None
    
    diseaseSymptomProcedure: "CodeableConcept" = None
    
    diseaseStatus: "CodeableConcept" = None
    
    comorbidity: "CodeableConcept" = None
    
    intendedEffect: "CodeableConcept" = None
    
    duration: "Quantity" = None
    
    otherTherapy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    therapyRelationshipType: "CodeableConcept" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    medicationCodeableConcept: "Reference" = None
    
    undesirableEffect: "Reference" = None
    
    population: "Population" = None
    