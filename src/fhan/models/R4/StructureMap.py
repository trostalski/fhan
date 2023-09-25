"""
Generated class for StructureMap. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Distance import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Duration import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Count import *
from fhan.models.R4.Address import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Age import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.DomainResource import *


    
    

class Structure(ModelBase):
    """ A structure definition used by this map. The structure definition may describe instances that are converted, or the instances that are produced.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: Canonical reference to structure definition
    :param str mode: source | queried | target | produced
    :param str alias: Name for type in this map
    :param str documentation: Documentation on use of structure
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  mode: str = None,  alias: str = None,  documentation: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.mode: str = mode 
        self.alias: str = alias 
        self.documentation: str = documentation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Structure":
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


    
        
    
    

class Input(ModelBase):
    """ A name assigned to an instance of data. The instance must be provided when the mapping is invoked.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name for this instance of data
    :param str type: Type for this instance of data
    :param str mode: source | target
    :param str documentation: Documentation for this instance of data
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  type: str = None,  mode: str = None,  documentation: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.type: str = type 
        self.mode: str = mode 
        self.documentation: str = documentation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Input":
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


    
        
    
    

class Source(ModelBase):
    """ Source inputs to the mapping.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValueBase64Binary: Default value if no value exists
    :param bool defaultValueBoolean: Default value if no value exists
    :param str defaultValueCanonical: Default value if no value exists
    :param str defaultValueCode: Default value if no value exists
    :param str defaultValueDate: Default value if no value exists
    :param str defaultValueDateTime: Default value if no value exists
    :param float defaultValueDecimal: Default value if no value exists
    :param str defaultValueId: Default value if no value exists
    :param str defaultValueInstant: Default value if no value exists
    :param int defaultValueInteger: Default value if no value exists
    :param str defaultValueMarkdown: Default value if no value exists
    :param str defaultValueOid: Default value if no value exists
    :param int defaultValuePositiveInt: Default value if no value exists
    :param str defaultValueString: Default value if no value exists
    :param str defaultValueTime: Default value if no value exists
    :param int defaultValueUnsignedInt: Default value if no value exists
    :param str defaultValueUri: Default value if no value exists
    :param str defaultValueUrl: Default value if no value exists
    :param str defaultValueUuid: Default value if no value exists
    :param 'Address' defaultValueAddress: Default value if no value exists
    :param 'Age' defaultValueAge: Default value if no value exists
    :param 'Annotation' defaultValueAnnotation: Default value if no value exists
    :param 'Attachment' defaultValueAttachment: Default value if no value exists
    :param 'CodeableConcept' defaultValueCodeableConcept: Default value if no value exists
    :param 'Coding' defaultValueCoding: Default value if no value exists
    :param 'ContactPoint' defaultValueContactPoint: Default value if no value exists
    :param 'Count' defaultValueCount: Default value if no value exists
    :param 'Distance' defaultValueDistance: Default value if no value exists
    :param 'Duration' defaultValueDuration: Default value if no value exists
    :param 'HumanName' defaultValueHumanName: Default value if no value exists
    :param 'Identifier' defaultValueIdentifier: Default value if no value exists
    :param 'Money' defaultValueMoney: Default value if no value exists
    :param 'Period' defaultValuePeriod: Default value if no value exists
    :param 'Quantity' defaultValueQuantity: Default value if no value exists
    :param 'Range' defaultValueRange: Default value if no value exists
    :param 'Ratio' defaultValueRatio: Default value if no value exists
    :param 'Reference' defaultValueReference: Default value if no value exists
    :param 'SampledData' defaultValueSampledData: Default value if no value exists
    :param 'Signature' defaultValueSignature: Default value if no value exists
    :param 'Timing' defaultValueTiming: Default value if no value exists
    :param 'ContactDetail' defaultValueContactDetail: Default value if no value exists
    :param 'Contributor' defaultValueContributor: Default value if no value exists
    :param 'DataRequirement' defaultValueDataRequirement: Default value if no value exists
    :param 'Expression' defaultValueExpression: Default value if no value exists
    :param 'ParameterDefinition' defaultValueParameterDefinition: Default value if no value exists
    :param 'RelatedArtifact' defaultValueRelatedArtifact: Default value if no value exists
    :param 'TriggerDefinition' defaultValueTriggerDefinition: Default value if no value exists
    :param 'UsageContext' defaultValueUsageContext: Default value if no value exists
    :param 'Dosage' defaultValueDosage: Default value if no value exists
    :param 'Meta' defaultValueMeta: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  context: str = None,  min: int = None,  max: str = None,  type: str = None,  defaultValueBase64Binary: str = None,  defaultValueBoolean: bool = None,  defaultValueCanonical: str = None,  defaultValueCode: str = None,  defaultValueDate: str = None,  defaultValueDateTime: str = None,  defaultValueDecimal: float = None,  defaultValueId: str = None,  defaultValueInstant: str = None,  defaultValueInteger: int = None,  defaultValueMarkdown: str = None,  defaultValueOid: str = None,  defaultValuePositiveInt: int = None,  defaultValueString: str = None,  defaultValueTime: str = None,  defaultValueUnsignedInt: int = None,  defaultValueUri: str = None,  defaultValueUrl: str = None,  defaultValueUuid: str = None,  defaultValueAddress: 'Address' = None,  defaultValueAge: 'Age' = None,  defaultValueAnnotation: 'Annotation' = None,  defaultValueAttachment: 'Attachment' = None,  defaultValueCodeableConcept: 'CodeableConcept' = None,  defaultValueCoding: 'Coding' = None,  defaultValueContactPoint: 'ContactPoint' = None,  defaultValueCount: 'Count' = None,  defaultValueDistance: 'Distance' = None,  defaultValueDuration: 'Duration' = None,  defaultValueHumanName: 'HumanName' = None,  defaultValueIdentifier: 'Identifier' = None,  defaultValueMoney: 'Money' = None,  defaultValuePeriod: 'Period' = None,  defaultValueQuantity: 'Quantity' = None,  defaultValueRange: 'Range' = None,  defaultValueRatio: 'Ratio' = None,  defaultValueReference: 'Reference' = None,  defaultValueSampledData: 'SampledData' = None,  defaultValueSignature: 'Signature' = None,  defaultValueTiming: 'Timing' = None,  defaultValueContactDetail: 'ContactDetail' = None,  defaultValueContributor: 'Contributor' = None,  defaultValueDataRequirement: 'DataRequirement' = None,  defaultValueExpression: 'Expression' = None,  defaultValueParameterDefinition: 'ParameterDefinition' = None,  defaultValueRelatedArtifact: 'RelatedArtifact' = None,  defaultValueTriggerDefinition: 'TriggerDefinition' = None,  defaultValueUsageContext: 'UsageContext' = None,  defaultValueDosage: 'Dosage' = None,  defaultValueMeta: 'Meta' = None,  element: str = None,  listMode: str = None,  variable: str = None,  condition: str = None,  check: str = None,  logMessage: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.context: str = context 
        self.min: int = min 
        self.max: str = max 
        self.type: str = type 
        self.defaultValueBase64Binary: str = defaultValueBase64Binary 
        self.defaultValueBoolean: bool = defaultValueBoolean 
        self.defaultValueCanonical: str = defaultValueCanonical 
        self.defaultValueCode: str = defaultValueCode 
        self.defaultValueDate: str = defaultValueDate 
        self.defaultValueDateTime: str = defaultValueDateTime 
        self.defaultValueDecimal: float = defaultValueDecimal 
        self.defaultValueId: str = defaultValueId 
        self.defaultValueInstant: str = defaultValueInstant 
        self.defaultValueInteger: int = defaultValueInteger 
        self.defaultValueMarkdown: str = defaultValueMarkdown 
        self.defaultValueOid: str = defaultValueOid 
        self.defaultValuePositiveInt: int = defaultValuePositiveInt 
        self.defaultValueString: str = defaultValueString 
        self.defaultValueTime: str = defaultValueTime 
        self.defaultValueUnsignedInt: int = defaultValueUnsignedInt 
        self.defaultValueUri: str = defaultValueUri 
        self.defaultValueUrl: str = defaultValueUrl 
        self.defaultValueUuid: str = defaultValueUuid 
        self.defaultValueAddress: 'Address' = defaultValueAddress 
        self.defaultValueAge: 'Age' = defaultValueAge 
        self.defaultValueAnnotation: 'Annotation' = defaultValueAnnotation 
        self.defaultValueAttachment: 'Attachment' = defaultValueAttachment 
        self.defaultValueCodeableConcept: 'CodeableConcept' = defaultValueCodeableConcept 
        self.defaultValueCoding: 'Coding' = defaultValueCoding 
        self.defaultValueContactPoint: 'ContactPoint' = defaultValueContactPoint 
        self.defaultValueCount: 'Count' = defaultValueCount 
        self.defaultValueDistance: 'Distance' = defaultValueDistance 
        self.defaultValueDuration: 'Duration' = defaultValueDuration 
        self.defaultValueHumanName: 'HumanName' = defaultValueHumanName 
        self.defaultValueIdentifier: 'Identifier' = defaultValueIdentifier 
        self.defaultValueMoney: 'Money' = defaultValueMoney 
        self.defaultValuePeriod: 'Period' = defaultValuePeriod 
        self.defaultValueQuantity: 'Quantity' = defaultValueQuantity 
        self.defaultValueRange: 'Range' = defaultValueRange 
        self.defaultValueRatio: 'Ratio' = defaultValueRatio 
        self.defaultValueReference: 'Reference' = defaultValueReference 
        self.defaultValueSampledData: 'SampledData' = defaultValueSampledData 
        self.defaultValueSignature: 'Signature' = defaultValueSignature 
        self.defaultValueTiming: 'Timing' = defaultValueTiming 
        self.defaultValueContactDetail: 'ContactDetail' = defaultValueContactDetail 
        self.defaultValueContributor: 'Contributor' = defaultValueContributor 
        self.defaultValueDataRequirement: 'DataRequirement' = defaultValueDataRequirement 
        self.defaultValueExpression: 'Expression' = defaultValueExpression 
        self.defaultValueParameterDefinition: 'ParameterDefinition' = defaultValueParameterDefinition 
        self.defaultValueRelatedArtifact: 'RelatedArtifact' = defaultValueRelatedArtifact 
        self.defaultValueTriggerDefinition: 'TriggerDefinition' = defaultValueTriggerDefinition 
        self.defaultValueUsageContext: 'UsageContext' = defaultValueUsageContext 
        self.defaultValueDosage: 'Dosage' = defaultValueDosage 
        self.defaultValueMeta: 'Meta' = defaultValueMeta 
        self.element: str = element 
        self.listMode: str = listMode 
        self.variable: str = variable 
        self.condition: str = condition 
        self.check: str = check 
        self.logMessage: str = logMessage 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Source":
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


    
        
    
    

