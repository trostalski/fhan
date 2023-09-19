"""
Generated class for ResearchStudy. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ResearchStudy:
    """ A scientific study of nature that sometimes includes processes involved in health and disease. For example, clinical trials are research studies that involve people. These studies may be related to new ways to screen, prevent, diagnose, and treat disease. They may also study certain outcomes and certain groups of people by looking at data collected in the past or future.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this study resource
    :param Identifier identifier: Business Identifier for study
    :param str version: The business version for the study record
    :param str name: Name for this study (computer friendly)
    :param str title: Human readable name of the study
    :param BackboneElement label: Additional names for the study
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: primary | official | scientific | plain-language | subtitle | short-title | acronym | earlier-title | language | auto-translated | human-use | machine-use | duplicate-uid
    :param str value: The name
    :param Reference protocol: Steps followed in executing study
    :param Reference partOf: Part of larger study
    :param RelatedArtifact relatedArtifact: References, URLs, and attachments
    :param str date: Date the resource last changed
    :param str status: draft | active | retired | unknown
    :param CodeableConcept primaryPurposeType: treatment | prevention | diagnostic | supportive-care | screening | health-services-research | basic-science | device-feasibility
    :param CodeableConcept phase: n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | phase-2-phase-3 | phase-3 | phase-4
    :param CodeableConcept studyDesign: Classifications of the study design characteristics
    :param CodeableReference focus: Drugs, devices, etc. under study
    :param CodeableConcept condition: Condition being studied
    :param CodeableConcept keyword: Used to search for the study
    :param CodeableConcept region: Geographic area for the study
    :param str descriptionSummary: Brief text explaining the study
    :param str description: Detailed narrative of the study
    :param Period period: When the study began and ended
    :param Reference site: Facility where study activities are conducted
    :param Annotation note: Comments made about the study
    :param CodeableConcept classifier: Classification for the study
    :param BackboneElement associatedParty: Sponsors, collaborators, and other parties
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of associated party
    :param CodeableConcept role: sponsor | lead-sponsor | sponsor-investigator | primary-investigator | collaborator | funding-source | general-contact | recruitment-contact | sub-investigator | study-director | study-chair
    :param Period period: When active in the role
    :param CodeableConcept classifier: nih | fda | government | nonprofit | academic | industry
    :param Reference party: Individual or organization associated with study (use practitionerRole to specify their organisation)
    :param BackboneElement progressStatus: Status of study with time for that status
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept state: Label for status or state (e.g. recruitment status)
    :param bool actual: Actual if true else anticipated
    :param Period period: Date range
    :param CodeableConcept whyStopped: accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-study-progress | temporarily-closed-per-study-design
    :param BackboneElement recruitment: Target or actual group of participants enrolled in study
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int targetNumber: Estimated total number of participants to be enrolled
    :param int actualNumber: Actual total number of participants enrolled in study
    :param Reference eligibility: Inclusion and exclusion criteria
    :param Reference actualGroup: Group of participants who were enrolled in study
    :param BackboneElement comparisonGroup: Defined path through the study for a subject
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Allows the comparisonGroup for the study and the comparisonGroup for the subject to be linked easily
    :param str name: Label for study comparisonGroup
    :param CodeableConcept type: Categorization of study comparisonGroup
    :param str description: Short explanation of study path
    :param Reference intendedExposure: Interventions or exposures in this comparisonGroup or cohort
    :param Reference observedGroup: Group of participants who were enrolled in study comparisonGroup
    :param BackboneElement objective: A goal for the study
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the objective
    :param CodeableConcept type: primary | secondary | exploratory
    :param str description: Description of the objective
    :param BackboneElement outcomeMeasure: A variable measured during the study
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the outcome
    :param CodeableConcept type: primary | secondary | exploratory
    :param str description: Description of the outcome
    :param Reference reference: Structured outcome definition
    :param Reference result: Link to results generated during the study
    
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
    
    label: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    value: str = None
    
    protocol: "Reference" = None
    
    partOf: "Reference" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    date: str = None
    
    status: str = None
    
    primaryPurposeType: "CodeableConcept" = None
    
    phase: "CodeableConcept" = None
    
    studyDesign: "CodeableConcept" = None
    
    focus: "CodeableReference" = None
    
    condition: "CodeableConcept" = None
    
    keyword: "CodeableConcept" = None
    
    region: "CodeableConcept" = None
    
    descriptionSummary: str = None
    
    description: str = None
    
    period: "Period" = None
    
    site: "Reference" = None
    
    note: "Annotation" = None
    
    classifier: "CodeableConcept" = None
    
    associatedParty: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    role: "CodeableConcept" = None
    
    period: "Period" = None
    
    classifier: "CodeableConcept" = None
    
    party: "Reference" = None
    
    progressStatus: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    state: "CodeableConcept" = None
    
    actual: bool = None
    
    period: "Period" = None
    
    whyStopped: "CodeableConcept" = None
    
    recruitment: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    targetNumber: int = None
    
    actualNumber: int = None
    
    eligibility: "Reference" = None
    
    actualGroup: "Reference" = None
    
    comparisonGroup: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    intendedExposure: "Reference" = None
    
    observedGroup: "Reference" = None
    
    objective: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    outcomeMeasure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    reference: "Reference" = None
    
    result: "Reference" = None
    