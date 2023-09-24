"""
Generated class for InsurancePlan. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Address import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Money import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Contact(Element):
    """ The contact for the health insurance product for a certain purpose.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: A name associated with the contact
    :param ContactPoint telecom: Contact details (telephone, email, etc.)  for a contact
    :param Address address: Visiting or postal addresses for the contact
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    purpose:  "CodeableConcept" = CodeableConcept()
    
    name:  "HumanName" = HumanName()
    
    telecom:  list["ContactPoint"] = [ContactPoint()]
    
    address:  "Address" = Address()
    

    
        
    
        
    
    
@dataclass
class Limit(Element):
    """ The specific limits on the benefit.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity value: Maximum value allowed
    :param CodeableConcept code: Benefit limit details
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    value:  "Quantity" = Quantity()
    
    code:  "CodeableConcept" = CodeableConcept()
    

  
    
    
@dataclass
class Benefit(Element):
    """ Specific benefits under this type of coverage.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of benefit
    :param str requirement: Referral requirements
    :param Limit limit: Benefit limits
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    requirement: str = None
    
    limit:  list["Limit"] = [Limit()]
    

  
    
    
@dataclass
class Coverage(Element):
    """ Details about the coverage offered by the insurance product.:param Reference coverageArea: Where product applies
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of coverage
    :param Reference network: What networks provide coverage
    :param Benefit benefit: List of benefits
    """
    coverageArea:  list["Reference"] = [Reference()]
    
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    network:  list["Reference"] = [Reference()]
    
    benefit:  list["Benefit"] = [Benefit()]
    

    
        
    
    
@dataclass
class GeneralCost(Element):
    """ Overall costs associated with the plan.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param int groupSize: Number of enrollees
    :param Money cost: Cost value
    :param str comment: Additional cost information
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    groupSize: int = None
    
    cost:  "Money" = Money()
    
    comment: str = None
    

    
        
    
        
    
    
@dataclass
class Cost(Element):
    """ List of the costs associated with a specific benefit.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of cost
    :param CodeableConcept applicability: in-network | out-of-network | other
    :param CodeableConcept qualifiers: Additional information about the cost
    :param Quantity value: The actual cost value
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    applicability:  "CodeableConcept" = CodeableConcept()
    
    qualifiers:  list["CodeableConcept"] = [CodeableConcept()]
    
    value:  "Quantity" = Quantity()
    

  
    
    
@dataclass
class Benefit(Element):
    """ List of the specific benefits under this category of benefit.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of specific benefit
    :param Cost cost: List of the costs
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    cost:  list["Cost"] = [Cost()]
    

  
    
    
@dataclass
class SpecificCost(Element):
    """ Costs associated with the coverage provided by the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: General category of benefit
    :param Benefit benefit: Benefits list
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    category:  "CodeableConcept" = CodeableConcept()
    
    benefit:  list["Benefit"] = [Benefit()]
    

  
    
    
@dataclass
class Plan(Element):
    """ Details about an insurance plan.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Business Identifier for Product
    :param CodeableConcept type: Type of plan
    :param Reference coverageArea: Where product applies
    :param Reference network: What networks provide coverage
    :param GeneralCost generalCost: Overall costs
    :param SpecificCost specificCost: Specific costs
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    identifier:  list["Identifier"] = [Identifier()]
    
    type:  "CodeableConcept" = CodeableConcept()
    
    coverageArea:  list["Reference"] = [Reference()]
    
    network:  list["Reference"] = [Reference()]
    
    generalCost:  list["GeneralCost"] = [GeneralCost()]
    
    specificCost:  list["SpecificCost"] = [SpecificCost()]
    

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
    :param Contact contact: Contact for the product
    :param Reference endpoint: Technical endpoint
    :param Reference network: What networks are Included
    :param Coverage coverage: Coverage details
    :param Plan plan: Plan details
    """

    resourceType: str = "InsurancePlan"
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
    
    contact: list["Contact"] = None
    
    endpoint: list["Reference"] = None
    
    network: list["Reference"] = None
    
    coverage: list["Coverage"] = None
    
    plan: list["Plan"] = None
    