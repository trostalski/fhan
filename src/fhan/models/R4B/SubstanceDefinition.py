"""
Generated class for SubstanceDefinition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Ratio import *
from fhan.models.R4B.Reference import *


@dataclass
class SubstanceDefinition:
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
    
    version: str = None
    
    status: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    domain: "CodeableConcept" = None
    
    grade: "CodeableConcept" = None
    
    description: str = None
    
    informationSource: "Reference" = None
    
    note: "Annotation" = None
    
    manufacturer: "Reference" = None
    
    supplier: "Reference" = None
    
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
    
    measurementType: "CodeableConcept" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Attachment" = None
    
    molecularWeight: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    method: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    amount: "Quantity" = None
    
    structure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    stereochemistry: "CodeableConcept" = None
    
    opticalActivity: "CodeableConcept" = None
    
    molecularFormula: str = None
    
    molecularFormulaByMoiety: str = None
    
    molecularWeight: "BackboneElement" = None
    
    technique: "CodeableConcept" = None
    
    sourceDocument: "Reference" = None
    
    representation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    format: "CodeableConcept" = None
    
    document: "Reference" = None
    
    code: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    note: "Annotation" = None
    
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
    
    relationship: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substanceDefinitionReference: "Reference" = None
    
    substanceDefinitionReference: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: "Ratio" = None
    
    amountQuantity: str = None
    
    ratioHighLimitAmount: "Ratio" = None
    
    comparator: "CodeableConcept" = None
    
    source: "Reference" = None
    
    sourceMaterial: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    genus: "CodeableConcept" = None
    
    species: "CodeableConcept" = None
    
    part: "CodeableConcept" = None
    
    countryOfOrigin: "CodeableConcept" = None
    