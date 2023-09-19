"""
Generated class for Request. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Request:
    """ Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param Identifier identifier: Business Identifier for {{title}}
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference replaces: Request(s) replaced by this {{title}}
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str intent: proposal | plan | order (immutable)
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: true if request is prohibiting action
    :param CodeableConcept category: Partitions the {{title}} into one or more categories that can be used to filter searching, to govern access control and/or to guide system behavior.
    :param CodeableConcept code: Service requested/ordered
    :param CodeableReference product: Product requested/ordered
    :param Reference subject: Individual the service is ordered/prohibited for
    :param Reference encounter: Encounter the {{title}} is tied to
    :param str occurrencedateTime: When service should (not) occur
    :param Period occurrencedateTime: When service should (not) occur
    :param Timing occurrencedateTime: When service should (not) occur
    :param str authoredOn: When request was created/transitioned to active
    :param Reference requester: Who/what is requesting service
    :param bool reportedboolean: Reported rather than primary record
    :param Reference reportedboolean: Reported rather than primary record
    :param CodeableConcept performerType: Desired kind of service performer
    :param Reference performer: Specific desired (non)performer
    :param Reference deliverTo: Who should receive result of {{title}}
    :param CodeableReference reason: Why is service (not) needed?
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Extra information to use in performing request
    :param Annotation note: Comments made about {{title}}
    :param Reference relevantHistory: Key events in history of {{title}}
    
    """
    identifier: "Identifier" = None
    
    basedOn: "Reference" = None
    
    replaces: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    intent: str = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    product: "CodeableReference" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    reportedboolean: bool = None
    
    reportedboolean: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    performer: "Reference" = None
    
    deliverTo: "Reference" = None
    
    reason: "CodeableReference" = None
    
    insurance: "Reference" = None
    
    supportingInfo: "Reference" = None
    
    note: "Annotation" = None
    
    relevantHistory: "Reference" = None
    