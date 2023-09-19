"""
Generated class for MedicinalProduct. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class MedicinalProduct:
    """
    Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
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
    
    type: "CodeableConcept" = None
    
    domain: "Coding" = None
    
    combinedPharmaceuticalDoseForm: "CodeableConcept" = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    additionalMonitoringIndicator: "CodeableConcept" = None
    
    specialMeasures: str = None
    
    paediatricUseIndicator: "CodeableConcept" = None
    
    productClassification: "CodeableConcept" = None
    
    marketingStatus: "MarketingStatus" = None
    
    pharmaceuticalProduct: "Reference" = None
    
    packagedMedicinalProduct: "Reference" = None
    
    attachedDocument: "Reference" = None
    
    masterFile: "Reference" = None
    
    contact: "Reference" = None
    
    clinicalTrial: "Reference" = None
    
    name: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    productName: str = None
    
    namePart: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    part: str = None
    
    type: "Coding" = None
    
    countryLanguage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    language: "CodeableConcept" = None
    
    crossReference: "Identifier" = None
    
    manufacturingBusinessOperation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    operationType: "CodeableConcept" = None
    
    authorisationReferenceNumber: "Identifier" = None
    
    effectiveDate: str = None
    
    confidentialityIndicator: "CodeableConcept" = None
    
    manufacturer: "Reference" = None
    
    regulator: "Reference" = None
    
    specialDesignation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    intendedUse: "CodeableConcept" = None
    
    indicationCodeableConcept: "CodeableConcept" = None
    
    indicationCodeableConcept: "Reference" = None
    
    status: "CodeableConcept" = None
    
    date: str = None
    
    species: "CodeableConcept" = None
    