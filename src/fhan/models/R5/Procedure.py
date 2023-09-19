"""
Generated class for Procedure. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Age import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class Procedure:
    """ An action that is or was performed on or for a patient, practitioner, device, organization, or location. For example, this can be a physical intervention on a patient like an operation, or less invasive like long term services, counseling, or hypnotherapy.  This can be a quality or safety inspection for a location, organization, or device.  This can be an accreditation procedure on a practitioner for licensing.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Identifiers for this procedure
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: A request for this procedure
    :param Reference partOf: Part of referenced event
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: Classification of the procedure
    :param CodeableConcept code: Identification of the procedure
    :param Reference subject: Individual or entity the procedure was performed on
    :param Reference focus: Who is the target of the procedure when it is not the subject of record only
    :param Reference encounter: The Encounter during which this Procedure was created
    :param str occurrencedateTime: When the procedure occurred or is occurring
    :param Period occurrencedateTime: When the procedure occurred or is occurring
    :param str occurrencedateTime: When the procedure occurred or is occurring
    :param Age occurrencedateTime: When the procedure occurred or is occurring
    :param Range occurrencedateTime: When the procedure occurred or is occurring
    :param Timing occurrencedateTime: When the procedure occurred or is occurring
    :param str recorded: When the procedure was first captured in the subject's record
    :param Reference recorder: Who recorded the procedure
    :param bool reportedboolean: Reported rather than primary record
    :param Reference reportedboolean: Reported rather than primary record
    :param BackboneElement performer: Who performed the procedure and what they did
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the procedure
    :param Reference onBehalfOf: Organization the device or practitioner was acting for
    :param Period period: When the performer performed the procedure
    :param Reference location: Where the procedure happened
    :param CodeableReference reason: The justification that the procedure was performed
    :param CodeableConcept bodySite: Target body sites
    :param CodeableConcept outcome: The result of procedure
    :param Reference report: Any report resulting from the procedure
    :param CodeableReference complication: Complication following the procedure
    :param CodeableConcept followUp: Instructions for follow up
    :param Annotation note: Additional information about the procedure
    :param BackboneElement focalDevice: Manipulated, implanted, or removed device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept action: Kind of change to device
    :param Reference manipulated: Device that was changed
    :param CodeableReference used: Items used during procedure
    :param Reference supportingInfo: Extra information relevant to the procedure
    
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
    
    partOf: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    focus: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Age" = None
    
    occurrencedateTime: "Range" = None
    
    occurrencedateTime: "Timing" = None
    
    recorded: str = None
    
    recorder: "Reference" = None
    
    reportedboolean: bool = None
    
    reportedboolean: "Reference" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    period: "Period" = None
    
    location: "Reference" = None
    
    reason: "CodeableReference" = None
    
    bodySite: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    report: "Reference" = None
    
    complication: "CodeableReference" = None
    
    followUp: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    focalDevice: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    action: "CodeableConcept" = None
    
    manipulated: "Reference" = None
    
    used: "CodeableReference" = None
    
    supportingInfo: "Reference" = None
    