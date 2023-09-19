"""
Generated class for MolecularSequence. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class MolecularSequence:
    """ Representation of a molecular sequence.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique ID for this particular sequence
    :param str type: aa | dna | rna
    :param Reference subject: Subject this sequence is associated too
    :param Reference focus: What the molecular sequence is about, when it is not about the subject of record
    :param Reference specimen: Specimen used for sequencing
    :param Reference device: The method for sequencing
    :param Reference performer: Who should be responsible for test result
    :param str literal: Sequence that was observed
    :param Attachment formatted: Embedded file or a link (URL) which contains content to represent the sequence
    :param BackboneElement relative: A sequence defined relative to another sequence
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept coordinateSystem: Ways of identifying nucleotides or amino acids within a sequence
    :param int ordinalPosition: Indicates the order in which the sequence should be considered when putting multiple 'relative' elements together
    :param Range sequenceRange: Indicates the nucleotide range in the composed sequence when multiple 'relative' elements are used together
    :param BackboneElement startingSequence: A sequence used as starting sequence
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept genomeAssembly: The genome assembly used for starting sequence, e.g. GRCh38
    :param CodeableConcept chromosome: Chromosome Identifier
    :param CodeableConcept sequenceCodeableConcept: The reference sequence that represents the starting sequence
    :param str sequenceCodeableConcept: The reference sequence that represents the starting sequence
    :param Reference sequenceCodeableConcept: The reference sequence that represents the starting sequence
    :param int windowStart: Start position of the window on the starting sequence
    :param int windowEnd: End position of the window on the starting sequence
    :param str orientation: sense | antisense
    :param str strand: watson | crick
    :param BackboneElement edit: Changes in sequence from the starting sequence
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Start position of the edit on the starting sequence
    :param int end: End position of the edit on the starting sequence
    :param str replacementSequence: Allele that was observed
    :param str replacedSequence: Allele in the starting sequence
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: str = None
    
    subject: "Reference" = None
    
    focus: "Reference" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    performer: "Reference" = None
    
    literal: str = None
    
    formatted: "Attachment" = None
    
    relative: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    coordinateSystem: "CodeableConcept" = None
    
    ordinalPosition: int = None
    
    sequenceRange: "Range" = None
    
    startingSequence: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    genomeAssembly: "CodeableConcept" = None
    
    chromosome: "CodeableConcept" = None
    
    sequenceCodeableConcept: "CodeableConcept" = None
    
    sequenceCodeableConcept: str = None
    
    sequenceCodeableConcept: "Reference" = None
    
    windowStart: int = None
    
    windowEnd: int = None
    
    orientation: str = None
    
    strand: str = None
    
    edit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    start: int = None
    
    end: int = None
    
    replacementSequence: str = None
    
    replacedSequence: str = None
    