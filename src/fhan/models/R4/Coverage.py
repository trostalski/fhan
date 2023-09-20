"""
Generated class for Coverage. 
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
class _class(Element):
    """ A suite of underwriter specific classifiers.
    :param BackboneElement _class: Additional coverage classifications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of class such as 'group' or 'plan'
    :param str value: Value associated with the type
    :param str name: Human readable description of the type and value
    """
    _class: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    value: str = None
    
    name: str = None
    
@dataclass
class costToBeneficiary(Element):
    """ A suite of codes indicating the cost category and associated amount which have been detailed in the policy and may have been  included on the health card.
    :param BackboneElement costToBeneficiary: Patient payments for services/products
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Cost category
    :param Quantity valueQuantity: The amount or percentage due from the beneficiary
    :param Money valueQuantity: The amount or percentage due from the beneficiary
    :param BackboneElement exception: Exceptions for patient payments
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Exception category
    :param Period period: The effective period of the exception
    """
    costToBeneficiary: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "Money" = None
    
    exception: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    period: "Period" = None
    
@dataclass
class exception(Element):
    """ A suite of codes indicating exceptions or reductions to patient costs and their effective periods.
    :param BackboneElement exception: Exceptions for patient payments
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Exception category
    :param Period period: The effective period of the exception
    """
    exception: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    period: "Period" = None
    


@dataclass
class Coverage(ModelBase):
    """ Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for the coverage
    :param str status: active | cancelled | draft | entered-in-error
    :param CodeableConcept type: Coverage category such as medical or accident
    :param Reference policyHolder: Owner of the policy
    :param Reference subscriber: Subscriber to the policy
    :param str subscriberId: ID assigned to the subscriber
    :param Reference beneficiary: Plan beneficiary
    :param str dependent: Dependent number
    :param CodeableConcept relationship: Beneficiary relationship to the subscriber
    :param Period period: Coverage start and end dates
    :param Reference payor: Issuer of the policy
    :param BackboneElement _class: Additional coverage classifications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of class such as 'group' or 'plan'
    :param str value: Value associated with the type
    :param str name: Human readable description of the type and value
    :param int order: Relative order of the coverage
    :param str network: Insurer network
    :param BackboneElement costToBeneficiary: Patient payments for services/products
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Cost category
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
    
    type: "CodeableConcept" = None
    
    policyHolder: "Reference" = None
    
    subscriber: "Reference" = None
    
    subscriberId: str = None
    
    beneficiary: "Reference" = None
    
    dependent: str = None
    
    relationship: "CodeableConcept" = None
    
    period: "Period" = None
    
    payor: list["Reference"] = None
    
    _class: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    value: str = None
    
    name: str = None
    
    order: int = None
    
    network: str = None
    
    costToBeneficiary: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "Money" = None
    
    exception: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    period: "Period" = None
    
    subrogation: bool = None
    
    contract: list["Reference"] = None
    