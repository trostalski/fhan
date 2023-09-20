"""
Generated class for MedicationAdministration. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Performer(Element):
    """ Indicates who or what performed the medication administration and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the medication administration
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    function: "CodeableConcept" = None
    actor: "Reference" = None
    

    
    
@dataclass
class Dosage(Element):
    """ Describes the medication dosage information details e.g. dose, rate, site, route, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str text: Free text dosage instructions e.g. SIG
    :param CodeableConcept site: Body site administered to
    :param CodeableConcept route: Path of substance into body
    :param CodeableConcept method: How drug was administered
    :param Quantity dose: Amount of medication per dose
    :param Ratio rateRatio: Dose quantity per unit of time
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    text: str = None
    site: "CodeableConcept" = None
    route: "CodeableConcept" = None
    method: "CodeableConcept" = None
    dose: "Quantity" = None
    rateRatio: "Ratio" = None
    
@dataclass
class MedicationAdministration(ModelBase):
    """ Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param str instantiates: Instantiates protocol or definition
    :param Reference partOf: Part of referenced event
    :param str status: in-progress | not-done | on-hold | completed | entered-in-error | stopped | unknown
    :param CodeableConcept statusReason: Reason administration not performed
    :param CodeableConcept category: Type of medication usage
    :param CodeableConcept medicationCodeableConcept: What was administered
    :param Reference subject: Who received medication
    :param Reference context: Encounter or Episode of Care administered as part of
    :param Reference supportingInformation: Additional information to support administration
    :param str effectiveDateTime: Start and end time of administration
    :param Performer performer: Who performed the medication administration and what they did
    :param CodeableConcept reasonCode: Reason administration performed
    :param Reference reasonReference: Condition or observation that supports why the medication was administered
    :param Reference request: Request administration performed against
    :param Reference device: Device used to administer
    :param Annotation note: Information about the administration
    :param Dosage dosage: Details of how medication was taken
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
    
    instantiates: str = None
    
    partOf: list["Reference"] = None
    
    status: str = None
    
    statusReason: list["CodeableConcept"] = None
    
    category: "CodeableConcept" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    supportingInformation: list["Reference"] = None
    
    effectiveDateTime: str = None
    
    performer: list["Performer"] = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    request: "Reference" = None
    
    device: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    dosage: "Dosage" = None
    
    eventHistory: list["Reference"] = None
    