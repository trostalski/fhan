"""
Generated class for FiveWs. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.generator_models import ModelBase
@dataclass
class FiveWs(ModelBase):
    """ Logical Model: Who What When Where Why - Common pattern for all resources that deals with attribution.
    :param Identifier identifier: Business Identifier
    :param str version: Identifier for this version
    :param str status: Status Field
    :param CodeableConcept _class: Classifier Field
    :param CodeableConcept grade: A field that indicates the potential impact of the content of the resource
    :param CodeableConcept whatCodeableConcept: What this resource is about
    :param Reference subject: Who this resource is about
    :param Reference context: Context for the work described in this resource
    :param str init: When the work described in this resource was started (or will be)
    :param Timing planned: When this resource is planned to occur
    :param str doneDateTime: When the work described in this resource was completed (or will be)
    :param str recorded: When this resource itself was created
    :param Reference author: Who authored the content of the resource
    :param Reference source: Who provided the information in this resource
    :param Reference actor: Who did the work described the resource (or will do)
    :param Reference cause: Who prompted the work described in the resource
    :param Reference witness: Who attests to the content of the resource (individual or org)
    :param Reference who: An actor involved in the work described by this resource
    :param CodeableConcept whereCodeableConcept: The location of the work described
    :param CodeableConcept whyCodeableConcept: Why this work was done
    """
    identifier: list["Identifier"] = None
    
    version: str = None
    
    status: str = None
    
    _class: list["CodeableConcept"] = None
    
    grade: "CodeableConcept" = None
    
    whatCodeableConcept: "CodeableConcept" = None
    
    subject: list["Reference"] = None
    
    context: "Reference" = None
    
    init: str = None
    
    planned: list["Timing"] = None
    
    doneDateTime: str = None
    
    recorded: str = None
    
    author: list["Reference"] = None
    
    source: list["Reference"] = None
    
    actor: list["Reference"] = None
    
    cause: list["Reference"] = None
    
    witness: list["Reference"] = None
    
    who: list["Reference"] = None
    
    whereCodeableConcept: list["CodeableConcept"] = None
    
    whyCodeableConcept: list["CodeableConcept"] = None
    