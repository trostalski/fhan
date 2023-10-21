"""
Generated class for MolecularSequence. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class ReferenceSeq(BaseModel):
    """A sequence that is used as a reference to describe variants that are present in a sequence analyzed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept chromosome: Chromosome containing genetic finding
    :param str genomeBuild: The Genome Build used for reference, following GRCh build versions e.g. 'GRCh 37'
    :param str orientation: sense | antisense
    :param CodeableConcept referenceSeqId: Reference identifier
    :param Reference referenceSeqPointer: A pointer to another MolecularSequence entity as reference sequence
    :param str referenceSeqString: A string to represent reference sequence
    :param str strand: watson | crick
    :param int windowStart: Start position of the window on the  reference sequence
    :param int windowEnd: End position of the window on the reference sequence
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "chromosome": {"class_name": "CodeableConcept", "is_contained": False},
        "referenceSeqId": {"class_name": "CodeableConcept", "is_contained": False},
        "referenceSeqPointer": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        chromosome: "CodeableConcept" = None,
        genomeBuild: "str" = None,
        orientation: "str" = None,
        referenceSeqId: "CodeableConcept" = None,
        referenceSeqPointer: "Reference" = None,
        referenceSeqString: "str" = None,
        strand: "str" = None,
        windowStart: "int" = None,
        windowEnd: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.chromosome = chromosome
        self.genomeBuild = genomeBuild
        self.orientation = orientation
        self.referenceSeqId = referenceSeqId
        self.referenceSeqPointer = referenceSeqPointer
        self.referenceSeqString = referenceSeqString
        self.strand = strand
        self.windowStart = windowStart
        self.windowEnd = windowEnd

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Variant(BaseModel):
    """The definition of variant here originates from Sequence ontology ([variant_of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)). This element can represent amino acid or nucleic sequence change(including insertion,deletion,SNP,etc.)  It can represent some complex mutation or segment variation with the assist of CIGAR string.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Start position of the variant on the  reference sequence
    :param int end: End position of the variant on the reference sequence
    :param str observedAllele: Allele that was observed
    :param str referenceAllele: Allele in the reference sequence
    :param str cigar: Extended CIGAR string for aligning the sequence with reference bases
    :param Reference variantPointer: Pointer to observed variant information
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "variantPointer": {"class_name": "Reference", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        start: "int" = None,
        end: "int" = None,
        observedAllele: "str" = None,
        referenceAllele: "str" = None,
        cigar: "str" = None,
        variantPointer: "Reference" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.start = start
        self.end = end
        self.observedAllele = observedAllele
        self.referenceAllele = referenceAllele
        self.cigar = cigar
        self.variantPointer = variantPointer

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Roc(BaseModel):
    """Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity tradeoff.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int score: Genotype quality score
    :param int numTP: Roc score true positive numbers
    :param int numFP: Roc score false positive numbers
    :param int numFN: Roc score false negative numbers
    :param float precision: Precision of the GQ score
    :param float sensitivity: Sensitivity of the GQ score
    :param float fMeasure: FScore of the GQ score
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        score: list["int"] = None,
        numTP: list["int"] = None,
        numFP: list["int"] = None,
        numFN: list["int"] = None,
        precision: list["float"] = None,
        sensitivity: list["float"] = None,
        fMeasure: list["float"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.score = score or []
        self.numTP = numTP or []
        self.numFP = numFP or []
        self.numFN = numFN or []
        self.precision = precision or []
        self.sensitivity = sensitivity or []
        self.fMeasure = fMeasure or []

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Quality(BaseModel):
    """An experimental feature attribute that defines the quality of the feature in a quantitative way, such as a phred quality score ([SO:0001686](http://www.sequenceontology.org/browser/current_svn/term/SO:0001686)).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: indel | snp | unknown
    :param CodeableConcept standardSequence: Standard sequence for comparison
    :param int start: Start position of the sequence
    :param int end: End position of the sequence
    :param Quantity score: Quality score for the comparison
    :param CodeableConcept method: Method to get quality
    :param float truthTP: True positives from the perspective of the truth data
    :param float queryTP: True positives from the perspective of the query data
    :param float truthFN: False negatives
    :param float queryFP: False positives
    :param float gtFP: False positives where the non-REF alleles in the Truth and Query Call Sets match
    :param float precision: Precision of comparison
    :param float recall: Recall of comparison
    :param float fScore: F-score
    :param Roc roc: Receiver Operator Characteristic (ROC) Curve
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "standardSequence": {"class_name": "CodeableConcept", "is_contained": False},
        "score": {"class_name": "Quantity", "is_contained": False},
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        "roc": {"class_name": "Roc", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        standardSequence: "CodeableConcept" = None,
        start: "int" = None,
        end: "int" = None,
        score: "Quantity" = None,
        method: "CodeableConcept" = None,
        truthTP: "float" = None,
        queryTP: "float" = None,
        truthFN: "float" = None,
        queryFP: "float" = None,
        gtFP: "float" = None,
        precision: "float" = None,
        recall: "float" = None,
        fScore: "float" = None,
        roc: "Roc" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.standardSequence = standardSequence
        self.start = start
        self.end = end
        self.score = score
        self.method = method
        self.truthTP = truthTP
        self.queryTP = queryTP
        self.truthFN = truthFN
        self.queryFP = queryFP
        self.gtFP = gtFP
        self.precision = precision
        self.recall = recall
        self.fScore = fScore
        self.roc = roc

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Repository(BaseModel):
    """Configurations of the external repository. The repository shall store target's observedSeq or records related with target's observedSeq.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: directlink | openapi | login | oauth | other
    :param str url: URI of the repository
    :param str name: Repository's name
    :param str datasetId: Id of the dataset that used to call for dataset in repository
    :param str variantsetId: Id of the variantset that used to call for variantset in repository
    :param str readsetId: Id of the read
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        type: "str" = None,
        url: "str" = None,
        name: "str" = None,
        datasetId: "str" = None,
        variantsetId: "str" = None,
        readsetId: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.url = url
        self.name = name
        self.datasetId = datasetId
        self.variantsetId = variantsetId
        self.readsetId = readsetId

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Outer(BaseModel):
    """Structural variant outer.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant outer start
    :param int end: Structural variant outer end
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        start: "int" = None,
        end: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.start = start
        self.end = end

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Inner(BaseModel):
    """Structural variant inner.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant inner start
    :param int end: Structural variant inner end
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        start: "int" = None,
        end: "int" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.start = start
        self.end = end

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class StructureVariant(BaseModel):
    """Information about chromosome structure variation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept variantType: Structural variant change type
    :param bool exact: Does the structural variant have base pair resolution breakpoints?
    :param int length: Structural variant length
    :param Outer outer: Structural variant outer
    :param Inner inner: Structural variant inner
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "variantType": {"class_name": "CodeableConcept", "is_contained": False},
        "outer": {"class_name": "Outer", "is_contained": True},
        "inner": {"class_name": "Inner", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        variantType: "CodeableConcept" = None,
        exact: "bool" = None,
        length: "int" = None,
        outer: "Outer" = None,
        inner: "Inner" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.variantType = variantType
        self.exact = exact
        self.length = length
        self.outer = outer
        self.inner = inner

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MolecularSequence(DomainResource):
    """Raw data describing a biological sequence.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique ID for this particular sequence. This is a FHIR-defined id
    :param str type: aa | dna | rna
    :param int coordinateSystem: Base number of coordinate system (0 for 0-based numbering or coordinates, inclusive start, exclusive end, 1 for 1-based numbering, inclusive start, inclusive end)
    :param Reference patient: Who and/or what this is about
    :param Reference specimen: Specimen used for sequencing
    :param Reference device: The method for sequencing
    :param Reference performer: Who should be responsible for test result
    :param Quantity quantity: The number of copies of the sequence of interest.  (RNASeq)
    :param ReferenceSeq referenceSeq: A sequence used as reference
    :param Variant variant: Variant in sequence
    :param str observedSeq: Sequence that was observed
    :param Quality quality: An set of value as quality of sequence
    :param int readCoverage: Average number of reads representing a given nucleotide in the reconstructed sequence
    :param Repository repository: External repository which contains detailed report related with observedSeq in this resource
    :param Reference pointer: Pointer to next atomic sequence
    :param StructureVariant structureVariant: Structural variant
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "patient": {"class_name": "Reference", "is_contained": False},
        "specimen": {"class_name": "Reference", "is_contained": False},
        "device": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "quantity": {"class_name": "Quantity", "is_contained": False},
        "referenceSeq": {"class_name": "ReferenceSeq", "is_contained": True},
        "variant": {"class_name": "Variant", "is_contained": True},
        "quality": {"class_name": "Quality", "is_contained": True},
        "repository": {"class_name": "Repository", "is_contained": True},
        "pointer": {"class_name": "Reference", "is_contained": False},
        "structureVariant": {"class_name": "StructureVariant", "is_contained": True},
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
        type: "str" = None,
        coordinateSystem: "int" = None,
        patient: "Reference" = None,
        specimen: "Reference" = None,
        device: "Reference" = None,
        performer: "Reference" = None,
        quantity: "Quantity" = None,
        referenceSeq: "ReferenceSeq" = None,
        variant: list["Variant"] = None,
        observedSeq: "str" = None,
        quality: list["Quality"] = None,
        readCoverage: "int" = None,
        repository: list["Repository"] = None,
        pointer: list["Reference"] = None,
        structureVariant: list["StructureVariant"] = None,
    ):
        self.resourceType = resourceType or "MolecularSequence"
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
        self.coordinateSystem = coordinateSystem
        self.patient = patient
        self.specimen = specimen
        self.device = device
        self.performer = performer
        self.quantity = quantity
        self.referenceSeq = referenceSeq
        self.variant = variant or []
        self.observedSeq = observedSeq
        self.quality = quality or []
        self.readCoverage = readCoverage
        self.repository = repository or []
        self.pointer = pointer or []
        self.structureVariant = structureVariant or []

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
