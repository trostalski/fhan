"""
Generated class for InsurancePlan. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Money import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    name: str = None
    
    alias: str = None
    
    period: "Period" = None
    
    ownedBy: "Reference" = None
    
    administeredBy: "Reference" = None
    
    coverageArea: "Reference" = None
    
    contact: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    purpose: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: "ContactPoint" = None
    
    address: "Address" = None
    
    endpoint: "Reference" = None
    
    network: "Reference" = None
    
    coverage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    network: "Reference" = None
    
    benefit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    requirement: str = None
    
    limit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    value: "Quantity" = None
    
    code: "CodeableConcept" = None
    
    plan: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    coverageArea: "Reference" = None
    
    network: "Reference" = None
    
    generalCost: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    groupSize: int = None
    
    cost: "Money" = None
    
    comment: str = None
    
    specificCost: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    benefit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    cost: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    applicability: "CodeableConcept" = None
    
    qualifiers: "CodeableConcept" = None
    
    value: "Quantity" = None
    