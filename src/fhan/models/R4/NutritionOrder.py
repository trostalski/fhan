"""
Generated class for NutritionOrder. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class Nutrient(ModelBase):
    """ Class that defines the quantity and type of nutrient modifications (for example carbohydrate, fiber or sodium) required for the oral diet.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' modifier: Type of nutrient that is being modified
    :param 'Quantity' amount: Quantity of the specified nutrient
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  modifier: 'CodeableConcept' = None,  amount: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.modifier: 'CodeableConcept' = modifier 
        self.amount: 'Quantity' = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Nutrient":
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


    
    

class Texture(ModelBase):
    """ Class that describes any texture modifications required for the patient to safely consume various types of solid foods.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' modifier: Code to indicate how to alter the texture of the foods, e.g. pureed
    :param 'CodeableConcept' foodType: Concepts that are used to identify an entity that is ingested for nutritional purposes
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  modifier: 'CodeableConcept' = None,  foodType: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.modifier: 'CodeableConcept' = modifier 
        self.foodType: 'CodeableConcept' = foodType 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Texture":
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


  
    
    

class OralDiet(ModelBase):
    """ Diet given orally in contrast to enteral (tube) feeding.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] type: Type of oral diet or diet restrictions that describe what can be consumed orally
    :param list['Timing'] schedule: Scheduled frequency of diet
    :param list['Nutrient'] nutrient: Required  nutrient modifications
    :param list['Texture'] texture: Required  texture modifications
    :param list['CodeableConcept'] fluidConsistencyType: The required consistency of fluids and liquids provided to the patient
    :param str instruction: Instructions or additional information about the oral diet
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: list['CodeableConcept'] = None,  schedule: list['Timing'] = None,  nutrient: list['Nutrient'] = None,  texture: list['Texture'] = None,  fluidConsistencyType: list['CodeableConcept'] = None,  instruction: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: list['CodeableConcept'] = type or []
        self.schedule: list['Timing'] = schedule or []
        self.nutrient: list['Nutrient'] = nutrient or []
        self.texture: list['Texture'] = texture or []
        self.fluidConsistencyType: list['CodeableConcept'] = fluidConsistencyType or []
        self.instruction: str = instruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "OralDiet":
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


    
    

class Supplement(ModelBase):
    """ Oral nutritional products given in order to add further nutritional value to the patient's diet.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of supplement product requested
    :param str productName: Product or brand name of the nutritional supplement
    :param list['Timing'] schedule: Scheduled frequency of supplement
    :param 'Quantity' quantity: Amount of the nutritional supplement
    :param str instruction: Instructions or additional information about the oral supplement
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  productName: str = None,  schedule: list['Timing'] = None,  quantity: 'Quantity' = None,  instruction: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.productName: str = productName 
        self.schedule: list['Timing'] = schedule or []
        self.quantity: 'Quantity' = quantity 
        self.instruction: str = instruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Supplement":
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


    
        
    
    

class Administration(ModelBase):
    """ Formula administration instructions as structured data.  This repeating structure allows for changing the administration rate or volume over time for both bolus and continuous feeding.  An example of this would be an instruction to increase the rate of continuous feeding every 2 hours.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Timing' schedule: Scheduled frequency of enteral feeding
    :param 'Quantity' quantity: The volume of formula to provide
    :param 'Quantity' rateQuantity: Speed with which the formula is provided per period of time
    :param 'Ratio' rateRatio: Speed with which the formula is provided per period of time
    :param str administrationInstruction: Formula feeding instructions expressed as text
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  schedule: 'Timing' = None,  quantity: 'Quantity' = None,  rateQuantity: 'Quantity' = None,  rateRatio: 'Ratio' = None,  administrationInstruction: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.schedule: 'Timing' = schedule 
        self.quantity: 'Quantity' = quantity 
        self.rateQuantity: 'Quantity' = rateQuantity 
        self.rateRatio: 'Ratio' = rateRatio 
        self.administrationInstruction: str = administrationInstruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Administration":
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


  
    
    

