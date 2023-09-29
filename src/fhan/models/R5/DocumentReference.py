"""
Generated class for DocumentReference. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Attester(BaseModel):
    """ A participant who has authenticated the accuracy of the document.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept mode: personal | professional | legal | official
    :param str time: When the document was attested
    :param Reference party: Who attested the document
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
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class RelatesTo(BaseModel):
    """ Relationships that this document has with other document references that already exist.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The relationship type with another document
    :param Reference target: Target of the relationship
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "target": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  target:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.target = target 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Profile(BaseModel):
    """ An identifier of the document constraints, encoding, structure, and template that the document conforms to beyond the base format indicated in the mimeType.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding valueCoding: Code|uri|canonical
    :param str valueUri: Code|uri|canonical
    :param str valueCanonical: Code|uri|canonical
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  valueCoding:  'Coding'  = None,  valueUri:  'str'  = None,  valueCanonical:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.valueCoding = valueCoding 
        self.valueUri = valueUri 
        self.valueCanonical = valueCanonical 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Content(BaseModel):
    """ The document and format referenced.  If there are multiple content element repetitions, these must all represent the same document in different format, or attachment metadata.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment attachment: Where to access the document
    :param Profile profile: Content profile rules for the document
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "attachment": {"class_name": "Attachment", "is_contained": False},
        
        
        "profile": {"class_name": "Profile", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  attachment:  'Attachment'  = None,  profile:  list['Profile']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.attachment = attachment 
        self.profile = profile or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DocumentReference(DomainResource):
    """ A reference to a document of any kind for any purpose. While the term “document” implies a more narrow focus, for this resource this “document” encompasses *any* serialized object with a mime-type, it includes formal patient-centric documents (CDA), clinical notes, scanned paper, non-patient specific documents like policy text, as well as a photo, video, or audio recording acquired or used in healthcare.  The DocumentReference resource provides metadata about the document so that the document can be discovered and managed.  The actual content may be inline base64 encoded data or provided by direct reference.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifiers for the document
    :param str version: An explicitly assigned identifer of a variation of the content in the DocumentReference
    :param Reference basedOn: Procedure that caused this media to be created
    :param str status: current | superseded | entered-in-error
    :param str docStatus: registered | partial | preliminary | final | amended | corrected | appended | cancelled | entered-in-error | deprecated | unknown
    :param CodeableConcept modality: Imaging modality used
    :param CodeableConcept type: Kind of document (LOINC if possible)
    :param CodeableConcept category: Categorization of document
    :param Reference subject: Who/what is the subject of the document
    :param Reference context: Context of the document content
    :param CodeableReference event: Main clinical acts documented
    :param CodeableReference bodySite: Body part included
    :param CodeableConcept facilityType: Kind of facility where patient was seen
    :param CodeableConcept practiceSetting: Additional details about where the content was created (e.g. clinical specialty)
    :param Period period: Time of service that is being documented
    :param str date: When this document reference was created
    :param Reference author: Who and/or what authored the document
    :param Attester attester: Attests to accuracy of the document
    :param Reference custodian: Organization which maintains the document
    :param RelatesTo relatesTo: Relationships to other documents
    :param str description: Human-readable description
    :param CodeableConcept securityLabel: Document security-tags
    :param Content content: Document referenced
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
        
        
        
        
        "modality": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "context": {"class_name": "Reference", "is_contained": False},
        
        
        "event": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "facilityType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "practiceSetting": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        "attester": {"class_name": "Attester", "is_contained": True},
        
        
        "custodian": {"class_name": "Reference", "is_contained": False},
        
        
        "relatesTo": {"class_name": "RelatesTo", "is_contained": True},
        
        
        
        "securityLabel": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "content": {"class_name": "Content", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  basedOn:  list['Reference']  = None,  status:  'str'  = None,  docStatus:  'str'  = None,  modality:  list['CodeableConcept']  = None,  type:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  subject:  'Reference'  = None,  context:  list['Reference']  = None,  event:  list['CodeableReference']  = None,  bodySite:  list['CodeableReference']  = None,  facilityType:  'CodeableConcept'  = None,  practiceSetting:  'CodeableConcept'  = None,  period:  'Period'  = None,  date:  'str'  = None,  author:  list['Reference']  = None,  attester:  list['Attester']  = None,  custodian:  'Reference'  = None,  relatesTo:  list['RelatesTo']  = None,  description:  'str'  = None,  securityLabel:  list['CodeableConcept']  = None,  content:  list['Content']  = None, ):
        self.resourceType = resourceType or "DocumentReference"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.version = version 
        self.basedOn = basedOn or []
        self.status = status 
        self.docStatus = docStatus 
        self.modality = modality or []
        self.type = type 
        self.category = category or []
        self.subject = subject 
        self.context = context or []
        self.event = event or []
        self.bodySite = bodySite or []
        self.facilityType = facilityType 
        self.practiceSetting = practiceSetting 
        self.period = period 
        self.date = date 
        self.author = author or []
        self.attester = attester or []
        self.custodian = custodian 
        self.relatesTo = relatesTo or []
        self.description = description 
        self.securityLabel = securityLabel or []
        self.content = content or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DocumentReference":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DocumentReference":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()