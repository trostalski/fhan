"""
Generated class for SubstanceProtein. 
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


class Subunit(BaseModel):
    """This subclause refers to the description of each subunit constituting the SubstanceProtein. A subunit is a linear sequence of amino acids linked through peptide bonds. The Subunit information shall be provided when the finished SubstanceProtein is a complex of multiple sequences; subunits are not used to delineate domains within a single sequence. Subunits are listed in order of decreasing length; sequences of the same length will be ordered by decreasing molecular weight; subunits that have identical sequences will be repeated multiple times.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int subunit: Index of primary sequences of amino acids linked through peptide bonds in order of decreasing length. Sequences of the same length will be ordered by molecular weight. Subunits that have identical sequences will be repeated and have sequential subscripts
    :param str sequence: The sequence information shall be provided enumerating the amino acids from N- to C-terminal end using standard single-letter amino acid codes. Uppercase shall be used for L-amino acids and lowercase for D-amino acids. Transcribed SubstanceProteins will always be described using the translated sequence; for synthetic peptide containing amino acids that are not represented with a single letter code an X should be used within the sequence. The modified amino acids will be distinguished by their position in the sequence
    :param int length: Length of linear sequences of amino acids contained in the subunit
    :param Attachment sequenceAttachment: The sequence information shall be provided enumerating the amino acids from N- to C-terminal end using standard single-letter amino acid codes. Uppercase shall be used for L-amino acids and lowercase for D-amino acids. Transcribed SubstanceProteins will always be described using the translated sequence; for synthetic peptide containing amino acids that are not represented with a single letter code an X should be used within the sequence. The modified amino acids will be distinguished by their position in the sequence
    :param Identifier nTerminalModificationId: Unique identifier for molecular fragment modification based on the ISO 11238 Substance ID
    :param str nTerminalModification: The name of the fragment modified at the N-terminal of the SubstanceProtein shall be specified
    :param Identifier cTerminalModificationId: Unique identifier for molecular fragment modification based on the ISO 11238 Substance ID
    :param str cTerminalModification: The modification at the C-terminal shall be specified
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "sequenceAttachment": {"class_name": "Attachment", "is_contained": False},
        "nTerminalModificationId": {"class_name": "Identifier", "is_contained": False},
        "cTerminalModificationId": {"class_name": "Identifier", "is_contained": False},
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
        nTerminalModificationId: "Identifier" = None,
        nTerminalModification: "str" = None,
        cTerminalModificationId: "Identifier" = None,
        cTerminalModification: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.subunit = subunit
        self.sequence = sequence
        self.length = length
        self.sequenceAttachment = sequenceAttachment
        self.nTerminalModificationId = nTerminalModificationId
        self.nTerminalModification = nTerminalModification
        self.cTerminalModificationId = cTerminalModificationId
        self.cTerminalModification = cTerminalModification

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceProtein":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceProtein":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstanceProtein(DomainResource):
    """A SubstanceProtein is defined as a single unit of a linear amino acid sequence, or a combination of subunits that are either covalently linked or have a defined invariant stoichiometric relationship. This includes all synthetic, recombinant and purified SubstanceProteins of defined sequence, whether the use is therapeutic or prophylactic. This set of elements will be used to describe albumins, coagulation factors, cytokines, growth factors, peptide/SubstanceProtein hormones, enzymes, toxins, toxoids, recombinant vaccines, and immunomodulators.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept sequenceType: The SubstanceProtein descriptive elements will only be used when a complete or partial amino acid sequence is available or derivable from a nucleic acid sequence
    :param int numberOfSubunits: Number of linear sequences of amino acids linked through peptide bonds. The number of subunits constituting the SubstanceProtein shall be described. It is possible that the number of subunits can be variable
    :param str disulfideLinkage: The disulphide bond between two cysteine residues either on the same subunit or on two different subunits shall be described. The position of the disulfide bonds in the SubstanceProtein shall be listed in increasing order of subunit number and position within subunit followed by the abbreviation of the amino acids involved. The disulfide linkage positions shall actually contain the amino acid Cysteine at the respective positions
    :param Subunit subunit: This subclause refers to the description of each subunit constituting the SubstanceProtein. A subunit is a linear sequence of amino acids linked through peptide bonds. The Subunit information shall be provided when the finished SubstanceProtein is a complex of multiple sequences; subunits are not used to delineate domains within a single sequence. Subunits are listed in order of decreasing length; sequences of the same length will be ordered by decreasing molecular weight; subunits that have identical sequences will be repeated multiple times
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "sequenceType": {"class_name": "CodeableConcept", "is_contained": False},
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
        disulfideLinkage: list["str"] = None,
        subunit: list["Subunit"] = None,
    ):
        self.resourceType = resourceType or "SubstanceProtein"
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
        self.disulfideLinkage = disulfideLinkage or []
        self.subunit = subunit or []

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceProtein":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "SubstanceProtein":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
