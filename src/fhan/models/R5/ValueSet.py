"""
Generated class for ValueSet. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
        
    
        
    
    

class Designation(BaseModel):
    """ Additional representations for this concept when used in this value set - other languages, aliases, specialized purposes, used for particular purposes, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: Human language of the designation
    :param Coding use: Types of uses of designations
    :param Coding additionalUse: Additional ways how this designation would be used
    :param str value: The text value for this designation
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "use": {"class_name": "Coding", "is_contained": False},
        
        
        "additionalUse": {"class_name": "Coding", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  language:  'str'  = None,  use:  'Coding'  = None,  additionalUse:  list['Coding']  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.language = language 
        self.use = use 
        self.additionalUse = additionalUse or []
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Concept(BaseModel):
    """ Specifies a concept to be included or excluded.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code or expression from system
    :param str display: Text to display for this code for this value set in this valueset
    :param Designation designation: Additional representations for this concept
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "designation": {"class_name": "Designation", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  display:  'str'  = None,  designation:  list['Designation']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.display = display 
        self.designation = designation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Filter(BaseModel):
    """ Select concepts by specifying a matching criterion based on the properties (including relationships) defined by the system, or on filters defined by the system. If multiple filters are specified within the include, they SHALL all be true.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str property: A property/filter defined by the code system
    :param str op: = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | child-of | descendent-leaf | exists
    :param str value: Code from the system, or regex criteria, or boolean value for exists
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  property:  'str'  = None,  op:  'str'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.property = property 
        self.op = op 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Include(BaseModel):
    """ Include one or more codes from a code system or other value set(s).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: The system the codes come from
    :param str version: Specific version of the code system referred to
    :param Concept concept: A concept defined in the system
    :param Filter filter: Select codes/concepts by their properties (including relationships)
    :param str valueSet: Select the contents included in this value set
    :param str copyright: A copyright statement for the specific code system included in the value set
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "concept": {"class_name": "Concept", "is_contained": True},
        
        
        "filter": {"class_name": "Filter", "is_contained": True},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  system:  'str'  = None,  version:  'str'  = None,  concept:  list['Concept']  = None,  filter:  list['Filter']  = None,  valueSet:  list['str']  = None,  copyright:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.system = system 
        self.version = version 
        self.concept = concept or []
        self.filter = filter or []
        self.valueSet = valueSet or []
        self.copyright = copyright 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Compose(BaseModel):
    """ A set of criteria that define the contents of the value set by including or excluding codes selected from the specified code system(s) that the value set draws from. This is also known as the Content Logical Definition (CLD).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lockedDate: Fixed date for references with no specified version (transitive)
    :param bool inactive: Whether inactive codes are in the value set
    :param Include include: Include one or more codes from a code system or other value set(s)
    :param Exclude exclude: Explicitly exclude codes from a code system or other value sets
    :param str property: Property to return if client doesn't override
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "include": {"class_name": "Include", "is_contained": True},
        
        
        "exclude": {"class_name": "Exclude", "is_contained": True},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  lockedDate:  'str'  = None,  inactive:  'bool'  = None,  include:  list['Include']  = None,  exclude:  list['Exclude']  = None,  property:  list['str']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.lockedDate = lockedDate 
        self.inactive = inactive 
        self.include = include or []
        self.exclude = exclude or []
        self.property = property or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Parameter(BaseModel):
    """ A parameter that controlled the expansion process. These parameters may be used by users of expanded value sets to check whether the expansion is suitable for a particular purpose, or to pick the correct expansion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name as assigned by the client or server
    :param str valueString: Value of the named parameter
    :param bool valueBoolean: Value of the named parameter
    :param int valueInteger: Value of the named parameter
    :param float valueDecimal: Value of the named parameter
    :param str valueUri: Value of the named parameter
    :param str valueCode: Value of the named parameter
    :param str valueDateTime: Value of the named parameter
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  valueString:  'str'  = None,  valueBoolean:  'bool'  = None,  valueInteger:  'int'  = None,  valueDecimal:  'float'  = None,  valueUri:  'str'  = None,  valueCode:  'str'  = None,  valueDateTime:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.valueString = valueString 
        self.valueBoolean = valueBoolean 
        self.valueInteger = valueInteger 
        self.valueDecimal = valueDecimal 
        self.valueUri = valueUri 
        self.valueCode = valueCode 
        self.valueDateTime = valueDateTime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Property(BaseModel):
    """ A property defines an additional slot through which additional information can be provided about a concept.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies the property on the concepts, and when referred to in operations
    :param str uri: Formal identifier for the property
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  uri:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.uri = uri 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class SubProperty(BaseModel):
    """ A subproperty value for this concept.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to ValueSet.expansion.property.code
    :param str valueCode: Value of the subproperty for this concept
    :param Coding valueCoding: Value of the subproperty for this concept
    :param str valueString: Value of the subproperty for this concept
    :param int valueInteger: Value of the subproperty for this concept
    :param bool valueBoolean: Value of the subproperty for this concept
    :param str valueDateTime: Value of the subproperty for this concept
    :param float valueDecimal: Value of the subproperty for this concept
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  valueCode:  'str'  = None,  valueCoding:  'Coding'  = None,  valueString:  'str'  = None,  valueInteger:  'int'  = None,  valueBoolean:  'bool'  = None,  valueDateTime:  'str'  = None,  valueDecimal:  'float'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueCode = valueCode 
        self.valueCoding = valueCoding 
        self.valueString = valueString 
        self.valueInteger = valueInteger 
        self.valueBoolean = valueBoolean 
        self.valueDateTime = valueDateTime 
        self.valueDecimal = valueDecimal 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Property(BaseModel):
    """ A property value for this concept.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to ValueSet.expansion.property.code
    :param str valueCode: Value of the property for this concept
    :param Coding valueCoding: Value of the property for this concept
    :param str valueString: Value of the property for this concept
    :param int valueInteger: Value of the property for this concept
    :param bool valueBoolean: Value of the property for this concept
    :param str valueDateTime: Value of the property for this concept
    :param float valueDecimal: Value of the property for this concept
    :param SubProperty subProperty: SubProperty value for the concept
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        "subProperty": {"class_name": "SubProperty", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  valueCode:  'str'  = None,  valueCoding:  'Coding'  = None,  valueString:  'str'  = None,  valueInteger:  'int'  = None,  valueBoolean:  'bool'  = None,  valueDateTime:  'str'  = None,  valueDecimal:  'float'  = None,  subProperty:  list['SubProperty']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueCode = valueCode 
        self.valueCoding = valueCoding 
        self.valueString = valueString 
        self.valueInteger = valueInteger 
        self.valueBoolean = valueBoolean 
        self.valueDateTime = valueDateTime 
        self.valueDecimal = valueDecimal 
        self.subProperty = subProperty or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Contains(BaseModel):
    """ The codes that are contained in the value set expansion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: System value for the code
    :param bool abstract: If user cannot select this entry
    :param bool inactive: If concept is inactive in the code system
    :param str version: Version in which this code/display is defined
    :param str code: Code - if blank, this is not a selectable code
    :param str display: User display for the concept
    :param Designation designation: Additional representations for this item
    :param Property property: Property value for the concept
    :param Contains contains: Codes contained under this entry
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        "designation": {"class_name": "Designation", "is_contained": True},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "contains": {"class_name": "Contains", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  system:  'str'  = None,  abstract:  'bool'  = None,  inactive:  'bool'  = None,  version:  'str'  = None,  code:  'str'  = None,  display:  'str'  = None,  designation:  list['Designation']  = None,  property:  list['Property']  = None,  contains:  list['Contains']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.system = system 
        self.abstract = abstract 
        self.inactive = inactive 
        self.version = version 
        self.code = code 
        self.display = display 
        self.designation = designation or []
        self.property = property or []
        self.contains = contains or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Expansion(BaseModel):
    """ A value set can also be "expanded", where the value set is turned into a simple collection of enumerated codes. This element holds the expansion, if it has been performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identifier: Identifies the value set expansion (business identifier)
    :param str next: Opaque urls for paging through expansion results
    :param str timestamp: Time ValueSet expansion happened
    :param int total: Total number of codes in the expansion
    :param int offset: Offset at which this resource starts
    :param Parameter parameter: Parameter that controlled the expansion process
    :param Property property: Additional information supplied about each concept
    :param Contains contains: Codes in the value set
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        "parameter": {"class_name": "Parameter", "is_contained": True},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "contains": {"class_name": "Contains", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  'str'  = None,  next:  'str'  = None,  timestamp:  'str'  = None,  total:  'int'  = None,  offset:  'int'  = None,  parameter:  list['Parameter']  = None,  property:  list['Property']  = None,  contains:  list['Contains']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier 
        self.next = next 
        self.timestamp = timestamp 
        self.total = total 
        self.offset = offset 
        self.parameter = parameter or []
        self.property = property or []
        self.contains = contains or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Scope(BaseModel):
    """ Description of the semantic space the Value Set Expansion is intended to cover and should further clarify the text in ValueSet.description.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str inclusionCriteria: Criteria describing which concepts or codes should be included and why
    :param str exclusionCriteria: Criteria describing which concepts or codes should be excluded and why
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  inclusionCriteria:  'str'  = None,  exclusionCriteria:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.inclusionCriteria = inclusionCriteria 
        self.exclusionCriteria = exclusionCriteria 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ValueSet(DomainResource):
    """ A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this value set, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the value set (business identifier)
    :param str version: Business version of the value set
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this value set (computer friendly)
    :param str title: Name for this value set (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the value set
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for value set (if applicable)
    :param bool immutable: Indicates whether or not any change to the content logical definition may occur
    :param str purpose: Why this value set is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the ValueSet was approved by publisher
    :param str lastReviewDate: When the ValueSet was last reviewed by the publisher
    :param Period effectivePeriod: When the ValueSet is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the ValueSet
    :param ContactDetail editor: Who edited the ValueSet
    :param ContactDetail reviewer: Who reviewed the ValueSet
    :param ContactDetail endorser: Who endorsed the ValueSet
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param Compose compose: Content logical definition of the value set (CLD)
    :param Expansion expansion: Used when the value set is "expanded"
    :param Scope scope: Description of the semantic space the Value Set Expansion is intended to cover and should further clarify the text in ValueSet.description
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "compose": {"class_name": "Compose", "is_contained": True},
        
        
        "expansion": {"class_name": "Expansion", "is_contained": True},
        
        
        "scope": {"class_name": "Scope", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  immutable:  'bool'  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  topic:  list['CodeableConcept']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  compose:  'Compose'  = None,  expansion:  'Expansion'  = None,  scope:  'Scope'  = None, ):
        self.resourceType = resourceType or "ValueSet"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.status = status 
        self.experimental = experimental 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.immutable = immutable 
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.topic = topic or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatedArtifact = relatedArtifact or []
        self.compose = compose 
        self.expansion = expansion 
        self.scope = scope 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ValueSet":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ValueSet":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()