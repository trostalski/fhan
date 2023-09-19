"""
Generated class for Account. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Account(ModelBase):
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
    :param Reference partOf: Reference to a parent Account
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
    
    partOf: "Reference" = None
    