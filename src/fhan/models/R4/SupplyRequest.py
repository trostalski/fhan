"""
Generated class for SupplyRequest. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class SupplyRequest(ModelBase):
    """ A record of a request for a medication, substance or device used in the healthcare setting.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for SupplyRequest
    :param str status: draft | active | suspended +
    :param CodeableConcept category: The kind of supply (central, non-stock, etc.)
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept itemCodeableConcept: Medication, Substance, or Device requested to be supplied
    :param Reference itemCodeableConcept: Medication, Substance, or Device requested to be supplied
    :param Quantity quantity: The requested amount of the item indicated
    :param BackboneElement parameter: Ordered item details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Item detail
    :param CodeableConcept valueCodeableConcept: Value of detail
    :param Quantity valueCodeableConcept: Value of detail
    :param Range valueCodeableConcept: Value of detail
    :param bool valueCodeableConcept: Value of detail
    :param str occurrencedateTime: When the request should be fulfilled
    :param Period occurrencedateTime: When the request should be fulfilled
    :param Timing occurrencedateTime: When the request should be fulfilled
    :param str authoredOn: When the request was made
    :param Reference requester: Individual making the request
    :param Reference supplier: Who is intended to fulfill the request
    :param CodeableConcept reasonCode: The reason why the supply item was requested
    :param Reference reasonReference: The reason why the supply item was requested
    :param Reference deliverFrom: The origin of the supply
    :param Reference deliverTo: The destination of the supply
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
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    itemCodeableConcept: "CodeableConcept" = None
    
    itemCodeableConcept: "Reference" = None
    
    quantity: "Quantity" = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    
    valueCodeableConcept: bool = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    supplier: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    deliverFrom: "Reference" = None
    
    deliverTo: "Reference" = None
    