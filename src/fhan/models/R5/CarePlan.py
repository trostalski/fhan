"""
Generated class for CarePlan. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class CarePlan:
    """ Describes the intention of how one or more practitioners intend to deliver care for a particular patient, group or community for a period of time, possibly limited to care for a specific condition or set of conditions.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this plan
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference replaces: CarePlan replaced by this CarePlan
    :param Reference partOf: Part of referenced CarePlan
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | order | option | directive
    :param CodeableConcept category: Type of plan
    :param str title: Human-friendly name for the care plan
    :param str description: Summary of nature of plan
    :param Reference subject: Who the care plan is for
    :param Reference encounter: The Encounter during which this CarePlan was created
    :param Period period: Time period plan covers
    :param str created: Date record was first recorded
    :param Reference custodian: Who is the designated responsible party
    :param Reference contributor: Who provided the content of the care plan
    :param Reference careTeam: Who's involved in plan?
    :param CodeableReference addresses: Health issues this plan addresses
    :param Reference supportingInfo: Information considered as part of plan
    :param Reference goal: Desired outcome of plan
    :param BackboneElement activity: Action to occur or has occurred as part of plan
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference performedActivity: Results of the activity (concept, or Appointment, Encounter, Procedure, etc.)
    :param Annotation progress: Comments about the activity status/progress
    :param Reference plannedActivityReference: Activity that is intended to be part of the care plan
    :param Annotation note: Comments about the plan
    
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    replaces: "Reference" = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    intent: str = None
    
    category: "CodeableConcept" = None
    
    title: str = None
    
    description: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    period: "Period" = None
    
    created: str = None
    
    custodian: "Reference" = None
    
    contributor: "Reference" = None
    
    careTeam: "Reference" = None
    
    addresses: "CodeableReference" = None
    
    supportingInfo: "Reference" = None
    
    goal: "Reference" = None
    
    activity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    performedActivity: "CodeableReference" = None
    
    progress: "Annotation" = None
    
    plannedActivityReference: "Reference" = None
    
    note: "Annotation" = None
    