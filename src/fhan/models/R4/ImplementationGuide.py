"""
Generated class for ImplementationGuide. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class DependsOn(Element):
    """ Another implementation guide that this implementation depends on. Typically, an implementation guide uses value sets, profiles etc.defined in other implementation guides.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str uri: Identity of the IG that this depends on
    :param str packageId: NPM Package name for IG this depends on
    :param str version: Version of the IG
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    uri: str = None
    
    packageId: str = None
    
    version: str = None
    

    
    
@dataclass
class _global(Element):
    """ A set of profiles that all resources covered by this implementation guide must conform to.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: Type this profile applies to
    :param str profile: Profile that all resources must conform to
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    type: str = None
    
    profile: str = None
    

    
        
    
    
@dataclass
class Grouping(Element):
    """ A logical group of resources. Logical groups can be used when building pages.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Descriptive name for the package
    :param str description: Human readable text describing the package
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    
    description: str = None
    

    
    
@dataclass
class Resource(Element):
    """ A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Location of the resource
    :param str fhirVersion: Versions this applies to (if different to IG)
    :param str name: Human Name for the resource
    :param str description: Reason why included in guide
    :param bool exampleBoolean: Is an example/What is this an example of?
    :param str groupingId: Grouping this is part of
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    reference: "Reference" = None
    
    fhirVersion: str = None
    
    name: str = None
    
    description: str = None
    
    exampleBoolean: bool = None
    
    groupingId: str = None
    

    
    
@dataclass
class Page(Element):
    """ A page / section in the implementation guide. The root page is the implementation guide home page.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str nameUrl: Where to find that page
    :param str title: Short title shown for navigational assistance
    :param str generation: html | markdown | xml | generated
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    nameUrl: str = None
    
    title: str = None
    
    generation: str = None
    

    
    
@dataclass
class Parameter(Element):
    """ Defines how IG is built by tools.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: apply | path-resource | path-pages | path-tx-cache | expansion-parameter | rule-broken-links | generate-xml | generate-json | generate-turtle | html-template
    :param str value: Value for named type
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    code: str = None
    
    value: str = None
    

    
    
@dataclass
class Template(Element):
    """ A template for building resources.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Type of template specified
    :param str source: The source location for the template
    :param str scope: The scope in which the template applies
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    code: str = None
    
    source: str = None
    
    scope: str = None
    

  
    
    
@dataclass
class Definition(Element):
    """ The information needed by an IG publisher tool to publish the whole implementation guide.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Grouping grouping: Grouping used to present related resources in the IG
    :param Resource resource: Resource in the implementation guide
    :param Page page: Page/Section in the Guide
    :param Parameter parameter: Defines how IG is built by tools
    :param Template template: A template for building resources
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    grouping: list[Grouping] = None
    resource: list[Resource] = None
    page: "Page" = None
    parameter: list[Parameter] = None
    template: list[Template] = None
    

    
        
    
    
@dataclass
class Resource(Element):
    """ A resource that is part of the implementation guide. Conformance resources (value set, structure definition, capability statements etc.) are obvious candidates for inclusion, but any kind of resource can be included as an example resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Location of the resource
    :param bool exampleBoolean: Is an example/What is this an example of?
    :param str relativePath: Relative path for page in IG
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    reference: "Reference" = None
    
    exampleBoolean: bool = None
    
    relativePath: str = None
    

    
    
@dataclass
class Page(Element):
    """ Information about a page within the IG.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: HTML page name
    :param str title: Title of the page, for references
    :param str anchor: Anchor available on the page
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    
    title: str = None
    
    anchor: str = None
    

  
    
    
@dataclass
class Manifest(Element):
    """ Information about an assembled implementation guide, created by the publication tooling.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str rendering: Location of rendered implementation guide
    :param Resource resource: Resource in the implementation guide
    :param Page page: HTML page within the parent IG
    :param str image: Image within the IG
    :param str other: Additional linkable file in IG
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    rendering: str = None
    resource: list[Resource] = None
    page: list[Page] = None
    
    image: str = None
    
    other: str = None
    

@dataclass
class ImplementationGuide(ModelBase):
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
    :param str version: Business version of the implementation guide
    :param str name: Name for this implementation guide (computer friendly)
    :param str title: Name for this implementation guide (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the implementation guide
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for implementation guide (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str packageId: NPM Package name for IG
    :param str license: SPDX license code for this IG (or not-open-source)
    :param str fhirVersion: FHIR Version(s) this Implementation Guide targets
    :param DependsOn dependsOn: Another Implementation guide this depends on
    :param _global _global: Profiles that apply globally
    :param Definition definition: Information needed to build the IG
    :param Manifest manifest: Information about an assembled IG
    """

    resourceType: str = "ImplementationGuide"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    copyright: str = None
    
    packageId: str = None
    
    license: str = None
    
    fhirVersion: str = None
    
    dependsOn: list["DependsOn"] = None
    
    _global: list["_global"] = None
    
    definition: "Definition" = None
    
    manifest: "Manifest" = None
    