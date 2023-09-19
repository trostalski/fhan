"""
Generated class for DiagnosticReport. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class DiagnosticReport(ModelBase):
    """ Lipid Lab Report
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for report
    :param Reference basedOn: What was requested
    :param str status: registered | partial | preliminary | final +
    :param CodeableConcept category: Service category
    :param CodeableConcept code: LOINC Code for Lipid Panel with LDL
    :param Reference subject: The subject of the report - usually, but not always, the patient
    :param Reference encounter: Health care event when test ordered
    :param str effectivedateTime: Clinically relevant time/time-period for report
    :param Period effectivedateTime: Clinically relevant time/time-period for report
    :param str issued: DateTime this version was made
    :param Reference performer: Responsible Diagnostic Service
    :param Reference resultsInterpreter: Primary result interpreter
    :param Reference specimen: Specimens this report is based on
    :param Reference result: Observations
    :param Reference result:Cholesterol: Cholesterol Result
    :param Reference result:Triglyceride: Triglyceride Result
    :param Reference result:HDLCholesterol: HDL Cholesterol Result
    :param Reference result:LDLCholesterol: LDL Cholesterol result, if reported
    :param Reference imagingStudy: Reference to full details of imaging associated with the diagnostic report
    :param BackboneElement media: Key images associated with this report
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str comment: Comment about the image (e.g. explanation)
    :param Reference link: Reference to the image source
    :param str conclusion: Clinical Interpretation of Lipid Panel
    :param CodeableConcept conclusionCode: No codes for a lipid panel
    :param Attachment presentedForm: Entire report as issued
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
    
    basedOn: "Reference" = None
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    effectivedateTime: str = None
    
    effectivedateTime: "Period" = None
    
    issued: str = None
    
    performer: "Reference" = None
    
    resultsInterpreter: "Reference" = None
    
    specimen: "Reference" = None
    
    result: "Reference" = None
    
    result:Cholesterol: "Reference" = None
    
    result:Triglyceride: "Reference" = None
    
    result:HDLCholesterol: "Reference" = None
    
    result:LDLCholesterol: "Reference" = None
    
    imagingStudy: "Reference" = None
    
    media: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    comment: str = None
    
    link: "Reference" = None
    
    conclusion: str = None
    
    conclusionCode: "CodeableConcept" = None
    
    presentedForm: "Attachment" = None
    