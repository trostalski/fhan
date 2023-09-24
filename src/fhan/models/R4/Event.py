"""
Generated class for Event. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Timing import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

class Event(ModelBase):
    """ Logical Model: A pattern to be followed by resources that represent the performance of some activity, possibly in accordance with a request or service definition.
    :param list['Identifier'] identifier: Business Identifier for {{title}}
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: Fulfills plan, proposal or order
    :param list['Reference'] partOf: Part of referenced event
    :param list['Reference'] researchStudy: Associated research study
    :param str status: preparation | in-progress | not-done | suspended | aborted | completed | entered-in-error | unknown
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' code: What was done
    :param 'Reference' subject: Individual service was done for/to
    :param 'Reference' encounter: Encounter created as part of
    :param str occurrenceDateTime: When {{title}} occurred/is occurring
    :param str recorded: When {{title}} was first captured in the subject's record
    :param bool reportedBoolean: Reported rather than primary record
    :param list['Element'] performer: Who performed {{title}} and what they did
    :param 'CodeableConcept' function: Type of performance
    :param 'Reference' actor: Who performed {{title}}
    :param 'Reference' location: Where {{title}} occurred
    :param list['CodeableConcept'] reasonCode: Why was {{title}} performed?
    :param list['Reference'] reasonReference: Why was {{title}} performed?
    :param list['Annotation'] note: Comments made about the event
    """
    def __init__(self, resourceType: str = "Event",  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  partOf: list['Reference'] = None,  researchStudy: list['Reference'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  recorded: str = None,  reportedBoolean: bool = None,  performer: list['Element'] = None,  function: 'CodeableConcept' = None,  actor: 'Reference' = None,  location: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "Event"
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.partOf: list['Reference'] = partOf or []
        self.researchStudy: list['Reference'] = researchStudy or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.recorded: str = recorded 
        self.reportedBoolean: bool = reportedBoolean 
        self.performer: list['Element'] = performer or []
        self.function: 'CodeableConcept' = function 
        self.actor: 'Reference' = actor 
        self.location: 'Reference' = location 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        