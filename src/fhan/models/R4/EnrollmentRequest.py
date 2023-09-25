"""
Generated class for EnrollmentRequest. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class EnrollmentRequest(DomainResource):
    """ This resource provides the insurance enrollment details to the insurer regarding a specified coverage.
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
    :param str created: Creation date
    :param 'Reference' insurer: Target
    :param 'Reference' provider: Responsible practitioner
    :param 'Reference' candidate: The subject to be enrolled
    :param 'Reference' coverage: Insurance information
    """
    def __init__(self, resourceType: str = "EnrollmentRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  created: str = None,  insurer: 'Reference' = None,  provider: 'Reference' = None,  candidate: 'Reference' = None,  coverage: 'Reference' = None, ):
        self.resourceType: str = resourceType or "EnrollmentRequest"
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
        self.created: str = created 
        self.insurer: 'Reference' = insurer 
        self.provider: 'Reference' = provider 
        self.candidate: 'Reference' = candidate 
        self.coverage: 'Reference' = coverage 
        