"""
Generated class for ImagingStudy. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class ImagingStudy:
    """
    Representation of the content produced in a DICOM imaging study. A study comprises a set of series, each of which includes a set of Service-Object Pair Instances (SOP Instances - images or other data) acquired or produced in a common context.  A series is of only one modality (e.g. X-ray, CT, MR, ultrasound), but a study may have multiple series of different modalities.
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
    
    modality: "Coding" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    started: str = None
    
    basedOn: "Reference" = None
    
    referrer: "Reference" = None
    
    interpreter: "Reference" = None
    
    endpoint: "Reference" = None
    
    numberOfSeries: int = None
    
    numberOfInstances: int = None
    
    procedureReference: "Reference" = None
    
    procedureCode: "CodeableConcept" = None
    
    location: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    
    description: str = None
    
    series: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    uid: str = None
    
    number: int = None
    
    modality: "Coding" = None
    
    description: str = None
    
    numberOfInstances: int = None
    
    endpoint: "Reference" = None
    
    bodySite: "Coding" = None
    
    laterality: "Coding" = None
    
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
    