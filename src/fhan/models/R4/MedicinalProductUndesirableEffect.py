"""
Generated class for MedicinalProductUndesirableEffect. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Population import *
from fhan.models.generator_models import ModelBase

@dataclass
class MedicinalProductUndesirableEffect(ModelBase):
    """ Describe the undesirable effects of the medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference subject: The medication for which this is an indication
    :param CodeableConcept symptomConditionEffect: The symptom, condition or undesirable effect
    :param CodeableConcept classification: Classification of the effect
    :param CodeableConcept frequencyOfOccurrence: The frequency of occurrence of the effect
    :param Population population: The population group to which this applies
    """

    resourceType: str = "MedicinalProductUndesirableEffect"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    subject: list["Reference"] = None
    
    symptomConditionEffect: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    frequencyOfOccurrence: "CodeableConcept" = None
    
    population: list["Population"] = None
    