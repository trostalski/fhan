"""
Generated class for DetectedIssue. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Evidence(ModelBase):
    """ Supporting evidence or manifestations that provide the basis for identifying the detected issue such as a GuidanceResponse or MeasureReport.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] code: Manifestation
    :param list['Reference'] detail: Supporting information
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: list['CodeableConcept'] = None,  detail: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: list['CodeableConcept'] = code or []
        self.detail: list['Reference'] = detail or []
        

    
    

class Mitigation(ModelBase):
    """ Indicates an action that has been taken or is committed to reduce or eliminate the likelihood of the risk identified by the detected issue from manifesting.  Can also reflect an observation of known mitigating factors that may reduce/eliminate the need for any action.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' action: What mitigation?
    :param str date: Date committed
    :param 'Reference' author: Who is committing?
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  action: 'CodeableConcept' = None,  date: str = None,  author: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.action: 'CodeableConcept' = action 
        self.date: str = date 
        self.author: 'Reference' = author 
        

class DetectedIssue(DomainResource):
    """ Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique id for the detected issue
    :param str status: registered | preliminary | final | amended +
    :param 'CodeableConcept' code: Issue Category, e.g. drug-drug, duplicate therapy, etc.
    :param str severity: high | moderate | low
    :param 'Reference' patient: Associated patient
    :param str identifiedDateTime: When identified
    :param 'Reference' author: The provider or device that identified the issue
    :param list['Reference'] implicated: Problem resource
    :param list['Evidence'] evidence: Supporting evidence
    :param str detail: Description and context
    :param str reference: Authority for issue
    :param list['Mitigation'] mitigation: Step taken to address
    """
    def __init__(self, resourceType: str = "DetectedIssue",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  code: 'CodeableConcept' = None,  severity: str = None,  patient: 'Reference' = None,  identifiedDateTime: str = None,  author: 'Reference' = None,  implicated: list['Reference'] = None,  evidence: list['Evidence'] = None,  detail: str = None,  reference: str = None,  mitigation: list['Mitigation'] = None, ):
        self.resourceType: str = resourceType or "DetectedIssue"
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
        self.code: 'CodeableConcept' = code 
        self.severity: str = severity 
        self.patient: 'Reference' = patient 
        self.identifiedDateTime: str = identifiedDateTime 
        self.author: 'Reference' = author 
        self.implicated: list['Reference'] = implicated or []
        self.evidence: list['Evidence'] = evidence or []
        self.detail: str = detail 
        self.reference: str = reference 
        self.mitigation: list['Mitigation'] = mitigation or []
        