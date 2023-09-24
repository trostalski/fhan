"""
Generated class for FiveWs. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Timing import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

class FiveWs(ModelBase):
    """ Logical Model: Who What When Where Why - Common pattern for all resources that deals with attribution.
    :param list['Identifier'] identifier: Business Identifier
    :param str version: Identifier for this version
    :param str status: Status Field
    :param list['CodeableConcept'] _class: Classifier Field
    :param 'CodeableConcept' grade: A field that indicates the potential impact of the content of the resource
    :param 'CodeableConcept' whatCodeableConcept: What this resource is about
    :param list['Reference'] subject: Who this resource is about
    :param 'Reference' context: Context for the work described in this resource
    :param str init: When the work described in this resource was started (or will be)
    :param list['Timing'] planned: When this resource is planned to occur
    :param str doneDateTime: When the work described in this resource was completed (or will be)
    :param str recorded: When this resource itself was created
    :param list['Reference'] author: Who authored the content of the resource
    :param list['Reference'] source: Who provided the information in this resource
    :param list['Reference'] actor: Who did the work described the resource (or will do)
    :param list['Reference'] cause: Who prompted the work described in the resource
    :param list['Reference'] witness: Who attests to the content of the resource (individual or org)
    :param list['Reference'] who: An actor involved in the work described by this resource
    :param list['CodeableConcept'] whereCodeableConcept: The location of the work described
    :param list['CodeableConcept'] whyCodeableConcept: Why this work was done
    """
    def __init__(self, resourceType: str = "FiveWs",  identifier: list['Identifier'] = None,  version: str = None,  status: str = None,  _class: list['CodeableConcept'] = None,  grade: 'CodeableConcept' = None,  whatCodeableConcept: 'CodeableConcept' = None,  subject: list['Reference'] = None,  context: 'Reference' = None,  init: str = None,  planned: list['Timing'] = None,  doneDateTime: str = None,  recorded: str = None,  author: list['Reference'] = None,  source: list['Reference'] = None,  actor: list['Reference'] = None,  cause: list['Reference'] = None,  witness: list['Reference'] = None,  who: list['Reference'] = None,  whereCodeableConcept: list['CodeableConcept'] = None,  whyCodeableConcept: list['CodeableConcept'] = None, ):
        self.resourceType: str = resourceType or "FiveWs"
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.status: str = status 
        self._class: list['CodeableConcept'] = _class or []
        self.grade: 'CodeableConcept' = grade 
        self.whatCodeableConcept: 'CodeableConcept' = whatCodeableConcept 
        self.subject: list['Reference'] = subject or []
        self.context: 'Reference' = context 
        self.init: str = init 
        self.planned: list['Timing'] = planned or []
        self.doneDateTime: str = doneDateTime 
        self.recorded: str = recorded 
        self.author: list['Reference'] = author or []
        self.source: list['Reference'] = source or []
        self.actor: list['Reference'] = actor or []
        self.cause: list['Reference'] = cause or []
        self.witness: list['Reference'] = witness or []
        self.who: list['Reference'] = who or []
        self.whereCodeableConcept: list['CodeableConcept'] = whereCodeableConcept or []
        self.whyCodeableConcept: list['CodeableConcept'] = whyCodeableConcept or []
        