"""
Generated class for Procedure. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Age import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Performer(BaseModel):
    """ Indicates who or what performed the procedure and how they were involved.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performance
    :param Reference actor: Who performed the procedure
    :param Reference onBehalfOf: Organization the device or practitioner was acting for
    :param Period period: When the performer performed the procedure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        
        "onBehalfOf": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None,  onBehalfOf:  'Reference'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        self.onBehalfOf = onBehalfOf 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Procedure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class FocalDevice(BaseModel):
    """ A device that is implanted, removed or otherwise manipulated (calibration, battery replacement, fitting a prosthesis, attaching a wound-vac, etc.) as a focal portion of the Procedure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept action: Kind of change to device
    :param Reference manipulated: Device that was changed
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "action": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "manipulated": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  action:  'CodeableConcept'  = None,  manipulated:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.action = action 
        self.manipulated = manipulated 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Procedure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Procedure(DomainResource):
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
    :param str occurrenceDateTime: When the procedure occurred or is occurring
    :param Period occurrencePeriod: When the procedure occurred or is occurring
    :param str occurrenceString: When the procedure occurred or is occurring
    :param Age occurrenceAge: When the procedure occurred or is occurring
    :param Range occurrenceRange: When the procedure occurred or is occurring
    :param Timing occurrenceTiming: When the procedure occurred or is occurring
    :param str recorded: When the procedure was first captured in the subject's record
    :param Reference recorder: Who recorded the procedure
    :param bool reportedBoolean: Reported rather than primary record
    :param Reference reportedReference: Reported rather than primary record
    :param Performer performer: Who performed the procedure and what they did
    :param Reference location: Where the procedure happened
    :param CodeableReference reason: The justification that the procedure was performed
    :param CodeableConcept bodySite: Target body sites
    :param CodeableConcept outcome: The result of procedure
    :param Reference report: Any report resulting from the procedure
    :param CodeableReference complication: Complication following the procedure
    :param CodeableConcept followUp: Instructions for follow up
    :param Annotation note: Additional information about the procedure
    :param FocalDevice focalDevice: Manipulated, implanted, or removed device
    :param CodeableReference used: Items used during procedure
    :param Reference supportingInfo: Extra information relevant to the procedure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        
        "statusReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        "occurrenceAge": {"class_name": "Age", "is_contained": False},
        
        
        "occurrenceRange": {"class_name": "Range", "is_contained": False},
        
        
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        
        
        
        "recorder": {"class_name": "Reference", "is_contained": False},
        
        
        
        "reportedReference": {"class_name": "Reference", "is_contained": False},
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "outcome": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "report": {"class_name": "Reference", "is_contained": False},
        
        
        "complication": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "followUp": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "focalDevice": {"class_name": "FocalDevice", "is_contained": True},
        
        
        "used": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "supportingInfo": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  basedOn:  list['Reference']  = None,  partOf:  list['Reference']  = None,  status:  'str'  = None,  statusReason:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  focus:  'Reference'  = None,  encounter:  'Reference'  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  occurrenceString:  'str'  = None,  occurrenceAge:  'Age'  = None,  occurrenceRange:  'Range'  = None,  occurrenceTiming:  'Timing'  = None,  recorded:  'str'  = None,  recorder:  'Reference'  = None,  reportedBoolean:  'bool'  = None,  reportedReference:  'Reference'  = None,  performer:  list['Performer']  = None,  location:  'Reference'  = None,  reason:  list['CodeableReference']  = None,  bodySite:  list['CodeableConcept']  = None,  outcome:  'CodeableConcept'  = None,  report:  list['Reference']  = None,  complication:  list['CodeableReference']  = None,  followUp:  list['CodeableConcept']  = None,  note:  list['Annotation']  = None,  focalDevice:  list['FocalDevice']  = None,  used:  list['CodeableReference']  = None,  supportingInfo:  list['Reference']  = None, ):
        self.resourceType = resourceType or "Procedure"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.status = status 
        self.statusReason = statusReason 
        self.category = category or []
        self.code = code 
        self.subject = subject 
        self.focus = focus 
        self.encounter = encounter 
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.occurrenceString = occurrenceString 
        self.occurrenceAge = occurrenceAge 
        self.occurrenceRange = occurrenceRange 
        self.occurrenceTiming = occurrenceTiming 
        self.recorded = recorded 
        self.recorder = recorder 
        self.reportedBoolean = reportedBoolean 
        self.reportedReference = reportedReference 
        self.performer = performer or []
        self.location = location 
        self.reason = reason or []
        self.bodySite = bodySite or []
        self.outcome = outcome 
        self.report = report or []
        self.complication = complication or []
        self.followUp = followUp or []
        self.note = note or []
        self.focalDevice = focalDevice or []
        self.used = used or []
        self.supportingInfo = supportingInfo or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Procedure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()