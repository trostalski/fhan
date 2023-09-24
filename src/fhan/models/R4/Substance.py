"""
Generated class for Substance. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Instance(ModelBase):
    """ Substance may be used to describe a kind of substance, or a specific package/container of the substance: an instance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Identifier of the package/container
    :param str expiry: When no longer valid to use
    :param 'Quantity' quantity: Amount of substance in the package
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  expiry: str = None,  quantity: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.expiry: str = expiry 
        self.quantity: 'Quantity' = quantity 
        

    
    

class Ingredient(ModelBase):
    """ A substance can be composed of other substances.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Ratio' quantity: Optional amount (concentration)
    :param 'CodeableConcept' substanceCodeableConcept: A component of the substance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  quantity: 'Ratio' = None,  substanceCodeableConcept: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.quantity: 'Ratio' = quantity 
        self.substanceCodeableConcept: 'CodeableConcept' = substanceCodeableConcept 
        

class Substance(DomainResource):
    """ A homogeneous material with a definite composition.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique identifier
    :param str status: active | inactive | entered-in-error
    :param list['CodeableConcept'] category: What class/type of substance this is
    :param 'CodeableConcept' code: What substance this is
    :param str description: Textual description of the substance, comments
    :param list['Instance'] instance: If this describes a specific package/container of the substance
    :param list['Ingredient'] ingredient: Composition information about the substance
    """
    def __init__(self, resourceType: str = "Substance",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  category: list['CodeableConcept'] = None,  code: 'CodeableConcept' = None,  description: str = None,  instance: list['Instance'] = None,  ingredient: list['Ingredient'] = None, ):
        self.resourceType: str = resourceType or "Substance"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.category: list['CodeableConcept'] = category or []
        self.code: 'CodeableConcept' = code 
        self.description: str = description 
        self.instance: list['Instance'] = instance or []
        self.ingredient: list['Ingredient'] = ingredient or []
        