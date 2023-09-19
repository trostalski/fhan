"""
Generated class for Communication. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Communication(ModelBase):
    """ An occurrence of information being transmitted; e.g. an alert that was sent to a responsible provider, a public health agency that was notified about a reportable condition.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Request fulfilled by this communication
    :param Reference partOf: Part of this action
    :param Reference inResponseTo: Reply to
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: Message category
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept medium: A channel of communication
    :param Reference subject: Focus of message
    :param CodeableConcept topic: Description of the purpose/content
    :param Reference about: Resources that pertain to this communication
    :param Reference encounter: Encounter created as part of
    :param str sent: When sent
    :param str received: When received
    :param Reference recipient: Message recipient
    :param Reference sender: Message sender
    :param CodeableConcept reasonCode: Indication for message
    :param Reference reasonReference: Why was communication done?
    :param BackboneElement payload: Message payload
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str contentstring: Message part content
    :param Attachment contentstring: Message part content
    :param Reference contentstring: Message part content
    :param Annotation note: Comments made about the communication
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    inResponseTo: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    medium: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    topic: "CodeableConcept" = None
    
    about: "Reference" = None
    
    encounter: "Reference" = None
    
    sent: str = None
    
    received: str = None
    
    recipient: "Reference" = None
    
    sender: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    payload: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    contentstring: str = None
    
    contentstring: "Attachment" = None
    
    contentstring: "Reference" = None
    
    note: "Annotation" = None
    