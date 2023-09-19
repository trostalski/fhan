"""
Generated class for EnrollmentResponse. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class EnrollmentResponse:
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
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    request: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    created: str = None
    
    organization: "Reference" = None
    
    requestProvider: "Reference" = None
    