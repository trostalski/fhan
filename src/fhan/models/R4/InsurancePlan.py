"""
Generated class for InsurancePlan. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.HumanName import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Address import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Money import *
from fhan.models.generator_models import ModelBase

@dataclass
class contact(Element):
    """ The contact for the health insurance product for a certain purpose.
    :param BackboneElement contact: Contact for the product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: A name associated with the contact
    :param ContactPoint telecom: Contact details (telephone, email, etc.)  for a contact
    :param Address address: Visiting or postal addresses for the contact
    """
    contact: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    purpose: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: list["ContactPoint"] = None
    
    address: "Address" = None
    
@dataclass
class coverage(Element):
    """ Details about the coverage offered by the insurance product.
    :param Reference coverageArea: Where product applies
    :param BackboneElement coverage: Coverage details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of coverage
    :param Reference network: What networks provide coverage
    :param BackboneElement benefit: List of benefits
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of benefit
    :param str requirement: Referral requirements
    :param BackboneElement limit: Benefit limits
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity value: Maximum value allowed
    :param CodeableConcept code: Benefit limit details
    """
    coverageArea: list["Reference"] = None
    
    coverage: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    network: list["Reference"] = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    requirement: str = None
    
    limit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "Quantity" = None
    
    code: "CodeableConcept" = None
    
@dataclass
class benefit(Element):
    """ Specific benefits under this type of coverage.
    :param BackboneElement benefit: List of benefits
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of benefit
    :param str requirement: Referral requirements
    :param BackboneElement limit: Benefit limits
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity value: Maximum value allowed
    :param CodeableConcept code: Benefit limit details
    """
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    requirement: str = None
    
    limit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "Quantity" = None
    
    code: "CodeableConcept" = None
    
@dataclass
class limit(Element):
    """ The specific limits on the benefit.
    :param BackboneElement limit: Benefit limits
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity value: Maximum value allowed
    :param CodeableConcept code: Benefit limit details
    """
    limit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "Quantity" = None
    
    code: "CodeableConcept" = None
    
@dataclass
class plan(Element):
    """ Details about an insurance plan.
    :param BackboneElement plan: Plan details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business Identifier for Product
    :param CodeableConcept type: Type of plan
    :param Reference coverageArea: Where product applies
    :param Reference network: What networks provide coverage
    :param BackboneElement generalCost: Overall costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param int groupSize: Number of enrollees
    :param Money cost: Cost value
    :param str comment: Additional cost information
    :param BackboneElement specificCost: Specific costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: General category of benefit
    :param BackboneElement benefit: Benefits list
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of specific benefit
    :param BackboneElement cost: List of the costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param CodeableConcept applicability: in-network | out-of-network | other
    :param CodeableConcept qualifiers: Additional information about the cost
    :param Quantity value: The actual cost value
    """
    plan: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    type: "CodeableConcept" = None
    
    coverageArea: list["Reference"] = None
    
    network: list["Reference"] = None
    
    generalCost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    groupSize: int = None
    
    cost: "Money" = None
    
    comment: str = None
    
    specificCost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    category: "CodeableConcept" = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    cost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    applicability: "CodeableConcept" = None
    
    qualifiers: list["CodeableConcept"] = None
    
    value: "Quantity" = None
    
@dataclass
class generalCost(Element):
    """ Overall costs associated with the plan.
    :param BackboneElement generalCost: Overall costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param int groupSize: Number of enrollees
    :param Money cost: Cost value
    :param str comment: Additional cost information
    """
    generalCost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    groupSize: int = None
    
    cost: "Money" = None
    
    comment: str = None
    
@dataclass
class specificCost(Element):
    """ Costs associated with the coverage provided by the product.
    :param BackboneElement specificCost: Specific costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: General category of benefit
    :param BackboneElement benefit: Benefits list
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of specific benefit
    :param BackboneElement cost: List of the costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param CodeableConcept applicability: in-network | out-of-network | other
    :param CodeableConcept qualifiers: Additional information about the cost
    :param Quantity value: The actual cost value
    """
    specificCost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    category: "CodeableConcept" = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    cost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    applicability: "CodeableConcept" = None
    
    qualifiers: list["CodeableConcept"] = None
    
    value: "Quantity" = None
    
@dataclass
class benefit(Element):
    """ List of the specific benefits under this category of benefit.
    :param BackboneElement benefit: Benefits list
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of specific benefit
    :param BackboneElement cost: List of the costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param CodeableConcept applicability: in-network | out-of-network | other
    :param CodeableConcept qualifiers: Additional information about the cost
    :param Quantity value: The actual cost value
    """
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    cost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    applicability: "CodeableConcept" = None
    
    qualifiers: list["CodeableConcept"] = None
    
    value: "Quantity" = None
    
@dataclass
class cost(Element):
    """ List of the costs associated with a specific benefit.
    :param BackboneElement cost: List of the costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param CodeableConcept applicability: in-network | out-of-network | other
    :param CodeableConcept qualifiers: Additional information about the cost
    :param Quantity value: The actual cost value
    """
    cost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    applicability: "CodeableConcept" = None
    
    qualifiers: list["CodeableConcept"] = None
    
    value: "Quantity" = None
    


@dataclass
class InsurancePlan(ModelBase):
    """ Details of a Health Insurance product/plan provided by an organization.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for Product
    :param str status: draft | active | retired | unknown
    :param CodeableConcept type: Kind of product
    :param str name: Official name
    :param str alias: Alternate names
    :param Period period: When the product is available
    :param Reference ownedBy: Plan issuer
    :param Reference administeredBy: Product administrator
    :param Reference coverageArea: Where product applies
    :param BackboneElement contact: Contact for the product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: A name associated with the contact
    :param ContactPoint telecom: Contact details (telephone, email, etc.)  for a contact
    :param Address address: Visiting or postal addresses for the contact
    :param Reference endpoint: Technical endpoint
    :param Reference network: What networks are Included
    :param BackboneElement coverage: Coverage details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of coverage
    :param Reference network: What networks provide coverage
    :param BackboneElement benefit: List of benefits
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of benefit
    :param str requirement: Referral requirements
    :param BackboneElement limit: Benefit limits
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity value: Maximum value allowed
    :param CodeableConcept code: Benefit limit details
    :param BackboneElement plan: Plan details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business Identifier for Product
    :param CodeableConcept type: Type of plan
    :param Reference coverageArea: Where product applies
    :param Reference network: What networks provide coverage
    :param BackboneElement generalCost: Overall costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param int groupSize: Number of enrollees
    :param Money cost: Cost value
    :param str comment: Additional cost information
    :param BackboneElement specificCost: Specific costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: General category of benefit
    :param BackboneElement benefit: Benefits list
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of specific benefit
    :param BackboneElement cost: List of the costs
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param CodeableConcept applicability: in-network | out-of-network | other
    :param CodeableConcept qualifiers: Additional information about the cost
    :param Quantity value: The actual cost value
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
    
    type: list["CodeableConcept"] = None
    
    name: str = None
    
    alias: str = None
    
    period: "Period" = None
    
    ownedBy: "Reference" = None
    
    administeredBy: "Reference" = None
    
    coverageArea: list["Reference"] = None
    
    contact: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    purpose: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: list["ContactPoint"] = None
    
    address: "Address" = None
    
    endpoint: list["Reference"] = None
    
    network: list["Reference"] = None
    
    coverage: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    network: list["Reference"] = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    requirement: str = None
    
    limit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "Quantity" = None
    
    code: "CodeableConcept" = None
    
    plan: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    type: "CodeableConcept" = None
    
    coverageArea: list["Reference"] = None
    
    network: list["Reference"] = None
    
    generalCost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    groupSize: int = None
    
    cost: "Money" = None
    
    comment: str = None
    
    specificCost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    category: "CodeableConcept" = None
    
    benefit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    cost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    applicability: "CodeableConcept" = None
    
    qualifiers: list["CodeableConcept"] = None
    
    value: "Quantity" = None
    