"""
Generated class for EnrollmentResponse. 
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
class EnrollmentResponse(ModelBase):
    """ This resource provides enrollment and plan details from the processing of an EnrollmentRequest resource.
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
    :param Reference request: Claim reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str created: Creation date
    :param Reference organization: Insurer
    :param Reference requestProvider: Responsible practitioner
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
    
    request: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    created: str = None
    
    organization: "Reference" = None
    
    requestProvider: "Reference" = None
    