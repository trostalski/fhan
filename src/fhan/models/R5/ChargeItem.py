"""
Generated class for ChargeItem. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.MonetaryComponent import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Performer(BaseModel):
    """ Indicates who or what performed or participated in the charged service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: What type of performance was done
    :param Reference actor: Individual who was performing
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ChargeItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ChargeItem(DomainResource):
    """ The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for item
    :param str definitionUri: Defining information about the code of this charge item
    :param str definitionCanonical: Resource defining the code of this ChargeItem
    :param str status: planned | billable | not-billable | aborted | billed | entered-in-error | unknown
    :param Reference partOf: Part of referenced ChargeItem
    :param CodeableConcept code: A code that identifies the charge, like a billing code
    :param Reference subject: Individual service was done for/to
    :param Reference encounter: Encounter associated with this ChargeItem
    :param str occurrenceDateTime: When the charged service was applied
    :param Period occurrencePeriod: When the charged service was applied
    :param Timing occurrenceTiming: When the charged service was applied
    :param Performer performer: Who performed charged service
    :param Reference performingOrganization: Organization providing the charged service
    :param Reference requestingOrganization: Organization requesting the charged service
    :param Reference costCenter: Organization that has ownership of the (potential, future) revenue
    :param Quantity quantity: Quantity of which the charge item has been serviced
    :param CodeableConcept bodysite: Anatomical location, if relevant
    :param MonetaryComponent unitPriceComponent: Unit price overriding the associated rules
    :param MonetaryComponent totalPriceComponent: Total price overriding the associated rules
    :param CodeableConcept overrideReason: Reason for overriding the list price/factor
    :param Reference enterer: Individual who was entering
    :param str enteredDate: Date the charge item was entered
    :param CodeableConcept reason: Why was the charged  service rendered?
    :param CodeableReference service: Which rendered service is being charged?
    :param CodeableReference product: Product charged
    :param Reference account: Account to place this charge
    :param Annotation note: Comments made about the ChargeItem
    :param Reference supportingInformation: Further information supporting this charge
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "occurrencePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "occurrenceTiming": {"class_name": "Timing", "is_contained": False},
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "performingOrganization": {"class_name": "Reference", "is_contained": False},
        
        
        "requestingOrganization": {"class_name": "Reference", "is_contained": False},
        
        
        "costCenter": {"class_name": "Reference", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "bodysite": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "unitPriceComponent": {"class_name": "MonetaryComponent", "is_contained": False},
        
        
        "totalPriceComponent": {"class_name": "MonetaryComponent", "is_contained": False},
        
        
        "overrideReason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "enterer": {"class_name": "Reference", "is_contained": False},
        
        
        
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "service": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "product": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "account": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "supportingInformation": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  definitionUri:  list['str']  = None,  definitionCanonical:  list['str']  = None,  status:  'str'  = None,  partOf:  list['Reference']  = None,  code:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  occurrenceDateTime:  'str'  = None,  occurrencePeriod:  'Period'  = None,  occurrenceTiming:  'Timing'  = None,  performer:  list['Performer']  = None,  performingOrganization:  'Reference'  = None,  requestingOrganization:  'Reference'  = None,  costCenter:  'Reference'  = None,  quantity:  'Quantity'  = None,  bodysite:  list['CodeableConcept']  = None,  unitPriceComponent:  'MonetaryComponent'  = None,  totalPriceComponent:  'MonetaryComponent'  = None,  overrideReason:  'CodeableConcept'  = None,  enterer:  'Reference'  = None,  enteredDate:  'str'  = None,  reason:  list['CodeableConcept']  = None,  service:  list['CodeableReference']  = None,  product:  list['CodeableReference']  = None,  account:  list['Reference']  = None,  note:  list['Annotation']  = None,  supportingInformation:  list['Reference']  = None, ):
        self.resourceType = resourceType or "ChargeItem"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.definitionUri = definitionUri or []
        self.definitionCanonical = definitionCanonical or []
        self.status = status 
        self.partOf = partOf or []
        self.code = code 
        self.subject = subject 
        self.encounter = encounter 
        self.occurrenceDateTime = occurrenceDateTime 
        self.occurrencePeriod = occurrencePeriod 
        self.occurrenceTiming = occurrenceTiming 
        self.performer = performer or []
        self.performingOrganization = performingOrganization 
        self.requestingOrganization = requestingOrganization 
        self.costCenter = costCenter 
        self.quantity = quantity 
        self.bodysite = bodysite or []
        self.unitPriceComponent = unitPriceComponent 
        self.totalPriceComponent = totalPriceComponent 
        self.overrideReason = overrideReason 
        self.enterer = enterer 
        self.enteredDate = enteredDate 
        self.reason = reason or []
        self.service = service or []
        self.product = product or []
        self.account = account or []
        self.note = note or []
        self.supportingInformation = supportingInformation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItem":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ChargeItem":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()