class EnteralFormula(ModelBase):
    """ Feeding provided through the gastrointestinal tract via a tube, catheter, or stoma that delivers nutrition distal to the oral cavity.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' baseFormulaType: Type of enteral or infant formula
    :param str baseFormulaProductName: Product or brand name of the enteral or infant formula
    :param 'CodeableConcept' additiveType: Type of modular component to add to the feeding
    :param str additiveProductName: Product or brand name of the modular additive
    :param 'Quantity' caloricDensity: Amount of energy per specified volume that is required
    :param 'CodeableConcept' routeofAdministration: How the formula should enter the patient's gastrointestinal tract
    :param list['Administration'] administration: Formula feeding instruction as structured data
    :param 'Quantity' maxVolumeToDeliver: Upper limit on formula volume per unit of time
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  baseFormulaType: 'CodeableConcept' = None,  baseFormulaProductName: str = None,  additiveType: 'CodeableConcept' = None,  additiveProductName: str = None,  caloricDensity: 'Quantity' = None,  routeofAdministration: 'CodeableConcept' = None,  administration: list['Administration'] = None,  maxVolumeToDeliver: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.baseFormulaType: 'CodeableConcept' = baseFormulaType 
        self.baseFormulaProductName: str = baseFormulaProductName 
        self.additiveType: 'CodeableConcept' = additiveType 
        self.additiveProductName: str = additiveProductName 
        self.caloricDensity: 'Quantity' = caloricDensity 
        self.routeofAdministration: 'CodeableConcept' = routeofAdministration 
        self.administration: list['Administration'] = administration or []
        self.maxVolumeToDeliver: 'Quantity' = maxVolumeToDeliver 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EnteralFormula":
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


class NutritionOrder(DomainResource):
    """ A request to supply a diet, formula feeding (enteral) or oral nutritional supplement to a patient/resident.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Identifiers assigned to this order
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param str instantiates: Instantiates protocol or definition
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param 'Reference' patient: The person who requires the diet, formula or nutritional supplement
    :param 'Reference' encounter: The encounter associated with this nutrition order
    :param str dateTime: Date and time the nutrition order was requested
    :param 'Reference' orderer: Who ordered the diet, formula or nutritional supplement
    :param list['Reference'] allergyIntolerance: List of the patient's food and nutrition-related allergies and intolerances
    :param list['CodeableConcept'] foodPreferenceModifier: Order-specific modifier about the type of food that should be given
    :param list['CodeableConcept'] excludeFoodModifier: Order-specific modifier about the type of food that should not be given
    :param 'OralDiet' oralDiet: Oral diet components
    :param list['Supplement'] supplement: Supplement components
    :param 'EnteralFormula' enteralFormula: Enteral formula components
    :param list['Annotation'] note: Comments
    """
    def __init__(self, resourceType: str = "NutritionOrder",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  instantiates: str = None,  status: str = None,  intent: str = None,  patient: 'Reference' = None,  encounter: 'Reference' = None,  dateTime: str = None,  orderer: 'Reference' = None,  allergyIntolerance: list['Reference'] = None,  foodPreferenceModifier: list['CodeableConcept'] = None,  excludeFoodModifier: list['CodeableConcept'] = None,  oralDiet: 'OralDiet' = None,  supplement: list['Supplement'] = None,  enteralFormula: 'EnteralFormula' = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "NutritionOrder"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.instantiates: str = instantiates or []
        self.status: str = status 
        self.intent: str = intent 
        self.patient: 'Reference' = patient 
        self.encounter: 'Reference' = encounter 
        self.dateTime: str = dateTime 
        self.orderer: 'Reference' = orderer 
        self.allergyIntolerance: list['Reference'] = allergyIntolerance or []
        self.foodPreferenceModifier: list['CodeableConcept'] = foodPreferenceModifier or []
        self.excludeFoodModifier: list['CodeableConcept'] = excludeFoodModifier or []
        self.oralDiet: 'OralDiet' = oralDiet 
        self.supplement: list['Supplement'] = supplement or []
        self.enteralFormula: 'EnteralFormula' = enteralFormula 
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "NutritionOrder":
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