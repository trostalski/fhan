"""
Generated class for BiologicallyDerivedProduct. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Collection(ModelBase):
    """ How this product was collected.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' collector: Individual performing collection
    :param 'Reference' source: Who is product from
    :param str collectedDateTime: Time of product collection
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  collector: 'Reference' = None,  source: 'Reference' = None,  collectedDateTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.collector: 'Reference' = collector 
        self.source: 'Reference' = source 
        self.collectedDateTime: str = collectedDateTime 
        

    
    

class Processing(ModelBase):
    """ Any processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem Cells.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of of processing
    :param 'CodeableConcept' procedure: Procesing code
    :param 'Reference' additive: Substance added during processing
    :param str timeDateTime: Time of processing
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  description: str = None,  procedure: 'CodeableConcept' = None,  additive: 'Reference' = None,  timeDateTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.procedure: 'CodeableConcept' = procedure 
        self.additive: 'Reference' = additive 
        self.timeDateTime: str = timeDateTime 
        

    
    

class Manipulation(ModelBase):
    """ Any manipulation of product post-collection that is intended to alter the product.  For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusion.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of manipulation
    :param str timeDateTime: Time of manipulation
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  description: str = None,  timeDateTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.timeDateTime: str = timeDateTime 
        

    
    

class Storage(ModelBase):
    """ Product storage.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of storage
    :param float temperature: Storage temperature
    :param str scale: farenheit | celsius | kelvin
    :param 'Period' duration: Storage timeperiod
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  description: str = None,  temperature: float = None,  scale: str = None,  duration: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.description: str = description 
        self.temperature: float = temperature 
        self.scale: str = scale 
        self.duration: 'Period' = duration 
        

class BiologicallyDerivedProduct(DomainResource):
    """ A material substance originating from a biological entity intended to be transplanted or infused
into another (possibly the same) biological entity.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External ids for this item
    :param str productCategory: organ | tissue | fluid | cells | biologicalAgent
    :param 'CodeableConcept' productCode: What this biologically derived product is
    :param str status: available | unavailable
    :param list['Reference'] request: Procedure request
    :param int quantity: The amount of this biologically derived product
    :param list['Reference'] parent: BiologicallyDerivedProduct parent
    :param 'Collection' collection: How this product was collected
    :param list['Processing'] processing: Any processing of the product during collection
    :param 'Manipulation' manipulation: Any manipulation of product post-collection
    :param list['Storage'] storage: Product storage
    """
    def __init__(self, resourceType: str = "BiologicallyDerivedProduct",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  productCategory: str = None,  productCode: 'CodeableConcept' = None,  status: str = None,  request: list['Reference'] = None,  quantity: int = None,  parent: list['Reference'] = None,  collection: 'Collection' = None,  processing: list['Processing'] = None,  manipulation: 'Manipulation' = None,  storage: list['Storage'] = None, ):
        self.resourceType: str = resourceType or "BiologicallyDerivedProduct"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.productCategory: str = productCategory 
        self.productCode: 'CodeableConcept' = productCode 
        self.status: str = status 
        self.request: list['Reference'] = request or []
        self.quantity: int = quantity 
        self.parent: list['Reference'] = parent or []
        self.collection: 'Collection' = collection 
        self.processing: list['Processing'] = processing or []
        self.manipulation: 'Manipulation' = manipulation 
        self.storage: list['Storage'] = storage or []
        