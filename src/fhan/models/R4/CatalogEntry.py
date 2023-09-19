"""
Generated class for CatalogEntry. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class CatalogEntry:
    """
    Catalog entries are wrappers that contextualize items included in a catalog.
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
    
    orderable: bool = None
    
    referencedItem: "Reference" = None
    
    additionalIdentifier: "Identifier" = None
    
    classification: "CodeableConcept" = None
    
    status: str = None
    
    validityPeriod: "Period" = None
    
    validTo: str = None
    
    lastUpdated: str = None
    
    additionalCharacteristic: "CodeableConcept" = None
    
    additionalClassification: "CodeableConcept" = None
    
    relatedEntry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationtype: str = None
    
    item: "Reference" = None
    