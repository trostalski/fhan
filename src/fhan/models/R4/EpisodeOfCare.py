"""
Generated class for EpisodeOfCare. 
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
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class EpisodeOfCare(ModelBase):
    """ An association between a patient and an organization / healthcare provider(s) during which time encounters may occur. The managing organization assumes a level of responsibility for the patient during this time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier(s) relevant for this EpisodeOfCare
    :param str status: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
    :param BackboneElement statusHistory: Past list of status codes (the current status may be included to cover the start date of the status)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: planned | waitlist | active | onhold | finished | cancelled | entered-in-error
    :param Period period: Duration the EpisodeOfCare was in the specified status
    :param CodeableConcept type: Type/class  - e.g. specialist referral, disease management
    :param BackboneElement diagnosis: The list of diagnosis relevant to this episode of care
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference condition: Conditions/problems/diagnoses this episode of care is for
    :param CodeableConcept role: Role that this diagnosis has within the episode of care (e.g. admission, billing, discharge …)
    :param int rank: Ranking of the diagnosis (for each role type)
    :param Reference patient: The patient who is the focus of this episode of care
    :param Reference managingOrganization: Organization that assumes care
    :param Period period: Interval during responsibility is assumed
    :param Reference referralRequest: Originating Referral Request(s)
    :param Reference careManager: Care manager/care coordinator for the patient
    :param Reference team: Other practitioners facilitating this episode of care
    :param Reference account: The set of accounts that may be used for billing for this EpisodeOfCare
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
    
    statusHistory: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    status: str = None
    
    period: "Period" = None
    
    type: "CodeableConcept" = None
    
    diagnosis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    condition: "Reference" = None
    
    role: "CodeableConcept" = None
    
    rank: int = None
    
    patient: "Reference" = None
    
    managingOrganization: "Reference" = None
    
    period: "Period" = None
    
    referralRequest: "Reference" = None
    
    careManager: "Reference" = None
    
    team: "Reference" = None
    
    account: "Reference" = None
    