"""
Generated class for ImagingStudy. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Coding import *
from fhan.models.R4.DomainResource import *


class Performer(BaseModel):
    """Indicates who or what performed the series and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the series
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        function: "CodeableConcept" = None,
        actor: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function
        self.actor = actor

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingStudy":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImagingStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Instance(BaseModel):
    """A single SOP instance within the series, e.g. an image, or presentation state.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM SOP Instance UID
    :param Coding sopClass: DICOM class type
    :param int number: The number of this instance in the series
    :param str title: Description of instance
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "sopClass": {"class_name": "Coding", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        uid: "str" = None,
        sopClass: "Coding" = None,
        number: "int" = None,
        title: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.uid = uid
        self.sopClass = sopClass
        self.number = number
        self.title = title

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingStudy":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImagingStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Series(BaseModel):
    """Each study has one or more series of images or other content.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM Series Instance UID for the series
    :param int number: Numeric identifier of this series
    :param Coding modality: The modality of the instances in the series
    :param str description: A short human readable summary of the series
    :param int numberOfInstances: Number of Series Related Instances
    :param Reference endpoint: Series access endpoint
    :param Coding bodySite: Body part examined
    :param Coding laterality: Body part laterality
    :param Reference specimen: Specimen imaged
    :param str started: When the series started
    :param Performer performer: Who performed the series
    :param Instance instance: A single SOP instance from the series
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "modality": {"class_name": "Coding", "is_contained": False},
        "endpoint": {"class_name": "Reference", "is_contained": False},
        "bodySite": {"class_name": "Coding", "is_contained": False},
        "laterality": {"class_name": "Coding", "is_contained": False},
        "specimen": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Performer", "is_contained": True},
        "instance": {"class_name": "Instance", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        uid: "str" = None,
        number: "int" = None,
        modality: "Coding" = None,
        description: "str" = None,
        numberOfInstances: "int" = None,
        endpoint: list["Reference"] = None,
        bodySite: "Coding" = None,
        laterality: "Coding" = None,
        specimen: list["Reference"] = None,
        started: "str" = None,
        performer: list["Performer"] = None,
        instance: list["Instance"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.uid = uid
        self.number = number
        self.modality = modality
        self.description = description
        self.numberOfInstances = numberOfInstances
        self.endpoint = endpoint or []
        self.bodySite = bodySite
        self.laterality = laterality
        self.specimen = specimen or []
        self.started = started
        self.performer = performer or []
        self.instance = instance or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingStudy":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImagingStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ImagingStudy(DomainResource):
    """Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers for the whole study
    :param str status: registered | available | cancelled | entered-in-error | unknown
    :param Coding modality: All series modality if actual acquisition modalities
    :param Reference subject: Who or what is the subject of the study
    :param Reference encounter: Encounter with which this imaging study is associated
    :param str started: When the study was started
    :param Reference basedOn: Request fulfilled
    :param Reference referrer: Referring physician
    :param Reference interpreter: Who interpreted images
    :param Reference endpoint: Study access endpoint
    :param int numberOfSeries: Number of Study Related Series
    :param int numberOfInstances: Number of Study Related Instances
    :param Reference procedureReference: The performed Procedure reference
    :param CodeableConcept procedureCode: The performed procedure code
    :param Reference location: Where ImagingStudy occurred
    :param CodeableConcept reasonCode: Why the study was requested
    :param Reference reasonReference: Why was study performed
    :param Annotation note: User-defined comments
    :param str description: Institution-generated description
    :param Series series: Each study has one or more series of instances
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "modality": {"class_name": "Coding", "is_contained": False},
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "basedOn": {"class_name": "Reference", "is_contained": False},
        "referrer": {"class_name": "Reference", "is_contained": False},
        "interpreter": {"class_name": "Reference", "is_contained": False},
        "endpoint": {"class_name": "Reference", "is_contained": False},
        "procedureReference": {"class_name": "Reference", "is_contained": False},
        "procedureCode": {"class_name": "CodeableConcept", "is_contained": False},
        "location": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "series": {"class_name": "Series", "is_contained": True},
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
        status: "str" = None,
        modality: list["Coding"] = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        started: "str" = None,
        basedOn: list["Reference"] = None,
        referrer: "Reference" = None,
        interpreter: list["Reference"] = None,
        endpoint: list["Reference"] = None,
        numberOfSeries: "int" = None,
        numberOfInstances: "int" = None,
        procedureReference: "Reference" = None,
        procedureCode: list["CodeableConcept"] = None,
        location: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        note: list["Annotation"] = None,
        description: "str" = None,
        series: list["Series"] = None,
    ):
        self.resourceType = resourceType or "ImagingStudy"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status
        self.modality = modality or []
        self.subject = subject
        self.encounter = encounter
        self.started = started
        self.basedOn = basedOn or []
        self.referrer = referrer
        self.interpreter = interpreter or []
        self.endpoint = endpoint or []
        self.numberOfSeries = numberOfSeries
        self.numberOfInstances = numberOfInstances
        self.procedureReference = procedureReference
        self.procedureCode = procedureCode or []
        self.location = location
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.note = note or []
        self.description = description
        self.series = series or []

    @classmethod
    def from_dict(cls, data: dict) -> "ImagingStudy":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ImagingStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
