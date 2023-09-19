"""
Generated class for SubstanceSourceMaterial. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class SubstanceSourceMaterial:
    """
    Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a material that can result in or can be modified to form a substance. This set of data elements shall be used to define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described using a controlled vocabulary as required. This information is captured for naturally derived polymers ( . starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For Herbal preparations, the fraction information will be captured at the Substance information level and additional information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for further explanation the Substance Class: Structurally Diverse and the herbal annex.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sourceMaterialClass: "CodeableConcept" = None
    
    sourceMaterialType: "CodeableConcept" = None
    
    sourceMaterialState: "CodeableConcept" = None
    
    organismId: "Identifier" = None
    
    organismName: str = None
    
    parentSubstanceId: "Identifier" = None
    
    parentSubstanceName: str = None
    
    countryOfOrigin: "CodeableConcept" = None
    
    geographicalLocation: str = None
    
    developmentStage: "CodeableConcept" = None
    
    fractionDescription: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    fraction: str = None
    
    materialType: "CodeableConcept" = None
    
    organism: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    family: "CodeableConcept" = None
    
    genus: "CodeableConcept" = None
    
    species: "CodeableConcept" = None
    
    intraspecificType: "CodeableConcept" = None
    
    intraspecificDescription: str = None
    
    author: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    authorType: "CodeableConcept" = None
    
    authorDescription: str = None
    
    hybrid: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    maternalOrganismId: str = None
    
    maternalOrganismName: str = None
    
    paternalOrganismId: str = None
    
    paternalOrganismName: str = None
    
    hybridType: "CodeableConcept" = None
    
    organismGeneral: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    kingdom: "CodeableConcept" = None
    
    phylum: "CodeableConcept" = None
    
    class: "CodeableConcept" = None
    
    order: "CodeableConcept" = None
    
    partDescription: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    part: "CodeableConcept" = None
    
    partLocation: "CodeableConcept" = None
    