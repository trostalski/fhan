"""
Generated class for Person. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Address import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Link(Element):
    """ Link to a resource that concerns the same actual person.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference target: The resource to which this actual person is associated
    :param str assurance: level1 | level2 | level3 | level4
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    target: "Reference" = Reference()
    
    assurance: str = None
    

@dataclass
class Person(ModelBase):
    """ Demographics and administrative information about a person independent of a specific health-related context.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: A human identifier for this person
    :param HumanName name: A name associated with the person
    :param ContactPoint telecom: A contact detail for the person
    :param str gender: male | female | other | unknown
    :param str birthDate: The date on which the person was born
    :param Address address: One or more addresses for the person
    :param Attachment photo: Image of the person
    :param Reference managingOrganization: The organization that is the custodian of the person record
    :param bool active: This person's record is in active use
    :param Link link: Link to a resource that concerns the same actual person
    """

    resourceType: str = "Person"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    name: list[HumanName] = HumanName() 
    
    telecom: list[ContactPoint] = ContactPoint() 
    
    gender: str = None
    
    birthDate: str = None
    
    address: list[Address] = Address() 
    
    photo: "Attachment" = Attachment()
    
    managingOrganization: "Reference" = Reference()
    
    active: bool = None
    
    link: list[Link] = Link() 
    