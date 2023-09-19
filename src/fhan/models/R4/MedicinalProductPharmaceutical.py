"""
Generated class for MedicinalProductPharmaceutical. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductPharmaceutical:
    """
    A pharmaceutical product described in terms of its composition and dose form.
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
    
    administrableDoseForm: "CodeableConcept" = None
    
    unitOfPresentation: "CodeableConcept" = None
    
    ingredient: "Reference" = None
    
    device: "Reference" = None
    
    characteristics: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    routeOfAdministration: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    firstDose: "Quantity" = None
    
    maxSingleDose: "Quantity" = None
    
    maxDosePerDay: "Quantity" = None
    
    maxDosePerTreatmentPeriod: "Ratio" = None
    
    maxTreatmentPeriod: "Duration" = None
    
    targetSpecies: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    withdrawalPeriod: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    tissue: "CodeableConcept" = None
    
    value: "Quantity" = None
    
    supportingInformation: str = None
    