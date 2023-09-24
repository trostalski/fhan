"""
Generated class for DiagnosticReport. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Media(ModelBase):
    """ A list of key images associated with this report. The images are generally created during the diagnostic process, and may be directly of the patient, or of treated specimens (i.e. slides of interest).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str comment: Comment about the image (e.g. explanation)
    :param 'Reference' link: Reference to the image source
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  comment: str = None,  link: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.comment: str = comment 
        self.link: 'Reference' = link 
        

class DiagnosticReport(DomainResource):
    """ Lipid Lab Report
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier for report
    :param list['Reference'] basedOn: What was requested
    :param str status: registered | partial | preliminary | final +
    :param list['CodeableConcept'] category: Service category
    :param 'CodeableConcept' code: LOINC Code for Lipid Panel with LDL
    :param 'Reference' subject: The subject of the report - usually, but not always, the patient
    :param 'Reference' encounter: Health care event when test ordered
    :param str effectiveDateTime: Clinically relevant time/time-period for report
    :param str issued: DateTime this version was made
    :param list['Reference'] performer: Responsible Diagnostic Service
    :param list['Reference'] resultsInterpreter: Primary result interpreter
    :param list['Reference'] specimen: Specimens this report is based on
    :param list['Reference'] result: Observations
    :param list['Reference'] imagingStudy: Reference to full details of imaging associated with the diagnostic report
    :param list['Media'] media: Key images associated with this report
    :param str conclusion: Clinical Interpretation of Lipid Panel
    :param 'CodeableConcept' conclusionCode: No codes for a lipid panel
    :param list['Attachment'] presentedForm: Entire report as issued
    """
    def __init__(self, resourceType: str = "DiagnosticReport",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  basedOn: list['Reference'] = None,  status: str = None,  category: list['CodeableConcept'] = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  effectiveDateTime: str = None,  issued: str = None,  performer: list['Reference'] = None,  resultsInterpreter: list['Reference'] = None,  specimen: list['Reference'] = None,  result: list['Reference'] = None,  imagingStudy: list['Reference'] = None,  media: list['Media'] = None,  conclusion: str = None,  conclusionCode: 'CodeableConcept' = None,  presentedForm: list['Attachment'] = None, ):
        self.resourceType: str = resourceType or "DiagnosticReport"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.basedOn: list['Reference'] = basedOn or []
        self.status: str = status 
        self.category: list['CodeableConcept'] = category or []
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.effectiveDateTime: str = effectiveDateTime 
        self.issued: str = issued 
        self.performer: list['Reference'] = performer or []
        self.resultsInterpreter: list['Reference'] = resultsInterpreter or []
        self.specimen: list['Reference'] = specimen or []
        self.result: list['Reference'] = result or []
        self.imagingStudy: list['Reference'] = imagingStudy or []
        self.media: list['Media'] = media or []
        self.conclusion: str = conclusion 
        self.conclusionCode: 'CodeableConcept' = conclusionCode 
        self.presentedForm: list['Attachment'] = presentedForm or []
        