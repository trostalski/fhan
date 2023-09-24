"""
Generated class for Account. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Coverage(Element):
    """ The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference coverage: The party(s), such as insurances, that may contribute to the payment of this account
    :param int priority: The priority of the coverage in the context of this account
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    coverage:  "Reference" = Reference()
    
    priority: int = None
    

    
    
@dataclass
class Guarantor(Element):
    """ The parties responsible for balancing the account if other payment options fall short.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference party: Responsible entity
    :param bool onHold: Credit or other hold applied
    :param Period period: Guarantee account during
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    party:  "Reference" = Reference()
    
    onHold: bool = None
    
    period:  "Period" = Period()
    

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
    :param Coverage coverage: The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
    :param Reference owner: Entity managing the Account
    :param str description: Explanation of purpose/use
    :param Guarantor guarantor: The parties ultimately responsible for balancing the Account
    :param Reference partOf: Reference to a parent Account
    """

    resourceType: str = "Account"
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
    
    name: str = None
    
    subject: list["Reference"] = None
    
    servicePeriod: "Period" = None
    
    coverage: list["Coverage"] = None
    
    owner: "Reference" = None
    
    description: str = None
    
    guarantor: list["Guarantor"] = None
    
    partOf: "Reference" = None
    