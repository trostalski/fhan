"""
Generated class for ImmunizationRecommendation. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ImmunizationRecommendation:
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
    :param str doseNumber: Recommended dose number within series
    :param str seriesDoses: Recommended number of doses for immunity
    :param Reference supportingImmunization: Past immunizations supporting recommendation
    :param Reference supportingPatientInformation: Patient observations supporting recommendation
    
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
    
    patient: "Reference" = None
    
    date: str = None
    
    authority: "Reference" = None
    
    recommendation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    vaccineCode: "CodeableConcept" = None
    
    targetDisease: "CodeableConcept" = None
    
    contraindicatedVaccineCode: "CodeableConcept" = None
    
    forecastStatus: "CodeableConcept" = None
    
    forecastReason: "CodeableConcept" = None
    
    dateCriterion: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    value: str = None
    
    description: str = None
    
    series: str = None
    
    doseNumber: str = None
    
    seriesDoses: str = None
    
    supportingImmunization: "Reference" = None
    
    supportingPatientInformation: "Reference" = None
    