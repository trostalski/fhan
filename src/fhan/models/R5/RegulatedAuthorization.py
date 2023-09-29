"""
Generated class for RegulatedAuthorization. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Case(BaseModel):
    """ The case or regulatory procedure for granting or amending a regulated authorization. An authorization is granted in response to submissions/applications by those seeking authorization. A case is the administrative process that deals with the application(s) that relate to this and assesses them. Note: This area is subject to ongoing review and the workgroup is seeking implementer feedback on its use (see link at bottom of page).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier by which this case can be referenced
    :param CodeableConcept type: The defining type of case
    :param CodeableConcept status: The status associated with the case
    :param Period datePeriod: Relevant date for this case
    :param str dateDateTime: Relevant date for this case
    :param Application application: Applications submitted to obtain a regulated authorization. Steps within the longer running case or procedure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "datePeriod": {"class_name": "Period", "is_contained": False},
        
        
        
        "application": {"class_name": "Application", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  'Identifier'  = None,  type:  'CodeableConcept'  = None,  status:  'CodeableConcept'  = None,  datePeriod:  'Period'  = None,  dateDateTime:  'str'  = None,  application:  list['Application']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier 
        self.type = type 
        self.status = status 
        self.datePeriod = datePeriod 
        self.dateDateTime = dateDateTime 
        self.application = application or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RegulatedAuthorization":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RegulatedAuthorization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RegulatedAuthorization(DomainResource):
    """ Regulatory approval, clearance or licencing related to a regulated product, treatment, facility or activity that is cited in a guidance, regulation, rule or legislative act. An example is Market Authorization relating to a Medicinal Product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the authorization, typically assigned by the authorizing body
    :param Reference subject: The product type, treatment, facility or activity that is being authorized
    :param CodeableConcept type: Overall type of this authorization, for example drug marketing approval, orphan drug designation
    :param str description: General textual supporting information
    :param CodeableConcept region: The territory in which the authorization has been granted
    :param CodeableConcept status: The status that is authorised e.g. approved. Intermediate states can be tracked with cases and applications
    :param str statusDate: The date at which the current status was assigned
    :param Period validityPeriod: The time period in which the regulatory approval etc. is in effect, e.g. a Marketing Authorization includes the date of authorization and/or expiration date
    :param CodeableReference indication: Condition for which the use of the regulated product applies
    :param CodeableConcept intendedUse: The intended use of the product, e.g. prevention, treatment
    :param CodeableConcept basis: The legal/regulatory framework or reasons under which this authorization is granted
    :param Reference holder: The organization that has been granted this authorization, by the regulator
    :param Reference regulator: The regulatory authority or authorizing body granting the authorization
    :param Reference attachedDocument: Additional information or supporting documentation about the authorization
    :param Case case: The case or regulatory procedure for granting or amending a regulated authorization. Note: This area is subject to ongoing review and the workgroup is seeking implementer feedback on its use (see link at bottom of page)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "region": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "validityPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "indication": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "intendedUse": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "basis": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "holder": {"class_name": "Reference", "is_contained": False},
        
        
        "regulator": {"class_name": "Reference", "is_contained": False},
        
        
        "attachedDocument": {"class_name": "Reference", "is_contained": False},
        
        
        "case": {"class_name": "Case", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  subject:  list['Reference']  = None,  type:  'CodeableConcept'  = None,  description:  'str'  = None,  region:  list['CodeableConcept']  = None,  status:  'CodeableConcept'  = None,  statusDate:  'str'  = None,  validityPeriod:  'Period'  = None,  indication:  list['CodeableReference']  = None,  intendedUse:  'CodeableConcept'  = None,  basis:  list['CodeableConcept']  = None,  holder:  'Reference'  = None,  regulator:  'Reference'  = None,  attachedDocument:  list['Reference']  = None,  case:  'Case'  = None, ):
        self.resourceType = resourceType or "RegulatedAuthorization"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.subject = subject or []
        self.type = type 
        self.description = description 
        self.region = region or []
        self.status = status 
        self.statusDate = statusDate 
        self.validityPeriod = validityPeriod 
        self.indication = indication or []
        self.intendedUse = intendedUse 
        self.basis = basis or []
        self.holder = holder 
        self.regulator = regulator 
        self.attachedDocument = attachedDocument or []
        self.case = case 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RegulatedAuthorization":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RegulatedAuthorization":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()