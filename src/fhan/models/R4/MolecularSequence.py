"""
Generated class for MolecularSequence. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class ReferenceSeq(Element):
    """ A sequence that is used as a reference to describe variants that are present in a sequence analyzed.:param str id: Unique id for inter-element referencing
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
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    chromosome: "CodeableConcept" = CodeableConcept()
    
    genomeBuild: str = None
    
    orientation: str = None
    referenceSeqId: "CodeableConcept" = CodeableConcept()
    referenceSeqPointer: "Reference" = Reference()
    
    referenceSeqString: str = None
    
    strand: str = None
    
    windowStart: int = None
    
    windowEnd: int = None
    

    
    
@dataclass
class Variant(Element):
    """ The definition of variant here originates from Sequence ontology ([variant_of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)). This element can represent amino acid or nucleic sequence change(including insertion,deletion,SNP,etc.)  It can represent some complex mutation or segment variation with the assist of CIGAR string.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Start position of the variant on the  reference sequence
    :param int end: End position of the variant on the reference sequence
    :param str observedAllele: Allele that was observed
    :param str referenceAllele: Allele in the reference sequence
    :param str cigar: Extended CIGAR string for aligning the sequence with reference bases
    :param Reference variantPointer: Pointer to observed variant information
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    start: int = None
    
    end: int = None
    
    observedAllele: str = None
    
    referenceAllele: str = None
    
    cigar: str = None
    variantPointer: "Reference" = Reference()
    

    
        
    
    
@dataclass
class Roc(Element):
    """ Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity tradeoff.:param str id: Unique id for inter-element referencing
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
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    score: int = None
    
    numTP: int = None
    
    numFP: int = None
    
    numFN: int = None
    
    precision: float = None
    
    sensitivity: float = None
    
    fMeasure: float = None
    

  
    
    
@dataclass
class Quality(Element):
    """ An experimental feature attribute that defines the quality of the feature in a quantitative way, such as a phred quality score ([SO:0001686](http://www.sequenceontology.org/browser/current_svn/term/SO:0001686)).:param str id: Unique id for inter-element referencing
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
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    type: str = None
    standardSequence: "CodeableConcept" = CodeableConcept()
    
    start: int = None
    
    end: int = None
    score: "Quantity" = Quantity()
    method: "CodeableConcept" = CodeableConcept()
    
    truthTP: float = None
    
    queryTP: float = None
    
    truthFN: float = None
    
    queryFP: float = None
    
    gtFP: float = None
    
    precision: float = None
    
    recall: float = None
    
    fScore: float = None
    roc: "Roc" = Roc()
    

    
    
@dataclass
class Repository(Element):
    """ Configurations of the external repository. The repository shall store target's observedSeq or records related with target's observedSeq.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: directlink | openapi | login | oauth | other
    :param str url: URI of the repository
    :param str name: Repository's name
    :param str datasetId: Id of the dataset that used to call for dataset in repository
    :param str variantsetId: Id of the variantset that used to call for variantset in repository
    :param str readsetId: Id of the read
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    type: str = None
    
    url: str = None
    
    name: str = None
    
    datasetId: str = None
    
    variantsetId: str = None
    
    readsetId: str = None
    

    
        
    
    
@dataclass
class Outer(Element):
    """ Structural variant outer.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant outer start
    :param int end: Structural variant outer end
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    start: int = None
    
    end: int = None
    

    
    
@dataclass
class Inner(Element):
    """ Structural variant inner.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant inner start
    :param int end: Structural variant inner end
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    start: int = None
    
    end: int = None
    

  
    
    
@dataclass
class StructureVariant(Element):
    """ Information about chromosome structure variation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept variantType: Structural variant change type
    :param bool exact: Does the structural variant have base pair resolution breakpoints?
    :param int length: Structural variant length
    :param Outer outer: Structural variant outer
    :param Inner inner: Structural variant inner
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    variantType: "CodeableConcept" = CodeableConcept()
    
    exact: bool = None
    
    length: int = None
    outer: "Outer" = Outer()
    inner: "Inner" = Inner()
    

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
    :param ReferenceSeq referenceSeq: A sequence used as reference
    :param Variant variant: Variant in sequence
    :param str observedSeq: Sequence that was observed
    :param Quality quality: An set of value as quality of sequence
    :param int readCoverage: Average number of reads representing a given nucleotide in the reconstructed sequence
    :param Repository repository: External repository which contains detailed report related with observedSeq in this resource
    :param Reference pointer: Pointer to next atomic sequence
    :param StructureVariant structureVariant: Structural variant
    """

    resourceType: str = "MolecularSequence"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    type: str = None
    
    coordinateSystem: int = None
    
    patient: "Reference" = Reference()
    
    specimen: "Reference" = Reference()
    
    device: "Reference" = Reference()
    
    performer: "Reference" = Reference()
    
    quantity: "Quantity" = Quantity()
    
    referenceSeq: "ReferenceSeq" = ReferenceSeq()
    
    variant: list[Variant] = Variant() 
    
    observedSeq: str = None
    
    quality: list[Quality] = Quality() 
    
    readCoverage: int = None
    
    repository: list[Repository] = Repository() 
    
    pointer: list[Reference] = Reference() 
    
    structureVariant: list[StructureVariant] = StructureVariant() 
    