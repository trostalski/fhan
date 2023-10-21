"""
Generated class for SupplyDelivery. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class SuppliedItem(BaseModel):
    """The item that is being delivered or has been supplied.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: Amount dispensed
    :param CodeableConcept itemCodeableConcept: Medication, Substance, or Device supplied
    :param Reference itemReference: Medication, Substance, or Device supplied
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        "itemReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        quantity: "Quantity" = None,
        itemCodeableConcept: "CodeableConcept" = None,
        itemReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.quantity = quantity
        self.itemCodeableConcept = itemCodeableConcept
        self.itemReference = itemReference

    @classmethod
    def from_dict(cls, data: dict) -> "SupplyDelivery":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SupplyDelivery":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SupplyDelivery(DomainResource):
    """Record of delivery of what is supplied.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param str status: in-progress | completed | abandoned | entered-in-error
    :param Reference patient: Patient for whom the item is supplied
    :param CodeableConcept type: Category of dispense event
    :param SuppliedItem suppliedItem: The item that is delivered or supplied
    :param str occurrenceDateTime: When event occurred
    :param Period occurrencePeriod: When event occurred
    :param Timing occurrenceTiming: When event occurred
    :param Reference supplier: Dispenser
    :param Reference destination: Where the Supply was sent
    :param Reference receiver: Who collected the Supply
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "partOf": {"class_name": "Reference", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "suppliedItem": {"class_name": "SuppliedItem", "is_contained": True},
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        "supplier": {"class_name": "Reference", "is_contained": False},
        "destination": {"class_name": "Reference", "is_contained": False},
        "receiver": {"class_name": "Reference", "is_contained": False},
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
        basedOn: list["Reference"] = None,
        partOf: list["Reference"] = None,
        status: "str" = None,
        patient: "Reference" = None,
        type: "CodeableConcept" = None,
        suppliedItem: "SuppliedItem" = None,
        occurrenceDateTime: "str" = None,
        occurrencePeriod: "Period" = None,
        occurrenceTiming: "Timing" = None,
        supplier: "Reference" = None,
        destination: "Reference" = None,
        receiver: list["Reference"] = None,
    ):
        self.resourceType = resourceType or "SupplyDelivery"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.status = status
        self.patient = patient
        self.type = type
        self.suppliedItem = suppliedItem
        self.occurrenceDateTime = occurrenceDateTime
        self.occurrencePeriod = occurrencePeriod
        self.occurrenceTiming = occurrenceTiming
        self.supplier = supplier
        self.destination = destination
        self.receiver = receiver or []

    @classmethod
    def from_dict(cls, data: dict) -> "SupplyDelivery":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SupplyDelivery":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
