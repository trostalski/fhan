"""
Generated class for ServiceRequest. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Parameter(BaseModel):
    """ The parameter details for the service being requested.:param CodeableReference parameterFocus: The context of the order details by reference
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The detail of the order being requested
    :param Quantity valueQuantity: The value for the order detail
    :param Ratio valueRatio: The value for the order detail
    :param Range valueRange: The value for the order detail
    :param bool valueBoolean: The value for the order detail
    :param CodeableConcept valueCodeableConcept: The value for the order detail
    :param str valueString: The value for the order detail
    :param Period valuePeriod: The value for the order detail
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "parameterFocus": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valuePeriod": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  parameterFocus:  'CodeableReference'  = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueRatio:  'Ratio'  = None,  valueRange:  'Range'  = None,  valueBoolean:  'bool'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueString:  'str'  = None,  valuePeriod:  'Period'  = None, ):
        self.parameterFocus = parameterFocus 
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueQuantity = valueQuantity 
        self.valueRatio = valueRatio 
        self.valueRange = valueRange 
        self.valueBoolean = valueBoolean 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueString = valueString 
        self.valuePeriod = valuePeriod 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ServiceRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ServiceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class OrderDetail(BaseModel):
    """ Additional details and instructions about the how the services are to be delivered.   For example, and order for a urinary catheter may have an order detail for an external or indwelling catheter, or an order for a bandage may require additional instructions specifying how the bandage should be applied.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference parameterFocus: The context of the order details by reference
    :param Parameter parameter: The parameter details for the service being requested
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "parameterFocus": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "parameter": {"class_name": "Parameter", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  parameterFocus:  'CodeableReference'  = None,  parameter:  list['Parameter']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.parameterFocus = parameterFocus 
        self.parameter = parameter or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ServiceRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ServiceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class PatientInstruction(BaseModel):
    """ Instructions in terms that are understood by the patient or consumer.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str instructionMarkdown: Patient or consumer-oriented instructions
    :param Reference instructionReference: Patient or consumer-oriented instructions
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "instructionReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  instructionMarkdown:  'str'  = None,  instructionReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.instructionMarkdown = instructionMarkdown 
        self.instructionReference = instructionReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ServiceRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ServiceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ServiceRequest(DomainResource):
    """ A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers assigned to this order
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Reference replaces: What request replaces
    :param Identifier requisition: Composite Request ID
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order +
    :param CodeableConcept category: Classification of service
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if service/procedure should not be performed
    :param CodeableReference code: What is being requested/ordered
    :param OrderDetail orderDetail: Additional order information
    :param Quantity quantityQuantity: Service amount
    :param Ratio quantityRatio: Service amount
    :param Range quantityRange: Service amount
    :param Reference subject: Individual or Entity the service is ordered for
    :param Reference focus: What the service request is about, when it is not about the subject of record
    :param Reference encounter: Encounter in which the request was created
    :param str occurrenceDateTime: When service should occur
    :param Period occurrencePeriod: When service should occur
    :param Timing occurrenceTiming: When service should occur
    :param bool asNeededBoolean: Preconditions for service
    :param CodeableConcept asNeededCodeableConcept: Preconditions for service
    :param str authoredOn: Date request signed
    :param Reference requester: Who/what is requesting service
    :param CodeableConcept performerType: Performer role
    :param Reference performer: Requested performer
    :param CodeableReference location: Requested location
    :param CodeableReference reason: Explanation/Justification for procedure or service
    :param Reference insurance: Associated insurance coverage
    :param CodeableReference supportingInfo: Additional clinical information
    :param Reference specimen: Procedure Samples
    :param CodeableConcept bodySite: Coded location on Body
    :param Reference bodyStructure: BodyStructure-based location on the body
    :param Annotation note: Comments
    :param PatientInstruction patientInstruction: Patient or consumer-oriented instructions
    :param Reference relevantHistory: Request provenance
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
        
        
        "replaces": {"class_name": "Reference", "is_contained": False},
        
        
        "requisition": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "code": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "orderDetail": {"class_name": "OrderDetail", "is_contained": True},
        
        
        "quantityQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "quantityRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        "quantityRange": {"class_name": "Range", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        
        
        
        "asNeededCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "requester": {"class_name": "Reference", "is_contained": False},
        
        
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "performer": {"class_name": "Reference", "is_contained": False},
        
        
        "location": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "insurance": {"class_name": "Reference", "is_contained": False},
        
        
        "supportingInfo": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "specimen": {"class_name": "Reference", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "bodyStructure": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "patientInstruction": {"class_name": "PatientInstruction", "is_contained": True},
        
        
        "relevantHistory": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  basedOn:  list['Reference']  = None,  replaces:  list['Reference']  = None,  requisition:  'Identifier'  = None,  status:  'str'  = None,  intent:  'str'  = None,  category:  list['CodeableConcept']  = None,  priority:  'str'  = None,  doNotPerform:  'bool'  = None,  code:  'CodeableReference'  = None,  orderDetail:  list['OrderDetail']  = None,  quantityQuantity:  'Quantity'  = None,  quantityRatio:  'Ratio'  = None,  quantityRange:  'Range'  = None,  subject:  'Reference'  = None,  focus:  list['Reference']  = None,  encounter:  'Reference'  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  occurrenceTiming:  'Timing'  = None,  asNeededBoolean:  'bool'  = None,  asNeededCodeableConcept:  'CodeableConcept'  = None,  authoredOn:  'str'  = None,  requester:  'Reference'  = None,  performerType:  'CodeableConcept'  = None,  performer:  list['Reference']  = None,  location:  list['CodeableReference']  = None,  reason:  list['CodeableReference']  = None,  insurance:  list['Reference']  = None,  supportingInfo:  list['CodeableReference']  = None,  specimen:  list['Reference']  = None,  bodySite:  list['CodeableConcept']  = None,  bodyStructure:  'Reference'  = None,  note:  list['Annotation']  = None,  patientInstruction:  list['PatientInstruction']  = None,  relevantHistory:  list['Reference']  = None, ):
        self.resourceType = resourceType or "ServiceRequest"
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
        self.replaces = replaces or []
        self.requisition = requisition 
        self.status = status 
        self.intent = intent 
        self.category = category or []
        self.priority = priority 
        self.doNotPerform = doNotPerform 
        self.code = code 
        self.orderDetail = orderDetail or []
        self.quantityQuantity = quantityQuantity 
        self.quantityRatio = quantityRatio 
        self.quantityRange = quantityRange 
        self.subject = subject 
        self.focus = focus or []
        self.encounter = encounter 
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.occurrenceTiming = occurrenceTiming 
        self.asNeededBoolean = asNeededBoolean 
        self.asNeededCodeableConcept = asNeededCodeableConcept 
        self.authoredOn = authoredOn 
        self.requester = requester 
        self.performerType = performerType 
        self.performer = performer or []
        self.location = location or []
        self.reason = reason or []
        self.insurance = insurance or []
        self.supportingInfo = supportingInfo or []
        self.specimen = specimen or []
        self.bodySite = bodySite or []
        self.bodyStructure = bodyStructure 
        self.note = note or []
        self.patientInstruction = patientInstruction or []
        self.relevantHistory = relevantHistory or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ServiceRequest":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ServiceRequest":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()