"""
Generated class for ConditionDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ConditionDefinition:
    """ A definition of a condition and information relevant to managing it.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this condition definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the condition definition
    :param str version: Business version of the condition definition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this condition definition (computer friendly)
    :param str title: Name for this condition definition (human friendly)
    :param str subtitle: Subordinate title of the event definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the condition definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for condition definition (if applicable)
    :param CodeableConcept code: Identification of the condition, problem or diagnosis
    :param CodeableConcept severity: Subjective severity of condition
    :param CodeableConcept bodySite: Anatomical location, if relevant
    :param CodeableConcept stage: Stage/grade, usually assessed formally
    :param bool hasSeverity: Whether Severity is appropriate
    :param bool hasBodySite: Whether bodySite is appropriate
    :param bool hasStage: Whether stage is appropriate
    :param str definition: Formal Definition for the condition
    :param BackboneElement observation: Observations particularly relevant to this condition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Category that is relevant
    :param CodeableConcept code: Code for relevant Observation
    :param BackboneElement medication: Medications particularly relevant for this condition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: Category that is relevant
    :param CodeableConcept code: Code for relevant Medication
    :param BackboneElement precondition: Observation that suggets this condition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: sensitive | specific
    :param CodeableConcept code: Code for relevant Observation
    :param CodeableConcept valueCodeableConcept: Value of Observation
    :param Quantity valueCodeableConcept: Value of Observation
    :param Reference team: Appropriate team for this condition
    :param BackboneElement questionnaire: Questionnaire for this condition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str purpose: preadmit | diff-diagnosis | outcome
    :param Reference reference: Specific Questionnaire
    :param BackboneElement plan: Plan that is appropriate
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Use for the plan
    :param Reference reference: The actual plan
    
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
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    subtitle: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    severity: "CodeableConcept" = None
    
    bodySite: "CodeableConcept" = None
    
    stage: "CodeableConcept" = None
    
    hasSeverity: bool = None
    
    hasBodySite: bool = None
    
    hasStage: bool = None
    
    definition: str = None
    
    observation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    medication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    precondition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    code: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    team: "Reference" = None
    
    questionnaire: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    purpose: str = None
    
    reference: "Reference" = None
    
    plan: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    reference: "Reference" = None
    