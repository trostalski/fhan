"""
Generated class for ObservationDefinition. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Range import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class QuantitativeDetails(Element):
    """ Characteristics for quantitative results of this observation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept customaryUnit: Customary unit for quantitative results
    :param CodeableConcept unit: SI unit for quantitative results
    :param float conversionFactor: SI to Customary unit conversion factor
    :param int decimalPrecision: Decimal precision of observation quantitative results
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    customaryUnit: "CodeableConcept" = CodeableConcept()
    unit: "CodeableConcept" = CodeableConcept()
    
    conversionFactor: float = None
    
    decimalPrecision: int = None
    

    
    
@dataclass
class QualifiedInterval(Element):
    """ Multiple  ranges of results qualified by different contexts for ordinal or continuous observations conforming to this ObservationDefinition.:param str id: Unique id for inter-element referencing
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
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    category: str = None
    range: "Range" = Range()
    context: "CodeableConcept" = CodeableConcept()
    appliesTo: list[CodeableConcept] = CodeableConcept() 
    
    gender: str = None
    age: "Range" = Range()
    gestationalAge: "Range" = Range()
    
    condition: str = None
    

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
    :param QuantitativeDetails quantitativeDetails: Characteristics of quantitative results
    :param QualifiedInterval qualifiedInterval: Qualified range for continuous and ordinal observation results
    :param Reference validCodedValueSet: Value set of valid coded values for the observations conforming to this ObservationDefinition
    :param Reference normalCodedValueSet: Value set of normal coded values for the observations conforming to this ObservationDefinition
    :param Reference abnormalCodedValueSet: Value set of abnormal coded values for the observations conforming to this ObservationDefinition
    :param Reference criticalCodedValueSet: Value set of critical coded values for the observations conforming to this ObservationDefinition
    """

    resourceType: str = "ObservationDefinition"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    category: list[CodeableConcept] = CodeableConcept() 
    
    code: "CodeableConcept" = CodeableConcept()
    
    identifier: list[Identifier] = Identifier() 
    
    permittedDataType: str = None
    
    multipleResultsAllowed: bool = None
    
    method: "CodeableConcept" = CodeableConcept()
    
    preferredReportName: str = None
    
    quantitativeDetails: "QuantitativeDetails" = QuantitativeDetails()
    
    qualifiedInterval: list[QualifiedInterval] = QualifiedInterval() 
    
    validCodedValueSet: "Reference" = Reference()
    
    normalCodedValueSet: "Reference" = Reference()
    
    abnormalCodedValueSet: "Reference" = Reference()
    
    criticalCodedValueSet: "Reference" = Reference()
    