"""
Generated class for MolecularSequence. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class referenceSeq(Element):
    """ A sequence that is used as a reference to describe variants that are present in a sequence analyzed.
    :param BackboneElement referenceSeq: A sequence used as reference
    :param str id: Unique id for inter-element referencing
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
    referenceSeq: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    chromosome: "CodeableConcept" = None
    
    genomeBuild: str = None
    
    orientation: str = None
    
    referenceSeqId: "CodeableConcept" = None
    
    referenceSeqPointer: "Reference" = None
    
    referenceSeqString: str = None
    
    strand: str = None
    
    windowStart: int = None
    
    windowEnd: int = None
    
@dataclass
class variant(Element):
    """ The definition of variant here originates from Sequence ontology ([variant_of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)). This element can represent amino acid or nucleic sequence change(including insertion,deletion,SNP,etc.)  It can represent some complex mutation or segment variation with the assist of CIGAR string.
    :param BackboneElement variant: Variant in sequence
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Start position of the variant on the  reference sequence
    :param int end: End position of the variant on the reference sequence
    :param str observedAllele: Allele that was observed
    :param str referenceAllele: Allele in the reference sequence
    :param str cigar: Extended CIGAR string for aligning the sequence with reference bases
    :param Reference variantPointer: Pointer to observed variant information
    """
    variant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    
    observedAllele: str = None
    
    referenceAllele: str = None
    
    cigar: str = None
    
    variantPointer: "Reference" = None
    
@dataclass
class quality(Element):
    """ An experimental feature attribute that defines the quality of the feature in a quantitative way, such as a phred quality score ([SO:0001686](http://www.sequenceontology.org/browser/current_svn/term/SO:0001686)).
    :param BackboneElement quality: An set of value as quality of sequence
    :param str id: Unique id for inter-element referencing
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
    :param BackboneElement roc: Receiver Operator Characteristic (ROC) Curve
    :param str id: Unique id for inter-element referencing
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
    quality: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    standardSequence: "CodeableConcept" = None
    
    start: int = None
    
    end: int = None
    
    score: "Quantity" = None
    
    method: "CodeableConcept" = None
    
    truthTP: float = None
    
    queryTP: float = None
    
    truthFN: float = None
    
    queryFP: float = None
    
    gtFP: float = None
    
    precision: float = None
    
    recall: float = None
    
    fScore: float = None
    
    roc: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    score: int = None
    
    numTP: int = None
    
    numFP: int = None
    
    numFN: int = None
    
    precision: float = None
    
    sensitivity: float = None
    
    fMeasure: float = None
    
@dataclass
class roc(Element):
    """ Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity tradeoff.
    :param BackboneElement roc: Receiver Operator Characteristic (ROC) Curve
    :param str id: Unique id for inter-element referencing
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
    roc: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    score: int = None
    
    numTP: int = None
    
    numFP: int = None
    
    numFN: int = None
    
    precision: float = None
    
    sensitivity: float = None
    
    fMeasure: float = None
    
@dataclass
class repository(Element):
    """ Configurations of the external repository. The repository shall store target's observedSeq or records related with target's observedSeq.
    :param BackboneElement repository: External repository which contains detailed report related with observedSeq in this resource
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: directlink | openapi | login | oauth | other
    :param str url: URI of the repository
    :param str name: Repository's name
    :param str datasetId: Id of the dataset that used to call for dataset in repository
    :param str variantsetId: Id of the variantset that used to call for variantset in repository
    :param str readsetId: Id of the read
    """
    repository: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    url: str = None
    
    name: str = None
    
    datasetId: str = None
    
    variantsetId: str = None
    
    readsetId: str = None
    
@dataclass
class structureVariant(Element):
    """ Information about chromosome structure variation.
    :param BackboneElement structureVariant: Structural variant
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept variantType: Structural variant change type
    :param bool exact: Does the structural variant have base pair resolution breakpoints?
    :param int length: Structural variant length
    :param BackboneElement outer: Structural variant outer
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant outer start
    :param int end: Structural variant outer end
    :param BackboneElement inner: Structural variant inner
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant inner start
    :param int end: Structural variant inner end
    """
    structureVariant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    variantType: "CodeableConcept" = None
    
    exact: bool = None
    
    length: int = None
    
    outer: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    
    inner: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    
