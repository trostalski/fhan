"""
Generated class for MeasureReport. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class MeasureReport:
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
    :param str type: individual | subject-list | summary | data-exchange
    :param str dataUpdateType: incremental | snapshot
    :param str measure: What measure was calculated
    :param Reference subject: What individual(s) the report is for
    :param str date: When the measure was calculated
    :param Reference reporter: Who is reporting the data
    :param Reference reportingVendor: What vendor prepared the data
    :param Reference location: Where the reported data is from
    :param Period period: What period the report covers
    :param Reference inputParameters: What parameters were provided to the report
    :param CodeableConcept scoring: What scoring method (e.g. proportion, ratio, continuous-variable)
    :param CodeableConcept improvementNotation: increase | decrease
    :param BackboneElement group: Measure results for each group
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific group from Measure
    :param CodeableConcept code: Meaning of the group
    :param Reference subject: What individual(s) the report is for
    :param BackboneElement population: The populations in the group
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific population from Measure
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    :param Reference subjectReport: For subject-list reports, a subject result in this population
    :param Reference subjects: What individual(s) in the population
    :param Quantity measureScoreQuantity: What score this group achieved
    :param str measureScoreQuantity: What score this group achieved
    :param CodeableConcept measureScoreQuantity: What score this group achieved
    :param Period measureScoreQuantity: What score this group achieved
    :param Range measureScoreQuantity: What score this group achieved
    :param Duration measureScoreQuantity: What score this group achieved
    :param BackboneElement stratifier: Stratification results
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific stratifier from Measure
    :param CodeableConcept code: What stratifier of the group
    :param BackboneElement stratum: Stratum results, one for each unique value, or set of values, in the stratifier, or stratifier components
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept valueCodeableConcept: The stratum value, e.g. male
    :param bool valueCodeableConcept: The stratum value, e.g. male
    :param Quantity valueCodeableConcept: The stratum value, e.g. male
    :param Range valueCodeableConcept: The stratum value, e.g. male
    :param Reference valueCodeableConcept: The stratum value, e.g. male
    :param BackboneElement component: Stratifier component values
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific stratifier component from Measure
    :param CodeableConcept code: What stratifier component of the group
    :param CodeableConcept valueCodeableConcept: The stratum component value, e.g. male
    :param bool valueCodeableConcept: The stratum component value, e.g. male
    :param Quantity valueCodeableConcept: The stratum component value, e.g. male
    :param Range valueCodeableConcept: The stratum component value, e.g. male
    :param Reference valueCodeableConcept: The stratum component value, e.g. male
    :param BackboneElement population: Population results in this stratum
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific population from Measure
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    :param Reference subjectReport: For subject-list reports, a subject result in this population
    :param Reference subjects: What individual(s) in the population
    :param Quantity measureScoreQuantity: What score this stratum achieved
    :param str measureScoreQuantity: What score this stratum achieved
    :param CodeableConcept measureScoreQuantity: What score this stratum achieved
    :param Period measureScoreQuantity: What score this stratum achieved
    :param Range measureScoreQuantity: What score this stratum achieved
    :param Duration measureScoreQuantity: What score this stratum achieved
    :param Reference supplementalData: Additional information collected for the report
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
    
    dataUpdateType: str = None
    
    measure: str = None
    
    subject: "Reference" = None
    
    date: str = None
    
    reporter: "Reference" = None
    
    reportingVendor: "Reference" = None
    
    location: "Reference" = None
    
    period: "Period" = None
    
    inputParameters: "Reference" = None
    
    scoring: "CodeableConcept" = None
    
    improvementNotation: "CodeableConcept" = None
    
    group: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    population: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    subjectReport: "Reference" = None
    
    subjects: "Reference" = None
    
    measureScoreQuantity: "Quantity" = None
    
    measureScoreQuantity: str = None
    
    measureScoreQuantity: "CodeableConcept" = None
    
    measureScoreQuantity: "Period" = None
    
    measureScoreQuantity: "Range" = None
    
    measureScoreQuantity: "Duration" = None
    
    stratifier: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    stratum: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    
    valueCodeableConcept: "Reference" = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    
    valueCodeableConcept: "Reference" = None
    
    population: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    linkId: str = None
    
    code: "CodeableConcept" = None
    
    count: int = None
    
    subjectResults: "Reference" = None
    
    subjectReport: "Reference" = None
    
    subjects: "Reference" = None
    
    measureScoreQuantity: "Quantity" = None
    
    measureScoreQuantity: str = None
    
    measureScoreQuantity: "CodeableConcept" = None
    
    measureScoreQuantity: "Period" = None
    
    measureScoreQuantity: "Range" = None
    
    measureScoreQuantity: "Duration" = None
    
    supplementalData: "Reference" = None
    
    evaluatedResource: "Reference" = None
    