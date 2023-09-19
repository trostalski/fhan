"""
Generated class for BodyStructure. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase


@dataclass
class BodyStructure(ModelBase):
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
    :param CodeableConcept location: Body site
    :param CodeableConcept locationQualifier: Body site modifier
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
    
    location: "CodeableConcept" = None
    
    locationQualifier: "CodeableConcept" = None
    
    description: str = None
    
    image: "Attachment" = None
    
    patient: "Reference" = None
    