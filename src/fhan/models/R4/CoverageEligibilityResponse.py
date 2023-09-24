"""
Generated class for CoverageEligibilityResponse. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Money import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
        
    
        
    
    

class Benefit(ModelBase):
    """ Benefits used to date.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Benefit classification
    :param int allowedUnsignedInt: Benefits allowed
    :param int usedUnsignedInt: Benefits used
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  allowedUnsignedInt: int = None,  usedUnsignedInt: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.allowedUnsignedInt: int = allowedUnsignedInt 
        self.usedUnsignedInt: int = usedUnsignedInt 
        

  
    
    

class Item(ModelBase):
    """ Benefits and optionally current balances, and authorization details by category or service.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: Benefit classification
    :param 'CodeableConcept' productOrService: Billing, service, product, or drug code
    :param list['CodeableConcept'] modifier: Product or service billing modifiers
    :param 'Reference' provider: Performing practitioner
    :param bool excluded: Excluded from the plan
    :param str name: Short name for the benefit
    :param str description: Description of the benefit or services covered
    :param 'CodeableConcept' network: In or out of network
    :param 'CodeableConcept' unit: Individual or family
    :param 'CodeableConcept' term: Annual or lifetime
    :param list['Benefit'] benefit: Benefit Summary
    :param bool authorizationRequired: Authorization required flag
    :param list['CodeableConcept'] authorizationSupporting: Type of required supporting materials
    :param str authorizationUrl: Preauthorization requirements endpoint
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  category: 'CodeableConcept' = None,  productOrService: 'CodeableConcept' = None,  modifier: list['CodeableConcept'] = None,  provider: 'Reference' = None,  excluded: bool = None,  name: str = None,  description: str = None,  network: 'CodeableConcept' = None,  unit: 'CodeableConcept' = None,  term: 'CodeableConcept' = None,  benefit: list['Benefit'] = None,  authorizationRequired: bool = None,  authorizationSupporting: list['CodeableConcept'] = None,  authorizationUrl: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: 'CodeableConcept' = category 
        self.productOrService: 'CodeableConcept' = productOrService 
        self.modifier: list['CodeableConcept'] = modifier or []
        self.provider: 'Reference' = provider 
        self.excluded: bool = excluded 
        self.name: str = name 
        self.description: str = description 
        self.network: 'CodeableConcept' = network 
        self.unit: 'CodeableConcept' = unit 
        self.term: 'CodeableConcept' = term 
        self.benefit: list['Benefit'] = benefit or []
        self.authorizationRequired: bool = authorizationRequired 
        self.authorizationSupporting: list['CodeableConcept'] = authorizationSupporting or []
        self.authorizationUrl: str = authorizationUrl 
        

  
    
    

class Insurance(ModelBase):
    """ Financial instruments for reimbursement for the health care products and services.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' coverage: Insurance information
    :param bool inforce: Coverage inforce indicator
    :param 'Period' benefitPeriod: When the benefits are applicable
    :param list['Item'] item: Benefits and authorization details
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  coverage: 'Reference' = None,  inforce: bool = None,  benefitPeriod: 'Period' = None,  item: list['Item'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.coverage: 'Reference' = coverage 
        self.inforce: bool = inforce 
        self.benefitPeriod: 'Period' = benefitPeriod 
        self.item: list['Item'] = item or []
        

    
    

class Error(ModelBase):
    """ Errors encountered during the processing of the request.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Error code detailing processing issues
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        

class CoverageEligibilityResponse(DomainResource):
    """ This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
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
    :param str purpose: auth-requirements | benefits | discovery | validation
    :param 'Reference' patient: Intended recipient of products and services
    :param str servicedDate: Estimated date or dates of service
    :param str created: Response creation date
    :param 'Reference' requestor: Party responsible for the request
    :param 'Reference' request: Eligibility request reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param 'Reference' insurer: Coverage issuer
    :param list['Insurance'] insurance: Patient insurance information
    :param str preAuthRef: Preauthorization reference
    :param 'CodeableConcept' form: Printed form identifier
    :param list['Error'] error: Processing errors
    """
    def __init__(self, resourceType: str = "CoverageEligibilityResponse",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  purpose: str = None,  patient: 'Reference' = None,  servicedDate: str = None,  created: str = None,  requestor: 'Reference' = None,  request: 'Reference' = None,  outcome: str = None,  disposition: str = None,  insurer: 'Reference' = None,  insurance: list['Insurance'] = None,  preAuthRef: str = None,  form: 'CodeableConcept' = None,  error: list['Error'] = None, ):
        self.resourceType: str = resourceType or "CoverageEligibilityResponse"
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
        self.purpose: str = purpose or []
        self.patient: 'Reference' = patient 
        self.servicedDate: str = servicedDate 
        self.created: str = created 
        self.requestor: 'Reference' = requestor 
        self.request: 'Reference' = request 
        self.outcome: str = outcome 
        self.disposition: str = disposition 
        self.insurer: 'Reference' = insurer 
        self.insurance: list['Insurance'] = insurance or []
        self.preAuthRef: str = preAuthRef 
        self.form: 'CodeableConcept' = form 
        self.error: list['Error'] = error or []
        