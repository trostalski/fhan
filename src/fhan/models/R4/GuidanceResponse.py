"""
Generated class for GuidanceResponse. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class GuidanceResponse:
    """
    A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    requestIdentifier: "Identifier" = None
    
    identifier: "Identifier" = None
    
    moduleuri: str = None
    
    moduleuri: str = None
    
    moduleuri: "CodeableConcept" = None
    
    status: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrenceDateTime: str = None
    
    performer: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    
    evaluationMessage: "Reference" = None
    
    outputParameters: "Reference" = None
    
    result: "Reference" = None
    
    dataRequirement: "DataRequirement" = None
    