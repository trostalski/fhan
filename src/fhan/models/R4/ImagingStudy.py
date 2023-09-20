"""
Generated class for ImagingStudy. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.generator_models import ModelBase

@dataclass
class series(Element):
    """ Each study has one or more series of images or other content.
    :param BackboneElement series: Each study has one or more series of instances
    :param str id: Unique id for inter-element referencing
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
    series: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    uid: str = None
    
    number: int = None
    
    modality: "Coding" = None
    
    description: str = None
    
    numberOfInstances: int = None
    
    endpoint: list["Reference"] = None
    
    bodySite: "Coding" = None
    
    laterality: "Coding" = None
    
    specimen: list["Reference"] = None
    
    started: str = None
    
    performer: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    instance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    uid: str = None
    
    sopClass: "Coding" = None
    
    number: int = None
    
    title: str = None
    
@dataclass
class performer(Element):
    """ Indicates who or what performed the series and how they were involved.
    :param BackboneElement performer: Who performed the series
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the series
    """
    performer: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
@dataclass
class instance(Element):
    """ A single SOP instance within the series, e.g. an image, or presentation state.
    :param BackboneElement instance: A single SOP instance from the series
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM SOP Instance UID
    :param Coding sopClass: DICOM class type
    :param int number: The number of this instance in the series
    :param str title: Description of instance
    """
    instance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    uid: str = None
    
    sopClass: "Coding" = None
    
    number: int = None
    
    title: str = None
    


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
    :param BackboneElement series: Each study has one or more series of instances
    :param str id: Unique id for inter-element referencing
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
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    modality: list["Coding"] = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    started: str = None
    
    basedOn: list["Reference"] = None
    
    referrer: "Reference" = None
    
    interpreter: list["Reference"] = None
    
    endpoint: list["Reference"] = None
    
    numberOfSeries: int = None
    
    numberOfInstances: int = None
    
    procedureReference: "Reference" = None
    
    procedureCode: list["CodeableConcept"] = None
    
    location: "Reference" = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    description: str = None
    
    series: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    uid: str = None
    
    number: int = None
    
    modality: "Coding" = None
    
    description: str = None
    
    numberOfInstances: int = None
    
    endpoint: list["Reference"] = None
    
    bodySite: "Coding" = None
    
    laterality: "Coding" = None
    
    specimen: list["Reference"] = None
    
    started: str = None
    
    performer: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    instance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    uid: str = None
    
    sopClass: "Coding" = None
    
    number: int = None
    
    title: str = None
    