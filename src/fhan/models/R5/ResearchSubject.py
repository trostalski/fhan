"""
Generated class for ResearchSubject. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ResearchSubject:
    """ A ResearchSubject is a participant or object which is the recipient of investigative activities in a research study.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for research subject in a study
    :param str status: draft | active | retired | unknown
    :param BackboneElement progress: Subject status
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: state | milestone
    :param CodeableConcept subjectState: candidate | eligible | follow-up | ineligible | not-registered | off-study | on-study | on-study-intervention | on-study-observation | pending-on-study | potential-candidate | screening | withdrawn
    :param CodeableConcept milestone: SignedUp | Screened | Randomized
    :param CodeableConcept reason: State change reason
    :param str startDate: State change date
    :param str endDate: State change date
    :param Period period: Start and end of participation
    :param Reference study: Study subject is part of
    :param Reference subject: Who or what is part of study
    :param str assignedComparisonGroup: What path should be followed
    :param str actualComparisonGroup: What path was followed
    :param Reference consent: Agreement to participate in study
    
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
    
    status: str = None
    
    progress: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    subjectState: "CodeableConcept" = None
    
    milestone: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    startDate: str = None
    
    endDate: str = None
    
    period: "Period" = None
    
    study: "Reference" = None
    
    subject: "Reference" = None
    
    assignedComparisonGroup: str = None
    
    actualComparisonGroup: str = None
    
    consent: "Reference" = None
    