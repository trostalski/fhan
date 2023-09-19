"""
Generated class for ParticipantLiving. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Attachment import *
from fhan.models.R5.CodeableConcept import *


@dataclass
class ParticipantLiving:
    """ Logical Model: A pattern followed by resources that represent the participant in some activity, process, or responsible for providing information about a resource.
    :param str birthDate: The date of birth for the {{title}}
    :param str gender: male | female | other | unknown
    :param Attachment photo: Image of the {{title}
    :param CodeableConcept communication: Language used by {{title}}
    
    """
    birthDate: str = None
    
    gender: str = None
    
    photo: "Attachment" = None
    
    communication: "CodeableConcept" = None
    