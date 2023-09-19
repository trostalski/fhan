"""
Generated class for InventoryItem. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Address import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class InventoryItem:
    """ functional description of an inventory item used in inventory and supply-related workflows.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the inventory item
    :param str status: active | inactive | entered-in-error | unknown
    :param CodeableConcept category: Category or class of the item
    :param CodeableConcept code: Code designating the specific type of item
    :param BackboneElement name: The item name(s) - the brand name, or common name, functional name, generic name or others
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding nameType: The type of name e.g. 'brand-name', 'functional-name', 'common-name'
    :param str language: The language used to express the item name
    :param str name: The name or designation of the item
    :param BackboneElement responsibleOrganization: Organization(s) responsible for the product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: The role of the organization e.g. manufacturer, distributor, or other
    :param Reference organization: An organization that is associated with the item
    :param BackboneElement description: Descriptive characteristics of the item
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: The language that is used in the item description
    :param str description: Textual description of the item
    :param CodeableConcept inventoryStatus: The usage status like recalled, in use, discarded
    :param CodeableConcept baseUnit: The base unit of measure - the unit in which the product is used or counted
    :param Quantity netContent: Net content or amount present in the item
    :param BackboneElement association: Association with other items or products
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept associationType: The type of association between the device and the other item
    :param Reference relatedItem: The related item or product
    :param Ratio quantity: The quantity of the product in this product
    :param BackboneElement characteristic: Characteristic of the item
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept characteristicType: The characteristic that is being defined
    :param str valuestring: The value of the attribute
    :param int valuestring: The value of the attribute
    :param float valuestring: The value of the attribute
    :param bool valuestring: The value of the attribute
    :param str valuestring: The value of the attribute
    :param str valuestring: The value of the attribute
    :param Quantity valuestring: The value of the attribute
    :param Range valuestring: The value of the attribute
    :param Ratio valuestring: The value of the attribute
    :param Annotation valuestring: The value of the attribute
    :param Address valuestring: The value of the attribute
    :param Duration valuestring: The value of the attribute
    :param CodeableConcept valuestring: The value of the attribute
    :param BackboneElement instance: Instances or occurrences of the product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: The identifier for the physical instance, typically a serial number
    :param str lotNumber: The lot or batch number of the item
    :param str expiry: The expiry date or date and time for the product
    :param Reference subject: The subject that the item is associated with
    :param Reference location: The location that the item is associated with
    :param Reference productReference: Link to a product resource used in clinical workflows
    
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
    
    code: "CodeableConcept" = None
    
    name: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    nameType: "Coding" = None
    
    language: str = None
    
    name: str = None
    
    responsibleOrganization: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    organization: "Reference" = None
    
    description: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: str = None
    
    description: str = None
    
    inventoryStatus: "CodeableConcept" = None
    
    baseUnit: "CodeableConcept" = None
    
    netContent: "Quantity" = None
    
    association: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    associationType: "CodeableConcept" = None
    
    relatedItem: "Reference" = None
    
    quantity: "Ratio" = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    characteristicType: "CodeableConcept" = None
    
    valuestring: str = None
    
    valuestring: int = None
    
    valuestring: float = None
    
    valuestring: bool = None
    
    valuestring: str = None
    
    valuestring: str = None
    
    valuestring: "Quantity" = None
    
    valuestring: "Range" = None
    
    valuestring: "Ratio" = None
    
    valuestring: "Annotation" = None
    
    valuestring: "Address" = None
    
    valuestring: "Duration" = None
    
    valuestring: "CodeableConcept" = None
    
    instance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    lotNumber: str = None
    
    expiry: str = None
    
    subject: "Reference" = None
    
    location: "Reference" = None
    
    productReference: "Reference" = None
    