"""
Generated class for MedicinalProductPackaged. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class batchIdentifier(Element):
    """ Batch numbering.
    :param BackboneElement batchIdentifier: Batch numbering
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier outerPackaging: A number appearing on the outer packaging of a specific batch
    :param Identifier immediatePackaging: A number appearing on the immediate packaging (and not the outer packaging)
    """
    batchIdentifier: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    outerPackaging: "Identifier" = None
    
    immediatePackaging: "Identifier" = None
    
@dataclass
class packageItem(Element):
    """ A packaging item, as a contained for medicine, possibly with other packaging items within.
    :param BackboneElement packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Including possibly Data Carrier Identifier
    :param CodeableConcept type: The physical type of the container of the medicine
    :param Quantity quantity: The quantity of this package in the medicinal product, at the current level of packaging. The outermost is always 1
    :param CodeableConcept material: Material type of the package item
    :param CodeableConcept alternateMaterial: A possible alternate material for the packaging
    :param Reference device: A device accompanying a medicinal product
    :param Reference manufacturedItem: The manufactured item as contained in the packaged medicinal product
    :param BackboneElement packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    :param ProdCharacteristic physicalCharacteristics: Dimensions, color etc.
    :param CodeableConcept otherCharacteristics: Other codeable characteristics
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param Reference manufacturer: Manufacturer of this Package Item
    """
    packageItem: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    material: list["CodeableConcept"] = None
    
    alternateMaterial: list["CodeableConcept"] = None
    
    device: list["Reference"] = None
    
    manufacturedItem: list["Reference"] = None
    
    packageItem: list["BackboneElement"] = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    otherCharacteristics: list["CodeableConcept"] = None
    
    shelfLifeStorage: list["ProductShelfLife"] = None
    
    manufacturer: list["Reference"] = None
    
@dataclass
class packageItem(Element):
    """ A packaging item, as a contained for medicine, possibly with other packaging items within.
    :param BackboneElement packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Including possibly Data Carrier Identifier
    :param CodeableConcept type: The physical type of the container of the medicine
    :param Quantity quantity: The quantity of this package in the medicinal product, at the current level of packaging. The outermost is always 1
    :param CodeableConcept material: Material type of the package item
    :param CodeableConcept alternateMaterial: A possible alternate material for the packaging
    :param Reference device: A device accompanying a medicinal product
    :param Reference manufacturedItem: The manufactured item as contained in the packaged medicinal product
    :param BackboneElement packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    :param ProdCharacteristic physicalCharacteristics: Dimensions, color etc.
    :param CodeableConcept otherCharacteristics: Other codeable characteristics
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param Reference manufacturer: Manufacturer of this Package Item
    """
    packageItem: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    material: list["CodeableConcept"] = None
    
    alternateMaterial: list["CodeableConcept"] = None
    
    device: list["Reference"] = None
    
    manufacturedItem: list["Reference"] = None
    
    packageItem: list["BackboneElement"] = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    otherCharacteristics: list["CodeableConcept"] = None
    
    shelfLifeStorage: list["ProductShelfLife"] = None
    
    manufacturer: list["Reference"] = None
    


@dataclass
class MedicinalProductPackaged(ModelBase):
    """ A medicinal product in a container or package.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param Reference subject: The product with this is a pack for
    :param str description: Textual description
    :param CodeableConcept legalStatusOfSupply: The legal status of supply of the medicinal product as classified by the regulator
    :param MarketingStatus marketingStatus: Marketing information
    :param Reference marketingAuthorization: Manufacturer of this Package Item
    :param Reference manufacturer: Manufacturer of this Package Item
    :param BackboneElement batchIdentifier: Batch numbering
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier outerPackaging: A number appearing on the outer packaging of a specific batch
    :param Identifier immediatePackaging: A number appearing on the immediate packaging (and not the outer packaging)
    :param BackboneElement packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Including possibly Data Carrier Identifier
    :param CodeableConcept type: The physical type of the container of the medicine
    :param Quantity quantity: The quantity of this package in the medicinal product, at the current level of packaging. The outermost is always 1
    :param CodeableConcept material: Material type of the package item
    :param CodeableConcept alternateMaterial: A possible alternate material for the packaging
    :param Reference device: A device accompanying a medicinal product
    :param Reference manufacturedItem: The manufactured item as contained in the packaged medicinal product
    :param BackboneElement packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    :param ProdCharacteristic physicalCharacteristics: Dimensions, color etc.
    :param CodeableConcept otherCharacteristics: Other codeable characteristics
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param Reference manufacturer: Manufacturer of this Package Item
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
    
    subject: list["Reference"] = None
    
    description: str = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    marketingStatus: list["MarketingStatus"] = None
    
    marketingAuthorization: "Reference" = None
    
    manufacturer: list["Reference"] = None
    
    batchIdentifier: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    outerPackaging: "Identifier" = None
    
    immediatePackaging: "Identifier" = None
    
    packageItem: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    material: list["CodeableConcept"] = None
    
    alternateMaterial: list["CodeableConcept"] = None
    
    device: list["Reference"] = None
    
    manufacturedItem: list["Reference"] = None
    
    packageItem: list["BackboneElement"] = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    otherCharacteristics: list["CodeableConcept"] = None
    
    shelfLifeStorage: list["ProductShelfLife"] = None
    
    manufacturer: list["Reference"] = None
    