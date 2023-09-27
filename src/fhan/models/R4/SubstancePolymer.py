"""
Generated class for SubstancePolymer. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.SubstanceAmount import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class StartingMaterial(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' material: Todo
    :param 'CodeableConcept' type: Todo
    :param bool isDefining: Todo
    :param 'SubstanceAmount' amount: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  material: 'CodeableConcept' = None,  type: 'CodeableConcept' = None,  isDefining: bool = None,  amount: 'SubstanceAmount' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.material: 'CodeableConcept' = material 
        self.type: 'CodeableConcept' = type 
        self.isDefining: bool = isDefining 
        self.amount: 'SubstanceAmount' = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StartingMaterial":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class MonomerSet(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' ratioType: Todo
    :param 'StartingMaterial' startingMaterial: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  ratioType: 'CodeableConcept' = None,  startingMaterial: 'StartingMaterial' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.ratioType: 'CodeableConcept' = ratioType 
        self.startingMaterial: list['StartingMaterial'] = startingMaterial or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MonomerSet":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
        
    
        
    
    

class DegreeOfPolymerisation(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' degree: Todo
    :param 'SubstanceAmount' amount: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  degree: 'CodeableConcept' = None,  amount: 'SubstanceAmount' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.degree: 'CodeableConcept' = degree 
        self.amount: 'SubstanceAmount' = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DegreeOfPolymerisation":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


    
    

class StructuralRepresentation(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Todo
    :param str representation: Todo
    :param 'Attachment' attachment: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  representation: str = None,  attachment: 'Attachment' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.representation: str = representation 
        self.attachment: 'Attachment' = attachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructuralRepresentation":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class RepeatUnit(BaseModel):
    """ Todo.:param 'CodeableConcept' repeatUnitAmountType: Todo
    :param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' orientationOfPolymerisation: Todo
    :param str repeatUnit: Todo
    :param 'SubstanceAmount' amount: Todo
    :param 'DegreeOfPolymerisation' degreeOfPolymerisation: Todo
    :param 'StructuralRepresentation' structuralRepresentation: Todo
    """
    def __init__(self,  repeatUnitAmountType: 'CodeableConcept' = None,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  orientationOfPolymerisation: 'CodeableConcept' = None,  repeatUnit: str = None,  amount: 'SubstanceAmount' = None,  degreeOfPolymerisation: 'DegreeOfPolymerisation' = None,  structuralRepresentation: 'StructuralRepresentation' = None, ):
        self.repeatUnitAmountType: 'CodeableConcept' = repeatUnitAmountType 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.orientationOfPolymerisation: 'CodeableConcept' = orientationOfPolymerisation 
        self.repeatUnit: str = repeatUnit 
        self.amount: 'SubstanceAmount' = amount 
        self.degreeOfPolymerisation: list['DegreeOfPolymerisation'] = degreeOfPolymerisation or []
        self.structuralRepresentation: list['StructuralRepresentation'] = structuralRepresentation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RepeatUnit":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


  
    
    

class Repeat(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int numberOfUnits: Todo
    :param str averageMolecularFormula: Todo
    :param 'CodeableConcept' repeatUnitAmountType: Todo
    :param 'RepeatUnit' repeatUnit: Todo
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  numberOfUnits: int = None,  averageMolecularFormula: str = None,  repeatUnitAmountType: 'CodeableConcept' = None,  repeatUnit: 'RepeatUnit' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.numberOfUnits: int = numberOfUnits 
        self.averageMolecularFormula: str = averageMolecularFormula 
        self.repeatUnitAmountType: 'CodeableConcept' = repeatUnitAmountType 
        self.repeatUnit: list['RepeatUnit'] = repeatUnit or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Repeat":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


class SubstancePolymer(DomainResource):
    """ Todo.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'CodeableConcept' _class: Todo
    :param 'CodeableConcept' geometry: Todo
    :param 'CodeableConcept' copolymerConnectivity: Todo
    :param str modification: Todo
    :param 'MonomerSet' monomerSet: Todo
    :param 'Repeat' repeat: Todo
    """
    def __init__(self, resourceType: str = "SubstancePolymer",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  _class: 'CodeableConcept' = None,  geometry: 'CodeableConcept' = None,  copolymerConnectivity: 'CodeableConcept' = None,  modification: str = None,  monomerSet: 'MonomerSet' = None,  repeat: 'Repeat' = None, ):
        self.resourceType: str = resourceType or "SubstancePolymer"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self._class: 'CodeableConcept' = _class 
        self.geometry: 'CodeableConcept' = geometry 
        self.copolymerConnectivity: list['CodeableConcept'] = copolymerConnectivity or []
        self.modification: list[str] = modification or []
        self.monomerSet: list['MonomerSet'] = monomerSet or []
        self.repeat: list['Repeat'] = repeat or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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