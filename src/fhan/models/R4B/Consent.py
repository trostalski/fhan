"""
Generated class for Consent. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Consent:
    """
    A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
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
    
    scope: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    dateTime: str = None
    
    performer: "Reference" = None
    
    organization: "Reference" = None
    
    sourceAttachment: "Attachment" = None
    
    sourceAttachment: "Reference" = None
    
    policy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    authority: str = None
    
    uri: str = None
    
    policyRule: "CodeableConcept" = None
    
    verification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    verified: bool = None
    
    verifiedWith: "Reference" = None
    
    verificationDate: str = None
    
    provision: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    period: "Period" = None
    
    actor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    reference: "Reference" = None
    
    action: "CodeableConcept" = None
    
    securityLabel: "Coding" = None
    
    purpose: "Coding" = None
    
    class: "Coding" = None
    
    code: "CodeableConcept" = None
    
    dataPeriod: "Period" = None
    
    data: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    meaning: str = None
    
    reference: "Reference" = None
    
    provision: "BackboneElement" = None
    