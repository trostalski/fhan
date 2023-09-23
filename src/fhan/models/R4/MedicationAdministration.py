"""
Generated class for MedicationAdministration. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    function: "CodeableConcept" = CodeableConcept()
    actor: "Reference" = Reference()
    

    
    
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    text: str = None
    site: "CodeableConcept" = CodeableConcept()
    route: "CodeableConcept" = CodeableConcept()
    method: "CodeableConcept" = CodeableConcept()
    dose: "Quantity" = Quantity()
    rateRatio: "Ratio" = Ratio()
    

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

    resourceType: str = "MedicationAdministration"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    instantiates: str = None
    
    partOf: list[Reference] = Reference() 
    
    status: str = None
    
    statusReason: list[CodeableConcept] = CodeableConcept() 
    
    category: "CodeableConcept" = CodeableConcept()
    
    medicationCodeableConcept: "CodeableConcept" = CodeableConcept()
    
    subject: "Reference" = Reference()
    
    context: "Reference" = Reference()
    
    supportingInformation: list[Reference] = Reference() 
    
    effectiveDateTime: str = None
    
    performer: list[Performer] = Performer() 
    
    reasonCode: list[CodeableConcept] = CodeableConcept() 
    
    reasonReference: list[Reference] = Reference() 
    
    request: "Reference" = Reference()
    
    device: list[Reference] = Reference() 
    
    note: list[Annotation] = Annotation() 
    
    dosage: "Dosage" = Dosage()
    
    eventHistory: list[Reference] = Reference() 
    