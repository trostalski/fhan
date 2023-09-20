"""
Generated class for SubstanceSourceMaterial. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class FractionDescription(Element):
    """ Many complex materials are fractions of parts of plants, animals, or minerals. Fraction elements are often necessary to define both Substances and Specified Group 1 Substances. For substances derived from Plants, fraction information will be captured at the Substance information level ( . Oils, Juices and Exudates). Additional information for Extracts, such as extraction solvent composition, will be captured at the Specified Substance Group 1 information level. For plasma-derived products fraction information will be captured at the Substance and the Specified Substance Group 1 levels.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str fraction: This element is capturing information about the fraction of a plant part, or human plasma for fractionation
    :param CodeableConcept materialType: The specific type of the material constituting the component. For Herbal preparations the particulars of the extracts (liquid/dry) is described in Specified Substance Group 1
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    fraction: str = None
    materialType: "CodeableConcept" = None
    

    
        
    
    
@dataclass
class Author(Element):
    """ 4.9.13.6.1 Author type (Conditional).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept authorType: The type of author of an organism species shall be specified. The parenthetical author of an organism species refers to the first author who published the plant/animal name (of any rank). The primary author of an organism species refers to the first author(s), who validly published the plant/animal name
    :param str authorDescription: The author of an organism species shall be specified. The author year of an organism shall also be specified when applicable; refers to the year in which the first author(s) published the infraspecific plant/animal name (of any rank)
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    authorType: "CodeableConcept" = None
    
    authorDescription: str = None
    

    
    
@dataclass
class Hybrid(Element):
    """ 4.9.13.8.1 Hybrid species maternal organism ID (Optional).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str maternalOrganismId: The identifier of the maternal species constituting the hybrid organism shall be specified based on a controlled vocabulary. For plants, the parents aren’t always known, and it is unlikely that it will be known which is maternal and which is paternal
    :param str maternalOrganismName: The name of the maternal species constituting the hybrid organism shall be specified. For plants, the parents aren’t always known, and it is unlikely that it will be known which is maternal and which is paternal
    :param str paternalOrganismId: The identifier of the paternal species constituting the hybrid organism shall be specified based on a controlled vocabulary
    :param str paternalOrganismName: The name of the paternal species constituting the hybrid organism shall be specified
    :param CodeableConcept hybridType: The hybrid type of an organism shall be specified
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    maternalOrganismId: str = None
    
    maternalOrganismName: str = None
    
    paternalOrganismId: str = None
    
    paternalOrganismName: str = None
    hybridType: "CodeableConcept" = None
    

    
    
@dataclass
class OrganismGeneral(Element):
    """ 4.9.13.7.1 Kingdom (Conditional).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept kingdom: The kingdom of an organism shall be specified
    :param CodeableConcept phylum: The phylum of an organism shall be specified
    :param CodeableConcept _class: The class of an organism shall be specified
    :param CodeableConcept order: The order of an organism shall be specified,
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    kingdom: "CodeableConcept" = None
    phylum: "CodeableConcept" = None
    _class: "CodeableConcept" = None
    order: "CodeableConcept" = None
    

  
    
    
@dataclass
class Organism(Element):
    """ This subclause describes the organism which the substance is derived from. For vaccines, the parent organism shall be specified based on these subclause elements. As an example, full taxonomy will be described for the Substance Name: ., Leaf.:param Identifier organismId: The unique identifier associated with the source material parent organism shall be specified
    :param str organismName: The organism accepted Scientific name shall be provided based on the organism taxonomy
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept family: The family of an organism shall be specified
    :param CodeableConcept genus: The genus of an organism shall be specified; refers to the Latin epithet of the genus element of the plant/animal scientific name; it is present in names for genera, species and infraspecies
    :param CodeableConcept species: The species of an organism shall be specified; refers to the Latin epithet of the species of the plant/animal; it is present in names for species and infraspecies
    :param CodeableConcept intraspecificType: The Intraspecific type of an organism shall be specified
    :param str intraspecificDescription: The intraspecific description of an organism shall be specified based on a controlled vocabulary. For Influenza Vaccine, the intraspecific description shall contain the syntax of the antigen in line with the WHO convention
    :param Author author: 4.9.13.6.1 Author type (Conditional)
    :param Hybrid hybrid: 4.9.13.8.1 Hybrid species maternal organism ID (Optional)
    :param OrganismGeneral organismGeneral: 4.9.13.7.1 Kingdom (Conditional)
    """organismId: "Identifier" = None
    
    organismName: str = None
    
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    family: "CodeableConcept" = None
    genus: "CodeableConcept" = None
    species: "CodeableConcept" = None
    intraspecificType: "CodeableConcept" = None
    
    intraspecificDescription: str = None
    author: list[Author] = None
    hybrid: "Hybrid" = None
    organismGeneral: "OrganismGeneral" = None
    

    
    
@dataclass
class PartDescription(Element):
    """ To do.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept part: Entity of anatomical origin of source material within an organism
    :param CodeableConcept partLocation: The detailed anatomic location when the part can be extracted from different anatomical locations of the organism. Multiple alternative locations may apply
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    part: "CodeableConcept" = None
    partLocation: "CodeableConcept" = None
    

