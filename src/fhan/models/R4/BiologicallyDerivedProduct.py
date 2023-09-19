"""
Generated class for BiologicallyDerivedProduct. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement collection: How this product was collected
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Individual performing collection
    :param Reference source: Who is product from
    :param str collecteddateTime: Time of product collection
    :param Period collecteddateTime: Time of product collection
    :param BackboneElement processing: Any processing of the product during collection
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of of processing
    :param CodeableConcept procedure: Procesing code
    :param Reference additive: Substance added during processing
    :param str timedateTime: Time of processing
    :param Period timedateTime: Time of processing
    :param BackboneElement manipulation: Any manipulation of product post-collection
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of manipulation
    :param str timedateTime: Time of manipulation
    :param Period timedateTime: Time of manipulation
    :param BackboneElement storage: Product storage
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of storage
    :param float temperature: Storage temperature
    :param str scale: farenheit | celsius | kelvin
    :param Period duration: Storage timeperiod
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    productCategory: str = None
    
    productCode: "CodeableConcept" = None
    
    status: str = None
    
    request: "Reference" = None
    
    quantity: int = None
    
    parent: "Reference" = None
    
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    collector: "Reference" = None
    
    source: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    processing: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    procedure: "CodeableConcept" = None
    
    additive: "Reference" = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    manipulation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    storage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    temperature: float = None
    
    scale: str = None
    
    duration: "Period" = None
    