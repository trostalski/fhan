"""
Generated class for Questionnaire. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Questionnaire:
    """
    A structured set of questions intended to guide the collection of answers from end-users. Questionnaires provide detailed control over order, presentation, phraseology and grouping to allow coherent, consistent data collection.
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
    
    name: str = None
    
    title: str = None
    
    derivedFrom: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectType: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    code: "Coding" = None
    
    item: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    definition: str = None
    
    code: "Coding" = None
    
    prefix: str = None
    
    text: str = None
    
    type: str = None
    
    enableWhen: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    question: str = None
    
    operator: str = None
    
    answerboolean: bool = None
    
    answerboolean: float = None
    
    answerboolean: int = None
    
    answerboolean: str = None
    
    answerboolean: str = None
    
    answerboolean: str = None
    
    answerboolean: str = None
    
    answerboolean: "Coding" = None
    
    answerboolean: "Quantity" = None
    
    answerboolean: "Reference" = None
    
    enableBehavior: str = None
    
    required: bool = None
    
    repeats: bool = None
    
    readOnly: bool = None
    
    maxLength: int = None
    
    answerValueSet: str = None
    
    answerOption: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    valueinteger: int = None
    
    valueinteger: str = None
    
    valueinteger: str = None
    
    valueinteger: str = None
    
    valueinteger: "Coding" = None
    
    valueinteger: "Reference" = None
    
    initialSelected: bool = None
    
    initial: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    valueboolean: bool = None
    
    valueboolean: float = None
    
    valueboolean: int = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: str = None
    
    valueboolean: "Attachment" = None
    
    valueboolean: "Coding" = None
    
    valueboolean: "Quantity" = None
    
    valueboolean: "Reference" = None
    
    item: "BackboneElement" = None
    