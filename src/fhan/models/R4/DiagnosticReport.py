"""
Generated class for DiagnosticReport. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class DiagnosticReport:
    """
    Lipid Lab Report
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
    