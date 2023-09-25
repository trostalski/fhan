"""
Generated class for SubstanceSourceMaterial. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class FractionDescription(ModelBase):
    """ Many complex materials are fractions of parts of plants, animals, or minerals. Fraction elements are often necessary to define both Substances and Specified Group 1 Substances. For substances derived from Plants, fraction information will be captured at the Substance information level ( . Oils, Juices and Exudates). Additional information for Extracts, such as extraction solvent composition, will be captured at the Specified Substance Group 1 information level. For plasma-derived products fraction information will be captured at the Substance and the Specified Substance Group 1 levels.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str fraction: This element is capturing information about the fraction of a plant part, or human plasma for fractionation
    :param 'CodeableConcept' materialType: The specific type of the material constituting the component. For Herbal preparations the particulars of the extracts (liquid/dry) is described in Specified Substance Group 1
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  fraction: str = None,  materialType: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.fraction: str = fraction 
        self.materialType: 'CodeableConcept' = materialType 
        

    @classmethod
    def from_dict(cls, data: dict) -> "FractionDescription":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
        
    
    

class Author(ModelBase):
    """ 4.9.13.6.1 Author type (Conditional).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' authorType: The type of author of an organism species shall be specified. The parenthetical author of an organism species refers to the first author who published the plant/animal name (of any rank). The primary author of an organism species refers to the first author(s), who validly published the plant/animal name
    :param str authorDescription: The author of an organism species shall be specified. The author year of an organism shall also be specified when applicable; refers to the year in which the first author(s) published the infraspecific plant/animal name (of any rank)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  authorType: 'CodeableConcept' = None,  authorDescription: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.authorType: 'CodeableConcept' = authorType 
        self.authorDescription: str = authorDescription 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Author":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class Hybrid(ModelBase):
    """ 4.9.13.8.1 Hybrid species maternal organism ID (Optional).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str maternalOrganismId: The identifier of the maternal species constituting the hybrid organism shall be specified based on a controlled vocabulary. For plants, the parents aren’t always known, and it is unlikely that it will be known which is maternal and which is paternal
    :param str maternalOrganismName: The name of the maternal species constituting the hybrid organism shall be specified. For plants, the parents aren’t always known, and it is unlikely that it will be known which is maternal and which is paternal
    :param str paternalOrganismId: The identifier of the paternal species constituting the hybrid organism shall be specified based on a controlled vocabulary
    :param str paternalOrganismName: The name of the paternal species constituting the hybrid organism shall be specified
    :param 'CodeableConcept' hybridType: The hybrid type of an organism shall be specified
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  maternalOrganismId: str = None,  maternalOrganismName: str = None,  paternalOrganismId: str = None,  paternalOrganismName: str = None,  hybridType: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.maternalOrganismId: str = maternalOrganismId 
        self.maternalOrganismName: str = maternalOrganismName 
        self.paternalOrganismId: str = paternalOrganismId 
        self.paternalOrganismName: str = paternalOrganismName 
        self.hybridType: 'CodeableConcept' = hybridType 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Hybrid":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class OrganismGeneral(ModelBase):
    """ 4.9.13.7.1 Kingdom (Conditional).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' kingdom: The kingdom of an organism shall be specified
    :param 'CodeableConcept' phylum: The phylum of an organism shall be specified
    :param 'CodeableConcept' _class: The class of an organism shall be specified
    :param 'CodeableConcept' order: The order of an organism shall be specified,
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  kingdom: 'CodeableConcept' = None,  phylum: 'CodeableConcept' = None,  _class: 'CodeableConcept' = None,  order: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.kingdom: 'CodeableConcept' = kingdom 
        self.phylum: 'CodeableConcept' = phylum 
        self._class: 'CodeableConcept' = _class 
        self.order: 'CodeableConcept' = order 
        

    @classmethod
    def from_dict(cls, data: dict) -> "OrganismGeneral":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


  
    
    

class Organism(ModelBase):
    """ This subclause describes the organism which the substance is derived from. For vaccines, the parent organism shall be specified based on these subclause elements. As an example, full taxonomy will be described for the Substance Name: ., Leaf.:param 'Identifier' organismId: The unique identifier associated with the source material parent organism shall be specified
    :param str organismName: The organism accepted Scientific name shall be provided based on the organism taxonomy
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' family: The family of an organism shall be specified
    :param 'CodeableConcept' genus: The genus of an organism shall be specified; refers to the Latin epithet of the genus element of the plant/animal scientific name; it is present in names for genera, species and infraspecies
    :param 'CodeableConcept' species: The species of an organism shall be specified; refers to the Latin epithet of the species of the plant/animal; it is present in names for species and infraspecies
    :param 'CodeableConcept' intraspecificType: The Intraspecific type of an organism shall be specified
    :param str intraspecificDescription: The intraspecific description of an organism shall be specified based on a controlled vocabulary. For Influenza Vaccine, the intraspecific description shall contain the syntax of the antigen in line with the WHO convention
    :param list['Author'] author: 4.9.13.6.1 Author type (Conditional)
    :param 'Hybrid' hybrid: 4.9.13.8.1 Hybrid species maternal organism ID (Optional)
    :param 'OrganismGeneral' organismGeneral: 4.9.13.7.1 Kingdom (Conditional)
    """
    def __init__(self,  organismId: 'Identifier' = None,  organismName: str = None,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  family: 'CodeableConcept' = None,  genus: 'CodeableConcept' = None,  species: 'CodeableConcept' = None,  intraspecificType: 'CodeableConcept' = None,  intraspecificDescription: str = None,  author: list['Author'] = None,  hybrid: 'Hybrid' = None,  organismGeneral: 'OrganismGeneral' = None, ):
        self.organismId: 'Identifier' = organismId 
        self.organismName: str = organismName 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.family: 'CodeableConcept' = family 
        self.genus: 'CodeableConcept' = genus 
        self.species: 'CodeableConcept' = species 
        self.intraspecificType: 'CodeableConcept' = intraspecificType 
        self.intraspecificDescription: str = intraspecificDescription 
        self.author: list['Author'] = author or []
        self.hybrid: 'Hybrid' = hybrid 
        self.organismGeneral: 'OrganismGeneral' = organismGeneral 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Organism":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class PartDescription(ModelBase):
    """ To do.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' part: Entity of anatomical origin of source material within an organism
    :param 'CodeableConcept' partLocation: The detailed anatomic location when the part can be extracted from different anatomical locations of the organism. Multiple alternative locations may apply
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  part: 'CodeableConcept' = None,  partLocation: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.part: 'CodeableConcept' = part 
        self.partLocation: 'CodeableConcept' = partLocation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PartDescription":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


