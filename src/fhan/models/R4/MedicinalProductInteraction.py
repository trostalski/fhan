"""
Generated class for MedicinalProductInteraction. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Interactant(Element):
    """ The specific medication, food or laboratory test that interacts.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: The specific medication, food or laboratory test that interacts
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    itemReference: "Reference" = Reference()
    

@dataclass
class MedicinalProductInteraction(ModelBase):
    """ The interactions of the medicinal product with other medicinal products, or other forms of interactions.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference subject: The medication for which this is a described interaction
    :param str description: The interaction described
    :param Interactant interactant: The specific medication, food or laboratory test that interacts
    :param CodeableConcept type: The type of the interaction e.g. drug-drug interaction, drug-food interaction, drug-lab test interaction
    :param CodeableConcept effect: The effect of the interaction, for example "reduced gastric absorption of primary medication"
    :param CodeableConcept incidence: The incidence of the interaction, e.g. theoretical, observed
    :param CodeableConcept management: Actions for managing the interaction
    """

    resourceType: str = "MedicinalProductInteraction"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    subject: list[Reference] = Reference() 
    
    description: str = None
    
    interactant: list[Interactant] = Interactant() 
    
    type: "CodeableConcept" = CodeableConcept()
    
    effect: "CodeableConcept" = CodeableConcept()
    
    incidence: "CodeableConcept" = CodeableConcept()
    
    management: "CodeableConcept" = CodeableConcept()
    