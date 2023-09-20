"""
Generated class for CoverageEligibilityResponse. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Money import *
from fhan.models.generator_models import ModelBase

@dataclass
class insurance(Element):
    """ Financial instruments for reimbursement for the health care products and services.
    :param BackboneElement insurance: Patient insurance information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: Insurance information
    :param bool inforce: Coverage inforce indicator
    :param Period benefitPeriod: When the benefits are applicable
    :param BackboneElement item: Benefits and authorization details
    :param str id: Unique id for inter-element referencing
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
    :param BackboneElement benefit: Benefit Summary
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedunsignedInt: Benefits allowed
    :param str allowedunsignedInt: Benefits allowed
    :param Money allowedunsignedInt: Benefits allowed
    :param int usedunsignedInt: Benefits used
    :param str usedunsignedInt: Benefits used
    :param Money usedunsignedInt: Benefits used
    :param bool authorizationRequired: Authorization required flag
    :param CodeableConcept authorizationSupporting: Type of required supporting materials
    :param str authorizationUrl: Preauthorization requirements endpoint
    """
    insurance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    coverage: "Reference" = None
    
    inforce: bool = None
    
    benefitPeriod: "Period" = None
    
    item: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: list["CodeableConcept"] = None
    
    provider: "Reference" = None
    
    excluded: bool = None
    
    name: str = None
    
    description: str = None
    
    network: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    term: "CodeableConcept" = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    allowedunsignedInt: int = None
    
    allowedunsignedInt: str = None
    
    allowedunsignedInt: "Money" = None
    
    usedunsignedInt: int = None
    
    usedunsignedInt: str = None
    
    usedunsignedInt: "Money" = None
    
    authorizationRequired: bool = None
    
    authorizationSupporting: list["CodeableConcept"] = None
    
    authorizationUrl: str = None
    
@dataclass
class item(Element):
    """ Benefits and optionally current balances, and authorization details by category or service.
    :param BackboneElement item: Benefits and authorization details
    :param str id: Unique id for inter-element referencing
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
    :param BackboneElement benefit: Benefit Summary
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedunsignedInt: Benefits allowed
    :param str allowedunsignedInt: Benefits allowed
    :param Money allowedunsignedInt: Benefits allowed
    :param int usedunsignedInt: Benefits used
    :param str usedunsignedInt: Benefits used
    :param Money usedunsignedInt: Benefits used
    :param bool authorizationRequired: Authorization required flag
    :param CodeableConcept authorizationSupporting: Type of required supporting materials
    :param str authorizationUrl: Preauthorization requirements endpoint
    """
    item: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: list["CodeableConcept"] = None
    
    provider: "Reference" = None
    
    excluded: bool = None
    
    name: str = None
    
    description: str = None
    
    network: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    term: "CodeableConcept" = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    allowedunsignedInt: int = None
    
    allowedunsignedInt: str = None
    
    allowedunsignedInt: "Money" = None
    
    usedunsignedInt: int = None
    
    usedunsignedInt: str = None
    
    usedunsignedInt: "Money" = None
    
    authorizationRequired: bool = None
    
    authorizationSupporting: list["CodeableConcept"] = None
    
    authorizationUrl: str = None
    
@dataclass
class benefit(Element):
    """ Benefits used to date.
    :param BackboneElement benefit: Benefit Summary
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedunsignedInt: Benefits allowed
    :param str allowedunsignedInt: Benefits allowed
    :param Money allowedunsignedInt: Benefits allowed
    :param int usedunsignedInt: Benefits used
    :param str usedunsignedInt: Benefits used
    :param Money usedunsignedInt: Benefits used
    """
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    allowedunsignedInt: int = None
    
    allowedunsignedInt: str = None
    
    allowedunsignedInt: "Money" = None
    
    usedunsignedInt: int = None
    
    usedunsignedInt: str = None
    
    usedunsignedInt: "Money" = None
    
@dataclass
class error(Element):
    """ Errors encountered during the processing of the request.
    :param BackboneElement error: Processing errors
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Error code detailing processing issues
    """
    error: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
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
    :param str serviceddate: Estimated date or dates of service
    :param Period serviceddate: Estimated date or dates of service
    :param str created: Response creation date
    :param Reference requestor: Party responsible for the request
    :param Reference request: Eligibility request reference
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition Message
    :param Reference insurer: Coverage issuer
    :param BackboneElement insurance: Patient insurance information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: Insurance information
    :param bool inforce: Coverage inforce indicator
    :param Period benefitPeriod: When the benefits are applicable
    :param BackboneElement item: Benefits and authorization details
    :param str id: Unique id for inter-element referencing
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
    :param BackboneElement benefit: Benefit Summary
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Benefit classification
    :param int allowedunsignedInt: Benefits allowed
    :param str allowedunsignedInt: Benefits allowed
    :param Money allowedunsignedInt: Benefits allowed
    :param int usedunsignedInt: Benefits used
    :param str usedunsignedInt: Benefits used
    :param Money usedunsignedInt: Benefits used
    :param bool authorizationRequired: Authorization required flag
    :param CodeableConcept authorizationSupporting: Type of required supporting materials
    :param str authorizationUrl: Preauthorization requirements endpoint
    :param str preAuthRef: Preauthorization reference
    :param CodeableConcept form: Printed form identifier
    :param BackboneElement error: Processing errors
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Error code detailing processing issues
    """
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
    
    serviceddate: str = None
    
    serviceddate: "Period" = None
    
    created: str = None
    
    requestor: "Reference" = None
    
    request: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    insurer: "Reference" = None
    
    insurance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    coverage: "Reference" = None
    
    inforce: bool = None
    
    benefitPeriod: "Period" = None
    
    item: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: list["CodeableConcept"] = None
    
    provider: "Reference" = None
    
    excluded: bool = None
    
    name: str = None
    
    description: str = None
    
    network: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    term: "CodeableConcept" = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    allowedunsignedInt: int = None
    
    allowedunsignedInt: str = None
    
    allowedunsignedInt: "Money" = None
    
    usedunsignedInt: int = None
    
    usedunsignedInt: str = None
    
    usedunsignedInt: "Money" = None
    
    authorizationRequired: bool = None
    
    authorizationSupporting: list["CodeableConcept"] = None
    
    authorizationUrl: str = None
    
    preAuthRef: str = None
    
    form: "CodeableConcept" = None
    
    error: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    