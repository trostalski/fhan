"""
Generated class for CoverageEligibilityRequest. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Money import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class SupportingInfo(ModelBase):
    """ Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param 'Reference' information: Data to be provided
    :param bool appliesToAll: Applies to all items
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  information: 'Reference' = None,  appliesToAll: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.information: 'Reference' = information 
        self.appliesToAll: bool = appliesToAll 
        

    
    

class Insurance(ModelBase):
    """ Financial instruments for reimbursement for the health care products and services.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Applicable coverage
    :param 'Reference' coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  focal: bool = None,  coverage: 'Reference' = None,  businessArrangement: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.focal: bool = focal 
        self.coverage: 'Reference' = coverage 
        self.businessArrangement: str = businessArrangement 
        

    
        
    
    

class Diagnosis(ModelBase):
    """ Patient diagnosis for which care is sought.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' diagnosisCodeableConcept: Nature of illness or problem
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  diagnosisCodeableConcept: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.diagnosisCodeableConcept: 'CodeableConcept' = diagnosisCodeableConcept 
        

  
    
    

class Item(ModelBase):
    """ Service categories or billable services for which benefit details and/or an authorization prior to service delivery may be required by the payor.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int supportingInfoSequence: Applicable exception or supporting information
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param list['CodeableConcept'] modifier: Product or service billing modifiers
    :param 'Reference' provider: Perfoming practitioner
    :param 'Quantity' quantity: Count of products or services
    :param 'Money' unitPrice: Fee, charge or cost per item
    :param 'Reference' facility: Servicing facility
    :param list['Diagnosis'] diagnosis: Applicable diagnosis
    :param list['Reference'] detail: Product or service details
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  supportingInfoSequence: int = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: list['CodeableConcept'] = None,  provider: 'Reference' = None,  quantity: 'Quantity' = None,  unitPrice: 'Money' = None,  facility: 'Reference' = None,  diagnosis: list['Diagnosis'] = None,  detail: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.supportingInfoSequence: int = supportingInfoSequence or []
        self.category: 'CodeableConcept' = category 
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.provider: 'Reference' = provider 
        self.quantity: 'Quantity' = quantity 
        self.unitPrice: 'Money' = unitPrice 
        self.facility: 'Reference' = facility 
        self.diagnosis: list['Diagnosis'] = diagnosis or []
        self.detail: list['Reference'] = detail or []
        

class CoverageEligibilityRequest(DomainResource):
    """ The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage is valid and in-force and optionally to provide the insurance details of the policy.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for coverage eligiblity request
    :param str status: active | cancelled | draft | entered-in-error
    :param 'CodeableConcept' priority: Desired processing priority
    :param str purpose: auth-requirements | benefits | discovery | validation
    :param 'Reference' patient: Intended recipient of products and services
    :param str servicedDate: Estimated date or dates of service
    :param str created: Creation date
    :param 'Reference' enterer: Author
    :param 'Reference' provider: Party responsible for the request
    :param 'Reference' insurer: Coverage issuer
    :param 'Reference' facility: Servicing facility
    :param list['SupportingInfo'] supportingInfo: Supporting information
    :param list['Insurance'] insurance: Patient insurance information
    :param list['Item'] item: Item to be evaluated for eligibiity
    """
    def __init__(self, resourceType: str = "CoverageEligibilityRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  priority: 'CodeableConcept' = None,  purpose: str = None,  patient: 'Reference' = None,  servicedDate: str = None,  created: str = None,  enterer: 'Reference' = None,  provider: 'Reference' = None,  insurer: 'Reference' = None,  facility: 'Reference' = None,  supportingInfo: list['SupportingInfo'] = None,  insurance: list['Insurance'] = None,  item: list['Item'] = None, ):
        self.resourceType: str = resourceType or "CoverageEligibilityRequest"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.priority: 'CodeableConcept' = priority 
        self.purpose: str = purpose or []
        self.patient: 'Reference' = patient 
        self.servicedDate: str = servicedDate 
        self.created: str = created 
        self.enterer: 'Reference' = enterer 
        self.provider: 'Reference' = provider 
        self.insurer: 'Reference' = insurer 
        self.facility: 'Reference' = facility 
        self.supportingInfo: list['SupportingInfo'] = supportingInfo or []
        self.insurance: list['Insurance'] = insurance or []
        self.item: list['Item'] = item or []
        