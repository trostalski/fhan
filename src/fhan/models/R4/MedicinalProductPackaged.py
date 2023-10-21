"""
Generated class for MedicinalProductPackaged. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class BatchIdentifier(BaseModel):
    """Batch numbering.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier outerPackaging: A number appearing on the outer packaging of a specific batch
    :param Identifier immediatePackaging: A number appearing on the immediate packaging (and not the outer packaging)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "outerPackaging": {"class_name": "Identifier", "is_contained": False},
        "immediatePackaging": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        outerPackaging: "Identifier" = None,
        immediatePackaging: "Identifier" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.outerPackaging = outerPackaging
        self.immediatePackaging = immediatePackaging

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPackaged":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPackaged":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PackageItem(BaseModel):
    """A packaging item, as a contained for medicine, possibly with other packaging items within.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Including possibly Data Carrier Identifier
    :param CodeableConcept type: The physical type of the container of the medicine
    :param Quantity quantity: The quantity of this package in the medicinal product, at the current level of packaging. The outermost is always 1
    :param CodeableConcept material: Material type of the package item
    :param CodeableConcept alternateMaterial: A possible alternate material for the packaging
    :param Reference device: A device accompanying a medicinal product
    :param Reference manufacturedItem: The manufactured item as contained in the packaged medicinal product
    :param PackageItem packageItem: Allows containers within containers
    :param ProdCharacteristic physicalCharacteristics: Dimensions, color etc.
    :param CodeableConcept otherCharacteristics: Other codeable characteristics
    :param ProductShelfLife shelfLifeStorage: Shelf Life and storage information
    :param Reference manufacturer: Manufacturer of this Package Item
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "material": {"class_name": "CodeableConcept", "is_contained": False},
        "alternateMaterial": {"class_name": "CodeableConcept", "is_contained": False},
        "device": {"class_name": "Reference", "is_contained": False},
        "manufacturedItem": {"class_name": "Reference", "is_contained": False},
        "packageItem": {"class_name": "PackageItem", "is_contained": True},
        "physicalCharacteristics": {
            "class_name": "ProdCharacteristic",
            "is_contained": False,
        },
        "otherCharacteristics": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "shelfLifeStorage": {"class_name": "ProductShelfLife", "is_contained": False},
        "manufacturer": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        type: "CodeableConcept" = None,
        quantity: "Quantity" = None,
        material: list["CodeableConcept"] = None,
        alternateMaterial: list["CodeableConcept"] = None,
        device: list["Reference"] = None,
        manufacturedItem: list["Reference"] = None,
        packageItem: list["PackageItem"] = None,
        physicalCharacteristics: "ProdCharacteristic" = None,
        otherCharacteristics: list["CodeableConcept"] = None,
        shelfLifeStorage: list["ProductShelfLife"] = None,
        manufacturer: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type
        self.quantity = quantity
        self.material = material or []
        self.alternateMaterial = alternateMaterial or []
        self.device = device or []
        self.manufacturedItem = manufacturedItem or []
        self.packageItem = packageItem or []
        self.physicalCharacteristics = physicalCharacteristics
        self.otherCharacteristics = otherCharacteristics or []
        self.shelfLifeStorage = shelfLifeStorage or []
        self.manufacturer = manufacturer or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPackaged":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPackaged":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProductPackaged(DomainResource):
    """A medicinal product in a container or package.
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
    :param BatchIdentifier batchIdentifier: Batch numbering
    :param PackageItem packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "legalStatusOfSupply": {"class_name": "CodeableConcept", "is_contained": False},
        "marketingStatus": {"class_name": "MarketingStatus", "is_contained": False},
        "marketingAuthorization": {"class_name": "Reference", "is_contained": False},
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        "batchIdentifier": {"class_name": "BatchIdentifier", "is_contained": True},
        "packageItem": {"class_name": "PackageItem", "is_contained": True},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        subject: list["Reference"] = None,
        description: "str" = None,
        legalStatusOfSupply: "CodeableConcept" = None,
        marketingStatus: list["MarketingStatus"] = None,
        marketingAuthorization: "Reference" = None,
        manufacturer: list["Reference"] = None,
        batchIdentifier: list["BatchIdentifier"] = None,
        packageItem: list["PackageItem"] = None,
    ):
        self.resourceType = resourceType or "MedicinalProductPackaged"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.subject = subject or []
        self.description = description
        self.legalStatusOfSupply = legalStatusOfSupply
        self.marketingStatus = marketingStatus or []
        self.marketingAuthorization = marketingAuthorization
        self.manufacturer = manufacturer or []
        self.batchIdentifier = batchIdentifier or []
        self.packageItem = packageItem or []

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductPackaged":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductPackaged":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
