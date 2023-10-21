"""
Generated class for SubstanceNucleicAcid. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Linkage(BaseModel):
    """The linkages between sugar residues will also be captured.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str connectivity: The entity that links the sugar residues together should also be captured for nearly all naturally occurring nucleic acid the linkage is a phosphate group. For many synthetic oligonucleotides phosphorothioate linkages are often seen. Linkage connectivity is assumed to be 3’-5’. If the linkage is either 3’-3’ or 5’-5’ this should be specified
    :param Identifier identifier: Each linkage will be registered as a fragment and have an ID
    :param str name: Each linkage will be registered as a fragment and have at least one name. A single name shall be assigned to each linkage
    :param str residueSite: Residues shall be captured as described in 5.3.6.8.3
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        connectivity: "str" = None,
        identifier: "Identifier" = None,
        name: "str" = None,
        residueSite: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.connectivity = connectivity
        self.identifier = identifier
        self.name = name
        self.residueSite = residueSite

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceNucleicAcid":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceNucleicAcid":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Sugar(BaseModel):
    """5.3.6.8.1 Sugar ID (Mandatory).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: The Substance ID of the sugar or sugar-like component that make up the nucleotide
    :param str name: The name of the sugar or sugar-like component that make up the nucleotide
    :param str residueSite: The residues that contain a given sugar will be captured. The order of given residues will be captured in the 5‘-3‘direction consistent with the base sequences listed above
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: "Identifier" = None,
        name: "str" = None,
        residueSite: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.name = name
        self.residueSite = residueSite

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceNucleicAcid":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceNucleicAcid":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Subunit(BaseModel):
    """Subunits are listed in order of decreasing length; sequences of the same length will be ordered by molecular weight; subunits that have identical sequences will be repeated multiple times.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int subunit: Index of linear sequences of nucleic acids in order of decreasing length. Sequences of the same length will be ordered by molecular weight. Subunits that have identical sequences will be repeated and have sequential subscripts
    :param str sequence: Actual nucleotide sequence notation from 5' to 3' end using standard single letter codes. In addition to the base sequence, sugar and type of phosphate or non-phosphate linkage should also be captured
    :param int length: The length of the sequence shall be captured
    :param Attachment sequenceAttachment: (TBC)
    :param CodeableConcept fivePrime: The nucleotide present at the 5’ terminal shall be specified based on a controlled vocabulary. Since the sequence is represented from the 5' to the 3' end, the 5’ prime nucleotide is the letter at the first position in the sequence. A separate representation would be redundant
    :param CodeableConcept threePrime: The nucleotide present at the 3’ terminal shall be specified based on a controlled vocabulary. Since the sequence is represented from the 5' to the 3' end, the 5’ prime nucleotide is the letter at the last position in the sequence. A separate representation would be redundant
    :param Linkage linkage: The linkages between sugar residues will also be captured
    :param Sugar sugar: 5.3.6.8.1 Sugar ID (Mandatory)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "sequenceAttachment": {"class_name": "Attachment", "is_contained": False},
        "fivePrime": {"class_name": "CodeableConcept", "is_contained": False},
        "threePrime": {"class_name": "CodeableConcept", "is_contained": False},
        "linkage": {"class_name": "Linkage", "is_contained": True},
        "sugar": {"class_name": "Sugar", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        subunit: "int" = None,
        sequence: "str" = None,
        length: "int" = None,
        sequenceAttachment: "Attachment" = None,
        fivePrime: "CodeableConcept" = None,
        threePrime: "CodeableConcept" = None,
        linkage: list["Linkage"] = None,
        sugar: list["Sugar"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.subunit = subunit
        self.sequence = sequence
        self.length = length
        self.sequenceAttachment = sequenceAttachment
        self.fivePrime = fivePrime
        self.threePrime = threePrime
        self.linkage = linkage or []
        self.sugar = sugar or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceNucleicAcid":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceNucleicAcid":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstanceNucleicAcid(DomainResource):
    """Nucleic acids are defined by three distinct elements: the base, sugar and linkage. Individual substance/moiety IDs will be created for each of these elements. The nucleotide sequence will be always entered in the 5’-3’ direction.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept sequenceType: The type of the sequence shall be specified based on a controlled vocabulary
    :param int numberOfSubunits: The number of linear sequences of nucleotides linked through phosphodiester bonds shall be described. Subunits would be strands of nucleic acids that are tightly associated typically through Watson-Crick base pairing. NOTE: If not specified in the reference source, the assumption is that there is 1 subunit
    :param str areaOfHybridisation: The area of hybridisation shall be described if applicable for double stranded RNA or DNA. The number associated with the subunit followed by the number associated to the residue shall be specified in increasing order. The underscore “” shall be used as separator as follows: “Subunitnumber Residue”
    :param CodeableConcept oligoNucleotideType: (TBC)
    :param Subunit subunit: Subunits are listed in order of decreasing length; sequences of the same length will be ordered by molecular weight; subunits that have identical sequences will be repeated multiple times
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "sequenceType": {"class_name": "CodeableConcept", "is_contained": False},
        "oligoNucleotideType": {"class_name": "CodeableConcept", "is_contained": False},
        "subunit": {"class_name": "Subunit", "is_contained": True},
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
        sequenceType: "CodeableConcept" = None,
        numberOfSubunits: "int" = None,
        areaOfHybridisation: "str" = None,
        oligoNucleotideType: "CodeableConcept" = None,
        subunit: list["Subunit"] = None,
    ):
        self.resourceType = resourceType or "SubstanceNucleicAcid"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequenceType = sequenceType
        self.numberOfSubunits = numberOfSubunits
        self.areaOfHybridisation = areaOfHybridisation
        self.oligoNucleotideType = oligoNucleotideType
        self.subunit = subunit or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceNucleicAcid":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceNucleicAcid":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
