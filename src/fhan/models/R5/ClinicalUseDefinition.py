"""
Generated class for ClinicalUseDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Expression import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class ClinicalUseDefinition:
    """ A single issue - either an indication, contraindication, interaction or an undesirable effect for a medicinal product, medication, device or procedure.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this issue
    :param str type: indication | contraindication | interaction | undesirable-effect | warning
    :param CodeableConcept category: A categorisation of the issue, primarily for dividing warnings into subject heading areas such as "Pregnancy", "Overdose"
    :param Reference subject: The medication, product, substance, device, procedure etc. for which this is an indication
    :param CodeableConcept status: Whether this is a current issue or one that has been retired etc
    :param BackboneElement contraindication: Specifics for when this is a contraindication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference diseaseSymptomProcedure: The situation that is being documented as contraindicating against this item
    :param CodeableReference diseaseStatus: The status of the disease or symptom for the contraindication
    :param CodeableReference comorbidity: A comorbidity (concurrent condition) or coinfection
    :param Reference indication: The indication which this is a contraidication for
    :param Expression applicability: An expression that returns true or false, indicating whether the indication is applicable or not, after having applied its other elements
    :param BackboneElement otherTherapy: Information about use of the product in relation to other therapies described as part of the contraindication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationshipType: The type of relationship between the product indication/contraindication and another therapy
    :param CodeableReference treatment: Reference to a specific medication, substance etc. as part of an indication or contraindication
    :param BackboneElement indication: Specifics for when this is an indication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference diseaseSymptomProcedure: The situation that is being documented as an indicaton for this item
    :param CodeableReference diseaseStatus: The status of the disease or symptom for the indication
    :param CodeableReference comorbidity: A comorbidity or coinfection as part of the indication
    :param CodeableReference intendedEffect: The intended effect, aim or strategy to be achieved
    :param Range durationRange: Timing or duration information
    :param str durationRange: Timing or duration information
    :param Reference undesirableEffect: An unwanted side effect or negative outcome of the subject of this resource when being used for this indication
    :param Expression applicability: An expression that returns true or false, indicating whether the indication is applicable or not, after having applied its other elements
    :param BackboneElement otherTherapy: Information about use of the product in relation to other therapies described as part of the contraindication
    :param BackboneElement interaction: Specifics for when this is an interaction
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement interactant: The specific medication, product, food etc. or laboratory test that interacts
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: The specific medication, product, food etc. or laboratory test that interacts
    :param CodeableConcept itemReference: The specific medication, product, food etc. or laboratory test that interacts
    :param CodeableConcept type: The type of the interaction e.g. drug-drug interaction, drug-lab test interaction
    :param CodeableReference effect: The effect of the interaction, for example "reduced gastric absorption of primary medication"
    :param CodeableConcept incidence: The incidence of the interaction, e.g. theoretical, observed
    :param CodeableConcept management: Actions for managing the interaction
    :param Reference population: The population group to which this applies
    :param str library: Logic used by the clinical use definition
    :param BackboneElement undesirableEffect: A possible negative outcome from the use of this treatment
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference symptomConditionEffect: The situation in which the undesirable effect may manifest
    :param CodeableConcept classification: High level classification of the effect
    :param CodeableConcept frequencyOfOccurrence: How often the effect is seen
    :param BackboneElement warning: Critical environmental, health or physical risks or hazards. For example 'Do not operate heavy machinery', 'May cause drowsiness'
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: A textual definition of this warning, with formatting
    :param CodeableConcept code: A coded or unformatted textual definition of this warning
    
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
    
    type: str = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    status: "CodeableConcept" = None
    
    contraindication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    diseaseSymptomProcedure: "CodeableReference" = None
    
    diseaseStatus: "CodeableReference" = None
    
    comorbidity: "CodeableReference" = None
    
    indication: "Reference" = None
    
    applicability: "Expression" = None
    
    otherTherapy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationshipType: "CodeableConcept" = None
    
    treatment: "CodeableReference" = None
    
    indication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    diseaseSymptomProcedure: "CodeableReference" = None
    
    diseaseStatus: "CodeableReference" = None
    
    comorbidity: "CodeableReference" = None
    
    intendedEffect: "CodeableReference" = None
    
    durationRange: "Range" = None
    
    durationRange: str = None
    
    undesirableEffect: "Reference" = None
    
    applicability: "Expression" = None
    
    otherTherapy: "BackboneElement" = None
    
    interaction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    interactant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    itemReference: "Reference" = None
    
    itemReference: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    effect: "CodeableReference" = None
    
    incidence: "CodeableConcept" = None
    
    management: "CodeableConcept" = None
    
    population: "Reference" = None
    
    library: str = None
    
    undesirableEffect: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    symptomConditionEffect: "CodeableReference" = None
    
    classification: "CodeableConcept" = None
    
    frequencyOfOccurrence: "CodeableConcept" = None
    
    warning: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    code: "CodeableConcept" = None
    