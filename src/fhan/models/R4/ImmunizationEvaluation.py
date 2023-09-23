"""
Generated class for ImmunizationEvaluation. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class ImmunizationEvaluation(ModelBase):
    """ Describes a comparison of an immunization event against published recommendations to determine if the administration is "valid" in relation to those  recommendations.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: completed | entered-in-error
    :param Reference patient: Who this evaluation is for
    :param str date: Date evaluation was performed
    :param Reference authority: Who is responsible for publishing the recommendations
    :param CodeableConcept targetDisease: Evaluation target disease
    :param Reference immunizationEvent: Immunization being evaluated
    :param CodeableConcept doseStatus: Status of the dose relative to published recommendations
    :param CodeableConcept doseStatusReason: Reason for the dose status
    :param str description: Evaluation notes
    :param str series: Name of vaccine series
    :param int doseNumberPositiveInt: Dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    """

    resourceType: str = "ImmunizationEvaluation"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    patient: "Reference" = Reference()
    
    date: str = None
    
    authority: "Reference" = Reference()
    
    targetDisease: "CodeableConcept" = CodeableConcept()
    
    immunizationEvent: "Reference" = Reference()
    
    doseStatus: "CodeableConcept" = CodeableConcept()
    
    doseStatusReason: list[CodeableConcept] = CodeableConcept() 
    
    description: str = None
    
    series: str = None
    
    doseNumberPositiveInt: int = None
    
    seriesDosesPositiveInt: int = None
    