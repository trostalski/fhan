"""
Generated class for MedicinalProductIngredient. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
        
    
    

class ReferenceStrength(ModelBase):
    """ Strength expressed in terms of a reference substance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' substance: Relevant reference substance
    :param 'Ratio' strength: Strength expressed in terms of a reference substance
    :param 'Ratio' strengthLowLimit: Strength expressed in terms of a reference substance
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param list['CodeableConcept'] country: The country or countries for which the strength range applies
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  substance: 'CodeableConcept' = None,  strength: 'Ratio' = None,  strengthLowLimit: 'Ratio' = None,  measurementPoint: str = None,  country: list['CodeableConcept'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.substance: 'CodeableConcept' = substance 
        self.strength: 'Ratio' = strength 
        self.strengthLowLimit: 'Ratio' = strengthLowLimit 
        self.measurementPoint: str = measurementPoint 
        self.country: list['CodeableConcept'] = country or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ReferenceStrength":
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


  
    
    

class Strength(ModelBase):
    """ Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Ratio' presentation: The quantity of substance in the unit of presentation, or in the volume (or mass) of the single pharmaceutical product or manufactured item
    :param 'Ratio' presentationLowLimit: A lower limit for the quantity of substance in the unit of presentation. For use when there is a range of strengths, this is the lower limit, with the presentation attribute becoming the upper limit
    :param 'Ratio' concentration: The strength per unitary volume (or mass)
    :param 'Ratio' concentrationLowLimit: A lower limit for the strength per unitary volume (or mass), for when there is a range. The concentration attribute then becomes the upper limit
    :param str measurementPoint: For when strength is measured at a particular point or distance
    :param list['CodeableConcept'] country: The country or countries for which the strength range applies
    :param list['ReferenceStrength'] referenceStrength: Strength expressed in terms of a reference substance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  presentation: 'Ratio' = None,  presentationLowLimit: 'Ratio' = None,  concentration: 'Ratio' = None,  concentrationLowLimit: 'Ratio' = None,  measurementPoint: str = None,  country: list['CodeableConcept'] = None,  referenceStrength: list['ReferenceStrength'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.presentation: 'Ratio' = presentation 
        self.presentationLowLimit: 'Ratio' = presentationLowLimit 
        self.concentration: 'Ratio' = concentration 
        self.concentrationLowLimit: 'Ratio' = concentrationLowLimit 
        self.measurementPoint: str = measurementPoint 
        self.country: list['CodeableConcept'] = country or []
        self.referenceStrength: list['ReferenceStrength'] = referenceStrength or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Strength":
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


  
    
    

class SpecifiedSubstance(ModelBase):
    """ A specified substance that comprises this ingredient.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: The specified substance
    :param 'CodeableConcept' group: The group of specified substance, e.g. group 1 to 4
    :param 'CodeableConcept' confidentiality: Confidentiality level of the specified substance as the ingredient
    :param list['Strength'] strength: Quantity of the substance or specified substance present in the manufactured item or pharmaceutical product
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  group: 'CodeableConcept' = None,  confidentiality: 'CodeableConcept' = None,  strength: list['Strength'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.group: 'CodeableConcept' = group 
        self.confidentiality: 'CodeableConcept' = confidentiality 
        self.strength: list['Strength'] = strength or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SpecifiedSubstance":
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


    
    

class Substance(ModelBase):
    """ The ingredient substance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: The ingredient substance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Substance":
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


class MedicinalProductIngredient(DomainResource):
    """ An ingredient of a manufactured item or pharmaceutical product.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Identifier for the ingredient
    :param 'CodeableConcept' role: Ingredient role e.g. Active ingredient, excipient
    :param bool allergenicIndicator: If the ingredient is a known or suspected allergen
    :param list['Reference'] manufacturer: Manufacturer of this Ingredient
    :param list['SpecifiedSubstance'] specifiedSubstance: A specified substance that comprises this ingredient
    :param 'Substance' substance: The ingredient substance
    """
    def __init__(self, resourceType: str = "MedicinalProductIngredient",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  role: 'CodeableConcept' = None,  allergenicIndicator: bool = None,  manufacturer: list['Reference'] = None,  specifiedSubstance: list['SpecifiedSubstance'] = None,  substance: 'Substance' = None, ):
        self.resourceType: str = resourceType or "MedicinalProductIngredient"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.role: 'CodeableConcept' = role 
        self.allergenicIndicator: bool = allergenicIndicator 
        self.manufacturer: list['Reference'] = manufacturer or []
        self.specifiedSubstance: list['SpecifiedSubstance'] = specifiedSubstance or []
        self.substance: 'Substance' = substance 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductIngredient":
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