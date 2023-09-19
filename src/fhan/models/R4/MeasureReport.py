"""
Generated class for MeasureReport. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class MeasureReport(ModelBase):
    """ The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to the resources involved in that calculation.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Additional identifier for the MeasureReport
    :param str status: complete | pending | error
    :param str type: individual | subject-list | summary | data-collection
    :param str measure: What measure was calculated
    :param Reference subject: What individual(s) the report is for
    :param str date: When the report was generated
    :param Reference reporter: Who is reporting the data
    :param Period period: What period the report covers
    :param CodeableConcept improvementNotation: increase | decrease
    :param BackboneElement group: Measure results for each group
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Meaning of the group
    :param BackboneElement population: The populations in the group
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    :param Quantity measureScore: What score this group achieved
    :param BackboneElement stratifier: Stratification results
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: What stratifier of the group
    :param BackboneElement stratum: Stratum results, one for each unique value, or set of values, in the stratifier, or stratifier components
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept value: The stratum value, e.g. male
    :param BackboneElement component: Stratifier component values
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: What stratifier component of the group
    :param CodeableConcept value: The stratum component value, e.g. male
    :param BackboneElement population: Population results in this stratum
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    :param Quantity measureScore: What score this stratum achieved
    :param Reference evaluatedResource: What data was used to calculate the measure score
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
    
    type: str = None
    
    measure: str = None
    
    subject: "Reference" = None
    
    date: str = None
    
    reporter: "Reference" = None
    
    period: "Period" = None
    
    improvementNotation: "CodeableConcept" = None
    
    group: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    population: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
    stratifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    stratum: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    value: "CodeableConcept" = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    value: "CodeableConcept" = None
    
    population: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
    evaluatedResource: "Reference" = None
    