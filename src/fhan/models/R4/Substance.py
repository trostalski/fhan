"""
Generated class for Substance. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class instance(Element):
    """ Substance may be used to describe a kind of substance, or a specific package/container of the substance: an instance.
    :param BackboneElement instance: If this describes a specific package/container of the substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier of the package/container
    :param str expiry: When no longer valid to use
    :param Quantity quantity: Amount of substance in the package
    """
    instance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: "Identifier" = None
    
    expiry: str = None
    
    quantity: "Quantity" = None
    
@dataclass
class ingredient(Element):
    """ A substance can be composed of other substances.
    :param BackboneElement ingredient: Composition information about the substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio quantity: Optional amount (concentration)
    :param CodeableConcept substanceCodeableConcept: A component of the substance
    :param Reference substanceCodeableConcept: A component of the substance
    """
    ingredient: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    quantity: "Ratio" = None
    
    substanceCodeableConcept: "CodeableConcept" = None
    
    substanceCodeableConcept: "Reference" = None
    


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
    :param BackboneElement instance: If this describes a specific package/container of the substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier of the package/container
    :param str expiry: When no longer valid to use
    :param Quantity quantity: Amount of substance in the package
    :param BackboneElement ingredient: Composition information about the substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Ratio quantity: Optional amount (concentration)
    :param CodeableConcept substanceCodeableConcept: A component of the substance
    :param Reference substanceCodeableConcept: A component of the substance
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    category: list["CodeableConcept"] = None
    
    code: "CodeableConcept" = None
    
    description: str = None
    
    instance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: "Identifier" = None
    
    expiry: str = None
    
    quantity: "Quantity" = None
    
    ingredient: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    quantity: "Ratio" = None
    
    substanceCodeableConcept: "CodeableConcept" = None
    
    substanceCodeableConcept: "Reference" = None
    