class Parameter(ModelBase):
    """ Parameters to the transform.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueId: Parameter value - variable or literal
    :param str valueString: Parameter value - variable or literal
    :param bool valueBoolean: Parameter value - variable or literal
    :param int valueInteger: Parameter value - variable or literal
    :param float valueDecimal: Parameter value - variable or literal
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  valueId: str = None,  valueString: str = None,  valueBoolean: bool = None,  valueInteger: int = None,  valueDecimal: float = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.valueId: str = valueId 
        self.valueString: str = valueString 
        self.valueBoolean: bool = valueBoolean 
        self.valueInteger: int = valueInteger 
        self.valueDecimal: float = valueDecimal 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Parameter":
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


  
    
    

class Target(ModelBase):
    """ Content to create because of this mapping rule.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param str contextType: type | variable
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | collate
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param list['Parameter'] parameter: Parameters to the transform
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  context: str = None,  contextType: str = None,  element: str = None,  variable: str = None,  listMode: str = None,  listRuleId: str = None,  transform: str = None,  parameter: list['Parameter'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.context: str = context 
        self.contextType: str = contextType 
        self.element: str = element 
        self.variable: str = variable 
        self.listMode: str = listMode or []
        self.listRuleId: str = listRuleId 
        self.transform: str = transform 
        self.parameter: list['Parameter'] = parameter or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Target":
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


    
    

class Dependent(ModelBase):
    """ Which other rules to apply in the context of this rule.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param str variable: Variable to pass to the rule or group
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  variable: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.variable: str = variable or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Dependent":
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


  
    
    

class Rule(ModelBase):
    """ Transform Rule from source to target.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of the rule for internal references
    :param list['Source'] source: Source inputs to the mapping
    :param list['Target'] target: Content to create because of this mapping rule
    :param list['Dependent'] dependent: Which other rules to apply in the context of this rule
    :param str documentation: Documentation for this instance of data
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  source: list['Source'] = None,  target: list['Target'] = None,  dependent: list['Dependent'] = None,  documentation: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.source: list['Source'] = source or []
        self.target: list['Target'] = target or []
        self.dependent: list['Dependent'] = dependent or []
        self.documentation: str = documentation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Rule":
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


  
    
    

class Group(ModelBase):
    """ Organizes the mapping into manageable chunks for human review/ease of maintenance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Human-readable label
    :param str extends: Another group that this group adds rules to
    :param str typeMode: none | types | type-and-types
    :param str documentation: Additional description/explanation for group
    :param list['Input'] input: Named instance provided when invoking the map
    :param list['Rule'] rule: Transform Rule from source to target
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  extends: str = None,  typeMode: str = None,  documentation: str = None,  input: list['Input'] = None,  rule: list['Rule'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.extends: str = extends 
        self.typeMode: str = typeMode 
        self.documentation: str = documentation 
        self.input: list['Input'] = input or []
        self.rule: list['Rule'] = rule or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Group":
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


class StructureMap(DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform data.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this structure map, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the structure map
    :param str version: Business version of the structure map
    :param str name: Name for this structure map (computer friendly)
    :param str title: Name for this structure map (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the structure map
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for structure map (if applicable)
    :param str purpose: Why this structure map is defined
    :param str copyright: Use and/or publishing restrictions
    :param list['Structure'] structure: Structure Definition used by this map
    :param str _import: Other maps used by this map (canonical URLs)
    :param list['Group'] group: Named sections for reader convenience
    """
    def __init__(self, resourceType: str = "StructureMap",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  title: str = None,  status: str = None,  experimental: bool = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  copyright: str = None,  structure: list['Structure'] = None,  _import: str = None,  group: list['Group'] = None, ):
        self.resourceType: str = resourceType or "StructureMap"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.name: str = name 
        self.title: str = title 
        self.status: str = status 
        self.experimental: bool = experimental 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.purpose: str = purpose 
        self.copyright: str = copyright 
        self.structure: list['Structure'] = structure or []
        self._import: str = _import or []
        self.group: list['Group'] = group or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
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