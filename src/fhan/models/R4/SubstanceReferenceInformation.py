"""
Generated class for SubstanceReferenceInformation. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Range import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class GeneElement(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param Identifier element: Todo
    :param Reference source: Todo
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    type: "CodeableConcept" = CodeableConcept()
    element: "Identifier" = Identifier()
    source: list[Reference] = Reference() 
    

  
    
    
@dataclass
class Gene(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept geneSequenceOrigin: Todo
    :param CodeableConcept gene: Todo
    :param Reference source: Todo
    :param GeneElement geneElement: Todo
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    geneSequenceOrigin: "CodeableConcept" = CodeableConcept()
    gene: "CodeableConcept" = CodeableConcept()
    source: list[Reference] = Reference() 
    geneElement: list[GeneElement] = GeneElement() 
    

    
    
@dataclass
class Classification(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept domain: Todo
    :param CodeableConcept classification: Todo
    :param CodeableConcept subtype: Todo
    :param Reference source: Todo
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    domain: "CodeableConcept" = CodeableConcept()
    classification: "CodeableConcept" = CodeableConcept()
    subtype: list[CodeableConcept] = CodeableConcept() 
    source: list[Reference] = Reference() 
    

    
    
@dataclass
class Target(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier target: Todo
    :param CodeableConcept type: Todo
    :param CodeableConcept interaction: Todo
    :param CodeableConcept organism: Todo
    :param CodeableConcept organismType: Todo
    :param Quantity amountQuantity: Todo
    :param CodeableConcept amountType: Todo
    :param Reference source: Todo
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    target: "Identifier" = Identifier()
    type: "CodeableConcept" = CodeableConcept()
    interaction: "CodeableConcept" = CodeableConcept()
    organism: "CodeableConcept" = CodeableConcept()
    organismType: "CodeableConcept" = CodeableConcept()
    amountQuantity: "Quantity" = Quantity()
    amountType: "CodeableConcept" = CodeableConcept()
    source: list[Reference] = Reference() 
    

@dataclass
class SubstanceReferenceInformation(ModelBase):
    """ Todo.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str comment: Todo
    :param Gene gene: Todo
    :param Classification classification: Todo
    :param Target target: Todo
    """

    resourceType: str = "SubstanceReferenceInformation"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    comment: str = None
    
    gene: list[Gene] = Gene() 
    
    classification: list[Classification] = Classification() 
    
    target: list[Target] = Target() 
    