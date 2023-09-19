"""
Generated class for GenomicStudy. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class GenomicStudy:
    """ A set of analyses performed to analyze and generate genomic data.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers for this genomic study
    :param str status: registered | available | cancelled | entered-in-error | unknown
    :param CodeableConcept type: The type of the study (e.g., Familial variant segregation, Functional variation detection, or Gene expression profiling)
    :param Reference subject: The primary subject of the genomic study
    :param Reference encounter: The healthcare event with which this genomics study is associated
    :param str startDate: When the genomic study was started
    :param Reference basedOn: Event resources that the genomic study is based on
    :param Reference referrer: Healthcare professional who requested or referred the genomic study
    :param Reference interpreter: Healthcare professionals who interpreted the genomic study
    :param CodeableReference reason: Why the genomic study was performed
    :param str instantiatesCanonical: The defined protocol that describes the study
    :param str instantiatesUri: The URL pointing to an externally maintained protocol that describes the study
    :param Annotation note: Comments related to the genomic study
    :param str description: Description of the genomic study
    :param BackboneElement analysis: Genomic Analysis Event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifiers for the analysis event
    :param CodeableConcept methodType: Type of the methods used in the analysis (e.g., FISH, Karyotyping, MSI)
    :param CodeableConcept changeType: Type of the genomic changes studied in the analysis (e.g., DNA, RNA, or AA change)
    :param CodeableConcept genomeBuild: Genome build that is used in this analysis
    :param str instantiatesCanonical: The defined protocol that describes the analysis
    :param str instantiatesUri: The URL pointing to an externally maintained protocol that describes the analysis
    :param str title: Name of the analysis event (human friendly)
    :param Reference focus: What the genomic analysis is about, when it is not about the subject of record
    :param Reference specimen: The specimen used in the analysis event
    :param str date: The date of the analysis event
    :param Annotation note: Any notes capture with the analysis event
    :param Reference protocolPerformed: The protocol that was performed for the analysis event
    :param Reference regionsStudied: The genomic regions to be studied in the analysis (BED file)
    :param Reference regionsCalled: Genomic regions actually called in the analysis event (BED file)
    :param BackboneElement input: Inputs for the analysis event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference file: File containing input data
    :param CodeableConcept type: Type of input data (e.g., BAM, CRAM, or FASTA)
    :param Identifier generatedByIdentifier: The analysis event or other GenomicStudy that generated this input file
    :param Reference generatedByIdentifier: The analysis event or other GenomicStudy that generated this input file
    :param BackboneElement output: Outputs for the analysis event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference file: File containing output data
    :param CodeableConcept type: Type of output data (e.g., VCF, MAF, or BAM)
    :param BackboneElement performer: Performer for the analysis event
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference actor: The organization, healthcare professional, or others who participated in performing this analysis
    :param CodeableConcept role: Role of the actor for this analysis
    :param BackboneElement device: Devices used for the analysis (e.g., instruments, software), with settings and parameters
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference device: Device used for the analysis
    :param CodeableConcept function: Specific function for the device used for the analysis
    
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
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    startDate: str = None
    
    basedOn: "Reference" = None
    
    referrer: "Reference" = None
    
    interpreter: "Reference" = None
    
    reason: "CodeableReference" = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    note: "Annotation" = None
    
    description: str = None
    
    analysis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    methodType: "CodeableConcept" = None
    
    changeType: "CodeableConcept" = None
    
    genomeBuild: "CodeableConcept" = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    title: str = None
    
    focus: "Reference" = None
    
    specimen: "Reference" = None
    
    date: str = None
    
    note: "Annotation" = None
    
    protocolPerformed: "Reference" = None
    
    regionsStudied: "Reference" = None
    
    regionsCalled: "Reference" = None
    
    input: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    file: "Reference" = None
    
    type: "CodeableConcept" = None
    
    generatedByIdentifier: "Identifier" = None
    
    generatedByIdentifier: "Reference" = None
    
    output: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    file: "Reference" = None
    
    type: "CodeableConcept" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    actor: "Reference" = None
    
    role: "CodeableConcept" = None
    
    device: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    device: "Reference" = None
    
    function: "CodeableConcept" = None
    