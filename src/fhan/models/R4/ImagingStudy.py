"""
Generated class for ImagingStudy. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Performer(Element):
    """ Indicates who or what performed the series and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the series
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    function: "CodeableConcept" = CodeableConcept()
    actor: "Reference" = Reference()
    

    
    
@dataclass
class Instance(Element):
    """ A single SOP instance within the series, e.g. an image, or presentation state.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM SOP Instance UID
    :param Coding sopClass: DICOM class type
    :param int number: The number of this instance in the series
    :param str title: Description of instance
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    uid: str = None
    sopClass: "Coding" = Coding()
    
    number: int = None
    
    title: str = None
    

  
    
    
@dataclass
class Series(Element):
    """ Each study has one or more series of images or other content.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM Series Instance UID for the series
    :param int number: Numeric identifier of this series
    :param Coding modality: The modality of the instances in the series
    :param str description: A short human readable summary of the series
    :param int numberOfInstances: Number of Series Related Instances
    :param Reference endpoint: Series access endpoint
    :param Coding bodySite: Body part examined
    :param Coding laterality: Body part laterality
    :param Reference specimen: Specimen imaged
    :param str started: When the series started
    :param Performer performer: Who performed the series
    :param Instance instance: A single SOP instance from the series
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    uid: str = None
    
    number: int = None
    modality: "Coding" = Coding()
    
    description: str = None
    
    numberOfInstances: int = None
    endpoint: list[Reference] = Reference() 
    bodySite: "Coding" = Coding()
    laterality: "Coding" = Coding()
    specimen: list[Reference] = Reference() 
    
    started: str = None
    performer: list[Performer] = Performer() 
    instance: list[Instance] = Instance() 
    

@dataclass
class ImagingStudy(ModelBase):
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
    :param Coding modality: All series modality if actual acquisition modalities
    :param Reference subject: Who or what is the subject of the study
    :param Reference encounter: Encounter with which this imaging study is associated
    :param str started: When the study was started
    :param Reference basedOn: Request fulfilled
    :param Reference referrer: Referring physician
    :param Reference interpreter: Who interpreted images
    :param Reference endpoint: Study access endpoint
    :param int numberOfSeries: Number of Study Related Series
    :param int numberOfInstances: Number of Study Related Instances
    :param Reference procedureReference: The performed Procedure reference
    :param CodeableConcept procedureCode: The performed procedure code
    :param Reference location: Where ImagingStudy occurred
    :param CodeableConcept reasonCode: Why the study was requested
    :param Reference reasonReference: Why was study performed
    :param Annotation note: User-defined comments
    :param str description: Institution-generated description
    :param Series series: Each study has one or more series of instances
    """

    resourceType: str = "ImagingStudy"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    modality: list[Coding] = Coding() 
    
    subject: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    started: str = None
    
    basedOn: list[Reference] = Reference() 
    
    referrer: "Reference" = Reference()
    
    interpreter: list[Reference] = Reference() 
    
    endpoint: list[Reference] = Reference() 
    
    numberOfSeries: int = None
    
    numberOfInstances: int = None
    
    procedureReference: "Reference" = Reference()
    
    procedureCode: list[CodeableConcept] = CodeableConcept() 
    
    location: "Reference" = Reference()
    
    reasonCode: list[CodeableConcept] = CodeableConcept() 
    
    reasonReference: list[Reference] = Reference() 
    
    note: list[Annotation] = Annotation() 
    
    description: str = None
    
    series: list[Series] = Series() 
    