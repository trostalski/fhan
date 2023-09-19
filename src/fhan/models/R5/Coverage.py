"""
Generated class for Coverage. 
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
from fhan.models.R5.Quantity import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Coverage:
    """ Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier(s) for this coverage
    :param str status: active | cancelled | draft | entered-in-error
    :param str kind: insurance | self-pay | other
    :param BackboneElement paymentBy: Self-pay parties and responsibility
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference party: Parties performing self-payment
    :param str responsibility: Party's responsibility
    :param CodeableConcept type: Coverage category such as medical or accident
    :param Reference policyHolder: Owner of the policy
    :param Reference subscriber: Subscriber to the policy
    :param Identifier subscriberId: ID assigned to the subscriber
    :param Reference beneficiary: Plan beneficiary
    :param str dependent: Dependent number
    :param CodeableConcept relationship: Beneficiary relationship to the subscriber
    :param Period period: Coverage start and end dates
    :param Reference insurer: Issuer of the policy
    :param BackboneElement class: Additional coverage classifications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of class such as 'group' or 'plan'
    :param Identifier value: Value associated with the type
    :param str name: Human readable description of the type and value
    :param int order: Relative order of the coverage
    :param str network: Insurer network
    :param BackboneElement costToBeneficiary: Patient payments for services/products
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Cost category
    :param CodeableConcept category: Benefit classification
    :param CodeableConcept network: In or out of network
    :param CodeableConcept unit: Individual or family
    :param CodeableConcept term: Annual or lifetime
    :param Quantity valueQuantity: The amount or percentage due from the beneficiary
    :param Money valueQuantity: The amount or percentage due from the beneficiary
    :param BackboneElement exception: Exceptions for patient payments
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Exception category
    :param Period period: The effective period of the exception
    :param bool subrogation: Reimbursement to insurer
    :param Reference contract: Contract details
    :param Reference insurancePlan: Insurance plan details
    
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
    
    kind: str = None
    
    paymentBy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    party: "Reference" = None
    
    responsibility: str = None
    
    type: "CodeableConcept" = None
    
    policyHolder: "Reference" = None
    
    subscriber: "Reference" = None
    
    subscriberId: "Identifier" = None
    
    beneficiary: "Reference" = None
    
    dependent: str = None
    
    relationship: "CodeableConcept" = None
    
    period: "Period" = None
    
    insurer: "Reference" = None
    
    class: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    value: "Identifier" = None
    
    name: str = None
    
    order: int = None
    
    network: str = None
    
    costToBeneficiary: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    network: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    term: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "Money" = None
    
    exception: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    period: "Period" = None
    
    subrogation: bool = None
    
    contract: "Reference" = None
    
    insurancePlan: "Reference" = None
    