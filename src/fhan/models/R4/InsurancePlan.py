"""
Generated class for InsurancePlan. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Address import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Money import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Meta import *


@dataclass
class InsurancePlan:
    """
    Details of a Health Insurance product/plan provided by an organization.
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
    