@dataclass
class SubstanceSourceMaterial(ModelBase):
    """ Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a material that can result in or can be modified to form a substance. This set of data elements shall be used to define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described using a controlled vocabulary as required. This information is captured for naturally derived polymers ( . starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For Herbal preparations, the fraction information will be captured at the Substance information level and additional information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for further explanation the Substance Class: Structurally Diverse and the herbal annex.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept sourceMaterialClass: General high level classification of the source material specific to the origin of the material
    :param CodeableConcept sourceMaterialType: The type of the source material shall be specified based on a controlled vocabulary. For vaccines, this subclause refers to the class of infectious agent
    :param CodeableConcept sourceMaterialState: The state of the source material when extracted
    :param Identifier organismId: The unique identifier associated with the source material parent organism shall be specified
    :param str organismName: The organism accepted Scientific name shall be provided based on the organism taxonomy
    :param Identifier parentSubstanceId: The parent of the herbal drug Ginkgo biloba, Leaf is the substance ID of the substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L. (Whole plant)
    :param str parentSubstanceName: The parent substance of the Herbal Drug, or Herbal preparation
    :param CodeableConcept countryOfOrigin: The country where the plant material is harvested or the countries where the plasma is sourced from as laid down in accordance with the Plasma Master File. For “Plasma-derived substances” the attribute country of origin provides information about the countries used for the manufacturing of the Cryopoor plama or Crioprecipitate
    :param str geographicalLocation: The place/region where the plant is harvested or the places/regions where the animal source material has its habitat
    :param CodeableConcept developmentStage: Stage of life for animals, plants, insects and microorganisms. This information shall be provided only when the substance is significantly different in these stages (e.g. foetal bovine serum)
    :param FractionDescription fractionDescription: Many complex materials are fractions of parts of plants, animals, or minerals. Fraction elements are often necessary to define both Substances and Specified Group 1 Substances. For substances derived from Plants, fraction information will be captured at the Substance information level ( . Oils, Juices and Exudates). Additional information for Extracts, such as extraction solvent composition, will be captured at the Specified Substance Group 1 information level. For plasma-derived products fraction information will be captured at the Substance and the Specified Substance Group 1 levels
    :param Organism organism: This subclause describes the organism which the substance is derived from. For vaccines, the parent organism shall be specified based on these subclause elements. As an example, full taxonomy will be described for the Substance Name: ., Leaf
    :param PartDescription partDescription: To do
    """

    resourceType: str = "SubstanceSourceMaterial"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    sourceMaterialClass: "CodeableConcept" = None
    
    sourceMaterialType: "CodeableConcept" = None
    
    sourceMaterialState: "CodeableConcept" = None
    
    organismId: "Identifier" = None
    
    organismName: str = None
    
    parentSubstanceId: list["Identifier"] = None
    
    parentSubstanceName: str = None
    
    countryOfOrigin: list["CodeableConcept"] = None
    
    geographicalLocation: str = None
    
    developmentStage: "CodeableConcept" = None
    
    fractionDescription: list["FractionDescription"] = None
    
    organism: "Organism" = None
    
    partDescription: list["PartDescription"] = None
    