"""
Generated class for Event. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Element import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Event:
    """ Logical Model: A pattern to be followed by resources that represent the performance of some activity, possibly in accordance with a request or service definition.
    :param Identifier identifier: Business identifier for {{title}}
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param Reference researchStudy: Associated research study
    :param str status: preparation | in-progress | not-done | suspended | aborted | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: High level categorization of {{title}}
    :param CodeableConcept code: What service was done
    :param CodeableReference product: Product used/provided
    :param Reference subject: Individual service was done for/to
    :param Reference encounter: Encounter the {{title}} is part of
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
    :param CodeableReference reason: Why was {{title}} performed?
    :param Annotation note: Comments made about the event
    :param Reference relevantHistory: Key events in history of {{title}}
    
    """
    identifier: "Identifier" = None
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    researchStudy: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    product: "CodeableReference" = None
    
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
    
    reason: "CodeableReference" = None
    
    note: "Annotation" = None
    
    relevantHistory: "Reference" = None
    