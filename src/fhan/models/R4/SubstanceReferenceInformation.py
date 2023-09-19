"""
Generated class for SubstanceReferenceInformation. 
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
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class SubstanceReferenceInformation:
    """
    Todo.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    comment: str = None
    
    gene: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    geneSequenceOrigin: "CodeableConcept" = None
    
    gene: "CodeableConcept" = None
    
    source: "Reference" = None
    
    geneElement: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    element: "Identifier" = None
    
    source: "Reference" = None
    
    classification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    domain: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    subtype: "CodeableConcept" = None
    
    source: "Reference" = None
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    target: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    interaction: "CodeableConcept" = None
    
    organism: "CodeableConcept" = None
    
    organismType: "CodeableConcept" = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: "Range" = None
    
    amountQuantity: str = None
    
    amountType: "CodeableConcept" = None
    
    source: "Reference" = None
    