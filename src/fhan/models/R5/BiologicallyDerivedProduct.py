"""
Generated class for BiologicallyDerivedProduct. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class BiologicallyDerivedProduct:
    """ A biological material originating from a biological entity intended to be transplanted or infused into another (possibly the same) biological entity.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Coding productCategory: organ | tissue | fluid | cells | biologicalAgent
    :param CodeableConcept productCode: A code that identifies the kind of this biologically derived product
    :param Reference parent: The parent biologically-derived product
    :param Reference request: Request to obtain and/or infuse this product
    :param Identifier identifier: Instance identifier
    :param Identifier biologicalSourceEvent: An identifier that supports traceability to the event during which material in this product from one or more biological entities was obtained or pooled
    :param Reference processingFacility: Processing facilities responsible for the labeling and distribution of this biologically derived product
    :param str division: A unique identifier for an aliquot of a product
    :param Coding productStatus: available | unavailable
    :param str expirationDate: Date, and where relevant time, of expiration
    :param BackboneElement collection: How this product was collected
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Individual performing collection
    :param Reference source: The patient who underwent the medical procedure to collect the product or the organization that facilitated the collection
    :param str collecteddateTime: Time of product collection
    :param Period collecteddateTime: Time of product collection
    :param Range storageTempRequirements: Product storage temperature requirements
    :param BackboneElement property: A property that is specific to this BiologicallyDerviedProduct instance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code that specifies the property
    :param bool valueboolean: Property values
    :param int valueboolean: Property values
    :param CodeableConcept valueboolean: Property values
    :param Period valueboolean: Property values
    :param Quantity valueboolean: Property values
    :param Range valueboolean: Property values
    :param Ratio valueboolean: Property values
    :param str valueboolean: Property values
    :param Attachment valueboolean: Property values
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    productCategory: "Coding" = None
    
    productCode: "CodeableConcept" = None
    
    parent: "Reference" = None
    
    request: "Reference" = None
    
    identifier: "Identifier" = None
    
    biologicalSourceEvent: "Identifier" = None
    
    processingFacility: "Reference" = None
    
    division: str = None
    
    productStatus: "Coding" = None
    
    expirationDate: str = None
    
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    collector: "Reference" = None
    
    source: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    storageTempRequirements: "Range" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueboolean: bool = None
    
    valueboolean: int = None
    
    valueboolean: "CodeableConcept" = None
    
    valueboolean: "Period" = None
    
    valueboolean: "Quantity" = None
    
    valueboolean: "Range" = None
    
    valueboolean: "Ratio" = None
    
    valueboolean: str = None
    
    valueboolean: "Attachment" = None
    