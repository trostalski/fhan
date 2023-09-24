"""
Generated class for Group. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Characteristic(Element):
    """ Identifies traits whose presence r absence is shared by members of the group.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Kind of characteristic
    :param CodeableConcept valueCodeableConcept: Value held by characteristic
    :param bool exclude: Group includes or excludes
    :param Period period: Period over which characteristic is tested
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    code:  "CodeableConcept" = CodeableConcept()
    
    valueCodeableConcept:  "CodeableConcept" = CodeableConcept()
    
    exclude: bool = None
    
    period:  "Period" = Period()
    

    
    
@dataclass
class Member(Element):
    """ Identifies the resource instances that are members of the group.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference entity: Reference to the group member
    :param Period period: Period member belonged to the group
    :param bool inactive: If member is no longer in group
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    entity:  "Reference" = Reference()
    
    period:  "Period" = Period()
    
    inactive: bool = None
    

@dataclass
class Group(ModelBase):
    """ Enforces a descriptive group that can be used in definitional resources
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique id
    :param bool active: Whether this group's record is in active use
    :param str type: person | animal | practitioner | device | medication | substance
    :param bool actual: Descriptive or actual
    :param CodeableConcept code: Kind of Group members
    :param str name: Label for Group
    :param int quantity: Number of members
    :param Reference managingEntity: Entity that is the custodian of the Group's definition
    :param Characteristic characteristic: Include / Exclude group members by Trait
    :param Member member: Who or what is in group
    """

    resourceType: str = "Group"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    active: bool = None
    
    type: str = None
    
    actual: bool = None
    
    code: "CodeableConcept" = None
    
    name: str = None
    
    quantity: int = None
    
    managingEntity: "Reference" = None
    
    characteristic: list["Characteristic"] = None
    
    member: "Member" = None
    