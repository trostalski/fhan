"""
Generated class for MedicationKnowledge. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Duration import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Money import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Resource import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class RelatedMedicationKnowledge(BaseModel):
    """ Associated or related knowledge about a medication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Category of medicationKnowledge
    :param 'Reference' reference: Associated documentation about the associated medication knowledge
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  reference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.reference: list['Reference'] = reference or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RelatedMedicationKnowledge":
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


    
    

class Monograph(BaseModel):
    """ Associated documentation about the medication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The category of medication document
    :param 'Reference' source: Associated documentation about the medication
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  source: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.source: 'Reference' = source 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Monograph":
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


    
    

class Ingredient(BaseModel):
    """ Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param 'Reference' itemReference: Medication(s) or substance(s) contained in the medication
    :param bool isActive: Active ingredient indicator
    :param 'Ratio' strength: Quantity of ingredient present
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  itemCodeableConcept: 'CodeableConcept' = None,  itemReference: 'Reference' = None,  isActive: bool = None,  strength: 'Ratio' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.itemReference: 'Reference' = itemReference 
        self.isActive: bool = isActive 
        self.strength: 'Ratio' = strength 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Ingredient":
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


    
    

class Cost(BaseModel):
    """ The price of the medication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The category of the cost information
    :param str source: The source or owner for the price information
    :param 'Money' cost: The price of the medication
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  source: str = None,  cost: 'Money' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.source: str = source 
        self.cost: 'Money' = cost 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Cost":
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


    
    

class MonitoringProgram(BaseModel):
    """ The program under which the medication is reviewed.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  name: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.name: str = name 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MonitoringProgram":
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


    
        
    
    

class Dosage(BaseModel):
    """ Dosage for the medication for the specific guidelines.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of dosage
    :param 'Dosage' dosage: Dosage for the medication for the specific guidelines
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  dosage: 'Dosage' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.dosage: list['Dosage'] = dosage or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Dosage":
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


    
    

class PatientCharacteristics(BaseModel):
    """ Characteristics of the patient that are relevant to the administration guidelines (for example, height, weight, gender, etc.).:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param 'Quantity' characteristicQuantity: Specific characteristic that is relevant to the administration guideline
    :param str value: The specific characteristic
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  characteristicCodeableConcept: 'CodeableConcept' = None,  characteristicQuantity: 'Quantity' = None,  value: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.characteristicCodeableConcept: 'CodeableConcept' = characteristicCodeableConcept 
        self.characteristicQuantity: 'Quantity' = characteristicQuantity 
        self.value: list[str] = value or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PatientCharacteristics":
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


  
    
    

class AdministrationGuidelines(BaseModel):
    """ Guidelines for the administration of the medication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Dosage' dosage: Dosage for the medication for the specific guidelines
    :param 'CodeableConcept' indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param 'Reference' indicationReference: Indication for use that apply to the specific administration guidelines
    :param 'PatientCharacteristics' patientCharacteristics: Characteristics of the patient that are relevant to the administration guidelines
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  dosage: 'Dosage' = None,  indicationCodeableConcept: 'CodeableConcept' = None,  indicationReference: 'Reference' = None,  patientCharacteristics: 'PatientCharacteristics' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.dosage: list['Dosage'] = dosage or []
        self.indicationCodeableConcept: 'CodeableConcept' = indicationCodeableConcept 
        self.indicationReference: 'Reference' = indicationReference 
        self.patientCharacteristics: list['PatientCharacteristics'] = patientCharacteristics or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdministrationGuidelines":
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


    
    

class MedicineClassification(BaseModel):
    """ Categorization of the medication within a formulary or classification system.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param 'CodeableConcept' classification: Specific category assigned to the medication
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  classification: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.classification: list['CodeableConcept'] = classification or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicineClassification":
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


    
    

class Packaging(BaseModel):
    """ Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: A code that defines the specific type of packaging that the medication can be found in
    :param 'Quantity' quantity: The number of product units the package would contain if fully loaded
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  quantity: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.quantity: 'Quantity' = quantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Packaging":
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


    
    

class DrugCharacteristic(BaseModel):
    """ Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Code specifying the type of characteristic of medication
    :param 'CodeableConcept' valueCodeableConcept: Description of the characteristic
    :param str valueString: Description of the characteristic
    :param 'Quantity' valueQuantity: Description of the characteristic
    :param str valueBase64Binary: Description of the characteristic
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueString: str = None,  valueQuantity: 'Quantity' = None,  valueBase64Binary: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueString: str = valueString 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueBase64Binary: str = valueBase64Binary 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DrugCharacteristic":
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


    
        
    
    

class Substitution(BaseModel):
    """ Specifies if changes are allowed when dispensing a medication from a regulatory perspective.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  type: 'CodeableConcept' = None,  allowed: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.allowed: bool = allowed 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Substitution":
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


    
    

class Schedule(BaseModel):
    """ Specifies the schedule of a medication in jurisdiction.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' schedule: Specifies the specific drug schedule
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  schedule: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.schedule: 'CodeableConcept' = schedule 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Schedule":
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


    
    

