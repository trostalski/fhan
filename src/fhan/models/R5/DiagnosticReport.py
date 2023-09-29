"""
Generated class for DiagnosticReport. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class SupportingInfo(BaseModel):
    """ This backbone element contains supporting information that was used in the creation of the report not included in the results already included in the report.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Supporting information role code
    :param Reference reference: Supporting information reference
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  reference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.reference = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DiagnosticReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DiagnosticReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Media(BaseModel):
    """ A list of key images or data associated with this report. The images or data are generally created during the diagnostic process, and may be directly of the patient, or of treated specimens (i.e. slides of interest).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str comment: Comment about the image or data (e.g. explanation)
    :param Reference link: Reference to the image or data source
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "link": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  comment:  'str'  = None,  link:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.comment = comment 
        self.link = link 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DiagnosticReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DiagnosticReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class DiagnosticReport(DomainResource):
    """ The findings and interpretation of diagnostic tests performed on patients, groups of patients, products, substances, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports. The report also includes non-clinical context such as batch analysis and stability reporting of products and substances.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for report
    :param Reference basedOn: What was requested
    :param str status: registered | partial | preliminary | modified | final | amended | corrected | appended | cancelled | entered-in-error | unknown
    :param CodeableConcept category: Service category
    :param CodeableConcept code: Name/Code for this diagnostic report
    :param Reference subject: The subject of the report - usually, but not always, the patient
    :param Reference encounter: Health care event when test ordered
    :param str effectiveDateTime: Clinically relevant time/time-period for report
    :param Period effectivePeriod: Clinically relevant time/time-period for report
    :param str issued: DateTime this version was made
    :param Reference performer: Responsible Diagnostic Service
    :param Reference resultsInterpreter: Primary result interpreter
    :param Reference specimen: Specimens this report is based on
    :param Reference result: Observations
    :param Annotation note: Comments about the diagnostic report
    :param Reference study: Reference to full details of an analysis associated with the diagnostic report
    :param SupportingInfo supportingInfo: Additional information supporting the diagnostic report
    :param Media media: Key images or data associated with this report
    :param Reference composition: Reference to a Composition resource for the DiagnosticReport structure
    :param str conclusion: Clinical conclusion (interpretation) of test results
    :param CodeableConcept conclusionCode: Codes for the clinical conclusion of test results
    :param Attachment presentedForm: Entire report as issued
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
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        "performer": {"class_name": "Reference", "is_contained": False},
        
        
        "resultsInterpreter": {"class_name": "Reference", "is_contained": False},
        
        
        "specimen": {"class_name": "Reference", "is_contained": False},
        
        
        "result": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "study": {"class_name": "Reference", "is_contained": False},
        
        
        "supportingInfo": {"class_name": "SupportingInfo", "is_contained": True},
        
        
        "media": {"class_name": "Media", "is_contained": True},
        
        
        "composition": {"class_name": "Reference", "is_contained": False},
        
        
        
        "conclusionCode": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "presentedForm": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  basedOn:  list['Reference']  = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  effectiveDateTime:  'str'  = None,  effectivePeriod:  'Period'  = None,  issued:  'str'  = None,  performer:  list['Reference']  = None,  resultsInterpreter:  list['Reference']  = None,  specimen:  list['Reference']  = None,  result:  list['Reference']  = None,  note:  list['Annotation']  = None,  study:  list['Reference']  = None,  supportingInfo:  list['SupportingInfo']  = None,  media:  list['Media']  = None,  composition:  'Reference'  = None,  conclusion:  'str'  = None,  conclusionCode:  list['CodeableConcept']  = None,  presentedForm:  list['Attachment']  = None, ):
        self.resourceType = resourceType or "DiagnosticReport"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.status = status 
        self.category = category or []
        self.code = code 
        self.subject = subject 
        self.encounter = encounter 
        self.effectiveDateTime = effectiveDateTime 
        self.effectivePeriod = effectivePeriod 
        self.issued = issued 
        self.performer = performer or []
        self.resultsInterpreter = resultsInterpreter or []
        self.specimen = specimen or []
        self.result = result or []
        self.note = note or []
        self.study = study or []
        self.supportingInfo = supportingInfo or []
        self.media = media or []
        self.composition = composition 
        self.conclusion = conclusion 
        self.conclusionCode = conclusionCode or []
        self.presentedForm = presentedForm or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DiagnosticReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "DiagnosticReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()