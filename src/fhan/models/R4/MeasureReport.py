"""
Generated class for MeasureReport. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class group(Element):
    """ The results of the calculation, one for each population group in the measure.
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
    """
    group: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
    stratifier: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: list["CodeableConcept"] = None
    
    stratum: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "CodeableConcept" = None
    
    component: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: "CodeableConcept" = None
    
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
@dataclass
class population(Element):
    """ The populations that make up the population group, one for each type of population appropriate for the measure.
    :param BackboneElement population: The populations in the group
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    """
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
@dataclass
class stratifier(Element):
    """ When a measure includes multiple stratifiers, there will be a stratifier group for each stratifier defined by the measure.
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
    """
    stratifier: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: list["CodeableConcept"] = None
    
    stratum: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "CodeableConcept" = None
    
    component: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: "CodeableConcept" = None
    
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
@dataclass
class stratum(Element):
    """ This element contains the results for a single stratum within the stratifier. For example, when stratifying on administrative gender, there will be four strata, one for each possible gender value.
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
    """
    stratum: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "CodeableConcept" = None
    
    component: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: "CodeableConcept" = None
    
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
@dataclass
class component(Element):
    """ A stratifier component value.
    :param BackboneElement component: Stratifier component values
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: What stratifier component of the group
    :param CodeableConcept value: The stratum component value, e.g. male
    """
    component: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: "CodeableConcept" = None
    
@dataclass
class population(Element):
    """ The populations that make up the stratum, one for each type of population appropriate to the measure.
    :param BackboneElement population: Population results in this stratum
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    """
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    


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
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    status: str = None
    
    type: str = None
    
    measure: str = None
    
    subject: "Reference" = None
    
    date: str = None
    
    reporter: "Reference" = None
    
    period: "Period" = None
    
    improvementNotation: "CodeableConcept" = None
    
    group: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
    stratifier: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: list["CodeableConcept"] = None
    
    stratum: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    value: "CodeableConcept" = None
    
    component: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    value: "CodeableConcept" = None
    
    population: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    measureScore: "Quantity" = None
    
    evaluatedResource: list["Reference"] = None
    