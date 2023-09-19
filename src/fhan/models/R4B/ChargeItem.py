"""
Generated class for ChargeItem. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Money import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Timing import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class ChargeItem:
    """
    The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.
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
    
    definitionUri: str = None
    
    definitionCanonical: str = None
    
    status: str = None
    
    partOf: "Reference" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    performingOrganization: "Reference" = None
    
    requestingOrganization: "Reference" = None
    
    costCenter: "Reference" = None
    
    quantity: "Quantity" = None
    
    bodysite: "CodeableConcept" = None
    
    factorOverride: float = None
    
    priceOverride: "Money" = None
    
    overrideReason: str = None
    
    enterer: "Reference" = None
    
    enteredDate: str = None
    
    reason: "CodeableConcept" = None
    
    service: "Reference" = None
    
    productReference: "Reference" = None
    
    productReference: "CodeableConcept" = None
    
    account: "Reference" = None
    
    note: "Annotation" = None
    
    supportingInformation: "Reference" = None
    