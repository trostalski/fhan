"""
Generated class for PackagedProductDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ProductShelfLife import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.MarketingStatus import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class PackagedProductDefinition:
    """ A medically related item or items, in a container or package.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: A unique identifier for this package as whole - not for the content of the package
    :param str name: A name for this package. Typically as listed in a drug formulary, catalogue, inventory etc
    :param CodeableConcept type: A high level category e.g. medicinal product, raw material, shipping container etc
    :param Reference packageFor: The product that this is a pack for
    :param CodeableConcept status: The status within the lifecycle of this item. High level - not intended to duplicate details elsewhere e.g. legal status, or authorization/marketing status
    :param str statusDate: The date at which the given status became applicable
    :param Quantity containedItemQuantity: A total of the complete count of contained items of a particular type/form, independent of sub-packaging or organization. This can be considered as the pack size. See also packaging.containedItem.amount (especially the long definition)
    :param str description: Textual description. Note that this is not the name of the package or product
    :param BackboneElement legalStatusOfSupply: The legal status of supply of the packaged item as classified by the regulator
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The actual status of supply. In what situation this package type may be supplied for use
    :param CodeableConcept jurisdiction: The place where the legal status of supply applies
    :param MarketingStatus marketingStatus: Allows specifying that an item is on the market for sale, or that it is not available, and the dates and locations associated
    :param bool copackagedIndicator: Identifies if the drug product is supplied with another item such as a diluent or adjuvant
    :param Reference manufacturer: Manufacturer of this package type (multiple means these are all possible manufacturers)
    :param Reference attachedDocument: Additional information or supporting documentation about the packaged product
    :param BackboneElement packaging: A packaging item, as a container for medically related items, possibly with other packaging items within, or a packaging component, such as bottle cap
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: An identifier that is specific to this particular part of the packaging. Including possibly a Data Carrier Identifier
    :param CodeableConcept type: The physical type of the container of the items
    :param bool componentPart: Is this a part of the packaging (e.g. a cap or bottle stopper), rather than the packaging itself (e.g. a bottle or vial)
    :param int quantity: The quantity of this level of packaging in the package that contains it (with the outermost level being 1)
    :param CodeableConcept material: Material type of the package item
    :param CodeableConcept alternateMaterial: A possible alternate material for this part of the packaging, that is allowed to be used instead of the usual material
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param Reference manufacturer: Manufacturer of this packaging item (multiple means these are all potential manufacturers)
    :param BackboneElement property: General characteristics of this item
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param Quantity valueCodeableConcept: A value for the characteristic
    :param str valueCodeableConcept: A value for the characteristic
    :param bool valueCodeableConcept: A value for the characteristic
    :param Attachment valueCodeableConcept: A value for the characteristic
    :param BackboneElement containedItem: The item(s) within the packaging
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The actual item(s) of medication, as manufactured, or a device, or other medically related item (food, biologicals, raw materials, medical fluids, gases etc.), as contained in the package
    :param Quantity amount: The number of this type of item within this packaging or for continuous items such as liquids it is the quantity (for example 25ml). See also PackagedProductDefinition.containedItemQuantity (especially the long definition)
    :param BackboneElement packaging: A packaging item, as a container for medically related items, possibly with other packaging items within, or a packaging component, such as bottle cap
    :param BackboneElement characteristic: General characteristics of this item
    
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
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    packageFor: "Reference" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    containedItemQuantity: "Quantity" = None
    
    description: str = None
    
    legalStatusOfSupply: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    marketingStatus: "MarketingStatus" = None
    
    copackagedIndicator: bool = None
    
    manufacturer: "Reference" = None
    
    attachedDocument: "Reference" = None
    
    packaging: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    componentPart: bool = None
    
    quantity: int = None
    
    material: "CodeableConcept" = None
    
    alternateMaterial: "CodeableConcept" = None
    
    shelfLifeStorage: "ProductShelfLife" = None
    
    manufacturer: "Reference" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Attachment" = None
    
    containedItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    item: "CodeableReference" = None
    
    amount: "Quantity" = None
    
    packaging: "BackboneElement" = None
    
    characteristic: "BackboneElement" = None
    