class SubstanceSourceMaterial(DomainResource):
    """ Source material shall capture information on the taxonomic and anatomical origins as well as the fraction of a material that can result in or can be modified to form a substance. This set of data elements shall be used to define polymer substances isolated from biological matrices. Taxonomic and anatomical origins shall be described using a controlled vocabulary as required. This information is captured for naturally derived polymers ( . starch) and structurally diverse substances. For Organisms belonging to the Kingdom Plantae the Substance level defines the fresh material of a single species or infraspecies, the Herbal Drug and the Herbal preparation. For Herbal preparations, the fraction information will be captured at the Substance information level and additional information for herbal extracts will be captured at the Specified Substance Group 1 information level. See for further explanation the Substance Class: Structurally Diverse and the herbal annex.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'CodeableConcept' sourceMaterialClass: General high level classification of the source material specific to the origin of the material
    :param 'CodeableConcept' sourceMaterialType: The type of the source material shall be specified based on a controlled vocabulary. For vaccines, this subclause refers to the class of infectious agent
    :param 'CodeableConcept' sourceMaterialState: The state of the source material when extracted
    :param 'Identifier' organismId: The unique identifier associated with the source material parent organism shall be specified
    :param str organismName: The organism accepted Scientific name shall be provided based on the organism taxonomy
    :param list['Identifier'] parentSubstanceId: The parent of the herbal drug Ginkgo biloba, Leaf is the substance ID of the substance (fresh) of Ginkgo biloba L. or Ginkgo biloba L. (Whole plant)
    :param str parentSubstanceName: The parent substance of the Herbal Drug, or Herbal preparation
    :param list['CodeableConcept'] countryOfOrigin: The country where the plant material is harvested or the countries where the plasma is sourced from as laid down in accordance with the Plasma Master File. For “Plasma-derived substances” the attribute country of origin provides information about the countries used for the manufacturing of the Cryopoor plama or Crioprecipitate
    :param str geographicalLocation: The place/region where the plant is harvested or the places/regions where the animal source material has its habitat
    :param 'CodeableConcept' developmentStage: Stage of life for animals, plants, insects and microorganisms. This information shall be provided only when the substance is significantly different in these stages (e.g. foetal bovine serum)
    :param list['FractionDescription'] fractionDescription: Many complex materials are fractions of parts of plants, animals, or minerals. Fraction elements are often necessary to define both Substances and Specified Group 1 Substances. For substances derived from Plants, fraction information will be captured at the Substance information level ( . Oils, Juices and Exudates). Additional information for Extracts, such as extraction solvent composition, will be captured at the Specified Substance Group 1 information level. For plasma-derived products fraction information will be captured at the Substance and the Specified Substance Group 1 levels
    :param 'Organism' organism: This subclause describes the organism which the substance is derived from. For vaccines, the parent organism shall be specified based on these subclause elements. As an example, full taxonomy will be described for the Substance Name: ., Leaf
    :param list['PartDescription'] partDescription: To do
    """
    def __init__(self, resourceType: str = "SubstanceSourceMaterial",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sourceMaterialClass: 'CodeableConcept' = None,  sourceMaterialType: 'CodeableConcept' = None,  sourceMaterialState: 'CodeableConcept' = None,  organismId: 'Identifier' = None,  organismName: str = None,  parentSubstanceId: list['Identifier'] = None,  parentSubstanceName: str = None,  countryOfOrigin: list['CodeableConcept'] = None,  geographicalLocation: str = None,  developmentStage: 'CodeableConcept' = None,  fractionDescription: list['FractionDescription'] = None,  organism: 'Organism' = None,  partDescription: list['PartDescription'] = None, ):
        self.resourceType: str = resourceType or "SubstanceSourceMaterial"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sourceMaterialClass: 'CodeableConcept' = sourceMaterialClass 
        self.sourceMaterialType: 'CodeableConcept' = sourceMaterialType 
        self.sourceMaterialState: 'CodeableConcept' = sourceMaterialState 
        self.organismId: 'Identifier' = organismId 
        self.organismName: str = organismName 
        self.parentSubstanceId: list['Identifier'] = parentSubstanceId or []
        self.parentSubstanceName: str = parentSubstanceName or []
        self.countryOfOrigin: list['CodeableConcept'] = countryOfOrigin or []
        self.geographicalLocation: str = geographicalLocation or []
        self.developmentStage: 'CodeableConcept' = developmentStage 
        self.fractionDescription: list['FractionDescription'] = fractionDescription or []
        self.organism: 'Organism' = organism 
        self.partDescription: list['PartDescription'] = partDescription or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSourceMaterial":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance