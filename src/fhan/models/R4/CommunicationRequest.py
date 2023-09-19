"""
Generated class for CommunicationRequest. 
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
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class CommunicationRequest:
    """
    A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.
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
    
    replaces: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    medium: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    about: "Reference" = None
    
    encounter: "Reference" = None
    
    payload: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    contentstring: str = None
    
    contentstring: "Attachment" = None
    
    contentstring: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    recipient: "Reference" = None
    
    sender: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    