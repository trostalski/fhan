"""
Generated class for BodyStructure. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class BodyStructure:
    """ Record details about an anatomical structure.  This resource may be used when a coded concept does not provide the necessary detail needed for the use case.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Bodystructure identifier
    :param bool active: Whether this record is in active use
    :param CodeableConcept morphology: Kind of Structure
    :param BackboneElement includedStructure: Included anatomic location(s)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept structure: Code that represents the included structure
    :param CodeableConcept laterality: Code that represents the included structure laterality
    :param BackboneElement bodyLandmarkOrientation: Landmark relative location
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept landmarkDescription: Body ]andmark description
    :param CodeableConcept clockFacePosition: Clockface orientation
    :param BackboneElement distanceFromLandmark: Landmark relative location
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference device: Measurement device
    :param Quantity value: Measured distance from body landmark
    :param CodeableConcept surfaceOrientation: Relative landmark surface orientation
    :param Reference spatialReference: Cartesian reference for structure
    :param CodeableConcept qualifier: Code that represents the included structure qualifier
    :param BackboneElement excludedStructure: Included anatomic location(s)
    :param str description: Text description
    :param Attachment image: Attached images
    :param Reference patient: Who this is about
    
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
    
    active: bool = None
    
    morphology: "CodeableConcept" = None
    
    includedStructure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    structure: "CodeableConcept" = None
    
    laterality: "CodeableConcept" = None
    
    bodyLandmarkOrientation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    landmarkDescription: "CodeableConcept" = None
    
    clockFacePosition: "CodeableConcept" = None
    
    distanceFromLandmark: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    device: "CodeableReference" = None
    
    value: "Quantity" = None
    
    surfaceOrientation: "CodeableConcept" = None
    
    spatialReference: "Reference" = None
    
    qualifier: "CodeableConcept" = None
    
    excludedStructure: "BackboneElement" = None
    
    description: str = None
    
    image: "Attachment" = None
    
    patient: "Reference" = None
    