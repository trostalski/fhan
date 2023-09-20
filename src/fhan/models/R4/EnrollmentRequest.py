"""
Generated class for EnrollmentRequest. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase



@dataclass
class EnrollmentRequest(ModelBase):
    """ This resource provides the insurance enrollment details to the insurer regarding a specified coverage.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier
    :param str status: active | cancelled | draft | entered-in-error
    :param str created: Creation date
    :param Reference insurer: Target
    :param Reference provider: Responsible practitioner
    :param Reference candidate: The subject to be enrolled
    :param Reference coverage: Insurance information
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
    
    created: str = None
    
    insurer: "Reference" = None
    
    provider: "Reference" = None
    
    candidate: "Reference" = None
    
    coverage: "Reference" = None
    