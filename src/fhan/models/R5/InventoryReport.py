"""
Generated class for InventoryReport. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class InventoryReport:
    """ A report of inventory or stock items.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the report
    :param str status: draft | requested | active | entered-in-error
    :param str countType: snapshot | difference
    :param CodeableConcept operationType: addition | subtraction
    :param CodeableConcept operationTypeReason: The reason for this count - regular count, ad-hoc count, new arrivals, etc
    :param str reportedDateTime: When the report has been submitted
    :param Reference reporter: Who submits the report
    :param Period reportingPeriod: The period the report refers to
    :param BackboneElement inventoryListing: An inventory listing section (grouped by any of the attributes)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location of the inventory items
    :param CodeableConcept itemStatus: The status of the items that are being reported
    :param str countingDateTime: The date and time when the items were counted
    :param BackboneElement item: The item or items in this listing
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: The inventory category or classification of the items being reported
    :param Quantity quantity: The quantity of the item or items being reported
    :param CodeableReference item: The code or reference to the item type
    :param Annotation note: A note associated with the InventoryReport
    
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
    
    countType: str = None
    
    operationType: "CodeableConcept" = None
    
    operationTypeReason: "CodeableConcept" = None
    
    reportedDateTime: str = None
    
    reporter: "Reference" = None
    
    reportingPeriod: "Period" = None
    
    inventoryListing: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    location: "Reference" = None
    
    itemStatus: "CodeableConcept" = None
    
    countingDateTime: str = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    item: "CodeableReference" = None
    
    note: "Annotation" = None
    