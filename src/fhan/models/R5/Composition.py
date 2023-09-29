"""
Generated class for Composition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Attester(BaseModel):
    """ A participant who has attested to the accuracy of the composition/document.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept mode: personal | professional | legal | official
    :param str time: When the composition was attested
    :param Reference party: Who attested the composition
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "mode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "party": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  mode:  'CodeableConcept'  = None,  time:  'str'  = None,  party:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode 
        self.time = time 
        self.party = party 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Event(BaseModel):
    """ The clinical service, such as a colonoscopy or an appendectomy, being documented.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period period: The period covered by the documentation
    :param CodeableReference detail: The event(s) being documented, as code(s), reference(s), or both
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "detail": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  period:  'Period'  = None,  detail:  list['CodeableReference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.period = period 
        self.detail = detail or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Section(BaseModel):
    """ The root of the sections that make up the composition.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for section (e.g. for ToC)
    :param CodeableConcept code: Classification of section (recommended)
    :param Reference author: Who and/or what authored the section
    :param Reference focus: Who/what the section is about, when it is not about the subject of composition
    :param Narrative text: Text summary of the section, for human interpretation
    :param CodeableConcept orderedBy: Order of section entries
    :param Reference entry: A reference to data that supports this section
    :param CodeableConcept emptyReason: Why the section is empty
    :param Section section: Nested Section
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "orderedBy": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "entry": {"class_name": "Reference", "is_contained": False},
        
        
        "emptyReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "section": {"class_name": "Section", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  title:  'str'  = None,  code:  'CodeableConcept'  = None,  author:  list['Reference']  = None,  focus:  'Reference'  = None,  text:  'Narrative'  = None,  orderedBy:  'CodeableConcept'  = None,  entry:  list['Reference']  = None,  emptyReason:  'CodeableConcept'  = None,  section:  list['Section']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title 
        self.code = code 
        self.author = author or []
        self.focus = focus 
        self.text = text 
        self.orderedBy = orderedBy 
        self.entry = entry or []
        self.emptyReason = emptyReason 
        self.section = section or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Composition(DomainResource):
    """ A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this Composition, represented as a URI (globally unique)
    :param Identifier identifier: Version-independent identifier for the Composition
    :param str version: An explicitly assigned identifer of a variation of the content in the Composition
    :param str status: registered | partial | preliminary | final | amended | corrected | appended | cancelled | entered-in-error | deprecated | unknown
    :param CodeableConcept type: Kind of composition (LOINC if possible)
    :param CodeableConcept category: Categorization of Composition
    :param Reference subject: Who and/or what the composition is about
    :param Reference encounter: Context of the Composition
    :param str date: Composition editing time
    :param UsageContext useContext: The context that the content is intended to support
    :param Reference author: Who and/or what authored the composition
    :param str name: Name for this Composition (computer friendly)
    :param str title: Human Readable name/title
    :param Annotation note: For any additional notes
    :param Attester attester: Attests to accuracy of composition
    :param Reference custodian: Organization which maintains the composition
    :param RelatedArtifact relatesTo: Relationships to other compositions/documents
    :param Event event: The clinical service(s) being documented
    :param Section section: Composition is broken into sections
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "attester": {"class_name": "Attester", "is_contained": True},
        
        
        "custodian": {"class_name": "Reference", "is_contained": False},
        
        
        "relatesTo": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "event": {"class_name": "Event", "is_contained": True},
        
        
        "section": {"class_name": "Section", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  status:  'str'  = None,  type:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  subject:  list['Reference']  = None,  encounter:  'Reference'  = None,  date:  'str'  = None,  useContext:  list['UsageContext']  = None,  author:  list['Reference']  = None,  name:  'str'  = None,  title:  'str'  = None,  note:  list['Annotation']  = None,  attester:  list['Attester']  = None,  custodian:  'Reference'  = None,  relatesTo:  list['RelatedArtifact']  = None,  event:  list['Event']  = None,  section:  list['Section']  = None, ):
        self.resourceType = resourceType or "Composition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.status = status 
        self.type = type 
        self.category = category or []
        self.subject = subject or []
        self.encounter = encounter 
        self.date = date 
        self.useContext = useContext or []
        self.author = author or []
        self.name = name 
        self.title = title 
        self.note = note or []
        self.attester = attester or []
        self.custodian = custodian 
        self.relatesTo = relatesTo or []
        self.event = event or []
        self.section = section or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Composition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Composition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()