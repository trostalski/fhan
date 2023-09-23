"""
Generated class for Substance. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Instance(Element):
    """ Substance may be used to describe a kind of substance, or a specific package/container of the substance: an instance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier of the package/container
    :param str expiry: When no longer valid to use
    :param Quantity quantity: Amount of substance in the package
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    identifier: "Identifier" = Identifier()
    
    expiry: str = None
    quantity: "Quantity" = Quantity()
    

    
    
@dataclass
class Ingredient(Element):
    """ A substance can be composed of other substances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio quantity: Optional amount (concentration)
    :param CodeableConcept substanceCodeableConcept: A component of the substance
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    quantity: "Ratio" = Ratio()
    substanceCodeableConcept: "CodeableConcept" = CodeableConcept()
    

@dataclass
class Substance(ModelBase):
    """ A homogeneous material with a definite composition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: What class/type of substance this is
    :param CodeableConcept code: What substance this is
    :param str description: Textual description of the substance, comments
    :param Instance instance: If this describes a specific package/container of the substance
    :param Ingredient ingredient: Composition information about the substance
    """

    resourceType: str = "Substance"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    category: list[CodeableConcept] = CodeableConcept() 
    
    code: "CodeableConcept" = CodeableConcept()
    
    description: str = None
    
    instance: list[Instance] = Instance() 
    
    ingredient: list[Ingredient] = Ingredient() 
    