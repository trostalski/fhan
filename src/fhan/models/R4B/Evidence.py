"""
Generated class for Evidence. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.RelatedArtifact import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Evidence:
    """
    The Evidence Resource provides a machine-interpretable expression of an evidence concept including the evidence variables (eg population, exposures/interventions, comparators, outcomes, measured variables, confounding variables), the statistics, and the certainty of this evidence.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    title: str = None
    
    citeAsReference: "Reference" = None
    
    citeAsReference: str = None
    
    status: str = None
    
    date: str = None
    
    useContext: "UsageContext" = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    description: str = None
    
    assertion: str = None
    
    note: "Annotation" = None
    
    variableDefinition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    variableRole: "CodeableConcept" = None
    
    observed: "Reference" = None
    
    intended: "Reference" = None
    
    directnessMatch: "CodeableConcept" = None
    
    synthesisType: "CodeableConcept" = None
    
    studyType: "CodeableConcept" = None
    
    statistic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    statisticType: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    numberOfEvents: int = None
    
    numberAffected: int = None
    
    sampleSize: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    numberOfStudies: int = None
    
    numberOfParticipants: int = None
    
    knownDataCount: int = None
    
    attributeEstimate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    level: float = None
    
    range: "Range" = None
    
    attributeEstimate: "BackboneElement" = None
    
    modelCharacteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    value: "Quantity" = None
    
    variable: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    variableDefinition: "Reference" = None
    
    handling: str = None
    
    valueCategory: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueRange: "Range" = None
    
    attributeEstimate: "BackboneElement" = None
    
    certainty: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    note: "Annotation" = None
    
    type: "CodeableConcept" = None
    
    rating: "CodeableConcept" = None
    
    rater: str = None
    
    subcomponent: "BackboneElement" = None
    