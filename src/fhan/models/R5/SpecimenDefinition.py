"""
Generated class for SpecimenDefinition. 
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
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class SpecimenDefinition:
    """ A kind of specimen with associated set of requirements.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Logical canonical URL to reference this SpecimenDefinition (globally unique)
    :param Identifier identifier: Business identifier
    :param str version: Business version of the SpecimenDefinition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this {{title}} (computer friendly)
    :param str title: Name for this SpecimenDefinition (Human friendly)
    :param str derivedFromCanonical: Based on FHIR definition of another SpecimenDefinition
    :param str derivedFromUri: Based on external definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: If this SpecimenDefinition is not for real usage
    :param CodeableConcept subjectCodeableConcept: Type of subject for specimen collection
    :param Reference subjectCodeableConcept: Type of subject for specimen collection
    :param str date: Date status first applied
    :param str publisher: The name of the individual or organization that published the SpecimenDefinition
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the SpecimenDefinition
    :param UsageContext useContext: Content intends to support these contexts
    :param CodeableConcept jurisdiction: Intended jurisdiction for this SpecimenDefinition (if applicable)
    :param str purpose: Why this SpecimenDefinition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When SpecimenDefinition was approved by publisher
    :param str lastReviewDate: The date on which the asset content was last reviewed by the publisher
    :param Period effectivePeriod: The effective date range for the SpecimenDefinition
    :param CodeableConcept typeCollected: Kind of material to collect
    :param CodeableConcept patientPreparation: Patient preparation for collection
    :param str timeAspect: Time aspect for collection
    :param CodeableConcept collection: Specimen collection procedure
    :param BackboneElement typeTested: Specimen in container intended for testing by lab
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool isDerived: Primary or secondary specimen
    :param CodeableConcept type: Type of intended specimen
    :param str preference: preferred | alternate
    :param BackboneElement container: The specimen's container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: The material type used for the container
    :param CodeableConcept type: Kind of container associated with the kind of specimen
    :param CodeableConcept cap: Color of container cap
    :param str description: The description of the kind of container
    :param Quantity capacity: The capacity of this kind of container
    :param Quantity minimumVolumeQuantity: Minimum volume
    :param str minimumVolumeQuantity: Minimum volume
    :param BackboneElement additive: Additive associated with container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveCodeableConcept: Additive associated with container
    :param str preparation: Special processing applied to the container for this specimen type
    :param str requirement: Requirements for specimen delivery and special handling
    :param Duration retentionTime: The usual time for retaining this kind of specimen
    :param bool singleUse: Specimen for single use only
    :param CodeableConcept rejectionCriterion: Criterion specified for specimen rejection
    :param BackboneElement handling: Specimen handling before testing
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept temperatureQualifier: Qualifies the interval of temperature
    :param Range temperatureRange: Temperature range for these handling instructions
    :param Duration maxDuration: Maximum preservation time
    :param str instruction: Preservation instruction
    :param CodeableConcept testingDestination: Where the specimen will be tested
    
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
    
    derivedFromCanonical: str = None
    
    derivedFromUri: str = None
    
    status: str = None
    
    experimental: bool = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    subjectCodeableConcept: "Reference" = None
    
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
    
    typeCollected: "CodeableConcept" = None
    
    patientPreparation: "CodeableConcept" = None
    
    timeAspect: str = None
    
    collection: "CodeableConcept" = None
    
    typeTested: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    isDerived: bool = None
    
    type: "CodeableConcept" = None
    
    preference: str = None
    
    container: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    cap: "CodeableConcept" = None
    
    description: str = None
    
    capacity: "Quantity" = None
    
    minimumVolumeQuantity: "Quantity" = None
    
    minimumVolumeQuantity: str = None
    
    additive: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
    preparation: str = None
    
    requirement: str = None
    
    retentionTime: "Duration" = None
    
    singleUse: bool = None
    
    rejectionCriterion: "CodeableConcept" = None
    
    handling: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    temperatureQualifier: "CodeableConcept" = None
    
    temperatureRange: "Range" = None
    
    maxDuration: "Duration" = None
    
    instruction: str = None
    
    testingDestination: "CodeableConcept" = None
    