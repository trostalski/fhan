"""
Generated class for RegulatedAuthorization. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.CodeableReference import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class RegulatedAuthorization:
    """
    Regulatory approval, clearance or licencing related to a regulated product, treatment, facility or activity that is cited in a guidance, regulation, rule or legislative act. An example is Market Authorization relating to a Medicinal Product.
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
    
    subject: "Reference" = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    region: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    validityPeriod: "Period" = None
    
    indication: "CodeableReference" = None
    
    intendedUse: "CodeableConcept" = None
    
    basis: "CodeableConcept" = None
    
    holder: "Reference" = None
    
    regulator: "Reference" = None
    
    case: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    datePeriod: "Period" = None
    
    datePeriod: str = None
    
    application: "BackboneElement" = None
    