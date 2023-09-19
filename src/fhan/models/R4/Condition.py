"""
Generated class for Condition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Age import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *


@dataclass
class Condition:
    """
    A clinical condition, problem, diagnosis, or other event, situation, issue, or clinical concept that has risen to a level of concern.
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

    clinicalStatus: "CodeableConcept" = None

    verificationStatus: "CodeableConcept" = None

    category: "CodeableConcept" = None

    severity: "CodeableConcept" = None

    code: "CodeableConcept" = None

    bodySite: "CodeableConcept" = None

    subject: "Reference" = None

    encounter: "Reference" = None

    onsetdateTime: str = None

    onsetdateTime: "Age" = None

    onsetdateTime: "Period" = None

    onsetdateTime: "Range" = None

    onsetdateTime: str = None

    abatementdateTime: str = None

    abatementdateTime: "Age" = None

    abatementdateTime: "Period" = None

    abatementdateTime: "Range" = None

    abatementdateTime: str = None

    recordedDate: str = None

    recorder: "Reference" = None

    asserter: "Reference" = None

    stage: "BackboneElement" = None

    id: str = None

    extension: "Extension" = None

    modifierExtension: "Extension" = None

    summary: "CodeableConcept" = None

    assessment: "Reference" = None

    type: "CodeableConcept" = None

    evidence: "BackboneElement" = None

    id: str = None

    extension: "Extension" = None

    modifierExtension: "Extension" = None

    code: "CodeableConcept" = None

    detail: "Reference" = None

    note: "Annotation" = None
