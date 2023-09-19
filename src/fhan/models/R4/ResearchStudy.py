"""
Generated class for ResearchStudy. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class ResearchStudy:
    """
    A process where a researcher or organization plans and then executes a series of steps intended to increase the field of healthcare-related knowledge.  This includes studies of safety, efficacy, comparative effectiveness and other information about medications, devices, therapies and other interventional and investigative techniques.  A ResearchStudy involves the gathering of information about human or animal subjects.
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
    
    title: str = None
    
    protocol: "Reference" = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    primaryPurposeType: "CodeableConcept" = None
    
    phase: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    focus: "CodeableConcept" = None
    
    condition: "CodeableConcept" = None
    
    contact: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    keyword: "CodeableConcept" = None
    
    location: "CodeableConcept" = None
    
    description: str = None
    
    enrollment: "Reference" = None
    
    period: "Period" = None
    
    sponsor: "Reference" = None
    
    principalInvestigator: "Reference" = None
    
    site: "Reference" = None
    
    reasonStopped: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    arm: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    objective: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    