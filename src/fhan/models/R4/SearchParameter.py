"""
Generated class for SearchParameter. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.DomainResource import *


    
    

class Component(ModelBase):
    """ Used to define the parts of a composite search parameter.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str definition: Defines how the part works
    :param str expression: Subexpression relative to main expression
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  definition: str = None,  expression: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.definition: str = definition 
        self.expression: str = expression 
        

class SearchParameter(DomainResource):
    """ A search parameter that defines a named search item that can be used to search/filter on a resource.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this search parameter, represented as a URI (globally unique)
    :param str version: Business version of the search parameter
    :param str name: Name for this search parameter (computer friendly)
    :param str derivedFrom: Original definition for the search parameter
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the search parameter
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for search parameter (if applicable)
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
    :param list['Component'] component: For Composite resources to define the parts
    """
    def __init__(self, resourceType: str = "SearchParameter",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  version: str = None,  name: str = None,  derivedFrom: str = None,  status: str = None,  experimental: bool = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  code: str = None,  base: str = None,  type: str = None,  expression: str = None,  xpath: str = None,  xpathUsage: str = None,  target: str = None,  multipleOr: bool = None,  multipleAnd: bool = None,  comparator: str = None,  modifier: str = None,  chain: str = None,  component: list['Component'] = None, ):
        self.resourceType: str = resourceType or "SearchParameter"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.version: str = version 
        self.name: str = name 
        self.derivedFrom: str = derivedFrom 
        self.status: str = status 
        self.experimental: bool = experimental 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.purpose: str = purpose 
        self.code: str = code 
        self.base: str = base or []
        self.type: str = type 
        self.expression: str = expression 
        self.xpath: str = xpath 
        self.xpathUsage: str = xpathUsage 
        self.target: str = target or []
        self.multipleOr: bool = multipleOr 
        self.multipleAnd: bool = multipleAnd 
        self.comparator: str = comparator or []
        self.modifier: str = modifier or []
        self.chain: str = chain or []
        self.component: list['Component'] = component or []
        