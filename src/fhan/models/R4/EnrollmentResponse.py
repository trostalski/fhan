"""
Generated class for EnrollmentResponse. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


class EnrollmentResponse(DomainResource):
    """ This resource provides enrollment and plan details from the processing of an EnrollmentRequest resource.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier
    :param str status: active | cancelled | draft | entered-in-error
    :param 'Reference' request: Claim reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param str created: Creation date
    :param 'Reference' organization: Insurer
    :param 'Reference' requestProvider: Responsible practitioner
    """
    def __init__(self, resourceType: str = "EnrollmentResponse",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  request: 'Reference' = None,  outcome: str = None,  disposition: str = None,  created: str = None,  organization: 'Reference' = None,  requestProvider: 'Reference' = None, ):
        self.resourceType: str = resourceType or "EnrollmentResponse"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.request: 'Reference' = request 
        self.outcome: str = outcome 
        self.disposition: str = disposition 
        self.created: str = created 
        self.organization: 'Reference' = organization 
        self.requestProvider: 'Reference' = requestProvider 
        