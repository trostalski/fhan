"""
Generated class for Schedule. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Schedule:
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
    :param CodeableReference serviceType: Specific service
    :param CodeableConcept specialty: Type of specialty needed
    :param str name: Human-readable label
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
    
    serviceType: "CodeableReference" = None
    
    specialty: "CodeableConcept" = None
    
    name: str = None
    
    actor: "Reference" = None
    
    planningHorizon: "Period" = None
    
    comment: str = None
    