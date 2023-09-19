"""
Generated class for MedicinalProductPackaged. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    subject: "Reference" = None
    
    description: str = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    marketingStatus: "MarketingStatus" = None
    
    marketingAuthorization: "Reference" = None
    
    manufacturer: "Reference" = None
    
    batchIdentifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    outerPackaging: "Identifier" = None
    
    immediatePackaging: "Identifier" = None
    
    packageItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    material: "CodeableConcept" = None
    
    alternateMaterial: "CodeableConcept" = None
    
    device: "Reference" = None
    
    manufacturedItem: "Reference" = None
    
    packageItem: "BackboneElement" = None
    
    physicalCharacteristics: "ProdCharacteristic" = None
    
    otherCharacteristics: "CodeableConcept" = None
    
    shelfLifeStorage: "ProductShelfLife" = None
    
    manufacturer: "Reference" = None
    