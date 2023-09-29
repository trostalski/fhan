"""
Generated class for Consent. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Expression import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class PolicyBasis(BaseModel):
    """ A Reference or URL used to uniquely identify the policy the organization will enforce for this Consent. This Reference or URL should be specific to the version of the policy and should be dereferencable to a computable policy of some form.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Reference backing policy resource
    :param str url: URL to a computable backing policy
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  reference:  'Reference'  = None,  url:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference 
        self.url = url 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Verification(BaseModel):
    """ Whether a treatment instruction (e.g. artificial respiration: yes or no) was verified with the patient, his/her family or another authorized person.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool verified: Has been verified
    :param CodeableConcept verificationType: Business case of verification
    :param Reference verifiedBy: Person conducting verification
    :param Reference verifiedWith: Person who verified
    :param str verificationDate: When consent verified
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "verificationType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "verifiedBy": {"class_name": "Reference", "is_contained": False},
        
        
        "verifiedWith": {"class_name": "Reference", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  verified:  'bool'  = None,  verificationType:  'CodeableConcept'  = None,  verifiedBy:  'Reference'  = None,  verifiedWith:  'Reference'  = None,  verificationDate:  list['str']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.verified = verified 
        self.verificationType = verificationType 
        self.verifiedBy = verifiedBy 
        self.verifiedWith = verifiedWith 
        self.verificationDate = verificationDate or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Actor(BaseModel):
    """ Who or what is controlled by this provision. Use group to identify a set of actors by some property they share (e.g. 'admitting officers').:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: How the actor is involved
    :param Reference reference: Resource for the actor (or group, by role)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  role:  'CodeableConcept'  = None,  reference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role 
        self.reference = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Data(BaseModel):
    """ The resources controlled by this provision if specific resources are referenced.:param Period dataPeriod: Timeframe for data controlled by this provision
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str meaning: instance | related | dependents | authoredby
    :param Reference reference: The actual data reference
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "dataPeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  dataPeriod:  'Period'  = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  meaning:  'str'  = None,  reference:  'Reference'  = None, ):
        self.dataPeriod = dataPeriod 
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.meaning = meaning 
        self.reference = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Provision(BaseModel):
    """ An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period period: Timeframe for this provision
    :param Actor actor: Who|what controlled by this provision (or group, by role)
    :param CodeableConcept action: Actions controlled by this provision
    :param Coding securityLabel: Security Labels that define affected resources
    :param Coding purpose: Context of activities covered by this provision
    :param Coding documentType: e.g. Resource Type, Profile, CDA, etc
    :param Coding resourceType: e.g. Resource Type, Profile, etc
    :param CodeableConcept code: e.g. LOINC or SNOMED CT code, etc. in the content
    :param Period dataPeriod: Timeframe for data controlled by this provision
    :param Data data: Data controlled by this provision
    :param Expression expression: A computable expression of the consent
    :param Provision provision: Nested Exception Provisions
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "actor": {"class_name": "Actor", "is_contained": True},
        
        
        "action": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "securityLabel": {"class_name": "Coding", "is_contained": False},
        
        
        "purpose": {"class_name": "Coding", "is_contained": False},
        
        
        "documentType": {"class_name": "Coding", "is_contained": False},
        
        
        "resourceType": {"class_name": "Coding", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "dataPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "data": {"class_name": "Data", "is_contained": True},
        
        
        "expression": {"class_name": "Expression", "is_contained": False},
        
        
        "provision": {"class_name": "Provision", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  period:  'Period'  = None,  actor:  list['Actor']  = None,  action:  list['CodeableConcept']  = None,  securityLabel:  list['Coding']  = None,  purpose:  list['Coding']  = None,  documentType:  list['Coding']  = None,  resourceType:  list['Coding']  = None,  code:  list['CodeableConcept']  = None,  dataPeriod:  'Period'  = None,  data:  list['Data']  = None,  expression:  'Expression'  = None,  provision:  list['Provision']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.period = period 
        self.actor = actor or []
        self.action = action or []
        self.securityLabel = securityLabel or []
        self.purpose = purpose or []
        self.documentType = documentType or []
        self.resourceType = resourceType or []
        self.code = code or []
        self.dataPeriod = dataPeriod 
        self.data = data or []
        self.expression = expression 
        self.provision = provision or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Consent(DomainResource):
    """ A record of a healthcare consumer’s  choices  or choices made on their behalf by a third party, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier for this record (external references)
    :param str status: draft | active | inactive | not-done | entered-in-error | unknown
    :param CodeableConcept category: Classification of the consent statement - for indexing/retrieval
    :param Reference subject: Who the consent applies to
    :param str date: Fully executed date of the consent
    :param Period period: Effective period for this Consent
    :param Reference grantor: Who is granting rights according to the policy and rules
    :param Reference grantee: Who is agreeing to the policy and rules
    :param Reference manager: Consent workflow management
    :param Reference controller: Consent Enforcer
    :param Attachment sourceAttachment: Source from which this consent is taken
    :param Reference sourceReference: Source from which this consent is taken
    :param CodeableConcept regulatoryBasis: Regulations establishing base Consent
    :param PolicyBasis policyBasis: Computable version of the backing policy
    :param Reference policyText: Human Readable Policy
    :param Verification verification: Consent Verified by patient or family
    :param str decision: deny | permit
    :param Provision provision: Constraints to the base Consent.policyRule/Consent.policy
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "grantor": {"class_name": "Reference", "is_contained": False},
        
        
        "grantee": {"class_name": "Reference", "is_contained": False},
        
        
        "manager": {"class_name": "Reference", "is_contained": False},
        
        
        "controller": {"class_name": "Reference", "is_contained": False},
        
        
        "sourceAttachment": {"class_name": "Attachment", "is_contained": False},
        
        
        "sourceReference": {"class_name": "Reference", "is_contained": False},
        
        
        "regulatoryBasis": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "policyBasis": {"class_name": "PolicyBasis", "is_contained": True},
        
        
        "policyText": {"class_name": "Reference", "is_contained": False},
        
        
        "verification": {"class_name": "Verification", "is_contained": True},
        
        
        
        "provision": {"class_name": "Provision", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  subject:  'Reference'  = None,  date:  'str'  = None,  period:  'Period'  = None,  grantor:  list['Reference']  = None,  grantee:  list['Reference']  = None,  manager:  list['Reference']  = None,  controller:  list['Reference']  = None,  sourceAttachment:  list['Attachment']  = None,  sourceReference:  list['Reference']  = None,  regulatoryBasis:  list['CodeableConcept']  = None,  policyBasis:  'PolicyBasis'  = None,  policyText:  list['Reference']  = None,  verification:  list['Verification']  = None,  decision:  'str'  = None,  provision:  list['Provision']  = None, ):
        self.resourceType = resourceType or "Consent"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.category = category or []
        self.subject = subject 
        self.date = date 
        self.period = period 
        self.grantor = grantor or []
        self.grantee = grantee or []
        self.manager = manager or []
        self.controller = controller or []
        self.sourceAttachment = sourceAttachment or []
        self.sourceReference = sourceReference or []
        self.regulatoryBasis = regulatoryBasis or []
        self.policyBasis = policyBasis 
        self.policyText = policyText or []
        self.verification = verification or []
        self.decision = decision 
        self.provision = provision or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Consent":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Consent":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()