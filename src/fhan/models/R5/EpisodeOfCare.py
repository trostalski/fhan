"""
Generated class for EpisodeOfCare. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class EpisodeOfCare:
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
    :param BackboneElement reason: The list of medical reasons that are expected to be addressed during the episode of care
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept use: What the reason value should be used for/as
    :param CodeableReference value: Medical reason to be addressed
    :param BackboneElement diagnosis: The list of medical conditions that were addressed during the episode of care
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference condition: The medical condition that was addressed during the episode of care
    :param CodeableConcept use: Role that this diagnosis has within the episode of care (e.g. admission, billing, discharge …)
    :param Reference patient: The patient who is the focus of this episode of care
    :param Reference managingOrganization: Organization that assumes responsibility for care coordination
    :param Period period: Interval during responsibility is assumed
    :param Reference referralRequest: Originating Referral Request(s)
    :param Reference careManager: Care manager/care coordinator for the patient
    :param Reference careTeam: Other practitioners facilitating this episode of care
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
    
    reason: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    use: "CodeableConcept" = None
    
    value: "CodeableReference" = None
    
    diagnosis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    condition: "CodeableReference" = None
    
    use: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    managingOrganization: "Reference" = None
    
    period: "Period" = None
    
    referralRequest: "Reference" = None
    
    careManager: "Reference" = None
    
    careTeam: "Reference" = None
    
    account: "Reference" = None
    