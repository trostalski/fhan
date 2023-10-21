"""
Generated class for BiologicallyDerivedProduct. 
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


class Collection(BaseModel):
    """How this product was collected.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Individual performing collection
    :param Reference source: Who is product from
    :param str collectedDateTime: Time of product collection
    :param Period collectedPeriod: Time of product collection
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "collector": {"class_name": "Reference", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
        "collectedPeriod": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        collector: "Reference" = None,
        source: "Reference" = None,
        collectedDateTime: "str" = None,
        collectedPeriod: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.collector = collector
        self.source = source
        self.collectedDateTime = collectedDateTime
        self.collectedPeriod = collectedPeriod

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Processing(BaseModel):
    """Any processing of the product during collection that does not change the fundamental nature of the product. For example adding anti-coagulants during the collection of Peripheral Blood Stem Cells.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of of processing
    :param CodeableConcept procedure: Procesing code
    :param Reference additive: Substance added during processing
    :param str timeDateTime: Time of processing
    :param Period timePeriod: Time of processing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "procedure": {"class_name": "CodeableConcept", "is_contained": False},
        "additive": {"class_name": "Reference", "is_contained": False},
        "timePeriod": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        description: "str" = None,
        procedure: "CodeableConcept" = None,
        additive: "Reference" = None,
        timeDateTime: "str" = None,
        timePeriod: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.procedure = procedure
        self.additive = additive
        self.timeDateTime = timeDateTime
        self.timePeriod = timePeriod

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Manipulation(BaseModel):
    """Any manipulation of product post-collection that is intended to alter the product.  For example a buffy-coat enrichment or CD8 reduction of Peripheral Blood Stem Cells to make it more suitable for infusion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of manipulation
    :param str timeDateTime: Time of manipulation
    :param Period timePeriod: Time of manipulation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "timePeriod": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        description: "str" = None,
        timeDateTime: "str" = None,
        timePeriod: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.timeDateTime = timeDateTime
        self.timePeriod = timePeriod

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Storage(BaseModel):
    """Product storage.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of storage
    :param float temperature: Storage temperature
    :param str scale: farenheit | celsius | kelvin
    :param Period duration: Storage timeperiod
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "duration": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        description: "str" = None,
        temperature: "float" = None,
        scale: "str" = None,
        duration: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.temperature = temperature
        self.scale = scale
        self.duration = duration

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class BiologicallyDerivedProduct(DomainResource):
    """A material substance originating from a biological entity intended to be transplanted or infused
    into another (possibly the same) biological entity.
        :param str id: Logical id of this artifact
        :param Meta meta: Metadata about the resource
        :param str implicitRules: A set of rules under which this content was created
        :param str language: Language of the resource content
        :param Narrative text: Text summary of the resource, for human interpretation
        :param Resource contained: Contained, inline Resources
        :param Extension extension: Additional content defined by implementations
        :param Extension modifierExtension: Extensions that cannot be ignored
        :param Identifier identifier: External ids for this item
        :param str productCategory: organ | tissue | fluid | cells | biologicalAgent
        :param CodeableConcept productCode: What this biologically derived product is
        :param str status: available | unavailable
        :param Reference request: Procedure request
        :param int quantity: The amount of this biologically derived product
        :param Reference parent: BiologicallyDerivedProduct parent
        :param Collection collection: How this product was collected
        :param Processing processing: Any processing of the product during collection
        :param Manipulation manipulation: Any manipulation of product post-collection
        :param Storage storage: Product storage
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "productCode": {"class_name": "CodeableConcept", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "parent": {"class_name": "Reference", "is_contained": False},
        "collection": {"class_name": "Collection", "is_contained": True},
        "processing": {"class_name": "Processing", "is_contained": True},
        "manipulation": {"class_name": "Manipulation", "is_contained": True},
        "storage": {"class_name": "Storage", "is_contained": True},
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
        productCategory: "str" = None,
        productCode: "CodeableConcept" = None,
        status: "str" = None,
        request: list["Reference"] = None,
        quantity: "int" = None,
        parent: list["Reference"] = None,
        collection: "Collection" = None,
        processing: list["Processing"] = None,
        manipulation: "Manipulation" = None,
        storage: list["Storage"] = None,
    ):
        self.resourceType = resourceType or "BiologicallyDerivedProduct"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.productCategory = productCategory
        self.productCode = productCode
        self.status = status
        self.request = request or []
        self.quantity = quantity
        self.parent = parent or []
        self.collection = collection
        self.processing = processing or []
        self.manipulation = manipulation
        self.storage = storage or []

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProduct":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProduct":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
