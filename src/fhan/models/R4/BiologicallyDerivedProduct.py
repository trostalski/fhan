"""
Generated class for BiologicallyDerivedProduct. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Collection(Element):
    """ How this product was collected.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Individual performing collection
    :param Reference source: Who is product from
    :param str collectedDateTime: Time of product collection
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    collector: "Reference" = Reference()
    source: "Reference" = Reference()
    
    collectedDateTime: str = None
    

    
    
@dataclass
class Processing(Element):
    """ Any processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem Cells.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of of processing
    :param CodeableConcept procedure: Procesing code
    :param Reference additive: Substance added during processing
    :param str timeDateTime: Time of processing
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    description: str = None
    procedure: "CodeableConcept" = CodeableConcept()
    additive: "Reference" = Reference()
    
    timeDateTime: str = None
    

    
    
@dataclass
class Manipulation(Element):
    """ Any manipulation of product post-collection that is intended to alter the product.  For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of manipulation
    :param str timeDateTime: Time of manipulation
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    description: str = None
    
    timeDateTime: str = None
    

    
    
@dataclass
class Storage(Element):
    """ Product storage.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of storage
    :param float temperature: Storage temperature
    :param str scale: farenheit | celsius | kelvin
    :param Period duration: Storage timeperiod
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    description: str = None
    
    temperature: float = None
    
    scale: str = None
    duration: "Period" = Period()
    

@dataclass
class BiologicallyDerivedProduct(ModelBase):
    """ A material substance originating from a biological entity intended to be transplanted or infused
into another (possibly the same) biological entity.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External ids for this item
    :param str productCategory: organ | tissue | fluid | cells | biologicalAgent
    :param CodeableConcept productCode: What this biologically derived product is
    :param str status: available | unavailable
    :param Reference request: Procedure request
    :param int quantity: The amount of this biologically derived product
    :param Reference parent: BiologicallyDerivedProduct parent
    :param Collection collection: How this product was collected
    :param Processing processing: Any processing of the product during collection
    :param Manipulation manipulation: Any manipulation of product post-collection
    :param Storage storage: Product storage
    """

    resourceType: str = "BiologicallyDerivedProduct"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    productCategory: str = None
    
    productCode: "CodeableConcept" = CodeableConcept()
    
    status: str = None
    
    request: list[Reference] = Reference() 
    
    quantity: int = None
    
    parent: list[Reference] = Reference() 
    
    collection: "Collection" = Collection()
    
    processing: list[Processing] = Processing() 
    
    manipulation: "Manipulation" = Manipulation()
    
    storage: list[Storage] = Storage() 
    