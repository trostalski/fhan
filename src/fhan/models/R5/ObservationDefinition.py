"""
Generated class for ObservationDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class ObservationDefinition:
    """ Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Logical canonical URL to reference this ObservationDefinition (globally unique)
    :param Identifier identifier: Business identifier of the ObservationDefinition
    :param str version: Business version of the ObservationDefinition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this ObservationDefinition (computer friendly)
    :param str title: Name for this ObservationDefinition (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: If for testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: The name of the individual or organization that published the ObservationDefinition
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the ObservationDefinition
    :param UsageContext useContext: Content intends to support these contexts
    :param CodeableConcept jurisdiction: Intended jurisdiction for this ObservationDefinition (if applicable)
    :param str purpose: Why this ObservationDefinition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When ObservationDefinition was approved by publisher
    :param str lastReviewDate: Date on which the asset content was last reviewed by the publisher
    :param Period effectivePeriod: The effective date range for the ObservationDefinition
    :param str derivedFromCanonical: Based on FHIR definition of another observation
    :param str derivedFromUri: Based on external definition
    :param CodeableConcept subject: Type of subject for the defined observation
    :param CodeableConcept performerType: Desired kind of performer for such kind of observation
    :param CodeableConcept category: General type of observation
    :param CodeableConcept code: Type of observation
    :param str permittedDataType: Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period
    :param bool multipleResultsAllowed: Multiple results allowed for conforming observations
    :param CodeableConcept bodySite: Body part to be observed
    :param CodeableConcept method: Method used to produce the observation
    :param Reference specimen: Kind of specimen used by this type of observation
    :param Reference device: Measurement device or model of device
    :param str preferredReportName: The preferred name to be used when reporting the observation results
    :param Coding permittedUnit: Unit for quantitative results
    :param BackboneElement qualifiedValue: Set of qualified values for observation results
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept context: Context qualifier for the set of qualified values
    :param CodeableConcept appliesTo: Targetted population for the set of qualified values
    :param str gender: male | female | other | unknown
    :param Range age: Applicable age range for the set of qualified values
    :param Range gestationalAge: Applicable gestational age range for the set of qualified values
    :param str condition: Condition associated with the set of qualified values
    :param str rangeCategory: reference | critical | absolute
    :param Range range: The range for continuous or ordinal observations
    :param str validCodedValueSet: Value set of valid coded values as part of this set of qualified values
    :param str normalCodedValueSet: Value set of normal coded values as part of this set of qualified values
    :param str abnormalCodedValueSet: Value set of abnormal coded values as part of this set of qualified values
    :param str criticalCodedValueSet: Value set of critical coded values as part of this set of qualified values
    :param Reference hasMember: Definitions of related resources belonging to this kind of observation group
    :param BackboneElement component: Component results
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of observation
    :param str permittedDataType: Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period
    :param Coding permittedUnit: Unit for quantitative results
    :param BackboneElement qualifiedValue: Set of qualified values for observation results
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    derivedFromCanonical: str = None
    
    derivedFromUri: str = None
    
    subject: "CodeableConcept" = None
    
    performerType: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    permittedDataType: str = None
    
    multipleResultsAllowed: bool = None
    
    bodySite: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    preferredReportName: str = None
    
    permittedUnit: "Coding" = None
    
    qualifiedValue: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    context: "CodeableConcept" = None
    
    appliesTo: "CodeableConcept" = None
    
    gender: str = None
    
    age: "Range" = None
    
    gestationalAge: "Range" = None
    
    condition: str = None
    
    rangeCategory: str = None
    
    range: "Range" = None
    
    validCodedValueSet: str = None
    
    normalCodedValueSet: str = None
    
    abnormalCodedValueSet: str = None
    
    criticalCodedValueSet: str = None
    
    hasMember: "Reference" = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    permittedDataType: str = None
    
    permittedUnit: "Coding" = None
    
    qualifiedValue: "BackboneElement" = None
    