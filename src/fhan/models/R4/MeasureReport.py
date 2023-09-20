"""
Generated class for MeasureReport. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Population(Element):
    """ The populations that make up the population group, one for each type of population appropriate for the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    
    count: int = None
    subjectResults: "Reference" = None
    

    
        
    
        
    
    
@dataclass
class Component(Element):
    """ A stratifier component value.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: What stratifier component of the group
    :param CodeableConcept value: The stratum component value, e.g. male
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    value: "CodeableConcept" = None
    

    
    
@dataclass
class Population(Element):
    """ The populations that make up the stratum, one for each type of population appropriate to the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    
    count: int = None
    subjectResults: "Reference" = None
    
  
    
    
@dataclass
class Stratum(Element):
    """ This element contains the results for a single stratum within the stratifier. For example, when stratifying on administrative gender, there will be four strata, one for each possible gender value.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept value: The stratum value, e.g. male
    :param Component component: Stratifier component values
    :param Population population: Population results in this stratum
    :param Quantity measureScore: What score this stratum achieved
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    value: "CodeableConcept" = None
    component: list[Component] = None
    population: list[Population] = None
    measureScore: "Quantity" = None
    
  
    
    
@dataclass
class Stratifier(Element):
    """ When a measure includes multiple stratifiers, there will be a stratifier group for each stratifier defined by the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: What stratifier of the group
    :param Stratum stratum: Stratum results, one for each unique value, or set of values, in the stratifier, or stratifier components
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: list[CodeableConcept] = None
    stratum: list[Stratum] = None
    
  
    
    
@dataclass
class Group(Element):
    """ The results of the calculation, one for each population group in the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Meaning of the group
    :param Population population: The populations in the group
    :param Quantity measureScore: What score this group achieved
    :param Stratifier stratifier: Stratification results
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    population: list[Population] = None
    measureScore: "Quantity" = None
    stratifier: list[Stratifier] = None
    
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
    :param Group group: Measure results for each group
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
    
    group: list["Group"] = None
    
    evaluatedResource: list["Reference"] = None
    