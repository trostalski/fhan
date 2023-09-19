"""
Generated class for Procedure. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Age import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.generator_models import ModelBase


@dataclass
class Procedure(ModelBase):
    """ An action that is or was performed on or for a patient. This can be a physical intervention like an operation, or less invasive like long term services, counseling, or hypnotherapy.
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
    :param Reference subject: Who the procedure was performed on
    :param Reference encounter: Encounter created as part of
    :param str performeddateTime: When the procedure was performed
    :param Period performeddateTime: When the procedure was performed
    :param str performeddateTime: When the procedure was performed
    :param Age performeddateTime: When the procedure was performed
    :param Range performeddateTime: When the procedure was performed
    :param Reference recorder: Who recorded the procedure
    :param Reference asserter: Person who asserts this procedure
    :param BackboneElement performer: The people who performed the procedure
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: The reference to the practitioner
    :param Reference onBehalfOf: Organization the device or practitioner was acting for
    :param Reference location: Where the procedure happened
    :param CodeableConcept reasonCode: Coded reason procedure performed
    :param Reference reasonReference: The justification that the procedure was performed
    :param CodeableConcept bodySite: Target body sites
    :param CodeableConcept outcome: The result of procedure
    :param Reference report: Any report resulting from the procedure
    :param CodeableConcept complication: Complication following the procedure
    :param Reference complicationDetail: A condition that is a result of the procedure
    :param CodeableConcept followUp: Instructions for follow up
    :param Annotation note: Additional information about the procedure
    :param BackboneElement focalDevice: Manipulated, implanted, or removed device
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept action: Kind of change to device
    :param Reference manipulated: Device that was changed
    :param Reference usedReference: Items used during procedure
    :param CodeableConcept usedCode: Coded items used during the procedure
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
    
    encounter: "Reference" = None
    
    performeddateTime: str = None
    
    performeddateTime: "Period" = None
    
    performeddateTime: str = None
    
    performeddateTime: "Age" = None
    
    performeddateTime: "Range" = None
    
    recorder: "Reference" = None
    
    asserter: "Reference" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    location: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    bodySite: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    report: "Reference" = None
    
    complication: "CodeableConcept" = None
    
    complicationDetail: "Reference" = None
    
    followUp: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    focalDevice: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    action: "CodeableConcept" = None
    
    manipulated: "Reference" = None
    
    usedReference: "Reference" = None
    
    usedCode: "CodeableConcept" = None
    