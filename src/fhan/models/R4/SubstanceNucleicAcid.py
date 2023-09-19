"""
Generated class for SubstanceNucleicAcid. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class SubstanceNucleicAcid:
    """
    Nucleic acids are defined by three distinct elements: the base, sugar and linkage. Individual substance/moiety IDs will be created for each of these elements. The nucleotide sequence will be always entered in the 5’-3’ direction.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequenceType: "CodeableConcept" = None
    
    numberOfSubunits: int = None
    
    areaOfHybridisation: str = None
    
    oligoNucleotideType: "CodeableConcept" = None
    
    subunit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    subunit: int = None
    
    sequence: str = None
    
    length: int = None
    
    sequenceAttachment: "Attachment" = None
    
    fivePrime: "CodeableConcept" = None
    
    threePrime: "CodeableConcept" = None
    
    linkage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    connectivity: str = None
    
    identifier: "Identifier" = None
    
    name: str = None
    
    residueSite: str = None
    
    sugar: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    name: str = None
    
    residueSite: str = None
    