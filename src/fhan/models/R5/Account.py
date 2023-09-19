"""
Generated class for Account. 
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
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Account:
    """ A financial tool for tracking value accrued for a particular purpose.  In the healthcare field, used to track charges for a patient, cost centers, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Account number
    :param str status: active | inactive | entered-in-error | on-hold | unknown
    :param CodeableConcept billingStatus: Tracks the lifecycle of the account through the billing process
    :param CodeableConcept type: E.g. patient, expense, depreciation
    :param str name: Human-readable label
    :param Reference subject: The entity that caused the expenses
    :param Period servicePeriod: Transaction window
    :param BackboneElement coverage: The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: The party(s), such as insurances, that may contribute to the payment of this account
    :param int priority: The priority of the coverage in the context of this account
    :param Reference owner: Entity managing the Account
    :param str description: Explanation of purpose/use
    :param BackboneElement guarantor: The parties ultimately responsible for balancing the Account
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference party: Responsible entity
    :param bool onHold: Credit or other hold applied
    :param Period period: Guarantee account during
    :param BackboneElement diagnosis: The list of diagnoses relevant to this account
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Ranking of the diagnosis (for each type)
    :param CodeableReference condition: The diagnosis relevant to the account
    :param str dateOfDiagnosis: Date of the diagnosis (when coded diagnosis)
    :param CodeableConcept type: Type that this diagnosis has relevant to the account (e.g. admission, billing, discharge …)
    :param bool onAdmission: Diagnosis present on Admission
    :param CodeableConcept packageCode: Package Code specific for billing
    :param BackboneElement procedure: The list of procedures relevant to this account
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Ranking of the procedure (for each type)
    :param CodeableReference code: The procedure relevant to the account
    :param str dateOfService: Date of the procedure (when coded procedure)
    :param CodeableConcept type: How this procedure value should be used in charging the account
    :param CodeableConcept packageCode: Package Code specific for billing
    :param Reference device: Any devices that were associated with the procedure
    :param BackboneElement relatedAccount: Other associated accounts related to this account
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationship: Relationship of the associated Account
    :param Reference account: Reference to an associated Account
    :param CodeableConcept currency: The base or default currency
    :param BackboneElement balance: Calculated account balance(s)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept aggregate: Who is expected to pay this part of the balance
    :param CodeableConcept term: current | 30 | 60 | 90 | 120
    :param bool estimate: Estimated balance
    :param Money amount: Calculated amount
    :param str calculatedAt: Time the balance amount was calculated
    
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
    
    billingStatus: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    name: str = None
    
    subject: "Reference" = None
    
    servicePeriod: "Period" = None
    
    coverage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    coverage: "Reference" = None
    
    priority: int = None
    
    owner: "Reference" = None
    
    description: str = None
    
    guarantor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    party: "Reference" = None
    
    onHold: bool = None
    
    period: "Period" = None
    
    diagnosis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    condition: "CodeableReference" = None
    
    dateOfDiagnosis: str = None
    
    type: "CodeableConcept" = None
    
    onAdmission: bool = None
    
    packageCode: "CodeableConcept" = None
    
    procedure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    code: "CodeableReference" = None
    
    dateOfService: str = None
    
    type: "CodeableConcept" = None
    
    packageCode: "CodeableConcept" = None
    
    device: "Reference" = None
    
    relatedAccount: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationship: "CodeableConcept" = None
    
    account: "Reference" = None
    
    currency: "CodeableConcept" = None
    
    balance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    aggregate: "CodeableConcept" = None
    
    term: "CodeableConcept" = None
    
    estimate: bool = None
    
    amount: "Money" = None
    
    calculatedAt: str = None
    