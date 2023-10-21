"""
Generated class for SubstanceSpecification. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Moiety(BaseModel):
    """Moiety, for structural modifications.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Role that the moiety is playing
    :param Identifier identifier: Identifier by which this moiety substance is known
    :param str name: Textual name for this moiety substance
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula
    :param Quantity amountQuantity: Quantitative value for this moiety
    :param str amountString: Quantitative value for this moiety
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "stereochemistry": {"class_name": "CodeableConcept", "is_contained": False},
        "opticalActivity": {"class_name": "CodeableConcept", "is_contained": False},
        "amountQuantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        role: "CodeableConcept" = None,
        identifier: "Identifier" = None,
        name: "str" = None,
        stereochemistry: "CodeableConcept" = None,
        opticalActivity: "CodeableConcept" = None,
        molecularFormula: "str" = None,
        amountQuantity: "Quantity" = None,
        amountString: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role
        self.identifier = identifier
        self.name = name
        self.stereochemistry = stereochemistry
        self.opticalActivity = opticalActivity
        self.molecularFormula = molecularFormula
        self.amountQuantity = amountQuantity
        self.amountString = amountString

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Property(BaseModel):
    """General specifications for this substance, including how it is related to other substances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: A category for this property, e.g. Physical, Chemical, Enzymatic
    :param CodeableConcept code: Property type e.g. viscosity, pH, isoelectric point
    :param str parameters: Parameters that were used in the measurement of a property (e.g. for viscosity: measured at 20C with a pH of 7.1)
    :param Reference definingSubstanceReference: A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol)
    :param CodeableConcept definingSubstanceCodeableConcept: A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol)
    :param Quantity amountQuantity: Quantitative value for this property
    :param str amountString: Quantitative value for this property
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "definingSubstanceReference": {
            "class_name": "Reference",
            "is_contained": False,
        },
        "definingSubstanceCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "amountQuantity": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        category: "CodeableConcept" = None,
        code: "CodeableConcept" = None,
        parameters: "str" = None,
        definingSubstanceReference: "Reference" = None,
        definingSubstanceCodeableConcept: "CodeableConcept" = None,
        amountQuantity: "Quantity" = None,
        amountString: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category
        self.code = code
        self.parameters = parameters
        self.definingSubstanceReference = definingSubstanceReference
        self.definingSubstanceCodeableConcept = definingSubstanceCodeableConcept
        self.amountQuantity = amountQuantity
        self.amountString = amountString

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MolecularWeight(BaseModel):
    """The molecular weight or weight range (for proteins, polymers or nucleic acids).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept method: The method by which the molecular weight was determined
    :param CodeableConcept type: Type of molecular weight such as exact, average (also known as. number average), weight average
    :param Quantity amount: Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "amount": {"class_name": "Quantity", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        method: "CodeableConcept" = None,
        type: "CodeableConcept" = None,
        amount: "Quantity" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.method = method
        self.type = type
        self.amount = amount

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Isotope(BaseModel):
    """Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Substance identifier for each non-natural or radioisotope
    :param CodeableConcept name: Substance name for each non-natural or radioisotope
    :param CodeableConcept substitution: The type of isotopic substitution present in a single substance
    :param Quantity halfLife: Half life - for a non-natural nuclide
    :param MolecularWeight molecularWeight: The molecular weight or weight range (for proteins, polymers or nucleic acids)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "name": {"class_name": "CodeableConcept", "is_contained": False},
        "substitution": {"class_name": "CodeableConcept", "is_contained": False},
        "halfLife": {"class_name": "Quantity", "is_contained": False},
        "molecularWeight": {"class_name": "MolecularWeight", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "Identifier" = None,
        name: "CodeableConcept" = None,
        substitution: "CodeableConcept" = None,
        halfLife: "Quantity" = None,
        molecularWeight: "MolecularWeight" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.name = name
        self.substitution = substitution
        self.halfLife = halfLife
        self.molecularWeight = molecularWeight

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Representation(BaseModel):
    """Molecular structural representation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of structure (e.g. Full, Partial, Representative)
    :param str representation: The structural representation as text string in a format e.g. InChI, SMILES, MOLFILE, CDX
    :param Attachment attachment: An attached file with the structural representation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "attachment": {"class_name": "Attachment", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "CodeableConcept" = None,
        representation: "str" = None,
        attachment: "Attachment" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.representation = representation
        self.attachment = attachment

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Structure(BaseModel):
    """Structural information.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula
    :param str molecularFormulaByMoiety: Specified per moiety according to the Hill system, i.e. first C, then H, then alphabetical, each moiety separated by a dot
    :param Isotope isotope: Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio
    :param MolecularWeight molecularWeight: The molecular weight or weight range (for proteins, polymers or nucleic acids)
    :param Reference source: Supporting literature
    :param Representation representation: Molecular structural representation
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "stereochemistry": {"class_name": "CodeableConcept", "is_contained": False},
        "opticalActivity": {"class_name": "CodeableConcept", "is_contained": False},
        "isotope": {"class_name": "Isotope", "is_contained": True},
        "molecularWeight": {"class_name": "MolecularWeight", "is_contained": True},
        "source": {"class_name": "Reference", "is_contained": False},
        "representation": {"class_name": "Representation", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        stereochemistry: "CodeableConcept" = None,
        opticalActivity: "CodeableConcept" = None,
        molecularFormula: "str" = None,
        molecularFormulaByMoiety: "str" = None,
        isotope: list["Isotope"] = None,
        molecularWeight: "MolecularWeight" = None,
        source: list["Reference"] = None,
        representation: list["Representation"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.stereochemistry = stereochemistry
        self.opticalActivity = opticalActivity
        self.molecularFormula = molecularFormula
        self.molecularFormulaByMoiety = molecularFormulaByMoiety
        self.isotope = isotope or []
        self.molecularWeight = molecularWeight
        self.source = source or []
        self.representation = representation or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Code(BaseModel):
    """Codes associated with the substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The specific code
    :param CodeableConcept status: Status of the code assignment
    :param str statusDate: The date at which the code status is changed as part of the terminology maintenance
    :param str comment: Any comment can be provided in this field, if necessary
    :param Reference source: Supporting literature
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        code: "CodeableConcept" = None,
        status: "CodeableConcept" = None,
        statusDate: "str" = None,
        comment: "str" = None,
        source: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code
        self.status = status
        self.statusDate = statusDate
        self.comment = comment
        self.source = source or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Official(BaseModel):
    """Details of the official nature of this name.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept authority: Which authority uses this official name
    :param CodeableConcept status: The status of the official name
    :param str date: Date of official name change
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "authority": {"class_name": "CodeableConcept", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        authority: "CodeableConcept" = None,
        status: "CodeableConcept" = None,
        date: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.authority = authority
        self.status = status
        self.date = date

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Name(BaseModel):
    """Names applicable to this substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The actual name
    :param CodeableConcept type: Name type
    :param CodeableConcept status: The status of the name
    :param bool preferred: If this is the preferred name for this substance
    :param CodeableConcept language: Language of the name
    :param CodeableConcept domain: The use context of this name for example if there is a different name a drug active ingredient as opposed to a food colour additive
    :param CodeableConcept jurisdiction: The jurisdiction where this name applies
    :param Synonym synonym: A synonym of this name
    :param Translation translation: A translation for this name
    :param Official official: Details of the official nature of this name
    :param Reference source: Supporting literature
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        "domain": {"class_name": "CodeableConcept", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "synonym": {"class_name": "Synonym", "is_contained": True},
        "translation": {"class_name": "Translation", "is_contained": True},
        "official": {"class_name": "Official", "is_contained": True},
        "source": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        type: "CodeableConcept" = None,
        status: "CodeableConcept" = None,
        preferred: "bool" = None,
        language: list["CodeableConcept"] = None,
        domain: list["CodeableConcept"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        synonym: list["Synonym"] = None,
        translation: list["Translation"] = None,
        official: list["Official"] = None,
        source: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.type = type
        self.status = status
        self.preferred = preferred
        self.language = language or []
        self.domain = domain or []
        self.jurisdiction = jurisdiction or []
        self.synonym = synonym or []
        self.translation = translation or []
        self.official = official or []
        self.source = source or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Relationship(BaseModel):
    """A link between this substance and another, with details of the relationship.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference substanceReference: A pointer to another substance, as a resource or just a representational code
    :param CodeableConcept substanceCodeableConcept: A pointer to another substance, as a resource or just a representational code
    :param CodeableConcept relationship: For example "salt to parent", "active moiety", "starting material"
    :param bool isDefining: For example where an enzyme strongly bonds with a particular substance, this is a defining relationship for that enzyme, out of several possible substance relationships
    :param Quantity amountQuantity: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param Range amountRange: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param Ratio amountRatio: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param str amountString: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param Ratio amountRatioLowLimit: For use when the numeric
    :param CodeableConcept amountType: An operator for the amount, for example "average", "approximately", "less than"
    :param Reference source: Supporting literature
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "substanceReference": {"class_name": "Reference", "is_contained": False},
        "substanceCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "relationship": {"class_name": "CodeableConcept", "is_contained": False},
        "amountQuantity": {"class_name": "Quantity", "is_contained": False},
        "amountRange": {"class_name": "Range", "is_contained": False},
        "amountRatio": {"class_name": "Ratio", "is_contained": False},
        "amountRatioLowLimit": {"class_name": "Ratio", "is_contained": False},
        "amountType": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        substanceReference: "Reference" = None,
        substanceCodeableConcept: "CodeableConcept" = None,
        relationship: "CodeableConcept" = None,
        isDefining: "bool" = None,
        amountQuantity: "Quantity" = None,
        amountRange: "Range" = None,
        amountRatio: "Ratio" = None,
        amountString: "str" = None,
        amountRatioLowLimit: "Ratio" = None,
        amountType: "CodeableConcept" = None,
        source: list["Reference"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.substanceReference = substanceReference
        self.substanceCodeableConcept = substanceCodeableConcept
        self.relationship = relationship
        self.isDefining = isDefining
        self.amountQuantity = amountQuantity
        self.amountRange = amountRange
        self.amountRatio = amountRatio
        self.amountString = amountString
        self.amountRatioLowLimit = amountRatioLowLimit
        self.amountType = amountType
        self.source = source or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstanceSpecification(DomainResource):
    """The detailed description of a substance, typically at a level beyond what is used for prescribing.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier by which this substance is known
    :param CodeableConcept type: High level categorization, e.g. polymer or nucleic acid
    :param CodeableConcept status: Status of substance within the catalogue e.g. approved
    :param CodeableConcept domain: If the substance applies to only human or veterinary use
    :param str description: Textual description of the substance
    :param Reference source: Supporting literature
    :param str comment: Textual comment about this record of a substance
    :param Moiety moiety: Moiety, for structural modifications
    :param Property property: General specifications for this substance, including how it is related to other substances
    :param Reference referenceInformation: General information detailing this substance
    :param Structure structure: Structural information
    :param Code code: Codes associated with the substance
    :param Name name: Names applicable to this substance
    :param MolecularWeight molecularWeight: The molecular weight or weight range (for proteins, polymers or nucleic acids)
    :param Relationship relationship: A link between this substance and another, with details of the relationship
    :param Reference nucleicAcid: Data items specific to nucleic acids
    :param Reference polymer: Data items specific to polymers
    :param Reference protein: Data items specific to proteins
    :param Reference sourceMaterial: Material or taxonomic/anatomical source for the substance
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
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        "domain": {"class_name": "CodeableConcept", "is_contained": False},
        "source": {"class_name": "Reference", "is_contained": False},
        "moiety": {"class_name": "Moiety", "is_contained": True},
        "property": {"class_name": "Property", "is_contained": True},
        "referenceInformation": {"class_name": "Reference", "is_contained": False},
        "structure": {"class_name": "Structure", "is_contained": True},
        "code": {"class_name": "Code", "is_contained": True},
        "name": {"class_name": "Name", "is_contained": True},
        "molecularWeight": {"class_name": "MolecularWeight", "is_contained": True},
        "relationship": {"class_name": "Relationship", "is_contained": True},
        "nucleicAcid": {"class_name": "Reference", "is_contained": False},
        "polymer": {"class_name": "Reference", "is_contained": False},
        "protein": {"class_name": "Reference", "is_contained": False},
        "sourceMaterial": {"class_name": "Reference", "is_contained": False},
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
        type: "CodeableConcept" = None,
        status: "CodeableConcept" = None,
        domain: "CodeableConcept" = None,
        description: "str" = None,
        source: list["Reference"] = None,
        comment: "str" = None,
        moiety: list["Moiety"] = None,
        property: list["Property"] = None,
        referenceInformation: "Reference" = None,
        structure: "Structure" = None,
        code: list["Code"] = None,
        name: list["Name"] = None,
        molecularWeight: list["MolecularWeight"] = None,
        relationship: list["Relationship"] = None,
        nucleicAcid: "Reference" = None,
        polymer: "Reference" = None,
        protein: "Reference" = None,
        sourceMaterial: "Reference" = None,
    ):
        self.resourceType = resourceType or "SubstanceSpecification"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.type = type
        self.status = status
        self.domain = domain
        self.description = description
        self.source = source or []
        self.comment = comment
        self.moiety = moiety or []
        self.property = property or []
        self.referenceInformation = referenceInformation
        self.structure = structure
        self.code = code or []
        self.name = name or []
        self.molecularWeight = molecularWeight or []
        self.relationship = relationship or []
        self.nucleicAcid = nucleicAcid
        self.polymer = polymer
        self.protein = protein
        self.sourceMaterial = sourceMaterial

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceSpecification":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
