"""
Generated class for StructureMap. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Structure(BaseModel):
    """ A structure definition used by this map. The structure definition may describe instances that are converted, or the instances that are produced.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: Canonical reference to structure definition
    :param str mode: source | queried | target | produced
    :param str alias: Name for type in this map
    :param str documentation: Documentation on use of structure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  mode:  'str'  = None,  alias:  'str'  = None,  documentation:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.mode = mode 
        self.alias = alias 
        self.documentation = documentation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Const(BaseModel):
    """ Definition of a constant value used in the map rules.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Constant name
    :param str value: FHIRPath exression - value of the constant
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Input(BaseModel):
    """ A name assigned to an instance of data. The instance must be provided when the mapping is invoked.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name for this instance of data
    :param str type: Type for this instance of data
    :param str mode: source | target
    :param str documentation: Documentation for this instance of data
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  type:  'str'  = None,  mode:  'str'  = None,  documentation:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.type = type 
        self.mode = mode 
        self.documentation = documentation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Source(BaseModel):
    """ Source inputs to the mapping.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValue: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  context:  'str'  = None,  min:  'int'  = None,  max:  'str'  = None,  type:  'str'  = None,  defaultValue:  'str'  = None,  element:  'str'  = None,  listMode:  'str'  = None,  variable:  'str'  = None,  condition:  'str'  = None,  check:  'str'  = None,  logMessage:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.context = context 
        self.min = min 
        self.max = max 
        self.type = type 
        self.defaultValue = defaultValue 
        self.element = element 
        self.listMode = listMode 
        self.variable = variable 
        self.condition = condition 
        self.check = check 
        self.logMessage = logMessage 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Parameter(BaseModel):
    """ Parameters to the transform.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueId: Parameter value - variable or literal
    :param str valueString: Parameter value - variable or literal
    :param bool valueBoolean: Parameter value - variable or literal
    :param int valueInteger: Parameter value - variable or literal
    :param float valueDecimal: Parameter value - variable or literal
    :param str valueDate: Parameter value - variable or literal
    :param str valueTime: Parameter value - variable or literal
    :param str valueDateTime: Parameter value - variable or literal
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  valueId:  'str'  = None,  valueString:  'str'  = None,  valueBoolean:  'bool'  = None,  valueInteger:  'int'  = None,  valueDecimal:  'float'  = None,  valueDate:  'str'  = None,  valueTime:  'str'  = None,  valueDateTime:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.valueId = valueId 
        self.valueString = valueString 
        self.valueBoolean = valueBoolean 
        self.valueInteger = valueInteger 
        self.valueDecimal = valueDecimal 
        self.valueDate = valueDate 
        self.valueTime = valueTime 
        self.valueDateTime = valueDateTime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Target(BaseModel):
    """ Content to create because of this mapping rule.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Variable this rule applies to
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | single
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param Parameter parameter: Parameters to the transform
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        "parameter": {"class_name": "Parameter", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  context:  'str'  = None,  element:  'str'  = None,  variable:  'str'  = None,  listMode:  list['str']  = None,  listRuleId:  'str'  = None,  transform:  'str'  = None,  parameter:  list['Parameter']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.context = context 
        self.element = element 
        self.variable = variable 
        self.listMode = listMode or []
        self.listRuleId = listRuleId 
        self.transform = transform 
        self.parameter = parameter or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Dependent(BaseModel):
    """ Which other rules to apply in the context of this rule.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param Parameter parameter: Parameter to pass to the rule or group
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "parameter": {"class_name": "Parameter", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  parameter:  list['Parameter']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.parameter = parameter or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Rule(BaseModel):
    """ Transform Rule from source to target.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of the rule for internal references
    :param Source source: Source inputs to the mapping
    :param Target target: Content to create because of this mapping rule
    :param Rule rule: Rules contained in this rule
    :param Dependent dependent: Which other rules to apply in the context of this rule
    :param str documentation: Documentation for this instance of data
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "source": {"class_name": "Source", "is_contained": True},
        
        
        "target": {"class_name": "Target", "is_contained": True},
        
        
        "rule": {"class_name": "Rule", "is_contained": True},
        
        
        "dependent": {"class_name": "Dependent", "is_contained": True},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  source:  list['Source']  = None,  target:  list['Target']  = None,  rule:  list['Rule']  = None,  dependent:  list['Dependent']  = None,  documentation:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.source = source or []
        self.target = target or []
        self.rule = rule or []
        self.dependent = dependent or []
        self.documentation = documentation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Group(BaseModel):
    """ Organizes the mapping into managable chunks for human review/ease of maintenance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Human-readable label
    :param str extends: Another group that this group adds rules to
    :param str typeMode: types | type-and-types
    :param str documentation: Additional description/explanation for group
    :param Input input: Named instance provided when invoking the map
    :param Rule rule: Transform Rule from source to target
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        "input": {"class_name": "Input", "is_contained": True},
        
        
        "rule": {"class_name": "Rule", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  extends:  'str'  = None,  typeMode:  'str'  = None,  documentation:  'str'  = None,  input:  list['Input']  = None,  rule:  list['Rule']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.extends = extends 
        self.typeMode = typeMode 
        self.documentation = documentation 
        self.input = input or []
        self.rule = rule or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class StructureMap(DomainResource):
    """ A Map of relationships between 2 structures that can be used to transform data.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this structure map, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the structure map
    :param str version: Business version of the structure map
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this structure map (computer friendly)
    :param str title: Name for this structure map (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the structure map
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for structure map (if applicable)
    :param str purpose: Why this structure map is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param Structure structure: Structure Definition used by this map
    :param str _import: Other maps used by this map (canonical URLs)
    :param Const const: Definition of the constant value used in the map rules
    :param Group group: Named sections for reader convenience
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
        
        
        
        
        
        "structure": {"class_name": "Structure", "is_contained": True},
        
        
        
        "const": {"class_name": "Const", "is_contained": True},
        
        
        "group": {"class_name": "Group", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  structure:  list['Structure']  = None,  _import:  list['str']  = None,  const:  list['Const']  = None,  group:  list['Group']  = None, ):
        self.resourceType = resourceType or "StructureMap"
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
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.structure = structure or []
        self._import = _import or []
        self.const = const or []
        self.group = group or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "StructureMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()