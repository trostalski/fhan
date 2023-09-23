"""
Generated class for ImmunizationRecommendation. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class DateCriterion(Element):
    """ Vaccine date recommendations.  For example, earliest date to administer, latest date to administer, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of date
    :param str value: Recommended date
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    
    value: str = None
    

  
    
    
@dataclass
class Recommendation(Element):
    """ Vaccine administration recommendations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept vaccineCode: Vaccine  or vaccine group recommendation applies to
    :param CodeableConcept targetDisease: Disease to be immunized against
    :param CodeableConcept contraindicatedVaccineCode: Vaccine which is contraindicated to fulfill the recommendation
    :param CodeableConcept forecastStatus: Vaccine recommendation status
    :param CodeableConcept forecastReason: Vaccine administration status reason
    :param DateCriterion dateCriterion: Dates governing proposed immunization
    :param str description: Protocol details
    :param str series: Name of vaccination series
    :param int doseNumberPositiveInt: Recommended dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    :param Reference supportingImmunization: Past immunizations supporting recommendation
    :param Reference supportingPatientInformation: Patient observations supporting recommendation
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    vaccineCode: list[CodeableConcept] = CodeableConcept() 
    targetDisease: "CodeableConcept" = CodeableConcept()
    contraindicatedVaccineCode: list[CodeableConcept] = CodeableConcept() 
    forecastStatus: "CodeableConcept" = CodeableConcept()
    forecastReason: list[CodeableConcept] = CodeableConcept() 
    dateCriterion: list[DateCriterion] = DateCriterion() 
    
    description: str = None
    
    series: str = None
    
    doseNumberPositiveInt: int = None
    
    seriesDosesPositiveInt: int = None
    supportingImmunization: list[Reference] = Reference() 
    supportingPatientInformation: list[Reference] = Reference() 
    

@dataclass
class ImmunizationRecommendation(ModelBase):
    """ A patient's point-in-time set of recommendations (i.e. forecasting) according to a published schedule with optional supporting justification.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param Reference patient: Who this profile is for
    :param str date: Date recommendation(s) created
    :param Reference authority: Who is responsible for protocol
    :param Recommendation recommendation: Vaccine administration recommendations
    """

    resourceType: str = "ImmunizationRecommendation"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    patient: "Reference" = Reference()
    
    date: str = None
    
    authority: "Reference" = Reference()
    
    recommendation: list[Recommendation] = Recommendation() 
    