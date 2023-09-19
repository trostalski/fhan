"""
Generated class for Event. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class Event(ModelBase):
    """ Logical Model: A pattern to be followed by resources that represent the performance of some activity, possibly in accordance with a request or service definition.
    :param Identifier identifier: Business Identifier for {{title}}
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param Reference researchStudy: Associated research study
    :param str status: preparation | in-progress | not-done | suspended | aborted | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept code: What was done
    :param Reference subject: Individual service was done for/to
    :param Reference encounter: Encounter created as part of
    :param str occurrencedateTime: When {{title}} occurred/is occurring
    :param Period occurrencedateTime: When {{title}} occurred/is occurring
    :param Timing occurrencedateTime: When {{title}} occurred/is occurring
    :param str recorded: When {{title}} was first captured in the subject's record
    :param bool reportedboolean: Reported rather than primary record
    :param Reference reportedboolean: Reported rather than primary record
    :param Element performer: Who performed {{title}} and what they did
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed {{title}}
    :param Reference location: Where {{title}} occurred
    :param CodeableConcept reasonCode: Why was {{title}} performed?
    :param Reference reasonReference: Why was {{title}} performed?
    :param Annotation note: Comments made about the event
    """
    identifier: "Identifier" = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    researchStudy: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    recorded: str = None
    
    reportedboolean: bool = None
    
    reportedboolean: "Reference" = None
    
    performer: "Element" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    location: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    