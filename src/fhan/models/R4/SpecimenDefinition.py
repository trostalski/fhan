"""
Generated class for SpecimenDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Additive(BaseModel):
    """Substance introduced in the kind of container to preserve, maintain or enhance the specimen. Examples: Formalin, Citrate, EDTA.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveReference: Additive associated with container
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
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
        additiveCodeableConcept: "CodeableConcept" = None,
        additiveReference: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.additiveCodeableConcept = additiveCodeableConcept
        self.additiveReference = additiveReference

    @classmethod
    def from_dict(cls, data: dict) -> "SpecimenDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SpecimenDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Container(BaseModel):
    """The specimen's container.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Container material
    :param CodeableConcept type: Kind of container associated with the kind of specimen
    :param CodeableConcept cap: Color of container cap
    :param str description: Container description
    :param Quantity capacity: Container capacity
    :param Quantity minimumVolumeQuantity: Minimum volume
    :param str minimumVolumeString: Minimum volume
    :param Additive additive: Additive associated with container
    :param str preparation: Specimen container preparation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "material": {"class_name": "CodeableConcept", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "cap": {"class_name": "CodeableConcept", "is_contained": False},
        "capacity": {"class_name": "Quantity", "is_contained": False},
        "minimumVolumeQuantity": {"class_name": "Quantity", "is_contained": False},
        "additive": {"class_name": "Additive", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        material: "CodeableConcept" = None,
        type: "CodeableConcept" = None,
        cap: "CodeableConcept" = None,
        description: "str" = None,
        capacity: "Quantity" = None,
        minimumVolumeQuantity: "Quantity" = None,
        minimumVolumeString: "str" = None,
        additive: list["Additive"] = None,
        preparation: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.material = material
        self.type = type
        self.cap = cap
        self.description = description
        self.capacity = capacity
        self.minimumVolumeQuantity = minimumVolumeQuantity
        self.minimumVolumeString = minimumVolumeString
        self.additive = additive or []
        self.preparation = preparation

    @classmethod
    def from_dict(cls, data: dict) -> "SpecimenDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SpecimenDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Handling(BaseModel):
    """Set of instructions for preservation/transport of the specimen at a defined temperature interval, prior the testing process.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept temperatureQualifier: Temperature qualifier
    :param Range temperatureRange: Temperature range
    :param Duration maxDuration: Maximum preservation time
    :param str instruction: Preservation instruction
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "temperatureQualifier": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "temperatureRange": {"class_name": "Range", "is_contained": False},
        "maxDuration": {"class_name": "Duration", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        temperatureQualifier: "CodeableConcept" = None,
        temperatureRange: "Range" = None,
        maxDuration: "Duration" = None,
        instruction: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.temperatureQualifier = temperatureQualifier
        self.temperatureRange = temperatureRange
        self.maxDuration = maxDuration
        self.instruction = instruction

    @classmethod
    def from_dict(cls, data: dict) -> "SpecimenDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SpecimenDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class TypeTested(BaseModel):
    """Specimen conditioned in a container as expected by the testing laboratory.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool isDerived: Primary or secondary specimen
    :param CodeableConcept type: Type of intended specimen
    :param str preference: preferred | alternate
    :param Container container: The specimen's container
    :param str requirement: Specimen requirements
    :param Duration retentionTime: Specimen retention time
    :param CodeableConcept rejectionCriterion: Rejection criterion
    :param Handling handling: Specimen handling before testing
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "container": {"class_name": "Container", "is_contained": True},
        "retentionTime": {"class_name": "Duration", "is_contained": False},
        "rejectionCriterion": {"class_name": "CodeableConcept", "is_contained": False},
        "handling": {"class_name": "Handling", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        isDerived: "bool" = None,
        type: "CodeableConcept" = None,
        preference: "str" = None,
        container: "Container" = None,
        requirement: "str" = None,
        retentionTime: "Duration" = None,
        rejectionCriterion: list["CodeableConcept"] = None,
        handling: list["Handling"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.isDerived = isDerived
        self.type = type
        self.preference = preference
        self.container = container
        self.requirement = requirement
        self.retentionTime = retentionTime
        self.rejectionCriterion = rejectionCriterion or []
        self.handling = handling or []

    @classmethod
    def from_dict(cls, data: dict) -> "SpecimenDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SpecimenDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SpecimenDefinition(DomainResource):
    """A kind of specimen with associated set of requirements.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier of a kind of specimen
    :param CodeableConcept typeCollected: Kind of material to collect
    :param CodeableConcept patientPreparation: Patient preparation for collection
    :param str timeAspect: Time aspect for collection
    :param CodeableConcept collection: Specimen collection procedure
    :param TypeTested typeTested: Specimen in container intended for testing by lab
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "typeCollected": {"class_name": "CodeableConcept", "is_contained": False},
        "patientPreparation": {"class_name": "CodeableConcept", "is_contained": False},
        "collection": {"class_name": "CodeableConcept", "is_contained": False},
        "typeTested": {"class_name": "TypeTested", "is_contained": True},
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
        identifier: "Identifier" = None,
        typeCollected: "CodeableConcept" = None,
        patientPreparation: list["CodeableConcept"] = None,
        timeAspect: "str" = None,
        collection: list["CodeableConcept"] = None,
        typeTested: list["TypeTested"] = None,
    ):
        self.resourceType = resourceType or "SpecimenDefinition"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.typeCollected = typeCollected
        self.patientPreparation = patientPreparation or []
        self.timeAspect = timeAspect
        self.collection = collection or []
        self.typeTested = typeTested or []

    @classmethod
    def from_dict(cls, data: dict) -> "SpecimenDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SpecimenDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