@dataclass
class outer(Element):
    """ Structural variant outer.
    :param BackboneElement outer: Structural variant outer
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant outer start
    :param int end: Structural variant outer end
    """
    outer: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    
@dataclass
class inner(Element):
    """ Structural variant inner.
    :param BackboneElement inner: Structural variant inner
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant inner start
    :param int end: Structural variant inner end
    """
    inner: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    


@dataclass
class MolecularSequence(ModelBase):
    """ Raw data describing a biological sequence.
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
    :param BackboneElement referenceSeq: A sequence used as reference
    :param str id: Unique id for inter-element referencing
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
    :param BackboneElement variant: Variant in sequence
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Start position of the variant on the  reference sequence
    :param int end: End position of the variant on the reference sequence
    :param str observedAllele: Allele that was observed
    :param str referenceAllele: Allele in the reference sequence
    :param str cigar: Extended CIGAR string for aligning the sequence with reference bases
    :param Reference variantPointer: Pointer to observed variant information
    :param str observedSeq: Sequence that was observed
    :param BackboneElement quality: An set of value as quality of sequence
    :param str id: Unique id for inter-element referencing
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
    :param BackboneElement roc: Receiver Operator Characteristic (ROC) Curve
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int score: Genotype quality score
    :param int numTP: Roc score true positive numbers
    :param int numFP: Roc score false positive numbers
    :param int numFN: Roc score false negative numbers
    :param float precision: Precision of the GQ score
    :param float sensitivity: Sensitivity of the GQ score
    :param float fMeasure: FScore of the GQ score
    :param int readCoverage: Average number of reads representing a given nucleotide in the reconstructed sequence
    :param BackboneElement repository: External repository which contains detailed report related with observedSeq in this resource
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: directlink | openapi | login | oauth | other
    :param str url: URI of the repository
    :param str name: Repository's name
    :param str datasetId: Id of the dataset that used to call for dataset in repository
    :param str variantsetId: Id of the variantset that used to call for variantset in repository
    :param str readsetId: Id of the read
    :param Reference pointer: Pointer to next atomic sequence
    :param BackboneElement structureVariant: Structural variant
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept variantType: Structural variant change type
    :param bool exact: Does the structural variant have base pair resolution breakpoints?
    :param int length: Structural variant length
    :param BackboneElement outer: Structural variant outer
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant outer start
    :param int end: Structural variant outer end
    :param BackboneElement inner: Structural variant inner
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant inner start
    :param int end: Structural variant inner end
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    type: str = None
    
    coordinateSystem: int = None
    
    patient: "Reference" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    performer: "Reference" = None
    
    quantity: "Quantity" = None
    
    referenceSeq: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    chromosome: "CodeableConcept" = None
    
    genomeBuild: str = None
    
    orientation: str = None
    
    referenceSeqId: "CodeableConcept" = None
    
    referenceSeqPointer: "Reference" = None
    
    referenceSeqString: str = None
    
    strand: str = None
    
    windowStart: int = None
    
    windowEnd: int = None
    
    variant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    
    observedAllele: str = None
    
    referenceAllele: str = None
    
    cigar: str = None
    
    variantPointer: "Reference" = None
    
    observedSeq: str = None
    
    quality: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    standardSequence: "CodeableConcept" = None
    
    start: int = None
    
    end: int = None
    
    score: "Quantity" = None
    
    method: "CodeableConcept" = None
    
    truthTP: float = None
    
    queryTP: float = None
    
    truthFN: float = None
    
    queryFP: float = None
    
    gtFP: float = None
    
    precision: float = None
    
    recall: float = None
    
    fScore: float = None
    
    roc: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    score: int = None
    
    numTP: int = None
    
    numFP: int = None
    
    numFN: int = None
    
    precision: float = None
    
    sensitivity: float = None
    
    fMeasure: float = None
    
    readCoverage: int = None
    
    repository: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    url: str = None
    
    name: str = None
    
    datasetId: str = None
    
    variantsetId: str = None
    
    readsetId: str = None
    
    pointer: list["Reference"] = None
    
    structureVariant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    variantType: "CodeableConcept" = None
    
    exact: bool = None
    
    length: int = None
    
    outer: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    
    inner: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    start: int = None
    
    end: int = None
    