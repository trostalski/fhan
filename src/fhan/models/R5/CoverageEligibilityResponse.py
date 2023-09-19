"""
Generated class for CoverageEligibilityResponse. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class CoverageEligibilityResponse:
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
    :param BackboneElement event: Event information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specific event
    :param str whendateTime: Occurance date or period
    :param Period whendateTime: Occurance date or period
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
    :param str expression: FHIRPath of element(s) related to issue
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    purpose: str = None
    
    patient: "Reference" = None
    
    event: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    whendateTime: str = None
    
    whendateTime: "Period" = None
    
    serviceddate: str = None
    
    serviceddate: "Period" = None
    
    created: str = None
    
    requestor: "Reference" = None
    
    request: "Reference" = None
    
    outcome: str = None
    
    disposition: str = None
    
    insurer: "Reference" = None
    
    insurance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    coverage: "Reference" = None
    
    inforce: bool = None
    
    benefitPeriod: "Period" = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: "CodeableConcept" = None
    
    provider: "Reference" = None
    
    excluded: bool = None
    
    name: str = None
    
    description: str = None
    
    network: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    term: "CodeableConcept" = None
    
    benefit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    allowedunsignedInt: int = None
    
    allowedunsignedInt: str = None
    
    allowedunsignedInt: "Money" = None
    
    usedunsignedInt: int = None
    
    usedunsignedInt: str = None
    
    usedunsignedInt: "Money" = None
    
    authorizationRequired: bool = None
    
    authorizationSupporting: "CodeableConcept" = None
    
    authorizationUrl: str = None
    
    preAuthRef: str = None
    
    form: "CodeableConcept" = None
    
    error: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    expression: str = None
    