"""
Generated class for ElementDefinition. 
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
from fhan.models.R4.Element import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Age import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Money import *
from fhan.models.R4.Dosage import *
from fhan.models.generator_models import ModelBase

    
        
    
    

class Discriminator(ModelBase):
    """ Designates which child elements are used to discriminate between the slices when processing an instance. If one or more discriminators are provided, the value of the child elements in the instance data SHALL completely distinguish which slice the element in the resource matches based on the allowed values for those elements in each of the slices.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str type: value | exists | pattern | type | profile
    :param str path: Path to element value
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  type: str = None,  path: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.path: str = path 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Discriminator":
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


  
    
    

class Slicing(ModelBase):
    """ Indicates that the element is sliced into a set of alternative definitions (i.e. in a structure definition, there are multiple different constraints on a single element in the base resource). Slicing can be used in any resource that has cardinality ..* on the base resource, or any resource with a choice of types. The set of slices is any elements that come after this in the element sequence that have the same path, until a shorter path occurs (the shorter path terminates the set).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Discriminator'] discriminator: Element values that are used to distinguish the slices
    :param str description: Text description of how slicing works (or not)
    :param bool ordered: If elements must be in same order as slices
    :param str rules: closed | open | openAtEnd
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  discriminator: list['Discriminator'] = None,  description: str = None,  ordered: bool = None,  rules: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.discriminator: list['Discriminator'] = discriminator or []
        self.description: str = description 
        self.ordered: bool = ordered 
        self.rules: str = rules 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Slicing":
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


    
    

class Base(ModelBase):
    """ Information about the base definition of the element, provided to make it unnecessary for tools to trace the deviation of the element through the derived and related profiles. When the element definition is not the original definition of an element - i.g. either in a constraint on another type, or for elements from a super type in a snap shot - then the information in provided in the element definition may be different to the base definition. On the original definition of the element, it will be same.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: Path that identifies the base element
    :param int min: Min cardinality of the base element
    :param str max: Max cardinality of the base element
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  min: int = None,  max: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.min: int = min 
        self.max: str = max 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Base":
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


    
    

