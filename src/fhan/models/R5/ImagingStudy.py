"""
Generated class for ImagingStudy. 
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
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ImagingStudy:
    """ Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers for the whole study
    :param str status: registered | available | cancelled | entered-in-error | unknown
    :param CodeableConcept modality: All of the distinct values for series' modalities
    :param Reference subject: Who or what is the subject of the study
    :param Reference encounter: Encounter with which this imaging study is associated
    :param str started: When the study was started
    :param Reference basedOn: Request fulfilled
    :param Reference partOf: Part of referenced event
    :param Reference referrer: Referring physician
    :param Reference endpoint: Study access endpoint
    :param int numberOfSeries: Number of Study Related Series
    :param int numberOfInstances: Number of Study Related Instances
    :param CodeableReference procedure: The performed procedure or code
    :param Reference location: Where ImagingStudy occurred
    :param CodeableReference reason: Why the study was requested / performed
    :param Annotation note: User-defined comments
    :param str description: Institution-generated description
    :param BackboneElement series: Each study has one or more series of instances
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM Series Instance UID for the series
    :param int number: Numeric identifier of this series
    :param CodeableConcept modality: The modality used for this series
    :param str description: A short human readable summary of the series
    :param int numberOfInstances: Number of Series Related Instances
    :param Reference endpoint: Series access endpoint
    :param CodeableReference bodySite: Body part examined
    :param CodeableConcept laterality: Body part laterality
    :param Reference specimen: Specimen imaged
    :param str started: When the series started
    :param BackboneElement performer: Who performed the series
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the series
    :param BackboneElement instance: A single SOP instance from the series
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM SOP Instance UID
    :param Coding sopClass: DICOM class type
    :param int number: The number of this instance in the series
    :param str title: Description of instance
    
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
    
    modality: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    started: str = None
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    referrer: "Reference" = None
    
    endpoint: "Reference" = None
    
    numberOfSeries: int = None
    
    numberOfInstances: int = None
    
    procedure: "CodeableReference" = None
    
    location: "Reference" = None
    
    reason: "CodeableReference" = None
    
    note: "Annotation" = None
    
    description: str = None
    
    series: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    uid: str = None
    
    number: int = None
    
    modality: "CodeableConcept" = None
    
    description: str = None
    
    numberOfInstances: int = None
    
    endpoint: "Reference" = None
    
    bodySite: "CodeableReference" = None
    
    laterality: "CodeableConcept" = None
    
    specimen: "Reference" = None
    
    started: str = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    instance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    uid: str = None
    
    sopClass: "Coding" = None
    
    number: int = None
    
    title: str = None
    