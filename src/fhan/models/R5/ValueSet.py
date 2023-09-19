"""
Generated class for ValueSet. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
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


@dataclass
class ValueSet:
    """ Enforces the minimum information set for the value set metadata required by HL7 and other organizations that share and publish value sets
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Extension
    :param Extension extension:knowledgeRepresentationLevel: narrative | semi-structured | structured | executable
    :param Extension extension:authoritativeSource: Reference to the current trusted source of the ValueSet resource (metadata and definition)
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this value set, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the value set (business identifier)
    :param str version: Business version of the value set
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this value set (computer friendly)
    :param str title: Name for this value set (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the value set
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for value set (if applicable)
    :param bool immutable: Indicates whether or not any change to the content logical definition may occur
    :param str purpose: Why this value set is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the ValueSet was approved by publisher
    :param str lastReviewDate: When the ValueSet was last reviewed by the publisher
    :param Period effectivePeriod: When the ValueSet is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the ValueSet
    :param ContactDetail editor: Who edited the ValueSet
    :param ContactDetail reviewer: Who reviewed the ValueSet
    :param ContactDetail endorser: Who endorsed the ValueSet
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param BackboneElement compose: Content logical definition of the value set (CLD)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lockedDate: Fixed date for references with no specified version (transitive)
    :param bool inactive: Whether inactive codes are in the value set
    :param BackboneElement include: Include one or more codes from a code system or other value set(s)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: The system the codes come from
    :param str version: Specific version of the code system referred to
    :param BackboneElement concept: A concept defined in the system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code or expression from system
    :param str display: Text to display for this code for this value set in this valueset
    :param BackboneElement designation: Additional representations for this concept
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: Human language of the designation
    :param Coding use: Types of uses of designations
    :param Coding additionalUse: Additional ways how this designation would be used
    :param str value: The text value for this designation
    :param BackboneElement filter: Select codes/concepts by their properties (including relationships)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str property: A property/filter defined by the code system
    :param str op: = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | child-of | descendent-leaf | exists
    :param str value: Code from the system, or regex criteria, or boolean value for exists
    :param str valueSet: Select the contents included in this value set
    :param str copyright: A copyright statement for the specific code system included in the value set
    :param BackboneElement exclude: Include one or more codes from a code system or other value set(s)
    :param str property: Property to return if client doesn't override
    :param BackboneElement expansion: Used when the value set is "expanded"
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identifier: Identifies the value set expansion (business identifier)
    :param str next: Opaque urls for paging through expansion results
    :param str timestamp: Time ValueSet expansion happened
    :param int total: Total number of codes in the expansion
    :param int offset: Offset at which this resource starts
    :param BackboneElement parameter: Parameter that controlled the expansion process
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name as assigned by the client or server
    :param str valuestring: Value of the named parameter
    :param bool valuestring: Value of the named parameter
    :param int valuestring: Value of the named parameter
    :param float valuestring: Value of the named parameter
    :param str valuestring: Value of the named parameter
    :param str valuestring: Value of the named parameter
    :param str valuestring: Value of the named parameter
    :param BackboneElement property: Additional information supplied about each concept
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies the property on the concepts, and when referred to in operations
    :param str uri: Formal identifier for the property
    :param BackboneElement contains: Codes in the value set
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: System value for the code
    :param bool abstract: If user cannot select this entry
    :param bool inactive: If concept is inactive in the code system
    :param str version: Version in which this code/display is defined
    :param str code: Code - if blank, this is not a selectable code
    :param str display: User display for the concept
    :param BackboneElement designation: Additional representations for this concept
    :param BackboneElement property: Property value for the concept
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to ValueSet.expansion.property.code
    :param str valuecode: Value of the property for this concept
    :param Coding valuecode: Value of the property for this concept
    :param str valuecode: Value of the property for this concept
    :param int valuecode: Value of the property for this concept
    :param bool valuecode: Value of the property for this concept
    :param str valuecode: Value of the property for this concept
    :param float valuecode: Value of the property for this concept
    :param BackboneElement subProperty: SubProperty value for the concept
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to ValueSet.expansion.property.code
    :param str valuecode: Value of the subproperty for this concept
    :param Coding valuecode: Value of the subproperty for this concept
    :param str valuecode: Value of the subproperty for this concept
    :param int valuecode: Value of the subproperty for this concept
    :param bool valuecode: Value of the subproperty for this concept
    :param str valuecode: Value of the subproperty for this concept
    :param float valuecode: Value of the subproperty for this concept
    :param BackboneElement contains: Codes in the value set
    :param BackboneElement scope: Description of the semantic space the Value Set Expansion is intended to cover and should further clarify the text in ValueSet.description
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str inclusionCriteria: Criteria describing which concepts or codes should be included and why
    :param str exclusionCriteria: Criteria describing which concepts or codes should be excluded and why
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    extension:knowledgeRepresentationLevel: "Extension" = None
    
    extension:authoritativeSource: "Extension" = None
    
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
    
    immutable: bool = None
    
    purpose: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    topic: "CodeableConcept" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    compose: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    lockedDate: str = None
    
    inactive: bool = None
    
    include: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    system: str = None
    
    version: str = None
    
    concept: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    display: str = None
    
    designation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: str = None
    
    use: "Coding" = None
    
    additionalUse: "Coding" = None
    
    value: str = None
    
    filter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    property: str = None
    
    op: str = None
    
    value: str = None
    
    valueSet: str = None
    
    copyright: str = None
    
    exclude: "BackboneElement" = None
    
    property: str = None
    
    expansion: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: str = None
    
    next: str = None
    
    timestamp: str = None
    
    total: int = None
    
    offset: int = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    valuestring: str = None
    
    valuestring: bool = None
    
    valuestring: int = None
    
    valuestring: float = None
    
    valuestring: str = None
    
    valuestring: str = None
    
    valuestring: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    uri: str = None
    
    contains: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    system: str = None
    
    abstract: bool = None
    
    inactive: bool = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    designation: "BackboneElement" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    valuecode: str = None
    
    valuecode: "Coding" = None
    
    valuecode: str = None
    
    valuecode: int = None
    
    valuecode: bool = None
    
    valuecode: str = None
    
    valuecode: float = None
    
    subProperty: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    valuecode: str = None
    
    valuecode: "Coding" = None
    
    valuecode: str = None
    
    valuecode: int = None
    
    valuecode: bool = None
    
    valuecode: str = None
    
    valuecode: float = None
    
    contains: "BackboneElement" = None
    
    scope: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    inclusionCriteria: str = None
    
    exclusionCriteria: str = None
    