class Type(ModelBase):
    """ The data type or resource that the value of this element is permitted to be.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str code: Data type or Resource (reference to definition)
    :param str profile: Profiles (StructureDefinition or IG) - one must apply
    :param str targetProfile: Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    :param str aggregation: contained | referenced | bundled - how aggregated
    :param str versioning: either | independent | specific
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  code: str = None,  profile: str = None,  targetProfile: str = None,  aggregation: str = None,  versioning: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.code: str = code 
        self.profile: str = profile or []
        self.targetProfile: str = targetProfile or []
        self.aggregation: str = aggregation or []
        self.versioning: str = versioning 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Type":
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


    
    

class Example(ModelBase):
    """ A sample value for this element demonstrating the type of information that would typically be found in the element.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str label: Describes the purpose of this example
    :param str valueBase64Binary: Value of Example (one of allowed types)
    :param bool valueBoolean: Value of Example (one of allowed types)
    :param str valueCanonical: Value of Example (one of allowed types)
    :param str valueCode: Value of Example (one of allowed types)
    :param str valueDate: Value of Example (one of allowed types)
    :param str valueDateTime: Value of Example (one of allowed types)
    :param float valueDecimal: Value of Example (one of allowed types)
    :param str valueId: Value of Example (one of allowed types)
    :param str valueInstant: Value of Example (one of allowed types)
    :param int valueInteger: Value of Example (one of allowed types)
    :param str valueMarkdown: Value of Example (one of allowed types)
    :param str valueOid: Value of Example (one of allowed types)
    :param int valuePositiveInt: Value of Example (one of allowed types)
    :param str valueString: Value of Example (one of allowed types)
    :param str valueTime: Value of Example (one of allowed types)
    :param int valueUnsignedInt: Value of Example (one of allowed types)
    :param str valueUri: Value of Example (one of allowed types)
    :param str valueUrl: Value of Example (one of allowed types)
    :param str valueUuid: Value of Example (one of allowed types)
    :param 'Address' valueAddress: Value of Example (one of allowed types)
    :param 'Age' valueAge: Value of Example (one of allowed types)
    :param 'Annotation' valueAnnotation: Value of Example (one of allowed types)
    :param 'Attachment' valueAttachment: Value of Example (one of allowed types)
    :param 'CodeableConcept' valueCodeableConcept: Value of Example (one of allowed types)
    :param 'Coding' valueCoding: Value of Example (one of allowed types)
    :param 'ContactPoint' valueContactPoint: Value of Example (one of allowed types)
    :param 'Count' valueCount: Value of Example (one of allowed types)
    :param 'Distance' valueDistance: Value of Example (one of allowed types)
    :param 'Duration' valueDuration: Value of Example (one of allowed types)
    :param 'HumanName' valueHumanName: Value of Example (one of allowed types)
    :param 'Identifier' valueIdentifier: Value of Example (one of allowed types)
    :param 'Money' valueMoney: Value of Example (one of allowed types)
    :param 'Period' valuePeriod: Value of Example (one of allowed types)
    :param 'Quantity' valueQuantity: Value of Example (one of allowed types)
    :param 'Range' valueRange: Value of Example (one of allowed types)
    :param 'Ratio' valueRatio: Value of Example (one of allowed types)
    :param 'Reference' valueReference: Value of Example (one of allowed types)
    :param 'SampledData' valueSampledData: Value of Example (one of allowed types)
    :param 'Signature' valueSignature: Value of Example (one of allowed types)
    :param 'Timing' valueTiming: Value of Example (one of allowed types)
    :param 'ContactDetail' valueContactDetail: Value of Example (one of allowed types)
    :param 'Contributor' valueContributor: Value of Example (one of allowed types)
    :param 'DataRequirement' valueDataRequirement: Value of Example (one of allowed types)
    :param 'Expression' valueExpression: Value of Example (one of allowed types)
    :param 'ParameterDefinition' valueParameterDefinition: Value of Example (one of allowed types)
    :param 'RelatedArtifact' valueRelatedArtifact: Value of Example (one of allowed types)
    :param 'TriggerDefinition' valueTriggerDefinition: Value of Example (one of allowed types)
    :param 'UsageContext' valueUsageContext: Value of Example (one of allowed types)
    :param 'Dosage' valueDosage: Value of Example (one of allowed types)
    :param 'Meta' valueMeta: Value of Example (one of allowed types)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  label: str = None,  valueBase64Binary: str = None,  valueBoolean: bool = None,  valueCanonical: str = None,  valueCode: str = None,  valueDate: str = None,  valueDateTime: str = None,  valueDecimal: float = None,  valueId: str = None,  valueInstant: str = None,  valueInteger: int = None,  valueMarkdown: str = None,  valueOid: str = None,  valuePositiveInt: int = None,  valueString: str = None,  valueTime: str = None,  valueUnsignedInt: int = None,  valueUri: str = None,  valueUrl: str = None,  valueUuid: str = None,  valueAddress: 'Address' = None,  valueAge: 'Age' = None,  valueAnnotation: 'Annotation' = None,  valueAttachment: 'Attachment' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueCoding: 'Coding' = None,  valueContactPoint: 'ContactPoint' = None,  valueCount: 'Count' = None,  valueDistance: 'Distance' = None,  valueDuration: 'Duration' = None,  valueHumanName: 'HumanName' = None,  valueIdentifier: 'Identifier' = None,  valueMoney: 'Money' = None,  valuePeriod: 'Period' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueRatio: 'Ratio' = None,  valueReference: 'Reference' = None,  valueSampledData: 'SampledData' = None,  valueSignature: 'Signature' = None,  valueTiming: 'Timing' = None,  valueContactDetail: 'ContactDetail' = None,  valueContributor: 'Contributor' = None,  valueDataRequirement: 'DataRequirement' = None,  valueExpression: 'Expression' = None,  valueParameterDefinition: 'ParameterDefinition' = None,  valueRelatedArtifact: 'RelatedArtifact' = None,  valueTriggerDefinition: 'TriggerDefinition' = None,  valueUsageContext: 'UsageContext' = None,  valueDosage: 'Dosage' = None,  valueMeta: 'Meta' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.label: str = label 
        self.valueBase64Binary: str = valueBase64Binary 
        self.valueBoolean: bool = valueBoolean 
        self.valueCanonical: str = valueCanonical 
        self.valueCode: str = valueCode 
        self.valueDate: str = valueDate 
        self.valueDateTime: str = valueDateTime 
        self.valueDecimal: float = valueDecimal 
        self.valueId: str = valueId 
        self.valueInstant: str = valueInstant 
        self.valueInteger: int = valueInteger 
        self.valueMarkdown: str = valueMarkdown 
        self.valueOid: str = valueOid 
        self.valuePositiveInt: int = valuePositiveInt 
        self.valueString: str = valueString 
        self.valueTime: str = valueTime 
        self.valueUnsignedInt: int = valueUnsignedInt 
        self.valueUri: str = valueUri 
        self.valueUrl: str = valueUrl 
        self.valueUuid: str = valueUuid 
        self.valueAddress: 'Address' = valueAddress 
        self.valueAge: 'Age' = valueAge 
        self.valueAnnotation: 'Annotation' = valueAnnotation 
        self.valueAttachment: 'Attachment' = valueAttachment 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueCoding: 'Coding' = valueCoding 
        self.valueContactPoint: 'ContactPoint' = valueContactPoint 
        self.valueCount: 'Count' = valueCount 
        self.valueDistance: 'Distance' = valueDistance 
        self.valueDuration: 'Duration' = valueDuration 
        self.valueHumanName: 'HumanName' = valueHumanName 
        self.valueIdentifier: 'Identifier' = valueIdentifier 
        self.valueMoney: 'Money' = valueMoney 
        self.valuePeriod: 'Period' = valuePeriod 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueRange: 'Range' = valueRange 
        self.valueRatio: 'Ratio' = valueRatio 
        self.valueReference: 'Reference' = valueReference 
        self.valueSampledData: 'SampledData' = valueSampledData 
        self.valueSignature: 'Signature' = valueSignature 
        self.valueTiming: 'Timing' = valueTiming 
        self.valueContactDetail: 'ContactDetail' = valueContactDetail 
        self.valueContributor: 'Contributor' = valueContributor 
        self.valueDataRequirement: 'DataRequirement' = valueDataRequirement 
        self.valueExpression: 'Expression' = valueExpression 
        self.valueParameterDefinition: 'ParameterDefinition' = valueParameterDefinition 
        self.valueRelatedArtifact: 'RelatedArtifact' = valueRelatedArtifact 
        self.valueTriggerDefinition: 'TriggerDefinition' = valueTriggerDefinition 
        self.valueUsageContext: 'UsageContext' = valueUsageContext 
        self.valueDosage: 'Dosage' = valueDosage 
        self.valueMeta: 'Meta' = valueMeta 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Example":
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


    
    

