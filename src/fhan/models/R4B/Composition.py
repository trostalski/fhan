"""
Generated class for Composition. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Composition:
    """
    The Clinical Document profile constrains Composition to specify a clinical document (matching CDA). 

The base Composition is a general resource for compositions or documents about any kind of subject that might be encountered in healthcare including such things as guidelines, medicines, etc. A clinical document is focused on documents related to the provision of care process, where the subject is a patient, a group of patients, or a closely related concept. A clinical document has additional requirements around confidentiality that do not apply in the same way to other kinds of documents.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    extension:versionNumber: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    date: str = None
    
    author: "Reference" = None
    
    title: str = None
    
    confidentiality: str = None
    
    attester: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    time: str = None
    
    party: "Reference" = None
    
    custodian: "Reference" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    targetIdentifier: "Identifier" = None
    
    targetIdentifier: "Reference" = None
    
    event: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    period: "Period" = None
    
    detail: "Reference" = None
    
    section: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    code: "CodeableConcept" = None
    
    author: "Reference" = None
    
    focus: "Reference" = None
    
    text: "Narrative" = None
    
    mode: str = None
    
    orderedBy: "CodeableConcept" = None
    
    entry: "Reference" = None
    
    emptyReason: "CodeableConcept" = None
    
    section: "BackboneElement" = None
    