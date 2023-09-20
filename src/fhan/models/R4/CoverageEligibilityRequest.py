"""
Generated class for CoverageEligibilityRequest. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Money import *
from fhan.models.generator_models import ModelBase

@dataclass
class supportingInfo(Element):
    """ Additional information codes regarding exceptions, special considerations, the condition, situation, prior or concurrent issues.
    :param BackboneElement supportingInfo: Supporting information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param Reference information: Data to be provided
    :param bool appliesToAll: Applies to all items
    """
    supportingInfo: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    sequence: int = None
    
    information: "Reference" = None
    
    appliesToAll: bool = None
    
@dataclass
class insurance(Element):
    """ Financial instruments for reimbursement for the health care products and services.
    :param BackboneElement insurance: Patient insurance information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Applicable coverage
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    """
    insurance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    focal: bool = None
    
    coverage: "Reference" = None
    
    businessArrangement: str = None
    
@dataclass
class item(Element):
    """ Service categories or billable services for which benefit details and/or an authorization prior to service delivery may be required by the payor.
    :param BackboneElement item: Item to be evaluated for eligibiity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int supportingInfoSequence: Applicable exception or supporting information
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Product or service billing modifiers
    :param Reference provider: Perfoming practitioner
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param Reference facility: Servicing facility
    :param BackboneElement diagnosis: Applicable diagnosis
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisCodeableConcept: Nature of illness or problem
    :param Reference detail: Product or service details
    """
    item: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    supportingInfoSequence: int = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: list["CodeableConcept"] = None
    
    provider: "Reference" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    facility: "Reference" = None
    
    diagnosis: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    diagnosisCodeableConcept: "CodeableConcept" = None
    
    diagnosisCodeableConcept: "Reference" = None
    
    detail: list["Reference"] = None
    
@dataclass
class diagnosis(Element):
    """ Patient diagnosis for which care is sought.
    :param BackboneElement diagnosis: Applicable diagnosis
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisCodeableConcept: Nature of illness or problem
    """
    diagnosis: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    diagnosisCodeableConcept: "CodeableConcept" = None
    
    diagnosisCodeableConcept: "Reference" = None
    


@dataclass
class CoverageEligibilityRequest(ModelBase):
    """ The CoverageEligibilityRequest provides patient and insurance coverage information to an insurer for them to respond, in the form of an CoverageEligibilityResponse, with information regarding whether the stated coverage is valid and in-force and optionally to provide the insurance details of the policy.
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
    :param CodeableConcept priority: Desired processing priority
    :param str purpose: auth-requirements | benefits | discovery | validation
    :param Reference patient: Intended recipient of products and services
    :param str serviceddate: Estimated date or dates of service
    :param Period serviceddate: Estimated date or dates of service
    :param str created: Creation date
    :param Reference enterer: Author
    :param Reference provider: Party responsible for the request
    :param Reference insurer: Coverage issuer
    :param Reference facility: Servicing facility
    :param BackboneElement supportingInfo: Supporting information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Information instance identifier
    :param Reference information: Data to be provided
    :param bool appliesToAll: Applies to all items
    :param BackboneElement insurance: Patient insurance information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool focal: Applicable coverage
    :param Reference coverage: Insurance information
    :param str businessArrangement: Additional provider contract number
    :param BackboneElement item: Item to be evaluated for eligibiity
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int supportingInfoSequence: Applicable exception or supporting information
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept productOrService: Billing, service, product, or drug code
    :param CodeableConcept modifier: Product or service billing modifiers
    :param Reference provider: Perfoming practitioner
    :param Quantity quantity: Count of products or services
    :param Money unitPrice: Fee, charge or cost per item
    :param Reference facility: Servicing facility
    :param BackboneElement diagnosis: Applicable diagnosis
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept diagnosisCodeableConcept: Nature of illness or problem
    :param Reference diagnosisCodeableConcept: Nature of illness or problem
    :param Reference detail: Product or service details
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
    
    priority: "CodeableConcept" = None
    
    purpose: str = None
    
    patient: "Reference" = None
    
    serviceddate: str = None
    
    serviceddate: "Period" = None
    
    created: str = None
    
    enterer: "Reference" = None
    
    provider: "Reference" = None
    
    insurer: "Reference" = None
    
    facility: "Reference" = None
    
    supportingInfo: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    sequence: int = None
    
    information: "Reference" = None
    
    appliesToAll: bool = None
    
    insurance: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    focal: bool = None
    
    coverage: "Reference" = None
    
    businessArrangement: str = None
    
    item: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    supportingInfoSequence: int = None
    
    category: "CodeableConcept" = None
    
    productOrService: "CodeableConcept" = None
    
    modifier: list["CodeableConcept"] = None
    
    provider: "Reference" = None
    
    quantity: "Quantity" = None
    
    unitPrice: "Money" = None
    
    facility: "Reference" = None
    
    diagnosis: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    diagnosisCodeableConcept: "CodeableConcept" = None
    
    diagnosisCodeableConcept: "Reference" = None
    
    detail: list["Reference"] = None
    