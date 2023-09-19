"""
Generated class for CommunicationRequest. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class CommunicationRequest:
    """ A request to convey information; e.g. the CDS system proposes that an alert be sent to a responsible provider, the CDS system proposes that the public health agency be notified about a reportable condition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param Reference basedOn: Fulfills plan or proposal
    :param Reference replaces: Request(s) replaced by this request
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param CodeableConcept category: Message category
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if request is prohibiting action
    :param CodeableConcept medium: A channel of communication
    :param Reference subject: Focus of message
    :param Reference about: Resources that pertain to this communication request
    :param Reference encounter: The Encounter during which this CommunicationRequest was created
    :param BackboneElement payload: Message payload
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment contentAttachment: Message part content
    :param Reference contentAttachment: Message part content
    :param CodeableConcept contentAttachment: Message part content
    :param str occurrencedateTime: When scheduled
    :param Period occurrencedateTime: When scheduled
    :param str authoredOn: When request transitioned to being actionable
    :param Reference requester: Who asks for the information to be shared
    :param Reference recipient: Who to share the information with
    :param Reference informationProvider: Who should share the information
    :param CodeableReference reason: Why is communication needed?
    :param Annotation note: Comments made about communication request
    
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
    
    intent: str = None
    
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
    
    contentAttachment: "Attachment" = None
    
    contentAttachment: "Reference" = None
    
    contentAttachment: "CodeableConcept" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    recipient: "Reference" = None
    
    informationProvider: "Reference" = None
    
    reason: "CodeableReference" = None
    
    note: "Annotation" = None
    