class Constraint(ModelBase):
    """ Formal constraints such as co-occurrence and other constraints that can be computationally evaluated within the context of the instance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str key: Target of 'condition' reference above
    :param str requirements: Why this constraint is necessary or appropriate
    :param str severity: error | warning
    :param str human: Human description of constraint
    :param str expression: FHIRPath expression of constraint
    :param str xpath: XPath expression of constraint
    :param str source: Reference to original source of constraint
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  key: str = None,  requirements: str = None,  severity: str = None,  human: str = None,  expression: str = None,  xpath: str = None,  source: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.key: str = key 
        self.requirements: str = requirements 
        self.severity: str = severity 
        self.human: str = human 
        self.expression: str = expression 
        self.xpath: str = xpath 
        self.source: str = source 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Constraint":
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


    
    

class Binding(ModelBase):
    """ Binds to a value set if this element is coded (code, Coding, CodeableConcept, Quantity), or the data types (string, uri).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str strength: required | extensible | preferred | example
    :param str description: Human explanation of the value set
    :param str valueSet: Source of value set
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  strength: str = None,  description: str = None,  valueSet: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.strength: str = strength 
        self.description: str = description 
        self.valueSet: str = valueSet 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Binding":
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


    
    

class Mapping(ModelBase):
    """ Identifies a concept from an external specification that roughly corresponds to this element.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str identity: Reference to mapping declaration
    :param str language: Computable language of mapping
    :param str map: Details of the mapping
    :param str comment: Comments about the mapping or its use
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  identity: str = None,  language: str = None,  map: str = None,  comment: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.identity: str = identity 
        self.language: str = language 
        self.map: str = map 
        self.comment: str = comment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Mapping":
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


class ElementDefinition(ModelBase):
    """ Base StructureDefinition for ElementDefinition Type: Captures constraints on each element within the resource, profile, or extension.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: Path of the element in the hierarchy of elements
    :param str representation: xmlAttr | xmlText | typeAttr | cdaText | xhtml
    :param str sliceName: Name for this particular element (in a set of slices)
    :param bool sliceIsConstraining: If this slice definition constrains an inherited slice definition (or not)
    :param str label: Name for element to display with or prompt for element
    :param list['Coding'] code: Corresponding codes in terminologies
    :param 'Slicing' slicing: This element is sliced - slices follow
    :param str short: Concise definition for space-constrained presentation
    :param str definition: Full formal definition as narrative text
    :param str comment: Comments about the use of this element
    :param str requirements: Why this resource has been created
    :param str alias: Other names
    :param int min: Minimum Cardinality
    :param str max: Maximum Cardinality (a number or *)
    :param 'Base' base: Base definition information for tools
    :param str contentReference: Reference to definition of content for the element
    :param list['Type'] type: Data type and Profile for this element
    :param str defaultValueBase64Binary: Specified value if missing from instance
    :param bool defaultValueBoolean: Specified value if missing from instance
    :param str defaultValueCanonical: Specified value if missing from instance
    :param str defaultValueCode: Specified value if missing from instance
    :param str defaultValueDate: Specified value if missing from instance
    :param str defaultValueDateTime: Specified value if missing from instance
    :param float defaultValueDecimal: Specified value if missing from instance
    :param str defaultValueId: Specified value if missing from instance
    :param str defaultValueInstant: Specified value if missing from instance
    :param int defaultValueInteger: Specified value if missing from instance
    :param str defaultValueMarkdown: Specified value if missing from instance
    :param str defaultValueOid: Specified value if missing from instance
    :param int defaultValuePositiveInt: Specified value if missing from instance
    :param str defaultValueString: Specified value if missing from instance
    :param str defaultValueTime: Specified value if missing from instance
    :param int defaultValueUnsignedInt: Specified value if missing from instance
    :param str defaultValueUri: Specified value if missing from instance
    :param str defaultValueUrl: Specified value if missing from instance
    :param str defaultValueUuid: Specified value if missing from instance
    :param 'Address' defaultValueAddress: Specified value if missing from instance
    :param 'Age' defaultValueAge: Specified value if missing from instance
    :param 'Annotation' defaultValueAnnotation: Specified value if missing from instance
    :param 'Attachment' defaultValueAttachment: Specified value if missing from instance
    :param 'CodeableConcept' defaultValueCodeableConcept: Specified value if missing from instance
    :param 'Coding' defaultValueCoding: Specified value if missing from instance
    :param 'ContactPoint' defaultValueContactPoint: Specified value if missing from instance
    :param 'Count' defaultValueCount: Specified value if missing from instance
    :param 'Distance' defaultValueDistance: Specified value if missing from instance
    :param 'Duration' defaultValueDuration: Specified value if missing from instance
    :param 'HumanName' defaultValueHumanName: Specified value if missing from instance
    :param 'Identifier' defaultValueIdentifier: Specified value if missing from instance
    :param 'Money' defaultValueMoney: Specified value if missing from instance
    :param 'Period' defaultValuePeriod: Specified value if missing from instance
    :param 'Quantity' defaultValueQuantity: Specified value if missing from instance
    :param 'Range' defaultValueRange: Specified value if missing from instance
    :param 'Ratio' defaultValueRatio: Specified value if missing from instance
    :param 'Reference' defaultValueReference: Specified value if missing from instance
    :param 'SampledData' defaultValueSampledData: Specified value if missing from instance
    :param 'Signature' defaultValueSignature: Specified value if missing from instance
    :param 'Timing' defaultValueTiming: Specified value if missing from instance
    :param 'ContactDetail' defaultValueContactDetail: Specified value if missing from instance
    :param 'Contributor' defaultValueContributor: Specified value if missing from instance
    :param 'DataRequirement' defaultValueDataRequirement: Specified value if missing from instance
    :param 'Expression' defaultValueExpression: Specified value if missing from instance
    :param 'ParameterDefinition' defaultValueParameterDefinition: Specified value if missing from instance
    :param 'RelatedArtifact' defaultValueRelatedArtifact: Specified value if missing from instance
    :param 'TriggerDefinition' defaultValueTriggerDefinition: Specified value if missing from instance
    :param 'UsageContext' defaultValueUsageContext: Specified value if missing from instance
    :param 'Dosage' defaultValueDosage: Specified value if missing from instance
    :param 'Meta' defaultValueMeta: Specified value if missing from instance
    :param str meaningWhenMissing: Implicit meaning when this element is missing
    :param str orderMeaning: What the order of the elements means
    :param str fixedBase64Binary: Value must be exactly this
    :param bool fixedBoolean: Value must be exactly this
    :param str fixedCanonical: Value must be exactly this
    :param str fixedCode: Value must be exactly this
    :param str fixedDate: Value must be exactly this
    :param str fixedDateTime: Value must be exactly this
    :param float fixedDecimal: Value must be exactly this
    :param str fixedId: Value must be exactly this
    :param str fixedInstant: Value must be exactly this
    :param int fixedInteger: Value must be exactly this
    :param str fixedMarkdown: Value must be exactly this
    :param str fixedOid: Value must be exactly this
    :param int fixedPositiveInt: Value must be exactly this
    :param str fixedString: Value must be exactly this
    :param str fixedTime: Value must be exactly this
    :param int fixedUnsignedInt: Value must be exactly this
    :param str fixedUri: Value must be exactly this
    :param str fixedUrl: Value must be exactly this
    :param str fixedUuid: Value must be exactly this
    :param 'Address' fixedAddress: Value must be exactly this
    :param 'Age' fixedAge: Value must be exactly this
    :param 'Annotation' fixedAnnotation: Value must be exactly this
    :param 'Attachment' fixedAttachment: Value must be exactly this
    :param 'CodeableConcept' fixedCodeableConcept: Value must be exactly this
    :param 'Coding' fixedCoding: Value must be exactly this
    :param 'ContactPoint' fixedContactPoint: Value must be exactly this
    :param 'Count' fixedCount: Value must be exactly this
    :param 'Distance' fixedDistance: Value must be exactly this
    :param 'Duration' fixedDuration: Value must be exactly this
    :param 'HumanName' fixedHumanName: Value must be exactly this
    :param 'Identifier' fixedIdentifier: Value must be exactly this
    :param 'Money' fixedMoney: Value must be exactly this
    :param 'Period' fixedPeriod: Value must be exactly this
    :param 'Quantity' fixedQuantity: Value must be exactly this
    :param 'Range' fixedRange: Value must be exactly this
    :param 'Ratio' fixedRatio: Value must be exactly this
    :param 'Reference' fixedReference: Value must be exactly this
    :param 'SampledData' fixedSampledData: Value must be exactly this
    :param 'Signature' fixedSignature: Value must be exactly this
    :param 'Timing' fixedTiming: Value must be exactly this
    :param 'ContactDetail' fixedContactDetail: Value must be exactly this
    :param 'Contributor' fixedContributor: Value must be exactly this
    :param 'DataRequirement' fixedDataRequirement: Value must be exactly this
    :param 'Expression' fixedExpression: Value must be exactly this
    :param 'ParameterDefinition' fixedParameterDefinition: Value must be exactly this
    :param 'RelatedArtifact' fixedRelatedArtifact: Value must be exactly this
    :param 'TriggerDefinition' fixedTriggerDefinition: Value must be exactly this
    :param 'UsageContext' fixedUsageContext: Value must be exactly this
    :param 'Dosage' fixedDosage: Value must be exactly this
    :param 'Meta' fixedMeta: Value must be exactly this
    :param str patternBase64Binary: Value must have at least these property values
    :param bool patternBoolean: Value must have at least these property values
    :param str patternCanonical: Value must have at least these property values
    :param str patternCode: Value must have at least these property values
    :param str patternDate: Value must have at least these property values
    :param str patternDateTime: Value must have at least these property values
    :param float patternDecimal: Value must have at least these property values
    :param str patternId: Value must have at least these property values
    :param str patternInstant: Value must have at least these property values
    :param int patternInteger: Value must have at least these property values
    :param str patternMarkdown: Value must have at least these property values
    :param str patternOid: Value must have at least these property values
    :param int patternPositiveInt: Value must have at least these property values
    :param str patternString: Value must have at least these property values
    :param str patternTime: Value must have at least these property values
    :param int patternUnsignedInt: Value must have at least these property values
    :param str patternUri: Value must have at least these property values
    :param str patternUrl: Value must have at least these property values
    :param str patternUuid: Value must have at least these property values
    :param 'Address' patternAddress: Value must have at least these property values
    :param 'Age' patternAge: Value must have at least these property values
    :param 'Annotation' patternAnnotation: Value must have at least these property values
    :param 'Attachment' patternAttachment: Value must have at least these property values
    :param 'CodeableConcept' patternCodeableConcept: Value must have at least these property values
    :param 'Coding' patternCoding: Value must have at least these property values
    :param 'ContactPoint' patternContactPoint: Value must have at least these property values
    :param 'Count' patternCount: Value must have at least these property values
    :param 'Distance' patternDistance: Value must have at least these property values
    :param 'Duration' patternDuration: Value must have at least these property values
    :param 'HumanName' patternHumanName: Value must have at least these property values
    :param 'Identifier' patternIdentifier: Value must have at least these property values
    :param 'Money' patternMoney: Value must have at least these property values
    :param 'Period' patternPeriod: Value must have at least these property values
    :param 'Quantity' patternQuantity: Value must have at least these property values
    :param 'Range' patternRange: Value must have at least these property values
    :param 'Ratio' patternRatio: Value must have at least these property values
    :param 'Reference' patternReference: Value must have at least these property values
    :param 'SampledData' patternSampledData: Value must have at least these property values
    :param 'Signature' patternSignature: Value must have at least these property values
    :param 'Timing' patternTiming: Value must have at least these property values
    :param 'ContactDetail' patternContactDetail: Value must have at least these property values
    :param 'Contributor' patternContributor: Value must have at least these property values
    :param 'DataRequirement' patternDataRequirement: Value must have at least these property values
    :param 'Expression' patternExpression: Value must have at least these property values
    :param 'ParameterDefinition' patternParameterDefinition: Value must have at least these property values
    :param 'RelatedArtifact' patternRelatedArtifact: Value must have at least these property values
    :param 'TriggerDefinition' patternTriggerDefinition: Value must have at least these property values
    :param 'UsageContext' patternUsageContext: Value must have at least these property values
    :param 'Dosage' patternDosage: Value must have at least these property values
    :param 'Meta' patternMeta: Value must have at least these property values
    :param list['Example'] example: Example value (as defined for type)
    :param str minValueDate: Minimum Allowed Value (for some types)
    :param str minValueDateTime: Minimum Allowed Value (for some types)
    :param str minValueInstant: Minimum Allowed Value (for some types)
    :param str minValueTime: Minimum Allowed Value (for some types)
    :param float minValueDecimal: Minimum Allowed Value (for some types)
    :param int minValueInteger: Minimum Allowed Value (for some types)
    :param int minValuePositiveInt: Minimum Allowed Value (for some types)
    :param int minValueUnsignedInt: Minimum Allowed Value (for some types)
    :param 'Quantity' minValueQuantity: Minimum Allowed Value (for some types)
    :param str maxValueDate: Maximum Allowed Value (for some types)
    :param str maxValueDateTime: Maximum Allowed Value (for some types)
    :param str maxValueInstant: Maximum Allowed Value (for some types)
    :param str maxValueTime: Maximum Allowed Value (for some types)
    :param float maxValueDecimal: Maximum Allowed Value (for some types)
    :param int maxValueInteger: Maximum Allowed Value (for some types)
    :param int maxValuePositiveInt: Maximum Allowed Value (for some types)
    :param int maxValueUnsignedInt: Maximum Allowed Value (for some types)
    :param 'Quantity' maxValueQuantity: Maximum Allowed Value (for some types)
    :param int maxLength: Max length for strings
    :param str condition: Reference to invariant about presence
    :param list['Constraint'] constraint: Condition that must evaluate to true
    :param bool mustSupport: If the element must be supported
    :param bool isModifier: If this modifies the meaning of other elements
    :param str isModifierReason: Reason that this element is marked as a modifier
    :param bool isSummary: Include when _summary = true?
    :param 'Binding' binding: ValueSet details if this is coded
    :param list['Mapping'] mapping: Map element to another set of definitions
    """
    def __init__(self, resourceType: str = "ElementDefinition",  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  path: str = None,  representation: str = None,  sliceName: str = None,  sliceIsConstraining: bool = None,  label: str = None,  code: list['Coding'] = None,  slicing: 'Slicing' = None,  short: str = None,  definition: str = None,  comment: str = None,  requirements: str = None,  alias: str = None,  min: int = None,  max: str = None,  base: 'Base' = None,  contentReference: str = None,  type: list['Type'] = None,  defaultValueBase64Binary: str = None,  defaultValueBoolean: bool = None,  defaultValueCanonical: str = None,  defaultValueCode: str = None,  defaultValueDate: str = None,  defaultValueDateTime: str = None,  defaultValueDecimal: float = None,  defaultValueId: str = None,  defaultValueInstant: str = None,  defaultValueInteger: int = None,  defaultValueMarkdown: str = None,  defaultValueOid: str = None,  defaultValuePositiveInt: int = None,  defaultValueString: str = None,  defaultValueTime: str = None,  defaultValueUnsignedInt: int = None,  defaultValueUri: str = None,  defaultValueUrl: str = None,  defaultValueUuid: str = None,  defaultValueAddress: 'Address' = None,  defaultValueAge: 'Age' = None,  defaultValueAnnotation: 'Annotation' = None,  defaultValueAttachment: 'Attachment' = None,  defaultValueCodeableConcept: 'CodeableConcept' = None,  defaultValueCoding: 'Coding' = None,  defaultValueContactPoint: 'ContactPoint' = None,  defaultValueCount: 'Count' = None,  defaultValueDistance: 'Distance' = None,  defaultValueDuration: 'Duration' = None,  defaultValueHumanName: 'HumanName' = None,  defaultValueIdentifier: 'Identifier' = None,  defaultValueMoney: 'Money' = None,  defaultValuePeriod: 'Period' = None,  defaultValueQuantity: 'Quantity' = None,  defaultValueRange: 'Range' = None,  defaultValueRatio: 'Ratio' = None,  defaultValueReference: 'Reference' = None,  defaultValueSampledData: 'SampledData' = None,  defaultValueSignature: 'Signature' = None,  defaultValueTiming: 'Timing' = None,  defaultValueContactDetail: 'ContactDetail' = None,  defaultValueContributor: 'Contributor' = None,  defaultValueDataRequirement: 'DataRequirement' = None,  defaultValueExpression: 'Expression' = None,  defaultValueParameterDefinition: 'ParameterDefinition' = None,  defaultValueRelatedArtifact: 'RelatedArtifact' = None,  defaultValueTriggerDefinition: 'TriggerDefinition' = None,  defaultValueUsageContext: 'UsageContext' = None,  defaultValueDosage: 'Dosage' = None,  defaultValueMeta: 'Meta' = None,  meaningWhenMissing: str = None,  orderMeaning: str = None,  fixedBase64Binary: str = None,  fixedBoolean: bool = None,  fixedCanonical: str = None,  fixedCode: str = None,  fixedDate: str = None,  fixedDateTime: str = None,  fixedDecimal: float = None,  fixedId: str = None,  fixedInstant: str = None,  fixedInteger: int = None,  fixedMarkdown: str = None,  fixedOid: str = None,  fixedPositiveInt: int = None,  fixedString: str = None,  fixedTime: str = None,  fixedUnsignedInt: int = None,  fixedUri: str = None,  fixedUrl: str = None,  fixedUuid: str = None,  fixedAddress: 'Address' = None,  fixedAge: 'Age' = None,  fixedAnnotation: 'Annotation' = None,  fixedAttachment: 'Attachment' = None,  fixedCodeableConcept: 'CodeableConcept' = None,  fixedCoding: 'Coding' = None,  fixedContactPoint: 'ContactPoint' = None,  fixedCount: 'Count' = None,  fixedDistance: 'Distance' = None,  fixedDuration: 'Duration' = None,  fixedHumanName: 'HumanName' = None,  fixedIdentifier: 'Identifier' = None,  fixedMoney: 'Money' = None,  fixedPeriod: 'Period' = None,  fixedQuantity: 'Quantity' = None,  fixedRange: 'Range' = None,  fixedRatio: 'Ratio' = None,  fixedReference: 'Reference' = None,  fixedSampledData: 'SampledData' = None,  fixedSignature: 'Signature' = None,  fixedTiming: 'Timing' = None,  fixedContactDetail: 'ContactDetail' = None,  fixedContributor: 'Contributor' = None,  fixedDataRequirement: 'DataRequirement' = None,  fixedExpression: 'Expression' = None,  fixedParameterDefinition: 'ParameterDefinition' = None,  fixedRelatedArtifact: 'RelatedArtifact' = None,  fixedTriggerDefinition: 'TriggerDefinition' = None,  fixedUsageContext: 'UsageContext' = None,  fixedDosage: 'Dosage' = None,  fixedMeta: 'Meta' = None,  patternBase64Binary: str = None,  patternBoolean: bool = None,  patternCanonical: str = None,  patternCode: str = None,  patternDate: str = None,  patternDateTime: str = None,  patternDecimal: float = None,  patternId: str = None,  patternInstant: str = None,  patternInteger: int = None,  patternMarkdown: str = None,  patternOid: str = None,  patternPositiveInt: int = None,  patternString: str = None,  patternTime: str = None,  patternUnsignedInt: int = None,  patternUri: str = None,  patternUrl: str = None,  patternUuid: str = None,  patternAddress: 'Address' = None,  patternAge: 'Age' = None,  patternAnnotation: 'Annotation' = None,  patternAttachment: 'Attachment' = None,  patternCodeableConcept: 'CodeableConcept' = None,  patternCoding: 'Coding' = None,  patternContactPoint: 'ContactPoint' = None,  patternCount: 'Count' = None,  patternDistance: 'Distance' = None,  patternDuration: 'Duration' = None,  patternHumanName: 'HumanName' = None,  patternIdentifier: 'Identifier' = None,  patternMoney: 'Money' = None,  patternPeriod: 'Period' = None,  patternQuantity: 'Quantity' = None,  patternRange: 'Range' = None,  patternRatio: 'Ratio' = None,  patternReference: 'Reference' = None,  patternSampledData: 'SampledData' = None,  patternSignature: 'Signature' = None,  patternTiming: 'Timing' = None,  patternContactDetail: 'ContactDetail' = None,  patternContributor: 'Contributor' = None,  patternDataRequirement: 'DataRequirement' = None,  patternExpression: 'Expression' = None,  patternParameterDefinition: 'ParameterDefinition' = None,  patternRelatedArtifact: 'RelatedArtifact' = None,  patternTriggerDefinition: 'TriggerDefinition' = None,  patternUsageContext: 'UsageContext' = None,  patternDosage: 'Dosage' = None,  patternMeta: 'Meta' = None,  example: list['Example'] = None,  minValueDate: str = None,  minValueDateTime: str = None,  minValueInstant: str = None,  minValueTime: str = None,  minValueDecimal: float = None,  minValueInteger: int = None,  minValuePositiveInt: int = None,  minValueUnsignedInt: int = None,  minValueQuantity: 'Quantity' = None,  maxValueDate: str = None,  maxValueDateTime: str = None,  maxValueInstant: str = None,  maxValueTime: str = None,  maxValueDecimal: float = None,  maxValueInteger: int = None,  maxValuePositiveInt: int = None,  maxValueUnsignedInt: int = None,  maxValueQuantity: 'Quantity' = None,  maxLength: int = None,  condition: str = None,  constraint: list['Constraint'] = None,  mustSupport: bool = None,  isModifier: bool = None,  isModifierReason: str = None,  isSummary: bool = None,  binding: 'Binding' = None,  mapping: list['Mapping'] = None, ):
        self.resourceType: str = resourceType or "ElementDefinition"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.path: str = path 
        self.representation: str = representation or []
        self.sliceName: str = sliceName 
        self.sliceIsConstraining: bool = sliceIsConstraining 
        self.label: str = label 
        self.code: list['Coding'] = code or []
        self.slicing: 'Slicing' = slicing 
        self.short: str = short 
        self.definition: str = definition 
        self.comment: str = comment 
        self.requirements: str = requirements 
        self.alias: str = alias or []
        self.min: int = min 
        self.max: str = max 
        self.base: 'Base' = base 
        self.contentReference: str = contentReference 
        self.type: list['Type'] = type or []
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
        self.meaningWhenMissing: str = meaningWhenMissing 
        self.orderMeaning: str = orderMeaning 
        self.fixedBase64Binary: str = fixedBase64Binary 
        self.fixedBoolean: bool = fixedBoolean 
        self.fixedCanonical: str = fixedCanonical 
        self.fixedCode: str = fixedCode 
        self.fixedDate: str = fixedDate 
        self.fixedDateTime: str = fixedDateTime 
        self.fixedDecimal: float = fixedDecimal 
        self.fixedId: str = fixedId 
        self.fixedInstant: str = fixedInstant 
        self.fixedInteger: int = fixedInteger 
        self.fixedMarkdown: str = fixedMarkdown 
        self.fixedOid: str = fixedOid 
        self.fixedPositiveInt: int = fixedPositiveInt 
        self.fixedString: str = fixedString 
        self.fixedTime: str = fixedTime 
        self.fixedUnsignedInt: int = fixedUnsignedInt 
        self.fixedUri: str = fixedUri 
        self.fixedUrl: str = fixedUrl 
        self.fixedUuid: str = fixedUuid 
        self.fixedAddress: 'Address' = fixedAddress 
        self.fixedAge: 'Age' = fixedAge 
        self.fixedAnnotation: 'Annotation' = fixedAnnotation 
        self.fixedAttachment: 'Attachment' = fixedAttachment 
        self.fixedCodeableConcept: 'CodeableConcept' = fixedCodeableConcept 
        self.fixedCoding: 'Coding' = fixedCoding 
        self.fixedContactPoint: 'ContactPoint' = fixedContactPoint 
        self.fixedCount: 'Count' = fixedCount 
        self.fixedDistance: 'Distance' = fixedDistance 
        self.fixedDuration: 'Duration' = fixedDuration 
        self.fixedHumanName: 'HumanName' = fixedHumanName 
        self.fixedIdentifier: 'Identifier' = fixedIdentifier 
        self.fixedMoney: 'Money' = fixedMoney 
        self.fixedPeriod: 'Period' = fixedPeriod 
        self.fixedQuantity: 'Quantity' = fixedQuantity 
        self.fixedRange: 'Range' = fixedRange 
        self.fixedRatio: 'Ratio' = fixedRatio 
        self.fixedReference: 'Reference' = fixedReference 
        self.fixedSampledData: 'SampledData' = fixedSampledData 
        self.fixedSignature: 'Signature' = fixedSignature 
        self.fixedTiming: 'Timing' = fixedTiming 
        self.fixedContactDetail: 'ContactDetail' = fixedContactDetail 
        self.fixedContributor: 'Contributor' = fixedContributor 
        self.fixedDataRequirement: 'DataRequirement' = fixedDataRequirement 
        self.fixedExpression: 'Expression' = fixedExpression 
        self.fixedParameterDefinition: 'ParameterDefinition' = fixedParameterDefinition 
        self.fixedRelatedArtifact: 'RelatedArtifact' = fixedRelatedArtifact 
        self.fixedTriggerDefinition: 'TriggerDefinition' = fixedTriggerDefinition 
        self.fixedUsageContext: 'UsageContext' = fixedUsageContext 
        self.fixedDosage: 'Dosage' = fixedDosage 
        self.fixedMeta: 'Meta' = fixedMeta 
        self.patternBase64Binary: str = patternBase64Binary 
        self.patternBoolean: bool = patternBoolean 
        self.patternCanonical: str = patternCanonical 
        self.patternCode: str = patternCode 
        self.patternDate: str = patternDate 
        self.patternDateTime: str = patternDateTime 
        self.patternDecimal: float = patternDecimal 
        self.patternId: str = patternId 
        self.patternInstant: str = patternInstant 
        self.patternInteger: int = patternInteger 
        self.patternMarkdown: str = patternMarkdown 
        self.patternOid: str = patternOid 
        self.patternPositiveInt: int = patternPositiveInt 
        self.patternString: str = patternString 
        self.patternTime: str = patternTime 
        self.patternUnsignedInt: int = patternUnsignedInt 
        self.patternUri: str = patternUri 
        self.patternUrl: str = patternUrl 
        self.patternUuid: str = patternUuid 
        self.patternAddress: 'Address' = patternAddress 
        self.patternAge: 'Age' = patternAge 
        self.patternAnnotation: 'Annotation' = patternAnnotation 
        self.patternAttachment: 'Attachment' = patternAttachment 
        self.patternCodeableConcept: 'CodeableConcept' = patternCodeableConcept 
        self.patternCoding: 'Coding' = patternCoding 
        self.patternContactPoint: 'ContactPoint' = patternContactPoint 
        self.patternCount: 'Count' = patternCount 
        self.patternDistance: 'Distance' = patternDistance 
        self.patternDuration: 'Duration' = patternDuration 
        self.patternHumanName: 'HumanName' = patternHumanName 
        self.patternIdentifier: 'Identifier' = patternIdentifier 
        self.patternMoney: 'Money' = patternMoney 
        self.patternPeriod: 'Period' = patternPeriod 
        self.patternQuantity: 'Quantity' = patternQuantity 
        self.patternRange: 'Range' = patternRange 
        self.patternRatio: 'Ratio' = patternRatio 
        self.patternReference: 'Reference' = patternReference 
        self.patternSampledData: 'SampledData' = patternSampledData 
        self.patternSignature: 'Signature' = patternSignature 
        self.patternTiming: 'Timing' = patternTiming 
        self.patternContactDetail: 'ContactDetail' = patternContactDetail 
        self.patternContributor: 'Contributor' = patternContributor 
        self.patternDataRequirement: 'DataRequirement' = patternDataRequirement 
        self.patternExpression: 'Expression' = patternExpression 
        self.patternParameterDefinition: 'ParameterDefinition' = patternParameterDefinition 
        self.patternRelatedArtifact: 'RelatedArtifact' = patternRelatedArtifact 
        self.patternTriggerDefinition: 'TriggerDefinition' = patternTriggerDefinition 
        self.patternUsageContext: 'UsageContext' = patternUsageContext 
        self.patternDosage: 'Dosage' = patternDosage 
        self.patternMeta: 'Meta' = patternMeta 
        self.example: list['Example'] = example or []
        self.minValueDate: str = minValueDate 
        self.minValueDateTime: str = minValueDateTime 
        self.minValueInstant: str = minValueInstant 
        self.minValueTime: str = minValueTime 
        self.minValueDecimal: float = minValueDecimal 
        self.minValueInteger: int = minValueInteger 
        self.minValuePositiveInt: int = minValuePositiveInt 
        self.minValueUnsignedInt: int = minValueUnsignedInt 
        self.minValueQuantity: 'Quantity' = minValueQuantity 
        self.maxValueDate: str = maxValueDate 
        self.maxValueDateTime: str = maxValueDateTime 
        self.maxValueInstant: str = maxValueInstant 
        self.maxValueTime: str = maxValueTime 
        self.maxValueDecimal: float = maxValueDecimal 
        self.maxValueInteger: int = maxValueInteger 
        self.maxValuePositiveInt: int = maxValuePositiveInt 
        self.maxValueUnsignedInt: int = maxValueUnsignedInt 
        self.maxValueQuantity: 'Quantity' = maxValueQuantity 
        self.maxLength: int = maxLength 
        self.condition: str = condition or []
        self.constraint: list['Constraint'] = constraint or []
        self.mustSupport: bool = mustSupport 
        self.isModifier: bool = isModifier 
        self.isModifierReason: str = isModifierReason 
        self.isSummary: bool = isSummary 
        self.binding: 'Binding' = binding 
        self.mapping: list['Mapping'] = mapping or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ElementDefinition":
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