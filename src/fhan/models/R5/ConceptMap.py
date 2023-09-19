"""
Generated class for ConceptMap. 
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
from fhan.models.R5.Quantity import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *


@dataclass
class ConceptMap:
    """ Enforces the minimum information set for the concept map metadata required by HL7 and other organizations that share and publish concept maps
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Extension
    :param Extension extension:knowledgeRepresentationLevel: narrative | semi-structured | structured | executable
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this concept map, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the concept map
    :param str version: Business version of the concept map
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this concept map (computer friendly)
    :param str title: Name for this concept map (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the concept map
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for concept map (if applicable)
    :param str purpose: Why this concept map is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the ConceptMap was approved by publisher
    :param str lastReviewDate: When the ConceptMap was last reviewed by the publisher
    :param Period effectivePeriod: When the ConceptMap is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the ConceptMap
    :param ContactDetail editor: Who edited the ConceptMap
    :param ContactDetail reviewer: Who reviewed the ConceptMap
    :param ContactDetail endorser: Who endorsed the ConceptMap
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param BackboneElement property: Additional properties of the mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies the property on the mappings, and when referred to in the $translate operation
    :param str uri: Formal identifier for the property
    :param str description: Why the property is defined, and/or what it conveys
    :param str type: Coding | string | integer | boolean | dateTime | decimal | code
    :param str system: The CodeSystem from which code values come
    :param BackboneElement additionalAttribute: Definition of an additional attribute to act as a data source or target
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies this additional attribute through this resource
    :param str uri: Formal identifier for the data element referred to in this attribte
    :param str description: Why the additional attribute is defined, and/or what the data element it refers to is
    :param str type: code | Coding | string | boolean | Quantity
    :param str sourceScopeuri: The source value set that contains the concepts that are being mapped
    :param str sourceScopeuri: The source value set that contains the concepts that are being mapped
    :param str targetScopeuri: The target value set which provides context for the mappings
    :param str targetScopeuri: The target value set which provides context for the mappings
    :param BackboneElement group: Same source and target systems
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str source: Source system where concepts to be mapped are defined
    :param str target: Target system that the concepts are to be mapped to
    :param BackboneElement element: Mappings for a concept from the source set
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies element being mapped
    :param str display: Display for the code
    :param str valueSet: Identifies the set of concepts being mapped
    :param bool noMap: No mapping to a target concept for this source concept
    :param BackboneElement target: Concept in target system for element
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code that identifies the target element
    :param str display: Display for the code
    :param str valueSet: Identifies the set of target concepts
    :param str relationship: related-to | equivalent | source-is-narrower-than-target | source-is-broader-than-target | not-related-to
    :param str comment: Description of status/issues in mapping
    :param BackboneElement property: Property value for the source -> target mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to ConceptMap.property.code
    :param Coding valueCoding: Value of the property for this concept
    :param str valueCoding: Value of the property for this concept
    :param int valueCoding: Value of the property for this concept
    :param bool valueCoding: Value of the property for this concept
    :param str valueCoding: Value of the property for this concept
    :param float valueCoding: Value of the property for this concept
    :param str valueCoding: Value of the property for this concept
    :param BackboneElement dependsOn: Other properties required for this mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str attribute: A reference to a mapping attribute defined in ConceptMap.additionalAttribute
    :param str valuecode: Value of the referenced data element
    :param Coding valuecode: Value of the referenced data element
    :param str valuecode: Value of the referenced data element
    :param bool valuecode: Value of the referenced data element
    :param Quantity valuecode: Value of the referenced data element
    :param str valueSet: The mapping depends on a data element with a value from this value set
    :param BackboneElement product: Other properties required for this mapping
    :param BackboneElement unmapped: What to do when there is no mapping target for the source concept and ConceptMap.group.element.noMap is not true
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: use-source-code | fixed | other-map
    :param str code: Fixed code when mode = fixed
    :param str display: Display for the code
    :param str valueSet: Fixed code set when mode = fixed
    :param str relationship: related-to | equivalent | source-is-narrower-than-target | source-is-broader-than-target | not-related-to
    :param str otherMap: canonical reference to an additional ConceptMap to use for mapping if the source concept is unmapped
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    extension:knowledgeRepresentationLevel: "Extension" = None
    
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
    
    topic: "CodeableConcept" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    uri: str = None
    
    description: str = None
    
    type: str = None
    
    system: str = None
    
    additionalAttribute: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    uri: str = None
    
    description: str = None
    
    type: str = None
    
    sourceScopeuri: str = None
    
    sourceScopeuri: str = None
    
    targetScopeuri: str = None
    
    targetScopeuri: str = None
    
    group: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    source: str = None
    
    target: str = None
    
    element: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    display: str = None
    
    valueSet: str = None
    
    noMap: bool = None
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    display: str = None
    
    valueSet: str = None
    
    relationship: str = None
    
    comment: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    valueCoding: "Coding" = None
    
    valueCoding: str = None
    
    valueCoding: int = None
    
    valueCoding: bool = None
    
    valueCoding: str = None
    
    valueCoding: float = None
    
    valueCoding: str = None
    
    dependsOn: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    attribute: str = None
    
    valuecode: str = None
    
    valuecode: "Coding" = None
    
    valuecode: str = None
    
    valuecode: bool = None
    
    valuecode: "Quantity" = None
    
    valueSet: str = None
    
    product: "BackboneElement" = None
    
    unmapped: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    code: str = None
    
    display: str = None
    
    valueSet: str = None
    
    relationship: str = None
    
    otherMap: str = None
    