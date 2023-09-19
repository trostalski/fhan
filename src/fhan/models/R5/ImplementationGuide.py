"""
Generated class for ImplementationGuide. 
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
from fhan.models.R5.Reference import *


@dataclass
class ImplementationGuide:
    """ A set of rules of how a particular interoperability or standards problem is solved - typically through the use of FHIR resources. This resource is used to gather all the parts of an implementation guide into a logical whole and to publish a computable definition of all the parts.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this implementation guide, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the implementation guide (business identifier)
    :param str version: Business version of the implementation guide
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this implementation guide (computer friendly)
    :param str title: Name for this implementation guide (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the implementation guide
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for implementation guide (if applicable)
    :param str purpose: Why this implementation guide is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str packageId: NPM Package name for IG
    :param str license: SPDX license code for this IG (or not-open-source)
    :param str fhirVersion: FHIR Version(s) this Implementation Guide targets
    :param BackboneElement dependsOn: Another Implementation guide this depends on
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uri: Identity of the IG that this depends on
    :param str packageId: NPM Package name for IG this depends on
    :param str version: Version of the IG
    :param str reason: Why dependency exists
    :param BackboneElement global: Profiles that apply globally
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Type this profile applies to
    :param str profile: Profile that all resources must conform to
    :param BackboneElement definition: Information needed to build the IG
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement grouping: Grouping used to present related resources in the IG
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Descriptive name for the package
    :param str description: Human readable text describing the package
    :param BackboneElement resource: Resource in the implementation guide
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Location of the resource
    :param str fhirVersion: Versions this applies to (if different to IG)
    :param str name: Human readable name for the resource
    :param str description: Reason why included in guide
    :param bool isExample: Is this an example
    :param str profile: Profile(s) this is an example of
    :param str groupingId: Grouping this is part of
    :param BackboneElement page: Page/Section in the Guide
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str sourceurl: Source for page
    :param str sourceurl: Source for page
    :param str sourceurl: Source for page
    :param str name: Name of the page when published
    :param str title: Short title shown for navigational assistance
    :param str generation: html | markdown | xml | generated
    :param BackboneElement page: Page/Section in the Guide
    :param BackboneElement parameter: Defines how IG is built by tools
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding code: Code that identifies parameter
    :param str value: Value for named type
    :param BackboneElement template: A template for building resources
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Type of template specified
    :param str source: The source location for the template
    :param str scope: The scope in which the template applies
    :param BackboneElement manifest: Information about an assembled IG
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str rendering: Location of rendered implementation guide
    :param BackboneElement resource: Resource in the implementation guide
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Location of the resource
    :param bool isExample: Is this an example
    :param str profile: Profile(s) this is an example of
    :param str relativePath: Relative path for page in IG
    :param BackboneElement page: HTML page within the parent IG
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: HTML page name
    :param str title: Title of the page, for references
    :param str anchor: Anchor available on the page
    :param str image: Image within the IG
    :param str other: Additional linkable file in IG
    
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
    
    packageId: str = None
    
    license: str = None
    
    fhirVersion: str = None
    
    dependsOn: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    uri: str = None
    
    packageId: str = None
    
    version: str = None
    
    reason: str = None
    
    global: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    profile: str = None
    
    definition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    grouping: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    description: str = None
    
    resource: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: "Reference" = None
    
    fhirVersion: str = None
    
    name: str = None
    
    description: str = None
    
    isExample: bool = None
    
    profile: str = None
    
    groupingId: str = None
    
    page: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sourceurl: str = None
    
    sourceurl: str = None
    
    sourceurl: str = None
    
    name: str = None
    
    title: str = None
    
    generation: str = None
    
    page: "BackboneElement" = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "Coding" = None
    
    value: str = None
    
    template: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    source: str = None
    
    scope: str = None
    
    manifest: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    rendering: str = None
    
    resource: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: "Reference" = None
    
    isExample: bool = None
    
    profile: str = None
    
    relativePath: str = None
    
    page: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    title: str = None
    
    anchor: str = None
    
    image: str = None
    
    other: str = None
    