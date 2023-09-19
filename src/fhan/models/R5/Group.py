"""
Generated class for Group. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class Group:
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
    :param BackboneElement characteristic: Include / Exclude group members by Trait
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Kind of characteristic
    :param CodeableConcept valueCodeableConcept: Value held by characteristic
    :param bool valueCodeableConcept: Value held by characteristic
    :param Quantity valueCodeableConcept: Value held by characteristic
    :param Range valueCodeableConcept: Value held by characteristic
    :param Reference valueCodeableConcept: Value held by characteristic
    :param bool exclude: Group includes or excludes
    :param Period period: Period over which characteristic is tested
    :param BackboneElement member: Who or what is in group
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference entity: Reference to the group member
    :param Period period: Period member belonged to the group
    :param bool inactive: If member is no longer in group
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    active: bool = None
    
    type: str = None
    
    membership: str = None
    
    code: "CodeableConcept" = None
    
    name: str = None
    
    description: str = None
    
    quantity: int = None
    
    managingEntity: "Reference" = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    
    valueCodeableConcept: "Reference" = None
    
    exclude: bool = None
    
    period: "Period" = None
    
    member: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    entity: "Reference" = None
    
    period: "Period" = None
    
    inactive: bool = None
    