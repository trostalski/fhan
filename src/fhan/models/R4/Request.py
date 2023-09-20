"""
Generated class for Request. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.generator_models import ModelBase

@dataclass
class Request(ModelBase):
    """ Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param Identifier identifier: Business Identifier for {{title}}
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference replaces: Request(s) replaced by this {{title}}
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: draft | active | suspended | cancelled | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str intent: proposal | plan | order (immutable)
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: true if request is prohibiting action
    :param CodeableConcept code: What's being requested/ordered
    :param Reference subject: Individual the service is ordered/prohibited for
    :param Reference encounter: Encounter created as part of
    :param str occurrenceDateTime: When service should (not) occur
    :param str authoredOn: When request was created/transitioned to active
    :param Reference requester: Who/what is requesting service
    :param bool reportedBoolean: Reported rather than primary record
    :param CodeableConcept performerType: Desired kind of service performer
    :param Reference performer: Specific desired (non)performer
    :param CodeableConcept reasonCode: Why is service (not) needed?
    :param Reference reasonReference: Why is service (not) needed?
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Extra information to use in performing request
    :param Annotation note: Comments made about {{title}}
    :param Reference relevantHistory: Key events in history of {{title}}
    """

    resourceType: str = "Request"
    identifier: list["Identifier"] = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: list["Reference"] = None
    
    replaces: list["Reference"] = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    intent: str = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrenceDateTime: str = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    reportedBoolean: bool = None
    
    performerType: "CodeableConcept" = None
    
    performer: "Reference" = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    insurance: list["Reference"] = None
    
    supportingInfo: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    relevantHistory: list["Reference"] = None
    