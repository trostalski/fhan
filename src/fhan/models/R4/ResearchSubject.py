"""
Generated class for ResearchSubject. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class ResearchSubject(DomainResource):
    """ A physical entity which is the primary unit of operational and/or administrative interest in a study.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for research subject in a study
    :param str status: candidate | eligible | follow-up | ineligible | not-registered | off-study | on-study | on-study-intervention | on-study-observation | pending-on-study | potential-candidate | screening | withdrawn
    :param 'Period' period: Start and end of participation
    :param 'Reference' study: Study subject is part of
    :param 'Reference' individual: Who is part of study
    :param str assignedArm: What path should be followed
    :param str actualArm: What path was followed
    :param 'Reference' consent: Agreement to participate in study
    """
    def __init__(self, resourceType: str = "ResearchSubject",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  period: 'Period' = None,  study: 'Reference' = None,  individual: 'Reference' = None,  assignedArm: str = None,  actualArm: str = None,  consent: 'Reference' = None, ):
        self.resourceType: str = resourceType or "ResearchSubject"
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
        self.period: 'Period' = period 
        self.study: 'Reference' = study 
        self.individual: 'Reference' = individual 
        self.assignedArm: str = assignedArm 
        self.actualArm: str = actualArm 
        self.consent: 'Reference' = consent 
        