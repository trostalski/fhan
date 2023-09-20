"""
Generated class for ImmunizationRecommendation. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class recommendation(Element):
    """ Vaccine administration recommendations.
    :param BackboneElement recommendation: Vaccine administration recommendations
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept vaccineCode: Vaccine  or vaccine group recommendation applies to
    :param CodeableConcept targetDisease: Disease to be immunized against
    :param CodeableConcept contraindicatedVaccineCode: Vaccine which is contraindicated to fulfill the recommendation
    :param CodeableConcept forecastStatus: Vaccine recommendation status
    :param CodeableConcept forecastReason: Vaccine administration status reason
    :param BackboneElement dateCriterion: Dates governing proposed immunization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of date
    :param str value: Recommended date
    :param str description: Protocol details
    :param str series: Name of vaccination series
    :param int doseNumberpositiveInt: Recommended dose number within series
    :param str doseNumberpositiveInt: Recommended dose number within series
    :param int seriesDosespositiveInt: Recommended number of doses for immunity
    :param str seriesDosespositiveInt: Recommended number of doses for immunity
    :param Reference supportingImmunization: Past immunizations supporting recommendation
    :param Reference supportingPatientInformation: Patient observations supporting recommendation
    """
    recommendation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    vaccineCode: list["CodeableConcept"] = None
    
    targetDisease: "CodeableConcept" = None
    
    contraindicatedVaccineCode: list["CodeableConcept"] = None
    
    forecastStatus: "CodeableConcept" = None
    
    forecastReason: list["CodeableConcept"] = None
    
    dateCriterion: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: str = None
    
    description: str = None
    
    series: str = None
    
    doseNumberpositiveInt: int = None
    
    doseNumberpositiveInt: str = None
    
    seriesDosespositiveInt: int = None
    
    seriesDosespositiveInt: str = None
    
    supportingImmunization: list["Reference"] = None
    
    supportingPatientInformation: list["Reference"] = None
    
@dataclass
class dateCriterion(Element):
    """ Vaccine date recommendations.  For example, earliest date to administer, latest date to administer, etc.
    :param BackboneElement dateCriterion: Dates governing proposed immunization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of date
    :param str value: Recommended date
    """
    dateCriterion: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: str = None
    


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
    :param BackboneElement recommendation: Vaccine administration recommendations
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept vaccineCode: Vaccine  or vaccine group recommendation applies to
    :param CodeableConcept targetDisease: Disease to be immunized against
    :param CodeableConcept contraindicatedVaccineCode: Vaccine which is contraindicated to fulfill the recommendation
    :param CodeableConcept forecastStatus: Vaccine recommendation status
    :param CodeableConcept forecastReason: Vaccine administration status reason
    :param BackboneElement dateCriterion: Dates governing proposed immunization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of date
    :param str value: Recommended date
    :param str description: Protocol details
    :param str series: Name of vaccination series
    :param int doseNumberpositiveInt: Recommended dose number within series
    :param str doseNumberpositiveInt: Recommended dose number within series
    :param int seriesDosespositiveInt: Recommended number of doses for immunity
    :param str seriesDosespositiveInt: Recommended number of doses for immunity
    :param Reference supportingImmunization: Past immunizations supporting recommendation
    :param Reference supportingPatientInformation: Patient observations supporting recommendation
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    patient: "Reference" = None
    
    date: str = None
    
    authority: "Reference" = None
    
    recommendation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    vaccineCode: list["CodeableConcept"] = None
    
    targetDisease: "CodeableConcept" = None
    
    contraindicatedVaccineCode: list["CodeableConcept"] = None
    
    forecastStatus: "CodeableConcept" = None
    
    forecastReason: list["CodeableConcept"] = None
    
    dateCriterion: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: str = None
    
    description: str = None
    
    series: str = None
    
    doseNumberpositiveInt: int = None
    
    doseNumberpositiveInt: str = None
    
    seriesDosespositiveInt: int = None
    
    seriesDosespositiveInt: str = None
    
    supportingImmunization: list["Reference"] = None
    
    supportingPatientInformation: list["Reference"] = None
    