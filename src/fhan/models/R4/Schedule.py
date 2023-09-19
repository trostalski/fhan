"""
Generated class for Schedule. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase


@dataclass
class Schedule(ModelBase):
    """ A container for slots of time that may be available for booking appointments.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this item
    :param bool active: Whether this schedule is in active use
    :param CodeableConcept serviceCategory: High-level category
    :param CodeableConcept serviceType: Specific service
    :param CodeableConcept specialty: Type of specialty needed
    :param Reference actor: Resource(s) that availability information is being provided for
    :param Period planningHorizon: Period of time covered by schedule
    :param str comment: Comments on availability
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    active: bool = None
    
    serviceCategory: "CodeableConcept" = None
    
    serviceType: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    planningHorizon: "Period" = None
    
    comment: str = None
    