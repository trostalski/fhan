"""
Generated class for CoverageEligibilityResponse. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Money import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
        
    
        
    
    
@dataclass
class Benefit(Element):
    """ Benefits used to date.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedUnsignedInt: Benefits allowed
    :param int usedUnsignedInt: Benefits used
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    
    allowedUnsignedInt: int = None
    
    usedUnsignedInt: int = None
    

  
    
    
@dataclass
class Item(Element):
    """ Benefits and optionally current balances, and authorization details by category or service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Product or service billing modifiers
    :param Reference provider: Performing practitioner
    :param bool excluded: Excluded from the plan
    :param str name: Short name for the benefit
    :param str description: Description of the benefit or services covered
    :param CodeableConcept network: In or out of network
    :param CodeableConcept unit: Individual or family
    :param CodeableConcept term: Annual or lifetime
    :param Benefit benefit: Benefit Summary
    :param bool authorizationRequired: Authorization required flag
    :param CodeableConcept authorizationSupporting: Type of required supporting materials
    :param str authorizationUrl: Preauthorization requirements endpoint
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    category: "CodeableConcept" = None
    productOrService: "CodeableConcept" = None
    modifier: list[CodeableConcept] = None
    provider: "Reference" = None
    
    excluded: bool = None
    
    name: str = None
    
    description: str = None
    network: "CodeableConcept" = None
    unit: "CodeableConcept" = None
    term: "CodeableConcept" = None
    benefit: list[Benefit] = None
    
    authorizationRequired: bool = None
    authorizationSupporting: list[CodeableConcept] = None
    
    authorizationUrl: str = None
    

  
    
    
@dataclass
class Insurance(Element):
    """ Financial instruments for reimbursement for the health care products and services.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: Insurance information
    :param bool inforce: Coverage inforce indicator
    :param Period benefitPeriod: When the benefits are applicable
    :param Item item: Benefits and authorization details
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    coverage: "Reference" = None
    
    inforce: bool = None
    benefitPeriod: "Period" = None
    item: list[Item] = None
    

    
    
@dataclass
class Error(Element):
    """ Errors encountered during the processing of the request.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Error code detailing processing issues
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    

@dataclass
class CoverageEligibilityResponse(ModelBase):
    """ This resource provides eligibility and plan details from the processing of an CoverageEligibilityRequest resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for coverage eligiblity request
    :param str status: active | cancelled | draft | entered-in-error
    :param str purpose: auth-requirements | benefits | discovery | validation
    :param Reference patient: Intended recipient of products and services
    :param str servicedDate: Estimated date or dates of service
    :param str created: Response creation date
    :param Reference requestor: Party responsible for the request
    :param Reference request: Eligibility request reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param Reference insurer: Coverage issuer
    :param Insurance insurance: Patient insurance information
    :param str preAuthRef: Preauthorization reference
    :param CodeableConcept form: Printed form identifier
    :param Error error: Processing errors
    """

    resourceType: str = "CoverageEligibilityResponse"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    purpose: str = None
    
    patient: "Reference" = None
    
    servicedDate: str = None
    
    created: str = None
    
    requestor: "Reference" = None
    
    request: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    insurer: "Reference" = None
    
    insurance: list["Insurance"] = None
    
    preAuthRef: str = None
    
    form: "CodeableConcept" = None
    
    error: list["Error"] = None
    