"""
Generated class for OperationDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *


@dataclass
class OperationDefinition:
    """ A formal computable definition of an operation (on the RESTful interface) or a named query (using the search interaction).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this operation definition, represented as an absolute URI (globally unique)
    :param Identifier identifier: Additional identifier for the implementation guide (business identifier)
    :param str version: Business version of the operation definition
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this operation definition (computer friendly)
    :param str title: Name for this operation definition (human friendly)
    :param str status: draft | active | retired | unknown
    :param str kind: operation | query
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the operation definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for operation definition (if applicable)
    :param str purpose: Why this operation definition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param bool affectsState: Whether content is changed by the operation
    :param str code: Recommended name for operation in search url
    :param str comment: Additional information about use
    :param str base: Marks this as a profile of the base
    :param str resource: Types this operation applies to
    :param bool system: Invoke at the system level?
    :param bool type: Invoke at the type level?
    :param bool instance: Invoke on an instance?
    :param str inputProfile: Validation information for in parameters
    :param str outputProfile: Validation information for out parameters
    :param BackboneElement parameter: Parameters for the operation/query
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name in Parameters.parameter.name or in URL
    :param str use: in | out
    :param str scope: instance | type | system
    :param int min: Minimum Cardinality
    :param str max: Maximum Cardinality (a number or *)
    :param str documentation: Description of meaning/use
    :param str type: What type this parameter has
    :param str allowedType: Allowed sub-type this parameter can have (if type is abstract)
    :param str targetProfile: If type is Reference | canonical, allowed targets. If type is 'Resource', then this constrains the allowed resource types
    :param str searchType: number | date | string | token | reference | composite | quantity | uri | special
    :param BackboneElement binding: ValueSet details if this is coded
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str strength: required | extensible | preferred | example
    :param str valueSet: Source of value set
    :param BackboneElement referencedFrom: References to this parameter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str source: Referencing parameter
    :param str sourceId: Element id of reference
    :param BackboneElement part: Parameters for the operation/query
    :param BackboneElement overload: Define overloaded variants for when  generating code
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str parameterName: Name of parameter to include in overload
    :param str comment: Comments to go on overload
    
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
    
    kind: str = None
    
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
    
    affectsState: bool = None
    
    code: str = None
    
    comment: str = None
    
    base: str = None
    
    resource: str = None
    
    system: bool = None
    
    type: bool = None
    
    instance: bool = None
    
    inputProfile: str = None
    
    outputProfile: str = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    use: str = None
    
    scope: str = None
    
    min: int = None
    
    max: str = None
    
    documentation: str = None
    
    type: str = None
    
    allowedType: str = None
    
    targetProfile: str = None
    
    searchType: str = None
    
    binding: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    strength: str = None
    
    valueSet: str = None
    
    referencedFrom: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    source: str = None
    
    sourceId: str = None
    
    part: "BackboneElement" = None
    
    overload: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    parameterName: str = None
    
    comment: str = None
    