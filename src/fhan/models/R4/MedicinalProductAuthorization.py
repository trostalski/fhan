"""
Generated class for MedicinalProductAuthorization. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProductAuthorization:
    """
    The regulatory authorization of a medicinal product.
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
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    restoreDate: str = None
    
    validityPeriod: "Period" = None
    
    dataExclusivityPeriod: "Period" = None
    
    dateOfFirstAuthorization: str = None
    
    internationalBirthDate: str = None
    
    legalBasis: "CodeableConcept" = None
    
    jurisdictionalAuthorization: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    validityPeriod: "Period" = None
    
    holder: "Reference" = None
    
    regulator: "Reference" = None
    
    procedure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    datePeriod: "Period" = None
    
    datePeriod: str = None
    
    application: "BackboneElement" = None
    