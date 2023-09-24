"""
Generated class for Linkage. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Element import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Item(Element):
    """ Identifies which record considered as the reference to the same real-world occurrence as well as how the items should be evaluated within the collection of linked items.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: source | alternate | historical
    :param Reference resource: Resource being linked
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type: str = None
    
    resource:  "Reference" = Reference()
    

@dataclass
class Linkage(ModelBase):
    """ Identifies two or more records (resource instances) that refer to the same real-world "occurrence".
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param bool active: Whether this linkage assertion is active or not
    :param Reference author: Who is responsible for linkages
    :param Item item: Item to be linked
    """

    resourceType: str = "Linkage"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    active: bool = None
    
    author: "Reference" = None
    
    item: list["Item"] = None
    