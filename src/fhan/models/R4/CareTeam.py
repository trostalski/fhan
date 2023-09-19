"""
Generated class for CareTeam. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class CareTeam:
    """
    The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.
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
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    name: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    period: "Period" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    member: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    period: "Period" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    managingOrganization: "Reference" = None
    
    telecom: "ContactPoint" = None
    
    note: "Annotation" = None
    