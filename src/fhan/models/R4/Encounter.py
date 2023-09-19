"""
Generated class for Encounter. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Encounter:
    """
    An interaction between a patient and healthcare provider(s) for the purpose of providing healthcare service(s) or assessing the health status of a patient.
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
    
    statusHistory: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    status: str = None
    
    period: "Period" = None
    
    class: "Coding" = None
    
    classHistory: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    class: "Coding" = None
    
    period: "Period" = None
    
    type: "CodeableConcept" = None
    
    serviceType: "CodeableConcept" = None
    
    priority: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    episodeOfCare: "Reference" = None
    
    basedOn: "Reference" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    period: "Period" = None
    
    individual: "Reference" = None
    
    appointment: "Reference" = None
    
    period: "Period" = None
    
    length: "Duration" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    diagnosis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    condition: "Reference" = None
    
    use: "CodeableConcept" = None
    
    rank: int = None
    
    account: "Reference" = None
    
    hospitalization: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    preAdmissionIdentifier: "Identifier" = None
    
    origin: "Reference" = None
    
    admitSource: "CodeableConcept" = None
    
    reAdmission: "CodeableConcept" = None
    
    dietPreference: "CodeableConcept" = None
    
    specialCourtesy: "CodeableConcept" = None
    
    specialArrangement: "CodeableConcept" = None
    
    destination: "Reference" = None
    
    dischargeDisposition: "CodeableConcept" = None
    
    location: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    location: "Reference" = None
    
    status: str = None
    
    physicalType: "CodeableConcept" = None
    
    period: "Period" = None
    
    serviceProvider: "Reference" = None
    
    partOf: "Reference" = None
    