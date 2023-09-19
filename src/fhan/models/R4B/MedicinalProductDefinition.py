"""
Generated class for MedicinalProductDefinition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.CodeableReference import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.MarketingStatus import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class MedicinalProductDefinition:
    """
    Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use, drug catalogs, to support prescribing, adverse events management etc.).
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
    
    domain: "CodeableConcept" = None
    
    version: str = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    description: str = None
    
    combinedPharmaceuticalDoseForm: "CodeableConcept" = None
    
    route: "CodeableConcept" = None
    
    indication: str = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    additionalMonitoringIndicator: "CodeableConcept" = None
    
    specialMeasures: "CodeableConcept" = None
    
    pediatricUseIndicator: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    marketingStatus: "MarketingStatus" = None
    
    packagedMedicinalProduct: "CodeableConcept" = None
    
    ingredient: "CodeableConcept" = None
    
    impurity: "CodeableReference" = None
    
    attachedDocument: "Reference" = None
    
    masterFile: "Reference" = None
    
    contact: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    contact: "Reference" = None
    
    clinicalTrial: "Reference" = None
    
    code: "Coding" = None
    
    name: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    productName: str = None
    
    type: "CodeableConcept" = None
    
    namePart: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    part: str = None
    
    type: "CodeableConcept" = None
    
    countryLanguage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    language: "CodeableConcept" = None
    
    crossReference: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    product: "CodeableReference" = None
    
    type: "CodeableConcept" = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableReference" = None
    
    effectiveDate: "Period" = None
    
    organization: "Reference" = None
    
    confidentialityIndicator: "CodeableConcept" = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Attachment" = None
    