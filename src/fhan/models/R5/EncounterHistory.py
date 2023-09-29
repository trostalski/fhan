"""
Generated class for EncounterHistory. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Location(BaseModel):
    """ The location of the patient at this point in the encounter, the multiple cardinality permits de-normalizing the levels of the location hierarchy, such as site/ward/room/bed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location the encounter takes place
    :param CodeableConcept form: The physical type of the location (usually the level in the location hierarchy - bed, room, ward, virtual etc.)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "form": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  location:  'Reference'  = None,  form:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.location = location 
        self.form = form 
        

    @classmethod
    def from_dict(cls, data: dict) -> "EncounterHistory":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EncounterHistory":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class EncounterHistory(DomainResource):
    """ A record of significant events/milestones key data throughout the history of an Encounter
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference encounter: The Encounter associated with this set of historic values
    :param Identifier identifier: Identifier(s) by which this encounter is known
    :param str status: planned | in-progress | on-hold | discharged | completed | cancelled | discontinued | entered-in-error | unknown
    :param CodeableConcept _class: Classification of patient encounter
    :param CodeableConcept type: Specific type of encounter
    :param CodeableReference serviceType: Specific type of service
    :param Reference subject: The patient or group related to this encounter
    :param CodeableConcept subjectStatus: The current status of the subject in relation to the Encounter
    :param Period actualPeriod: The actual start and end time associated with this set of values associated with the encounter
    :param str plannedStartDate: The planned start date/time (or admission date) of the encounter
    :param str plannedEndDate: The planned end date/time (or discharge date) of the encounter
    :param Duration length: Actual quantity of time the encounter lasted (less time absent)
    :param Location location: Location of the patient at this point in the encounter
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "_class": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "serviceType": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "subjectStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actualPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        
        "length": {"class_name": "Duration", "is_contained": False},
        
        
        "location": {"class_name": "Location", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  encounter:  'Reference'  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  _class:  'CodeableConcept'  = None,  type:  list['CodeableConcept']  = None,  serviceType:  list['CodeableReference']  = None,  subject:  'Reference'  = None,  subjectStatus:  'CodeableConcept'  = None,  actualPeriod:  'Period'  = None,  plannedStartDate:  'str'  = None,  plannedEndDate:  'str'  = None,  length:  'Duration'  = None,  location:  list['Location']  = None, ):
        self.resourceType = resourceType or "EncounterHistory"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.encounter = encounter 
        self.identifier = identifier or []
        self.status = status 
        self._class = _class 
        self.type = type or []
        self.serviceType = serviceType or []
        self.subject = subject 
        self.subjectStatus = subjectStatus 
        self.actualPeriod = actualPeriod 
        self.plannedStartDate = plannedStartDate 
        self.plannedEndDate = plannedEndDate 
        self.length = length 
        self.location = location or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "EncounterHistory":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "EncounterHistory":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()