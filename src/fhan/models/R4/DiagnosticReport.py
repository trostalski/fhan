"""
Generated class for DiagnosticReport. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Media(Element):
    """ A list of key images associated with this report. The images are generally created during the diagnostic process, and may be directly of the patient, or of treated specimens (i.e. slides of interest).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str comment: Comment about the image (e.g. explanation)
    :param Reference link: Reference to the image source
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    comment: str = None
    link: "Reference" = Reference()
    

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
    :param str effectiveDateTime: Clinically relevant time/time-period for report
    :param str issued: DateTime this version was made
    :param Reference performer: Responsible Diagnostic Service
    :param Reference resultsInterpreter: Primary result interpreter
    :param Reference specimen: Specimens this report is based on
    :param Reference result: Observations
    :param Reference imagingStudy: Reference to full details of imaging associated with the diagnostic report
    :param Media media: Key images associated with this report
    :param str conclusion: Clinical Interpretation of Lipid Panel
    :param CodeableConcept conclusionCode: No codes for a lipid panel
    :param Attachment presentedForm: Entire report as issued
    """

    resourceType: str = "DiagnosticReport"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    basedOn: list[Reference] = Reference() 
    
    status: str = None
    
    category: list[CodeableConcept] = CodeableConcept() 
    
    code: "CodeableConcept" = CodeableConcept()
    
    subject: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    effectiveDateTime: str = None
    
    issued: str = None
    
    performer: list[Reference] = Reference() 
    
    resultsInterpreter: list[Reference] = Reference() 
    
    specimen: list[Reference] = Reference() 
    
    result: list[Reference] = Reference() 
    
    imagingStudy: list[Reference] = Reference() 
    
    media: list[Media] = Media() 
    
    conclusion: str = None
    
    conclusionCode: "CodeableConcept" = CodeableConcept()
    
    presentedForm: list[Attachment] = Attachment() 
    