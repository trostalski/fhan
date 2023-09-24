"""
Generated class for Flag. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


class Flag(DomainResource):
    """ Prospective warnings of potential issues when providing care to the patient.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier
    :param str status: active | inactive | entered-in-error
    :param list['CodeableConcept'] category: Clinical, administrative, etc.
    :param 'CodeableConcept' code: Coded or textual message to display to user
    :param 'Reference' subject: Who/What is flag about?
    :param 'Period' period: Time period when flag is active
    :param 'Reference' encounter: Alert relevant during encounter
    :param 'Reference' author: Flag creator
    """
    def __init__(self, resourceType: str = "Flag",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  category: list['CodeableConcept'] = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  period: 'Period' = None,  encounter: 'Reference' = None,  author: 'Reference' = None, ):
        self.resourceType: str = resourceType or "Flag"
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
        self.category: list['CodeableConcept'] = category or []
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.period: 'Period' = period 
        self.encounter: 'Reference' = encounter 
        self.author: 'Reference' = author 
        