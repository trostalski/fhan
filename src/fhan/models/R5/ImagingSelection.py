"""
Generated class for ImagingSelection. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ImagingSelection:
    """ A selection of DICOM SOP instances and/or frames within a single Study and Series. This might include additional specifics such as an image region, an Observation UID or a Segmentation Number, allowing linkage to an Observation Resource or transferring this information along with the ImagingStudy Resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for Imaging Selection
    :param str status: available | entered-in-error | unknown
    :param Reference subject: Subject of the selected instances
    :param str issued: Date / Time when this imaging selection was created
    :param BackboneElement performer: Selector of the instances (human or machine)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performer
    :param Reference actor: Author (human or machine)
    :param Reference basedOn: Associated request
    :param CodeableConcept category: Classifies the imaging selection
    :param CodeableConcept code: Imaging Selection purpose text or code
    :param str studyUid: DICOM Study Instance UID
    :param Reference derivedFrom: The imaging study from which the imaging selection is derived
    :param Reference endpoint: The network service providing retrieval for the images referenced in the imaging selection
    :param str seriesUid: DICOM Series Instance UID
    :param int seriesNumber: DICOM Series Number
    :param str frameOfReferenceUid: The Frame of Reference UID for the selected images
    :param CodeableReference bodySite: Body part examined
    :param Reference focus: Related resource that is the focus for the imaging selection
    :param BackboneElement instance: The selected instances
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uid: DICOM SOP Instance UID
    :param int number: DICOM Instance Number
    :param Coding sopClass: DICOM SOP Class UID
    :param str subset: The selected subset of the SOP Instance
    :param BackboneElement imageRegion2D: A specific 2D region in a DICOM image / frame
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str regionType: point | polyline | interpolated | circle | ellipse
    :param float coordinate: Specifies the coordinates that define the image region
    :param BackboneElement imageRegion3D: A specific 3D region in a DICOM frame of reference
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str regionType: point | multipoint | polyline | polygon | ellipse | ellipsoid
    :param float coordinate: Specifies the coordinates that define the image region
    
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
    
    subject: "Reference" = None
    
    issued: str = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    basedOn: "Reference" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    studyUid: str = None
    
    derivedFrom: "Reference" = None
    
    endpoint: "Reference" = None
    
    seriesUid: str = None
    
    seriesNumber: int = None
    
    frameOfReferenceUid: str = None
    
    bodySite: "CodeableReference" = None
    
    focus: "Reference" = None
    
    instance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    uid: str = None
    
    number: int = None
    
    sopClass: "Coding" = None
    
    subset: str = None
    
    imageRegion2D: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    regionType: str = None
    
    coordinate: float = None
    
    imageRegion3D: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    regionType: str = None
    
    coordinate: float = None
    