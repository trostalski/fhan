"""
Generated class for DetectedIssue. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class DetectedIssue(ModelBase):
    """ Indicates an actual or potential clinical issue with or between one or more active or proposed clinical actions for a patient; e.g. Drug-drug interaction, Ineffective treatment frequency, Procedure-condition conflict, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique id for the detected issue
    :param str status: registered | preliminary | final | amended +
    :param CodeableConcept code: Issue Category, e.g. drug-drug, duplicate therapy, etc.
    :param str severity: high | moderate | low
    :param Reference patient: Associated patient
    :param str identifieddateTime: When identified
    :param Period identifieddateTime: When identified
    :param Reference author: The provider or device that identified the issue
    :param Reference implicated: Problem resource
    :param BackboneElement evidence: Supporting evidence
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Manifestation
    :param Reference detail: Supporting information
    :param str detail: Description and context
    :param str reference: Authority for issue
    :param BackboneElement mitigation: Step taken to address
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept action: What mitigation?
    :param str date: Date committed
    :param Reference author: Who is committing?
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
    
    code: "CodeableConcept" = None
    
    severity: str = None
    
    patient: "Reference" = None
    
    identifieddateTime: str = None
    
    identifieddateTime: "Period" = None
    
    author: "Reference" = None
    
    implicated: "Reference" = None
    
    evidence: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    detail: "Reference" = None
    
    detail: str = None
    
    reference: str = None
    
    mitigation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    action: "CodeableConcept" = None
    
    date: str = None
    
    author: "Reference" = None
    