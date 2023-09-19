"""
Generated class for ResearchStudy. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.RelatedArtifact import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


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
    