class MaxDispense(BaseModel):
    """ The maximum number of units of the medication that can be dispensed in a period.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Quantity' quantity: The maximum number of units of the medication that can be dispensed
    :param 'Duration' period: The period that applies to the maximum number of units
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  quantity: 'Quantity' = None,  period: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.quantity: 'Quantity' = quantity 
        self.period: 'Duration' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MaxDispense":
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


  
    
    

class Regulatory(BaseModel):
    """ Regulatory information about a medication.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' regulatoryAuthority: Specifies the authority of the regulation
    :param 'Substitution' substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param 'Schedule' schedule: Specifies the schedule of a medication in jurisdiction
    :param 'MaxDispense' maxDispense: The maximum number of units of the medication that can be dispensed in a period
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  regulatoryAuthority: 'Reference' = None,  substitution: 'Substitution' = None,  schedule: 'Schedule' = None,  maxDispense: 'MaxDispense' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.regulatoryAuthority: 'Reference' = regulatoryAuthority 
        self.substitution: list['Substitution'] = substitution or []
        self.schedule: list['Schedule'] = schedule or []
        self.maxDispense: 'MaxDispense' = maxDispense 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Regulatory":
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


    
    

class Kinetics(BaseModel):
    """ The time course of drug absorption, distribution, metabolism and excretion of a medication from the body.:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Quantity' areaUnderCurve: The drug concentration measured at certain discrete points in time
    :param 'Quantity' lethalDose50: The median lethal dose of a drug
    :param 'Duration' halfLifePeriod: Time required for concentration in the body to decrease by half
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  areaUnderCurve: 'Quantity' = None,  lethalDose50: 'Quantity' = None,  halfLifePeriod: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.areaUnderCurve: list['Quantity'] = areaUnderCurve or []
        self.lethalDose50: list['Quantity'] = lethalDose50 or []
        self.halfLifePeriod: 'Duration' = halfLifePeriod 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Kinetics":
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


class MedicationKnowledge(DomainResource):
    """ Information about a medication that is used to support knowledge.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'CodeableConcept' code: Code that identifies this medication
    :param str status: active | inactive | entered-in-error
    :param 'Reference' manufacturer: Manufacturer of the item
    :param 'CodeableConcept' doseForm: powder | tablets | capsule +
    :param 'Quantity' amount: Amount of drug in package
    :param str synonym: Additional names for a medication
    :param 'RelatedMedicationKnowledge' relatedMedicationKnowledge: Associated or related medication information
    :param 'Reference' associatedMedication: A medication resource that is associated with this medication
    :param 'CodeableConcept' productType: Category of the medication or product
    :param 'Monograph' monograph: Associated documentation about the medication
    :param 'Ingredient' ingredient: Active or inactive ingredient
    :param str preparationInstruction: The instructions for preparing the medication
    :param 'CodeableConcept' intendedRoute: The intended or approved route of administration
    :param 'Cost' cost: The pricing of the medication
    :param 'MonitoringProgram' monitoringProgram: Program under which a medication is reviewed
    :param 'AdministrationGuidelines' administrationGuidelines: Guidelines for administration of the medication
    :param 'MedicineClassification' medicineClassification: Categorization of the medication within a formulary or classification system
    :param 'Packaging' packaging: Details about packaged medications
    :param 'DrugCharacteristic' drugCharacteristic: Specifies descriptive properties of the medicine
    :param 'Reference' contraindication: Potential clinical issue with or between medication(s)
    :param 'Regulatory' regulatory: Regulatory information about a medication
    :param 'Kinetics' kinetics: The time course of drug absorption, distribution, metabolism and excretion of a medication from the body
    """
    def __init__(self, resourceType: str = "MedicationKnowledge",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  code: 'CodeableConcept' = None,  status: str = None,  manufacturer: 'Reference' = None,  doseForm: 'CodeableConcept' = None,  amount: 'Quantity' = None,  synonym: str = None,  relatedMedicationKnowledge: 'RelatedMedicationKnowledge' = None,  associatedMedication: 'Reference' = None,  productType: 'CodeableConcept' = None,  monograph: 'Monograph' = None,  ingredient: 'Ingredient' = None,  preparationInstruction: str = None,  intendedRoute: 'CodeableConcept' = None,  cost: 'Cost' = None,  monitoringProgram: 'MonitoringProgram' = None,  administrationGuidelines: 'AdministrationGuidelines' = None,  medicineClassification: 'MedicineClassification' = None,  packaging: 'Packaging' = None,  drugCharacteristic: 'DrugCharacteristic' = None,  contraindication: 'Reference' = None,  regulatory: 'Regulatory' = None,  kinetics: 'Kinetics' = None, ):
        self.resourceType: str = resourceType or "MedicationKnowledge"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.status: str = status 
        self.manufacturer: 'Reference' = manufacturer 
        self.doseForm: 'CodeableConcept' = doseForm 
        self.amount: 'Quantity' = amount 
        self.synonym: list[str] = synonym or []
        self.relatedMedicationKnowledge: list['RelatedMedicationKnowledge'] = relatedMedicationKnowledge or []
        self.associatedMedication: list['Reference'] = associatedMedication or []
        self.productType: list['CodeableConcept'] = productType or []
        self.monograph: list['Monograph'] = monograph or []
        self.ingredient: list['Ingredient'] = ingredient or []
        self.preparationInstruction: str = preparationInstruction 
        self.intendedRoute: list['CodeableConcept'] = intendedRoute or []
        self.cost: list['Cost'] = cost or []
        self.monitoringProgram: list['MonitoringProgram'] = monitoringProgram or []
        self.administrationGuidelines: list['AdministrationGuidelines'] = administrationGuidelines or []
        self.medicineClassification: list['MedicineClassification'] = medicineClassification or []
        self.packaging: 'Packaging' = packaging 
        self.drugCharacteristic: list['DrugCharacteristic'] = drugCharacteristic or []
        self.contraindication: list['Reference'] = contraindication or []
        self.regulatory: list['Regulatory'] = regulatory or []
        self.kinetics: list['Kinetics'] = kinetics or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
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