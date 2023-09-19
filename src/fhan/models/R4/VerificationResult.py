"""
Generated class for VerificationResult. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Meta import *


@dataclass
class VerificationResult:
    """
    Describes validation requirements, source(s), status and dates for one or more elements.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    target: "Reference" = None
    
    targetLocation: str = None
    
    need: "CodeableConcept" = None
    
    status: str = None
    
    statusDate: str = None
    
    validationType: "CodeableConcept" = None
    
    validationProcess: "CodeableConcept" = None
    
    frequency: "Timing" = None
    
    lastPerformed: str = None
    
    nextScheduled: str = None
    
    failureAction: "CodeableConcept" = None
    
    primarySource: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    who: "Reference" = None
    
    type: "CodeableConcept" = None
    
    communicationMethod: "CodeableConcept" = None
    
    validationStatus: "CodeableConcept" = None
    
    validationDate: str = None
    
    canPushUpdates: "CodeableConcept" = None
    
    pushTypeAvailable: "CodeableConcept" = None
    
    attestation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    who: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    communicationMethod: "CodeableConcept" = None
    
    date: str = None
    
    sourceIdentityCertificate: str = None
    
    proxyIdentityCertificate: str = None
    
    proxySignature: "Signature" = None
    
    sourceSignature: "Signature" = None
    
    validator: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    organization: "Reference" = None
    
    identityCertificate: str = None
    
    attestationSignature: "Signature" = None
    