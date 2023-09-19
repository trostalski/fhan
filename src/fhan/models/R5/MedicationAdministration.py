"""
Generated class for MedicationAdministration. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class MedicationAdministration:
    """ Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion. Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner. This event can also be used to record waste using a status of not-done and the appropriate statusReason.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param Reference basedOn: Plan this is fulfilled by this administration
    :param Reference partOf: Part of referenced event
    :param str status: in-progress | not-done | on-hold | completed | entered-in-error | stopped | unknown
    :param CodeableConcept statusReason: Reason administration not performed
    :param CodeableConcept category: Type of medication administration
    :param CodeableReference medication: What was administered
    :param Reference subject: Who received medication
    :param Reference encounter: Encounter administered as part of
    :param Reference supportingInformation: Additional information to support administration
    :param str occurencedateTime: Specific date/time or interval of time during which the administration took place (or did not take place)
    :param Period occurencedateTime: Specific date/time or interval of time during which the administration took place (or did not take place)
    :param Timing occurencedateTime: Specific date/time or interval of time during which the administration took place (or did not take place)
    :param str recorded: When the MedicationAdministration was first captured in the subject's record
    :param bool isSubPotent: Full dose was not administered
    :param CodeableConcept subPotentReason: Reason full dose was not administered
    :param BackboneElement performer: Who or what performed the medication administration and what type of performance they did
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param CodeableReference actor: Who or what performed the medication administration
    :param CodeableReference reason: Concept, condition or observation that supports why the medication was administered
    :param Reference request: Request administration performed against
    :param CodeableReference device: Device used to administer
    :param Annotation note: Information about the administration
    :param BackboneElement dosage: Details of how medication was taken
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str text: Free text dosage instructions e.g. SIG
    :param CodeableConcept site: Body site administered to
    :param CodeableConcept route: Path of substance into body
    :param CodeableConcept method: How drug was administered
    :param Quantity dose: Amount of medication per dose
    :param Ratio rateRatio: Dose quantity per unit of time
    :param Quantity rateRatio: Dose quantity per unit of time
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
    
    partOf: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    medication: "CodeableReference" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    supportingInformation: "Reference" = None
    
    occurencedateTime: str = None
    
    occurencedateTime: "Period" = None
    
    occurencedateTime: "Timing" = None
    
    recorded: str = None
    
    isSubPotent: bool = None
    
    subPotentReason: "CodeableConcept" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "CodeableReference" = None
    
    reason: "CodeableReference" = None
    
    request: "Reference" = None
    
    device: "CodeableReference" = None
    
    note: "Annotation" = None
    
    dosage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    text: str = None
    
    site: "CodeableConcept" = None
    
    route: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    dose: "Quantity" = None
    
    rateRatio: "Ratio" = None
    
    rateRatio: "Quantity" = None
    
    eventHistory: "Reference" = None
    