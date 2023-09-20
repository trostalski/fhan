"""
Generated class for MedicationRequest. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Period import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class InitialFill(Element):
    """ Indicates the quantity or duration for the first dispense of the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: First fill quantity
    :param Duration duration: First fill duration
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    quantity: "Quantity" = None
    duration: "Duration" = None
    
  
    
    
@dataclass
class DispenseRequest(Element):
    """ Indicates the specific details for the dispense or medication supply part of a medication request (also known as a Medication Prescription or Medication Order).  Note that this information is not always sent with the order.  There may be in some settings (e.g. hospitals) institutional or system support for completing the dispense details in the pharmacy department.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param InitialFill initialFill: First fill details
    :param Duration dispenseInterval: Minimum period of time between dispenses
    :param Period validityPeriod: Time period supply is authorized for
    :param int numberOfRepeatsAllowed: Number of refills authorized
    :param Quantity quantity: Amount of medication to supply per dispense
    :param Duration expectedSupplyDuration: Number of days supply per dispense
    :param Reference performer: Intended dispenser
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    initialFill: "InitialFill" = None
    dispenseInterval: "Duration" = None
    validityPeriod: "Period" = None
    
    numberOfRepeatsAllowed: int = None
    quantity: "Quantity" = None
    expectedSupplyDuration: "Duration" = None
    performer: "Reference" = None
    

    
    
@dataclass
class Substitution(Element):
    """ Indicates whether or not substitution can or should be part of the dispense. In some cases, substitution must happen, in other cases substitution must not happen. This block explains the prescriber's intent. If nothing is specified substitution may be done.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool allowedBoolean: Whether substitution is allowed or not
    :param CodeableConcept reason: Why should (not) substitution be made
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    allowedBoolean: bool = None
    reason: "CodeableConcept" = None
    
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
    :param bool reportedBoolean: Reported rather than primary record
    :param CodeableConcept medicationCodeableConcept: Medication to be taken
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
    :param DispenseRequest dispenseRequest: Medication supply authorization
    :param Substitution substitution: Any restrictions on medication substitution
    :param Reference priorPrescription: An order/prescription that is being replaced
    :param Reference detectedIssue: Clinical Issue with action
    :param Reference eventHistory: A list of events of interest in the lifecycle
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    intent: str = None
    
    category: list["CodeableConcept"] = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    reportedBoolean: bool = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: list["Reference"] = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    performer: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    recorder: "Reference" = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: list["Reference"] = None
    
    groupIdentifier: "Identifier" = None
    
    courseOfTherapyType: "CodeableConcept" = None
    
    insurance: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    dosageInstruction: list["Dosage"] = None
    
    dispenseRequest: "DispenseRequest" = None
    
    substitution: "Substitution" = None
    
    priorPrescription: "Reference" = None
    
    detectedIssue: list["Reference"] = None
    
    eventHistory: list["Reference"] = None
    