"""
Generated class for MedicationAdministration. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Performer(ModelBase):
    """ Indicates who or what performed the medication administration and how they were involved.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' function: Type of performance
    :param 'Reference' actor: Who performed the medication administration
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  function: 'CodeableConcept' = None,  actor: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.function: 'CodeableConcept' = function 
        self.actor: 'Reference' = actor 
        

    
    

class Dosage(ModelBase):
    """ Describes the medication dosage information details e.g. dose, rate, site, route, etc.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str text: Free text dosage instructions e.g. SIG
    :param 'CodeableConcept' site: Body site administered to
    :param 'CodeableConcept' route: Path of substance into body
    :param 'CodeableConcept' method: How drug was administered
    :param 'Quantity' dose: Amount of medication per dose
    :param 'Ratio' rateRatio: Dose quantity per unit of time
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  text: str = None,  site: 'CodeableConcept' = None,  route: 'CodeableConcept' = None,  method: 'CodeableConcept' = None,  dose: 'Quantity' = None,  rateRatio: 'Ratio' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.text: str = text 
        self.site: 'CodeableConcept' = site 
        self.route: 'CodeableConcept' = route 
        self.method: 'CodeableConcept' = method 
        self.dose: 'Quantity' = dose 
        self.rateRatio: 'Ratio' = rateRatio 
        

class MedicationAdministration(DomainResource):
    """ Describes the event of a patient consuming or otherwise being administered a medication.  This may be as simple as swallowing a tablet or it may be a long running infusion.  Related resources tie this event to the authorizing prescription, and the specific encounter between patient and health care practitioner.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External identifier
    :param str instantiates: Instantiates protocol or definition
    :param list['Reference'] partOf: Part of referenced event
    :param str status: in-progress | not-done | on-hold | completed | entered-in-error | stopped | unknown
    :param list['CodeableConcept'] statusReason: Reason administration not performed
    :param 'CodeableConcept' category: Type of medication usage
    :param 'CodeableConcept' medicationCodeableConcept: What was administered
    :param 'Reference' subject: Who received medication
    :param 'Reference' context: Encounter or Episode of Care administered as part of
    :param list['Reference'] supportingInformation: Additional information to support administration
    :param str effectiveDateTime: Start and end time of administration
    :param list['Performer'] performer: Who performed the medication administration and what they did
    :param list['CodeableConcept'] reasonCode: Reason administration performed
    :param list['Reference'] reasonReference: Condition or observation that supports why the medication was administered
    :param 'Reference' request: Request administration performed against
    :param list['Reference'] device: Device used to administer
    :param list['Annotation'] note: Information about the administration
    :param 'Dosage' dosage: Details of how medication was taken
    :param list['Reference'] eventHistory: A list of events of interest in the lifecycle
    """
    def __init__(self, resourceType: str = "MedicationAdministration",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiates: str = None,  partOf: list['Reference'] = None,  status: str = None,  statusReason: list['CodeableConcept'] = None,  category: 'CodeableConcept' = None,  medicationCodeableConcept: 'CodeableConcept' = None,  subject: 'Reference' = None,  context: 'Reference' = None,  supportingInformation: list['Reference'] = None,  effectiveDateTime: str = None,  performer: list['Performer'] = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  request: 'Reference' = None,  device: list['Reference'] = None,  note: list['Annotation'] = None,  dosage: 'Dosage' = None,  eventHistory: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "MedicationAdministration"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiates: str = instantiates or []
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.statusReason: list['CodeableConcept'] = statusReason or []
        self.category: 'CodeableConcept' = category 
        self.medicationCodeableConcept: 'CodeableConcept' = medicationCodeableConcept 
        self.subject: 'Reference' = subject 
        self.context: 'Reference' = context 
        self.supportingInformation: list['Reference'] = supportingInformation or []
        self.effectiveDateTime: str = effectiveDateTime 
        self.performer: list['Performer'] = performer or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.request: 'Reference' = request 
        self.device: list['Reference'] = device or []
        self.note: list['Annotation'] = note or []
        self.dosage: 'Dosage' = dosage 
        self.eventHistory: list['Reference'] = eventHistory or []
        