"""
Generated class for SupplyRequest. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class SupplyRequest:
    """ A record of a non-patient specific request for a medication, substance, device, certain types of biologically derived product, and nutrition product used in the healthcare setting.
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
    :param Reference basedOn: What other request is fulfilled by this supply request
    :param CodeableConcept category: The kind of supply (central, non-stock, etc.)
    :param str priority: routine | urgent | asap | stat
    :param Reference deliverFor: The patient for who the supply request is for
    :param CodeableReference item: Medication, Substance, or Device requested to be supplied
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
    :param CodeableReference reason: The reason why the supply item was requested
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
    
    basedOn: "Reference" = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    deliverFor: "Reference" = None
    
    item: "CodeableReference" = None
    
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
    
    reason: "CodeableReference" = None
    
    deliverFrom: "Reference" = None
    
    deliverTo: "Reference" = None
    