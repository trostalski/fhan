"""
Generated class for Event. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Element import *
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
    :param str occurrenceDateTime: When {{title}} occurred/is occurring
    :param str recorded: When {{title}} was first captured in the subject's record
    :param bool reportedBoolean: Reported rather than primary record
    :param Element performer: Who performed {{title}} and what they did
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed {{title}}
    :param Reference location: Where {{title}} occurred
    :param CodeableConcept reasonCode: Why was {{title}} performed?
    :param Reference reasonReference: Why was {{title}} performed?
    :param Annotation note: Comments made about the event
    """

    resourceType: str = "Event"
    identifier: list[Identifier] = Identifier() 
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: list[Reference] = Reference() 
    
    partOf: list[Reference] = Reference() 
    
    researchStudy: list[Reference] = Reference() 
    
    status: str = None
    
    statusReason: "CodeableConcept" = CodeableConcept()
    
    code: "CodeableConcept" = CodeableConcept()
    
    subject: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    occurrenceDateTime: str = None
    
    recorded: str = None
    
    reportedBoolean: bool = None
    
    performer: list[Element] = Element() 
    
    function: "CodeableConcept" = CodeableConcept()
    
    actor: "Reference" = Reference()
    
    location: "Reference" = Reference()
    
    reasonCode: list[CodeableConcept] = CodeableConcept() 
    
    reasonReference: list[Reference] = Reference() 
    
    note: list[Annotation] = Annotation() 
    