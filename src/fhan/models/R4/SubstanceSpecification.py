"""
Generated class for SubstanceSpecification. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class SubstanceSpecification:
    """
    The detailed description of a substance, typically at a level beyond what is used for prescribing.
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
    
    type: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    domain: "CodeableConcept" = None
    
    description: str = None
    
    source: "Reference" = None
    
    comment: str = None
    
    moiety: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    identifier: "Identifier" = None
    
    name: str = None
    
    stereochemistry: "CodeableConcept" = None
    
    opticalActivity: "CodeableConcept" = None
    
    molecularFormula: str = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    parameters: str = None
    
    definingSubstanceReference: "Reference" = None
    
    definingSubstanceReference: "CodeableConcept" = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: str = None
    
    referenceInformation: "Reference" = None
    
    structure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    stereochemistry: "CodeableConcept" = None
    
    opticalActivity: "CodeableConcept" = None
    
    molecularFormula: str = None
    
    molecularFormulaByMoiety: str = None
    
    isotope: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    name: "CodeableConcept" = None
    
    substitution: "CodeableConcept" = None
    
    halfLife: "Quantity" = None
    
    molecularWeight: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    method: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    amount: "Quantity" = None
    
    molecularWeight: "BackboneElement" = None
    
    source: "Reference" = None
    
    representation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    attachment: "Attachment" = None
    
    code: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    comment: str = None
    
    source: "Reference" = None
    
    name: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    preferred: bool = None
    
    language: "CodeableConcept" = None
    
    domain: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    synonym: "BackboneElement" = None
    
    translation: "BackboneElement" = None
    
    official: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    authority: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    date: str = None
    
    source: "Reference" = None
    
    molecularWeight: "BackboneElement" = None
    
    relationship: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substanceReference: "Reference" = None
    
    substanceReference: "CodeableConcept" = None
    
    relationship: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: "Range" = None
    
    amountQuantity: "Ratio" = None
    
    amountQuantity: str = None
    
    amountRatioLowLimit: "Ratio" = None
    
    amountType: "CodeableConcept" = None
    
    source: "Reference" = None
    
    nucleicAcid: "Reference" = None
    
    polymer: "Reference" = None
    
    protein: "Reference" = None
    
    sourceMaterial: "Reference" = None
    