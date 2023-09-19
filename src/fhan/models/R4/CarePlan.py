"""
Generated class for CarePlan. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class CarePlan(ModelBase):
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
    :param Reference basedOn: Fulfills CarePlan
    :param Reference replaces: CarePlan replaced by this CarePlan
    :param Reference partOf: Part of referenced CarePlan
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | order | option
    :param CodeableConcept category: Type of plan
    :param str title: Human-friendly name for the care plan
    :param str description: Summary of nature of plan
    :param Reference subject: Who the care plan is for
    :param Reference encounter: Encounter created as part of
    :param Period period: Time period plan covers
    :param str created: Date record was first recorded
    :param Reference author: Who is the designated responsible party
    :param Reference contributor: Who provided the content of the care plan
    :param Reference careTeam: Who's involved in plan?
    :param Reference addresses: Health issues this plan addresses
    :param Reference supportingInfo: Information considered as part of plan
    :param Reference goal: Desired outcome of plan
    :param BackboneElement activity: Action to occur as part of plan
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept outcomeCodeableConcept: Results of the activity
    :param Reference outcomeReference: Appointment, Encounter, Procedure, etc.
    :param Annotation progress: Comments about the activity status/progress
    :param Reference reference: Activity details defined in specific resource
    :param BackboneElement detail: In-line definition of activity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: Appointment | CommunicationRequest | DeviceRequest | MedicationRequest | NutritionOrder | Task | ServiceRequest | VisionPrescription
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param CodeableConcept code: Detail type of activity
    :param CodeableConcept reasonCode: Why activity should be done or why activity was prohibited
    :param Reference reasonReference: Why activity is needed
    :param Reference goal: Goals this activity relates to
    :param str status: not-started | scheduled | in-progress | on-hold | completed | cancelled | stopped | unknown | entered-in-error
    :param CodeableConcept statusReason: Reason for current status
    :param bool doNotPerform: If true, activity is prohibiting action
    :param Timing scheduledTiming: When activity is to occur
    :param Period scheduledTiming: When activity is to occur
    :param str scheduledTiming: When activity is to occur
    :param Reference location: Where it should happen
    :param Reference performer: Who will be responsible?
    :param CodeableConcept productCodeableConcept: What is to be administered/supplied
    :param Reference productCodeableConcept: What is to be administered/supplied
    :param Quantity dailyAmount: How to consume/day?
    :param Quantity quantity: How much to administer/supply/consume
    :param str description: Extra info describing activity to perform
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
    
    author: "Reference" = None
    
    contributor: "Reference" = None
    
    careTeam: "Reference" = None
    
    addresses: "Reference" = None
    
    supportingInfo: "Reference" = None
    
    goal: "Reference" = None
    
    activity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    outcomeCodeableConcept: "CodeableConcept" = None
    
    outcomeReference: "Reference" = None
    
    progress: "Annotation" = None
    
    reference: "Reference" = None
    
    detail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    kind: str = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    code: "CodeableConcept" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    goal: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    doNotPerform: bool = None
    
    scheduledTiming: "Timing" = None
    
    scheduledTiming: "Period" = None
    
    scheduledTiming: str = None
    
    location: "Reference" = None
    
    performer: "Reference" = None
    
    productCodeableConcept: "CodeableConcept" = None
    
    productCodeableConcept: "Reference" = None
    
    dailyAmount: "Quantity" = None
    
    quantity: "Quantity" = None
    
    description: str = None
    
    note: "Annotation" = None
    