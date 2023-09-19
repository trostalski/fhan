"""
Generated class for MolecularSequence. 
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
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class MolecularSequence:
    """
    Raw data describing a biological sequence.
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
    
    type: str = None
    
    coordinateSystem: int = None
    
    patient: "Reference" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    performer: "Reference" = None
    
    quantity: "Quantity" = None
    
    referenceSeq: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    chromosome: "CodeableConcept" = None
    
    genomeBuild: str = None
    
    orientation: str = None
    
    referenceSeqId: "CodeableConcept" = None
    
    referenceSeqPointer: "Reference" = None
    
    referenceSeqString: str = None
    
    strand: str = None
    
    windowStart: int = None
    
    windowEnd: int = None
    
    variant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    start: int = None
    
    end: int = None
    
    observedAllele: str = None
    
    referenceAllele: str = None
    
    cigar: str = None
    
    variantPointer: "Reference" = None
    
    observedSeq: str = None
    
    quality: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    standardSequence: "CodeableConcept" = None
    
    start: int = None
    
    end: int = None
    
    score: "Quantity" = None
    
    method: "CodeableConcept" = None
    
    truthTP: float = None
    
    queryTP: float = None
    
    truthFN: float = None
    
    queryFP: float = None
    
    gtFP: float = None
    
    precision: float = None
    
    recall: float = None
    
    fScore: float = None
    
    roc: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    score: int = None
    
    numTP: int = None
    
    numFP: int = None
    
    numFN: int = None
    
    precision: float = None
    
    sensitivity: float = None
    
    fMeasure: float = None
    
    readCoverage: int = None
    
    repository: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    url: str = None
    
    name: str = None
    
    datasetId: str = None
    
    variantsetId: str = None
    
    readsetId: str = None
    
    pointer: "Reference" = None
    
    structureVariant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    variantType: "CodeableConcept" = None
    
    exact: bool = None
    
    length: int = None
    
    outer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    start: int = None
    
    end: int = None
    
    inner: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    start: int = None
    
    end: int = None
    