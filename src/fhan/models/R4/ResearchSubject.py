"""
Generated class for ResearchSubject. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class ResearchSubject(ModelBase):
    """ A physical entity which is the primary unit of operational and/or administrative interest in a study.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for research subject in a study
    :param str status: candidate | eligible | follow-up | ineligible | not-registered | off-study | on-study | on-study-intervention | on-study-observation | pending-on-study | potential-candidate | screening | withdrawn
    :param Period period: Start and end of participation
    :param Reference study: Study subject is part of
    :param Reference individual: Who is part of study
    :param str assignedArm: What path should be followed
    :param str actualArm: What path was followed
    :param Reference consent: Agreement to participate in study
    """

    resourceType: str = "ResearchSubject"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    period: "Period" = Period()
    
    study: "Reference" = Reference()
    
    individual: "Reference" = Reference()
    
    assignedArm: str = None
    
    actualArm: str = None
    
    consent: "Reference" = Reference()
    