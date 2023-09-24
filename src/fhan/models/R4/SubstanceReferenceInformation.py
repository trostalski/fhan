"""
Generated class for SubstanceReferenceInformation. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Range import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class GeneElement(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Todo
    :param 'Identifier' element: Todo
    :param list['Reference'] source: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  element: 'Identifier' = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.element: 'Identifier' = element 
        self.source: list['Reference'] = source or []
        

  
    
    

class Gene(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' geneSequenceOrigin: Todo
    :param 'CodeableConcept' gene: Todo
    :param list['Reference'] source: Todo
    :param list['GeneElement'] geneElement: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  geneSequenceOrigin: 'CodeableConcept' = None,  gene: 'CodeableConcept' = None,  source: list['Reference'] = None,  geneElement: list['GeneElement'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.geneSequenceOrigin: 'CodeableConcept' = geneSequenceOrigin 
        self.gene: 'CodeableConcept' = gene 
        self.source: list['Reference'] = source or []
        self.geneElement: list['GeneElement'] = geneElement or []
        

    
    

class Classification(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' domain: Todo
    :param 'CodeableConcept' classification: Todo
    :param list['CodeableConcept'] subtype: Todo
    :param list['Reference'] source: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  domain: 'CodeableConcept' = None,  classification: 'CodeableConcept' = None,  subtype: list['CodeableConcept'] = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.domain: 'CodeableConcept' = domain 
        self.classification: 'CodeableConcept' = classification 
        self.subtype: list['CodeableConcept'] = subtype or []
        self.source: list['Reference'] = source or []
        

    
    

class Target(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' target: Todo
    :param 'CodeableConcept' type: Todo
    :param 'CodeableConcept' interaction: Todo
    :param 'CodeableConcept' organism: Todo
    :param 'CodeableConcept' organismType: Todo
    :param 'Quantity' amountQuantity: Todo
    :param 'CodeableConcept' amountType: Todo
    :param list['Reference'] source: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  target: 'Identifier' = None,  type: 'CodeableConcept' = None,  interaction: 'CodeableConcept' = None,  organism: 'CodeableConcept' = None,  organismType: 'CodeableConcept' = None,  amountQuantity: 'Quantity' = None,  amountType: 'CodeableConcept' = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.target: 'Identifier' = target 
        self.type: 'CodeableConcept' = type 
        self.interaction: 'CodeableConcept' = interaction 
        self.organism: 'CodeableConcept' = organism 
        self.organismType: 'CodeableConcept' = organismType 
        self.amountQuantity: 'Quantity' = amountQuantity 
        self.amountType: 'CodeableConcept' = amountType 
        self.source: list['Reference'] = source or []
        

class SubstanceReferenceInformation(DomainResource):
    """ Todo.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str comment: Todo
    :param list['Gene'] gene: Todo
    :param list['Classification'] classification: Todo
    :param list['Target'] target: Todo
    """
    def __init__(self, resourceType: str = "SubstanceReferenceInformation",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  comment: str = None,  gene: list['Gene'] = None,  classification: list['Classification'] = None,  target: list['Target'] = None, ):
        self.resourceType: str = resourceType or "SubstanceReferenceInformation"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.comment: str = comment 
        self.gene: list['Gene'] = gene or []
        self.classification: list['Classification'] = classification or []
        self.target: list['Target'] = target or []
        