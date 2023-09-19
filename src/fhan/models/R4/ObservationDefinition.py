"""
Generated class for ObservationDefinition. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.generator_models import ModelBase


@dataclass
class ObservationDefinition(ModelBase):
    """ Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept category: Category of observation
    :param CodeableConcept code: Type of observation (code / type)
    :param Identifier identifier: Business identifier for this ObservationDefinition instance
    :param str permittedDataType: Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period
    :param bool multipleResultsAllowed: Multiple results allowed
    :param CodeableConcept method: Method used to produce the observation
    :param str preferredReportName: Preferred report name
    :param BackboneElement quantitativeDetails: Characteristics of quantitative results
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept customaryUnit: Customary unit for quantitative results
    :param CodeableConcept unit: SI unit for quantitative results
    :param float conversionFactor: SI to Customary unit conversion factor
    :param int decimalPrecision: Decimal precision of observation quantitative results
    :param BackboneElement qualifiedInterval: Qualified range for continuous and ordinal observation results
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str category: reference | critical | absolute
    :param Range range: The interval itself, for continuous or ordinal observations
    :param CodeableConcept context: Range context qualifier
    :param CodeableConcept appliesTo: Targetted population of the range
    :param str gender: male | female | other | unknown
    :param Range age: Applicable age range, if relevant
    :param Range gestationalAge: Applicable gestational age range, if relevant
    :param str condition: Condition associated with the reference range
    :param Reference validCodedValueSet: Value set of valid coded values for the observations conforming to this ObservationDefinition
    :param Reference normalCodedValueSet: Value set of normal coded values for the observations conforming to this ObservationDefinition
    :param Reference abnormalCodedValueSet: Value set of abnormal coded values for the observations conforming to this ObservationDefinition
    :param Reference criticalCodedValueSet: Value set of critical coded values for the observations conforming to this ObservationDefinition
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    identifier: "Identifier" = None
    
    permittedDataType: str = None
    
    multipleResultsAllowed: bool = None
    
    method: "CodeableConcept" = None
    
    preferredReportName: str = None
    
    quantitativeDetails: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    customaryUnit: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    conversionFactor: float = None
    
    decimalPrecision: int = None
    
    qualifiedInterval: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    category: str = None
    
    range: "Range" = None
    
    context: "CodeableConcept" = None
    
    appliesTo: "CodeableConcept" = None
    
    gender: str = None
    
    age: "Range" = None
    
    gestationalAge: "Range" = None
    
    condition: str = None
    
    validCodedValueSet: "Reference" = None
    
    normalCodedValueSet: "Reference" = None
    
    abnormalCodedValueSet: "Reference" = None
    
    criticalCodedValueSet: "Reference" = None
    