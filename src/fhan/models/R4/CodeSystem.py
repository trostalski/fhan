"""
Generated class for CodeSystem. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Coding import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class CodeSystem(ModelBase):
    """ Enforces the minimum information set for the value set metadata required by HL7 and other organizations that share and publish value sets
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this code system, represented as a URI (globally unique) (Coding.system)
    :param Identifier identifier: Additional identifier for the code system (business identifier)
    :param str version: Business version of the code system (Coding.version)
    :param str name: Name for this code system (computer friendly)
    :param str title: Name for this code system (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the code system
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for code system (if applicable)
    :param str purpose: Why this code system is defined
    :param str copyright: Use and/or publishing restrictions
    :param bool caseSensitive: If code comparison is case sensitive
    :param str valueSet: Canonical reference to the value set with entire code system
    :param str hierarchyMeaning: grouped-by | is-a | part-of | classified-with
    :param bool compositional: If code system defines a compositional grammar
    :param bool versionNeeded: If definitions are not stable
    :param str content: not-present | example | fragment | complete | supplement
    :param str supplements: Canonical URL of Code System this adds designations and properties to
    :param int count: Total concepts in the code system
    :param BackboneElement filter: Filter that can be used in a value set
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code that identifies the filter
    :param str description: How or why the filter is used
    :param str operator: = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    :param str value: What to use for the value
    :param BackboneElement property: Additional information supplied about each concept
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies the property on the concepts, and when referred to in operations
    :param str uri: Formal identifier for the property
    :param str description: Why the property is defined, and/or what it conveys
    :param str type: code | Coding | string | integer | boolean | dateTime | decimal
    :param BackboneElement concept: Concepts in the code system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code that identifies concept
    :param str display: Text to display to the user
    :param str definition: Formal definition
    :param BackboneElement designation: Additional representations for the concept
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: Human language of the designation
    :param Coding use: Details how this designation would be used
    :param str value: The text value for this designation
    :param BackboneElement property: Property value for the concept
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to CodeSystem.property.code
    :param str valuecode: Value of the property for this concept
    :param Coding valuecode: Value of the property for this concept
    :param str valuecode: Value of the property for this concept
    :param int valuecode: Value of the property for this concept
    :param bool valuecode: Value of the property for this concept
    :param str valuecode: Value of the property for this concept
    :param float valuecode: Value of the property for this concept
    :param BackboneElement concept: Concepts in the code system
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
    
    caseSensitive: bool = None
    
    valueSet: str = None
    
    hierarchyMeaning: str = None
    
    compositional: bool = None
    
    versionNeeded: bool = None
    
    content: str = None
    
    supplements: str = None
    
    count: int = None
    
    filter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    description: str = None
    
    operator: str = None
    
    value: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    uri: str = None
    
    description: str = None
    
    type: str = None
    
    concept: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    display: str = None
    
    definition: str = None
    
    designation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: str = None
    
    use: "Coding" = None
    
    value: str = None
    
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
    
    concept: "BackboneElement" = None
    