"""
Generated class for BiologicallyDerivedProduct. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class collection(Element):
    """ How this product was collected.
    :param BackboneElement collection: How this product was collected
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Individual performing collection
    :param Reference source: Who is product from
    :param str collecteddateTime: Time of product collection
    :param Period collecteddateTime: Time of product collection
    """
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    collector: "Reference" = None
    
    source: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
@dataclass
class processing(Element):
    """ Any processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem Cells.
    :param BackboneElement processing: Any processing of the product during collection
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of of processing
    :param CodeableConcept procedure: Procesing code
    :param Reference additive: Substance added during processing
    :param str timedateTime: Time of processing
    :param Period timedateTime: Time of processing
    """
    processing: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    procedure: "CodeableConcept" = None
    
    additive: "Reference" = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
@dataclass
class manipulation(Element):
    """ Any manipulation of product post-collection that is intended to alter the product.  For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusion.
    :param BackboneElement manipulation: Any manipulation of product post-collection
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of manipulation
    :param str timedateTime: Time of manipulation
    :param Period timedateTime: Time of manipulation
    """
    manipulation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
@dataclass
class storage(Element):
    """ Product storage.
    :param BackboneElement storage: Product storage
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of storage
    :param float temperature: Storage temperature
    :param str scale: farenheit | celsius | kelvin
    :param Period duration: Storage timeperiod
    """
    storage: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    temperature: float = None
    
    scale: str = None
    
    duration: "Period" = None
    


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
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    productCategory: str = None
    
    productCode: "CodeableConcept" = None
    
    status: str = None
    
    request: list["Reference"] = None
    
    quantity: int = None
    
    parent: list["Reference"] = None
    
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    collector: "Reference" = None
    
    source: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    processing: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    procedure: "CodeableConcept" = None
    
    additive: "Reference" = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    manipulation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    storage: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    temperature: float = None
    
    scale: str = None
    
    duration: "Period" = None
    