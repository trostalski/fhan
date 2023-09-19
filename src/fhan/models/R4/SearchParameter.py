"""
Generated class for SearchParameter. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class SearchParameter(ModelBase):
    """ A search parameter that defines a named search item that can be used to search/filter on a resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this search parameter, represented as a URI (globally unique)
    :param str version: Business version of the search parameter
    :param str name: Name for this search parameter (computer friendly)
    :param str derivedFrom: Original definition for the search parameter
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the search parameter
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for search parameter (if applicable)
    :param str purpose: Why this search parameter is defined
    :param str code: Code used in URL
    :param str base: The resource type(s) this search parameter applies to
    :param str type: number | date | string | token | reference | composite | quantity | uri | special
    :param str expression: FHIRPath expression that extracts the values
    :param str xpath: XPath that extracts the values
    :param str xpathUsage: normal | phonetic | nearby | distance | other
    :param str target: Types of resource (if a resource reference)
    :param bool multipleOr: Allow multiple values per parameter (or)
    :param bool multipleAnd: Allow multiple parameters (and)
    :param str comparator: eq | ne | gt | lt | ge | le | sa | eb | ap
    :param str modifier: missing | exact | contains | not | text | in | not-in | below | above | type | identifier | ofType
    :param str chain: Chained names supported
    :param BackboneElement component: For Composite resources to define the parts
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str definition: Defines how the part works
    :param str expression: Subexpression relative to main expression
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
    
    version: str = None
    
    name: str = None
    
    derivedFrom: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    code: str = None
    
    base: str = None
    
    type: str = None
    
    expression: str = None
    
    xpath: str = None
    
    xpathUsage: str = None
    
    target: str = None
    
    multipleOr: bool = None
    
    multipleAnd: bool = None
    
    comparator: str = None
    
    modifier: str = None
    
    chain: str = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    definition: str = None
    
    expression: str = None
    