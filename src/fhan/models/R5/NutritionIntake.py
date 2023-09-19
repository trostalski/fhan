"""
Generated class for NutritionIntake. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class NutritionIntake:
    """ A record of food or fluid that is being consumed by a patient.  A NutritionIntake may indicate that the patient may be consuming the food or fluid now or has consumed the food or fluid in the past.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay or through an app that tracks food or fluids consumed.   The consumption information may come from sources such as the patient's memory, from a nutrition label,  or from a clinician documenting observed intake.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfils plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param str status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept code: Code representing an overall type of nutrition intake
    :param Reference subject: Who is/was consuming the food or fluid
    :param Reference encounter: Encounter associated with NutritionIntake
    :param str occurrencedateTime: The date/time or interval when the food or fluid is/was consumed
    :param Period occurrencedateTime: The date/time or interval when the food or fluid is/was consumed
    :param str recorded: When the intake was recorded
    :param bool reportedboolean: Person or organization that provided the information about the consumption of this food or fluid
    :param Reference reportedboolean: Person or organization that provided the information about the consumption of this food or fluid
    :param BackboneElement consumedItem: What food or fluid product or item was consumed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of food or fluid product
    :param CodeableReference nutritionProduct: Code that identifies the food or fluid product that was consumed
    :param Timing schedule: Scheduled frequency of consumption
    :param Quantity amount: Quantity of the specified food
    :param Quantity rate: Rate at which enteral feeding was administered
    :param bool notConsumed: Flag to indicate if the food or fluid item was refused or otherwise not consumed
    :param CodeableConcept notConsumedReason: Reason food or fluid was not consumed
    :param BackboneElement ingredientLabel: Total nutrient for the whole meal, product, serving
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference nutrient: Total nutrient consumed
    :param Quantity amount: Total amount of nutrient consumed
    :param BackboneElement performer: Who was performed in the intake
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of performer
    :param Reference actor: Who performed the intake
    :param Reference location: Where the intake occurred
    :param Reference derivedFrom: Additional supporting information
    :param CodeableReference reason: Reason for why the food or fluid is /was consumed
    :param Annotation note: Further information about the consumption
    
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    statusReason: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    recorded: str = None
    
    reportedboolean: bool = None
    
    reportedboolean: "Reference" = None
    
    consumedItem: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    nutritionProduct: "CodeableReference" = None
    
    schedule: "Timing" = None
    
    amount: "Quantity" = None
    
    rate: "Quantity" = None
    
    notConsumed: bool = None
    
    notConsumedReason: "CodeableConcept" = None
    
    ingredientLabel: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    nutrient: "CodeableReference" = None
    
    amount: "Quantity" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    location: "Reference" = None
    
    derivedFrom: "Reference" = None
    
    reason: "CodeableReference" = None
    
    note: "Annotation" = None
    