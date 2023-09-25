"""
Generated class for Request. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase

class Request(ModelBase):
    """ Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param list['Identifier'] identifier: Business Identifier for {{title}}
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: Fulfills plan, proposal or order
    :param list['Reference'] replaces: Request(s) replaced by this {{title}}
    :param 'Identifier' groupIdentifier: Composite request this is part of
    :param str status: draft | active | suspended | cancelled | completed | entered-in-error | unknown
    :param 'CodeableConcept' statusReason: Reason for current status
    :param str intent: proposal | plan | order (immutable)
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: true if request is prohibiting action
    :param 'CodeableConcept' code: What's being requested/ordered
    :param 'Reference' subject: Individual the service is ordered/prohibited for
    :param 'Reference' encounter: Encounter created as part of
    :param str occurrenceDateTime: When service should (not) occur
    :param 'Period' occurrencePeriod: When service should (not) occur
    :param 'Timing' occurrenceTiming: When service should (not) occur
    :param str authoredOn: When request was created/transitioned to active
    :param 'Reference' requester: Who/what is requesting service
    :param bool reportedBoolean: Reported rather than primary record
    :param 'Reference' reportedReference: Reported rather than primary record
    :param 'CodeableConcept' performerType: Desired kind of service performer
    :param 'Reference' performer: Specific desired (non)performer
    :param list['CodeableConcept'] reasonCode: Why is service (not) needed?
    :param list['Reference'] reasonReference: Why is service (not) needed?
    :param list['Reference'] insurance: Associated insurance coverage
    :param list['Reference'] supportingInfo: Extra information to use in performing request
    :param list['Annotation'] note: Comments made about {{title}}
    :param list['Reference'] relevantHistory: Key events in history of {{title}}
    """
    def __init__(self, resourceType: str = "Request",  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  replaces: list['Reference'] = None,  groupIdentifier: 'Identifier' = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  intent: str = None,  priority: str = None,  doNotPerform: bool = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  authoredOn: str = None,  requester: 'Reference' = None,  reportedBoolean: bool = None,  reportedReference: 'Reference' = None,  performerType: 'CodeableConcept' = None,  performer: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  insurance: list['Reference'] = None,  supportingInfo: list['Reference'] = None,  note: list['Annotation'] = None,  relevantHistory: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "Request"
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.replaces: list['Reference'] = replaces or []
        self.groupIdentifier: 'Identifier' = groupIdentifier 
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.intent: str = intent 
        self.priority: str = priority 
        self.doNotPerform: bool = doNotPerform 
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.authoredOn: str = authoredOn 
        self.requester: 'Reference' = requester 
        self.reportedBoolean: bool = reportedBoolean 
        self.reportedReference: 'Reference' = reportedReference 
        self.performerType: 'CodeableConcept' = performerType 
        self.performer: 'Reference' = performer 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.insurance: list['Reference'] = insurance or []
        self.supportingInfo: list['Reference'] = supportingInfo or []
        self.note: list['Annotation'] = note or []
        self.relevantHistory: list['Reference'] = relevantHistory or []
        