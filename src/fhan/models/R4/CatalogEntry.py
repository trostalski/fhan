"""
Generated class for CatalogEntry. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class RelatedEntry(BaseModel):
    """Used for example, to point to a substance, or to a device used to administer a medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relationtype: triggers | is-replaced-by
    :param Reference item: The reference to the related item
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "item": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        relationtype: "str" = None,
        item: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relationtype = relationtype
        self.item = item

    @classmethod
    def from_dict(cls, data: dict) -> "CatalogEntry":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CatalogEntry":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class CatalogEntry(DomainResource):
    """Catalog entries are wrappers that contextualize items included in a catalog.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier of the catalog item
    :param CodeableConcept type: The type of item - medication, device, service, protocol or other
    :param bool orderable: Whether the entry represents an orderable item
    :param Reference referencedItem: The item that is being defined
    :param Identifier additionalIdentifier: Any additional identifier(s) for the catalog item, in the same granularity or concept
    :param CodeableConcept classification: Classification (category or class) of the item entry
    :param str status: draft | active | retired | unknown
    :param Period validityPeriod: The time period in which this catalog entry is expected to be active
    :param str validTo: The date until which this catalog entry is expected to be active
    :param str lastUpdated: When was this catalog last updated
    :param CodeableConcept additionalCharacteristic: Additional characteristics of the catalog entry
    :param CodeableConcept additionalClassification: Additional classification of the catalog entry
    :param RelatedEntry relatedEntry: An item that this catalog entry is related to
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "referencedItem": {"class_name": "Reference", "is_contained": False},
        "additionalIdentifier": {"class_name": "Identifier", "is_contained": False},
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
        "validityPeriod": {"class_name": "Period", "is_contained": False},
        "additionalCharacteristic": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "additionalClassification": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "relatedEntry": {"class_name": "RelatedEntry", "is_contained": True},
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
        type: "CodeableConcept" = None,
        orderable: "bool" = None,
        referencedItem: "Reference" = None,
        additionalIdentifier: list["Identifier"] = None,
        classification: list["CodeableConcept"] = None,
        status: "str" = None,
        validityPeriod: "Period" = None,
        validTo: "str" = None,
        lastUpdated: "str" = None,
        additionalCharacteristic: list["CodeableConcept"] = None,
        additionalClassification: list["CodeableConcept"] = None,
        relatedEntry: list["RelatedEntry"] = None,
    ):
        self.resourceType = resourceType or "CatalogEntry"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type
        self.orderable = orderable
        self.referencedItem = referencedItem
        self.additionalIdentifier = additionalIdentifier or []
        self.classification = classification or []
        self.status = status
        self.validityPeriod = validityPeriod
        self.validTo = validTo
        self.lastUpdated = lastUpdated
        self.additionalCharacteristic = additionalCharacteristic or []
        self.additionalClassification = additionalClassification or []
        self.relatedEntry = relatedEntry or []

    @classmethod
    def from_dict(cls, data: dict) -> "CatalogEntry":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "CatalogEntry":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
