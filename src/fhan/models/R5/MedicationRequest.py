"""
Generated class for MedicationRequest. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class MedicationRequest:
    """ An order or request for both supply of the medication and the instructions for administration of the medication to a patient. The resource is called "MedicationRequest" rather than "MedicationPrescription" or "MedicationOrder" to generalize the use across inpatient and outpatient settings, including care plans, etc., and to harmonize with workflow patterns.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External ids for this request
    :param Reference basedOn: A plan or request that is fulfilled in whole or in part by this medication request
    :param Reference priorPrescription: Reference to an order/prescription that is being replaced by this MedicationRequest
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: active | on-hold | ended | stopped | completed | cancelled | entered-in-error | draft | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str statusChanged: When the status was changed
    :param str intent: proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param CodeableConcept category: Grouping or category of medication request
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if patient is to stop taking or not to start taking the medication
    :param CodeableReference medication: Medication to be taken
    :param Reference subject: Individual or group for whom the medication has been requested
    :param Reference informationSource: The person or organization who provided the information about this request, if the source is someone other than the requestor
    :param Reference encounter: Encounter created as part of encounter/admission/stay
    :param Reference supportingInformation: Information to support fulfilling of the medication
    :param str authoredOn: When request was initially authored
    :param Reference requester: Who/What requested the Request
    :param bool reported: Reported rather than primary record
    :param CodeableConcept performerType: Desired kind of performer of the medication administration
    :param Reference performer: Intended performer of administration
    :param CodeableReference device: Intended type of device for the administration
    :param Reference recorder: Person who entered the request
    :param CodeableReference reason: Reason or indication for ordering or not ordering the medication
    :param CodeableConcept courseOfTherapyType: Overall pattern of medication administration
    :param Reference insurance: Associated insurance coverage
    :param Annotation note: Information about the prescription
    :param str renderedDosageInstruction: Full representation of the dosage instructions
    :param Period effectiveDosePeriod: Period over which the medication is to be taken
    :param Dosage dosageInstruction: Specific instructions for how the medication should be taken
    :param BackboneElement dispenseRequest: Medication supply authorization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement initialFill: First fill details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: First fill quantity
    :param Duration duration: First fill duration
    :param Duration dispenseInterval: Minimum period of time between dispenses
    :param Period validityPeriod: Time period supply is authorized for
    :param int numberOfRepeatsAllowed: Number of refills authorized
    :param Quantity quantity: Amount of medication to supply per dispense
    :param Duration expectedSupplyDuration: Number of days supply per dispense
    :param Reference dispenser: Intended performer of dispense
    :param Annotation dispenserInstruction: Additional information for the dispenser
    :param CodeableConcept doseAdministrationAid: Type of adherence packaging to use for the dispense
    :param BackboneElement substitution: Any restrictions on medication substitution
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool allowedboolean: Whether substitution is allowed or not
    :param CodeableConcept allowedboolean: Whether substitution is allowed or not
    :param CodeableConcept reason: Why should (not) substitution be made
    :param Reference eventHistory: A list of events of interest in the lifecycle
    
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
    
    basedOn: "Reference" = None
    
    priorPrescription: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    statusChanged: str = None
    
    intent: str = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    medication: "CodeableReference" = None
    
    subject: "Reference" = None
    
    informationSource: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    reported: bool = None
    
    performerType: "CodeableConcept" = None
    
    performer: "Reference" = None
    
    device: "CodeableReference" = None
    
    recorder: "Reference" = None
    
    reason: "CodeableReference" = None
    
    courseOfTherapyType: "CodeableConcept" = None
    
    insurance: "Reference" = None
    
    note: "Annotation" = None
    
    renderedDosageInstruction: str = None
    
    effectiveDosePeriod: "Period" = None
    
    dosageInstruction: "Dosage" = None
    
    dispenseRequest: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    initialFill: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    quantity: "Quantity" = None
    
    duration: "Duration" = None
    
    dispenseInterval: "Duration" = None
    
    validityPeriod: "Period" = None
    
    numberOfRepeatsAllowed: int = None
    
    quantity: "Quantity" = None
    
    expectedSupplyDuration: "Duration" = None
    
    dispenser: "Reference" = None
    
    dispenserInstruction: "Annotation" = None
    
    doseAdministrationAid: "CodeableConcept" = None
    
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    allowedboolean: bool = None
    
    allowedboolean: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    eventHistory: "Reference" = None
    