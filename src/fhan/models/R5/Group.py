"""
Generated class for Group. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Characteristic(BaseModel):
    """ Identifies traits whose presence r absence is shared by members of the group.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Kind of characteristic
    :param CodeableConcept valueCodeableConcept: Value held by characteristic
    :param bool valueBoolean: Value held by characteristic
    :param Quantity valueQuantity: Value held by characteristic
    :param Range valueRange: Value held by characteristic
    :param Reference valueReference: Value held by characteristic
    :param bool exclude: Group includes or excludes
    :param Period period: Period over which characteristic is tested
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueBoolean:  'bool'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueReference:  'Reference'  = None,  exclude:  'bool'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueBoolean = valueBoolean 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueReference = valueReference 
        self.exclude = exclude 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Group":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Group":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Member(BaseModel):
    """ Identifies the resource instances that are members of the group.:param str membership: definitional | enumerated
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference entity: Reference to the group member
    :param Period period: Period member belonged to the group
    :param bool inactive: If member is no longer in group
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "entity": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        }
    def __init__(self,  membership:  'str'  = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  entity:  'Reference'  = None,  period:  'Period'  = None,  inactive:  'bool'  = None, ):
        self.membership = membership 
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.entity = entity 
        self.period = period 
        self.inactive = inactive 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Group":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Group":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Group(DomainResource):
    """ Represents a defined collection of entities that may be discussed or acted upon collectively but which are not expected to act collectively, and are not formally or legally recognized; i.e. a collection of entities that isn't an Organization.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for this Group
    :param bool active: Whether this group's record is in active use
    :param str type: person | animal | practitioner | device | careteam | healthcareservice | location | organization | relatedperson | specimen
    :param str membership: definitional | enumerated
    :param CodeableConcept code: Kind of Group members
    :param str name: Label for Group
    :param str description: Natural language description of the group
    :param int quantity: Number of members
    :param Reference managingEntity: Entity that is the custodian of the Group's definition
    :param Characteristic characteristic: Include / Exclude group members by Trait
    :param Member member: Who or what is in group
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "managingEntity": {"class_name": "Reference", "is_contained": False},
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        
        "member": {"class_name": "Member", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  active:  'bool'  = None,  type:  'str'  = None,  membership:  'str'  = None,  code:  'CodeableConcept'  = None,  name:  'str'  = None,  description:  'str'  = None,  quantity:  'int'  = None,  managingEntity:  'Reference'  = None,  characteristic:  list['Characteristic']  = None,  member:  list['Member']  = None, ):
        self.resourceType = resourceType or "Group"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.active = active 
        self.type = type 
        self.membership = membership 
        self.code = code 
        self.name = name 
        self.description = description 
        self.quantity = quantity 
        self.managingEntity = managingEntity 
        self.characteristic = characteristic or []
        self.member = member or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Group":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Group":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()