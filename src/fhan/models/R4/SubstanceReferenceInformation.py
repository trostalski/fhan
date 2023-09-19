"""
Generated class for SubstanceReferenceInformation. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement gene: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept geneSequenceOrigin: Todo
    :param CodeableConcept gene: Todo
    :param Reference source: Todo
    :param BackboneElement geneElement: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param Identifier element: Todo
    :param Reference source: Todo
    :param BackboneElement classification: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept domain: Todo
    :param CodeableConcept classification: Todo
    :param CodeableConcept subtype: Todo
    :param Reference source: Todo
    :param BackboneElement target: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier target: Todo
    :param CodeableConcept type: Todo
    :param CodeableConcept interaction: Todo
    :param CodeableConcept organism: Todo
    :param CodeableConcept organismType: Todo
    :param Quantity amountQuantity: Todo
    :param Range amountQuantity: Todo
    :param str amountQuantity: Todo
    :param CodeableConcept amountType: Todo
    :param Reference source: Todo
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    comment: str = None
    
    gene: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    geneSequenceOrigin: "CodeableConcept" = None
    
    gene: "CodeableConcept" = None
    
    source: "Reference" = None
    
    geneElement: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    element: "Identifier" = None
    
    source: "Reference" = None
    
    classification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    domain: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    subtype: "CodeableConcept" = None
    
    source: "Reference" = None
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    target: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    interaction: "CodeableConcept" = None
    
    organism: "CodeableConcept" = None
    
    organismType: "CodeableConcept" = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: "Range" = None
    
    amountQuantity: str = None
    
    amountType: "CodeableConcept" = None
    
    source: "Reference" = None
    