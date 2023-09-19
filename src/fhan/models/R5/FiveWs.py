"""
Generated class for FiveWs. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class FiveWs:
    """ Logical Model: Who What When Where Why - Common pattern for all resources that deals with attribution.
    :param Identifier identifier: Business Identifier
    :param str version: Identifier for this version
    :param str status: Status Field
    :param CodeableConcept class: Classifier Field
    :param CodeableConcept grade: A field that indicates the potential impact of the content of the resource
    :param CodeableConcept whatCodeableConcept: What this resource is about
    :param Reference whatCodeableConcept: What this resource is about
    :param Reference subject: Who this resource is about
    :param Reference context: Context for the work described in this resource
    :param str init: When the work described in this resource was started (or will be)
    :param Timing planned: When this resource is planned to occur
    :param str donedateTime: When the work described in this resource was completed (or will be)
    :param Period donedateTime: When the work described in this resource was completed (or will be)
    :param str recorded: When this resource itself was created
    :param Reference author: Who authored the content of the resource
    :param Reference source: Who provided the information in this resource
    :param Reference actor: Who did the work described the resource (or will do)
    :param Reference cause: Who prompted the work described in the resource
    :param Reference witness: Who attests to the content of the resource (individual or org)
    :param Reference who: An actor involved in the work described by this resource
    :param CodeableConcept whereCodeableConcept: The location of the work described
    :param Reference whereCodeableConcept: The location of the work described
    :param CodeableConcept whyCodeableConcept: Why this work was done
    :param Reference whyCodeableConcept: Why this work was done
    
    """
    identifier: "Identifier" = None
    
    version: str = None
    
    status: str = None
    
    class: "CodeableConcept" = None
    
    grade: "CodeableConcept" = None
    
    whatCodeableConcept: "CodeableConcept" = None
    
    whatCodeableConcept: "Reference" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    init: str = None
    
    planned: "Timing" = None
    
    donedateTime: str = None
    
    donedateTime: "Period" = None
    
    recorded: str = None
    
    author: "Reference" = None
    
    source: "Reference" = None
    
    actor: "Reference" = None
    
    cause: "Reference" = None
    
    witness: "Reference" = None
    
    who: "Reference" = None
    
    whereCodeableConcept: "CodeableConcept" = None
    
    whereCodeableConcept: "Reference" = None
    
    whyCodeableConcept: "CodeableConcept" = None
    
    whyCodeableConcept: "Reference" = None
    