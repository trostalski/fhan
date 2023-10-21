"""
Generated class for SubstanceReferenceInformation. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class GeneElement(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param Identifier element: Todo
    :param Reference source: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "element": {"class_name": "Identifier", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        element: "Identifier" = None,
        source: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.element = element
        self.source = source or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceReferenceInformation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceReferenceInformation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Gene(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept geneSequenceOrigin: Todo
    :param CodeableConcept gene: Todo
    :param Reference source: Todo
    :param GeneElement geneElement: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "geneSequenceOrigin": {"class_name": "CodeableConcept", "is_contained": False},
        "gene": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
        "geneElement": {"class_name": "GeneElement", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        geneSequenceOrigin: "CodeableConcept" = None,
        gene: "CodeableConcept" = None,
        source: list["Reference"] = None,
        geneElement: list["GeneElement"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.geneSequenceOrigin = geneSequenceOrigin
        self.gene = gene
        self.source = source or []
        self.geneElement = geneElement or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceReferenceInformation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceReferenceInformation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Classification(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept domain: Todo
    :param CodeableConcept classification: Todo
    :param CodeableConcept subtype: Todo
    :param Reference source: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "domain": {"class_name": "CodeableConcept", "is_contained": False},
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
        "subtype": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        domain: "CodeableConcept" = None,
        classification: "CodeableConcept" = None,
        subtype: list["CodeableConcept"] = None,
        source: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.domain = domain
        self.classification = classification
        self.subtype = subtype or []
        self.source = source or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceReferenceInformation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceReferenceInformation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Target(BaseModel):
    """Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier target: Todo
    :param CodeableConcept type: Todo
    :param CodeableConcept interaction: Todo
    :param CodeableConcept organism: Todo
    :param CodeableConcept organismType: Todo
    :param Quantity amountQuantity: Todo
    :param Range amountRange: Todo
    :param str amountString: Todo
    :param CodeableConcept amountType: Todo
    :param Reference source: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "target": {"class_name": "Identifier", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "interaction": {"class_name": "CodeableConcept", "is_contained": False},
        "organism": {"class_name": "CodeableConcept", "is_contained": False},
        "organismType": {"class_name": "CodeableConcept", "is_contained": False},
        "amountQuantity": {"class_name": "Quantity", "is_contained": False},
        "amountRange": {"class_name": "Range", "is_contained": False},
        "amountType": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        target: "Identifier" = None,
        type: "CodeableConcept" = None,
        interaction: "CodeableConcept" = None,
        organism: "CodeableConcept" = None,
        organismType: "CodeableConcept" = None,
        amountQuantity: "Quantity" = None,
        amountRange: "Range" = None,
        amountString: "str" = None,
        amountType: "CodeableConcept" = None,
        source: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.target = target
        self.type = type
        self.interaction = interaction
        self.organism = organism
        self.organismType = organismType
        self.amountQuantity = amountQuantity
        self.amountRange = amountRange
        self.amountString = amountString
        self.amountType = amountType
        self.source = source or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceReferenceInformation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceReferenceInformation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstanceReferenceInformation(DomainResource):
    """Todo.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str comment: Todo
    :param Gene gene: Todo
    :param Classification classification: Todo
    :param Target target: Todo
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "gene": {"class_name": "Gene", "is_contained": True},
        "classification": {"class_name": "Classification", "is_contained": True},
        "target": {"class_name": "Target", "is_contained": True},
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
        comment: "str" = None,
        gene: list["Gene"] = None,
        classification: list["Classification"] = None,
        target: list["Target"] = None,
    ):
        self.resourceType = resourceType or "SubstanceReferenceInformation"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.comment = comment
        self.gene = gene or []
        self.classification = classification or []
        self.target = target or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceReferenceInformation":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceReferenceInformation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
