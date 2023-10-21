"""
Generated class for Specimen. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Collection(BaseModel):
    """Details concerning the specimen collection.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Who collected the specimen
    :param str collectedDateTime: Collection time
    :param Period collectedPeriod: Collection time
    :param Duration duration: How long it took to collect specimen
    :param Quantity quantity: The quantity of specimen collected
    :param CodeableConcept method: Technique used to perform collection
    :param CodeableConcept bodySite: Anatomical collection site
    :param CodeableConcept fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param Duration fastingStatusDuration: Whether or how long patient abstained from food and/or drink
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "collector": {"class_name": "Reference", "is_contained": False},
        "collectedPeriod": {"class_name": "Period", "is_contained": False},
        "duration": {"class_name": "Duration", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        "fastingStatusCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "fastingStatusDuration": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        collector: "Reference" = None,
        collectedDateTime: "str" = None,
        collectedPeriod: "Period" = None,
        duration: "Duration" = None,
        quantity: "Quantity" = None,
        method: "CodeableConcept" = None,
        bodySite: "CodeableConcept" = None,
        fastingStatusCodeableConcept: "CodeableConcept" = None,
        fastingStatusDuration: "Duration" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.collector = collector
        self.collectedDateTime = collectedDateTime
        self.collectedPeriod = collectedPeriod
        self.duration = duration
        self.quantity = quantity
        self.method = method
        self.bodySite = bodySite
        self.fastingStatusCodeableConcept = fastingStatusCodeableConcept
        self.fastingStatusDuration = fastingStatusDuration

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Processing(BaseModel):
    """Details concerning processing and processing steps for the specimen.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of procedure
    :param CodeableConcept procedure: Indicates the treatment step  applied to the specimen
    :param Reference additive: Material used in the processing step
    :param str timeDateTime: Date and time of specimen processing
    :param Period timePeriod: Date and time of specimen processing
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
        additive: list["Reference"] = None,
        timeDateTime: "str" = None,
        timePeriod: "Period" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description
        self.procedure = procedure
        self.additive = additive or []
        self.timeDateTime = timeDateTime
        self.timePeriod = timePeriod

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Container(BaseModel):
    """The container holding the specimen.  The recursive nature of containers; i.e. blood in tube in tray in rack is not addressed here.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Id for the container
    :param str description: Textual description of the container
    :param CodeableConcept type: Kind of container directly associated with specimen
    :param Quantity capacity: Container volume or size
    :param Quantity specimenQuantity: Quantity of specimen within container
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveReference: Additive associated with container
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "capacity": {"class_name": "Quantity", "is_contained": False},
        "specimenQuantity": {"class_name": "Quantity", "is_contained": False},
        "additiveCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "additiveReference": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        description: "str" = None,
        type: "CodeableConcept" = None,
        capacity: "Quantity" = None,
        specimenQuantity: "Quantity" = None,
        additiveCodeableConcept: "CodeableConcept" = None,
        additiveReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.description = description
        self.type = type
        self.capacity = capacity
        self.specimenQuantity = specimenQuantity
        self.additiveCodeableConcept = additiveCodeableConcept
        self.additiveReference = additiveReference

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Specimen(DomainResource):
    """A sample to be used for analysis.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Identifier
    :param Identifier accessionIdentifier: Identifier assigned by the lab
    :param str status: available | unavailable | unsatisfactory | entered-in-error
    :param CodeableConcept type: Kind of material that forms the specimen
    :param Reference subject: Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance or a device
    :param str receivedTime: The time when specimen was received for processing
    :param Reference parent: Specimen from which this specimen originated
    :param Reference request: Why the specimen was collected
    :param Collection collection: Collection details
    :param Processing processing: Processing and processing step details
    :param Container container: Direct container of specimen (tube/slide, etc.)
    :param CodeableConcept condition: State of the specimen
    :param Annotation note: Comments
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "accessionIdentifier": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "parent": {"class_name": "Reference", "is_contained": False},
        "request": {"class_name": "Reference", "is_contained": False},
        "collection": {"class_name": "Collection", "is_contained": True},
        "processing": {"class_name": "Processing", "is_contained": True},
        "container": {"class_name": "Container", "is_contained": True},
        "condition": {"class_name": "CodeableConcept", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
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
        accessionIdentifier: "Identifier" = None,
        status: "str" = None,
        type: "CodeableConcept" = None,
        subject: "Reference" = None,
        receivedTime: "str" = None,
        parent: list["Reference"] = None,
        request: list["Reference"] = None,
        collection: "Collection" = None,
        processing: list["Processing"] = None,
        container: list["Container"] = None,
        condition: list["CodeableConcept"] = None,
        note: list["Annotation"] = None,
    ):
        self.resourceType = resourceType or "Specimen"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.accessionIdentifier = accessionIdentifier
        self.status = status
        self.type = type
        self.subject = subject
        self.receivedTime = receivedTime
        self.parent = parent or []
        self.request = request or []
        self.collection = collection
        self.processing = processing or []
        self.container = container or []
        self.condition = condition or []
        self.note = note or []

    @classmethod
    def from_dict(cls, data: dict) -> "Specimen":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Specimen":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
