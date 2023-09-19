"""
Generated class for MedicationRequest. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class MedicationRequest(ModelBase):
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
    :param str status: active | on-hold | cancelled | completed | entered-in-error | stopped | draft | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param str intent: proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param CodeableConcept category: Type of medication usage
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if request is prohibiting action
    :param bool reportedboolean: Reported rather than primary record
    :param Reference reportedboolean: Reported rather than primary record
    :param CodeableConcept medicationCodeableConcept: Medication to be taken
    :param Reference medicationCodeableConcept: Medication to be taken
    :param Reference subject: Who or group medication request is for
    :param Reference encounter: Encounter created as part of encounter/admission/stay
    :param Reference supportingInformation: Information to support ordering of the medication
    :param str authoredOn: When request was initially authored
    :param Reference requester: Who/What requested the Request
    :param Reference performer: Intended performer of administration
    :param CodeableConcept performerType: Desired kind of performer of the medication administration
    :param Reference recorder: Person who entered the request
    :param CodeableConcept reasonCode: Reason or indication for ordering or not ordering the medication
    :param Reference reasonReference: Condition or observation that supports why the prescription is being written
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Identifier groupIdentifier: Composite request this is part of
    :param CodeableConcept courseOfTherapyType: Overall pattern of medication administration
    :param Reference insurance: Associated insurance coverage
    :param Annotation note: Information about the prescription
    :param Dosage dosageInstruction: How the medication should be taken
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
    :param Reference performer: Intended dispenser
    :param BackboneElement substitution: Any restrictions on medication substitution
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool allowedboolean: Whether substitution is allowed or not
    :param CodeableConcept allowedboolean: Whether substitution is allowed or not
    :param CodeableConcept reason: Why should (not) substitution be made
    :param Reference priorPrescription: An order/prescription that is being replaced
    :param Reference detectedIssue: Clinical Issue with action
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
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    intent: str = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    reportedboolean: bool = None
    
    reportedboolean: "Reference" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    medicationCodeableConcept: "Reference" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    performer: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    recorder: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    groupIdentifier: "Identifier" = None
    
    courseOfTherapyType: "CodeableConcept" = None
    
    insurance: "Reference" = None
    
    note: "Annotation" = None
    
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
    
    performer: "Reference" = None
    
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    allowedboolean: bool = None
    
    allowedboolean: "CodeableConcept" = None
    
    reason: "CodeableConcept" = None
    
    priorPrescription: "Reference" = None
    
    detectedIssue: "Reference" = None
    
    eventHistory: "Reference" = None
    