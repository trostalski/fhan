"""
Generated class for ImmunizationEvaluation. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ImmunizationEvaluation:
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
    :param CodeableConcept targetDisease: The vaccine preventable disease schedule being evaluated
    :param Reference immunizationEvent: Immunization being evaluated
    :param CodeableConcept doseStatus: Status of the dose relative to published recommendations
    :param CodeableConcept doseStatusReason: Reason why the doese is considered valid, invalid or some other status
    :param str description: Evaluation notes
    :param str series: Name of vaccine series
    :param str doseNumber: Dose number within series
    :param str seriesDoses: Recommended number of doses for immunity
    
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
    
    patient: "Reference" = None
    
    date: str = None
    
    authority: "Reference" = None
    
    targetDisease: "CodeableConcept" = None
    
    immunizationEvent: "Reference" = None
    
    doseStatus: "CodeableConcept" = None
    
    doseStatusReason: "CodeableConcept" = None
    
    description: str = None
    
    series: str = None
    
    doseNumber: str = None
    
    seriesDoses: str = None
    