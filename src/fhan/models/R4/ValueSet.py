"""
Generated class for ValueSet. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
        
    
        
    
        
    
    
@dataclass
class Designation(Element):
    """ Additional representations for this concept when used in this value set - other languages, aliases, specialized purposes, used for particular purposes, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str language: Human language of the designation
    :param Coding use: Types of uses of designations
    :param str value: The text value for this designation
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    language: str = None
    
    use:  "Coding" = Coding()
    
    value: str = None
    

  
    
    
@dataclass
class Concept(Element):
    """ Specifies a concept to be included or excluded.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code or expression from system
    :param str display: Text to display for this code for this value set in this valueset
    :param Designation designation: Additional representations for this concept
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    code: str = None
    
    display: str = None
    
    designation:  list["Designation"] = [Designation()]
    

    
    
@dataclass
class Filter(Element):
    """ Select concepts by specify a matching criterion based on the properties (including relationships) defined by the system, or on filters defined by the system. If multiple filters are specified, they SHALL all be true.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str property: A property/filter defined by the code system
    :param str op: = | is-a | descendent-of | is-not-a | regex | in | not-in | generalizes | exists
    :param str value: Code from the system, or regex criteria, or boolean value for exists
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    property: str = None
    
    op: str = None
    
    value: str = None
    

  
    
    
@dataclass
class Include(Element):
    """ Include one or more codes from a code system or other value set(s).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: The system the codes come from
    :param str version: Specific version of the code system referred to
    :param Concept concept: A concept defined in the system
    :param Filter filter: Select codes/concepts by their properties (including relationships)
    :param str valueSet: Select the contents included in this value set
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    system: str = None
    
    version: str = None
    
    concept:  list["Concept"] = [Concept()]
    
    filter:  list["Filter"] = [Filter()]
    
    valueSet: str = None
    

  
    
    
@dataclass
class Compose(Element):
    """ A set of criteria that define the contents of the value set by including or excluding codes selected from the specified code system(s) that the value set draws from. This is also known as the Content Logical Definition (CLD).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lockedDate: Fixed date for references with no specified version (transitive)
    :param bool inactive: Whether inactive codes are in the value set
    :param Include include: Include one or more codes from a code system or other value set(s)
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    lockedDate: str = None
    
    inactive: bool = None
    
    include:  list["Include"] = [Include()]
    

    
        
    
    
@dataclass
class Parameter(Element):
    """ A parameter that controlled the expansion process. These parameters may be used by users of expanded value sets to check whether the expansion is suitable for a particular purpose, or to pick the correct expansion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name as assigned by the client or server
    :param str valueString: Value of the named parameter
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    name: str = None
    
    valueString: str = None
    

    
    
@dataclass
class Contains(Element):
    """ The codes that are contained in the value set expansion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str system: System value for the code
    :param bool abstract: If user cannot select this entry
    :param bool inactive: If concept is inactive in the code system
    :param str version: Version in which this code/display is defined
    :param str code: Code - if blank, this is not a selectable code
    :param str display: User display for the concept
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    system: str = None
    
    abstract: bool = None
    
    inactive: bool = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    

  
    
    
@dataclass
class Expansion(Element):
    """ A value set can also be "expanded", where the value set is turned into a simple collection of enumerated codes. This element holds the expansion, if it has been performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str identifier: Identifies the value set expansion (business identifier)
    :param str timestamp: Time ValueSet expansion happened
    :param int total: Total number of codes in the expansion
    :param int offset: Offset at which this resource starts
    :param Parameter parameter: Parameter that controlled the expansion process
    :param Contains contains: Codes in the value set
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    identifier: str = None
    
    timestamp: str = None
    
    total: int = None
    
    offset: int = None
    
    parameter:  list["Parameter"] = [Parameter()]
    
    contains:  list["Contains"] = [Contains()]
    

@dataclass
class ValueSet(ModelBase):
    """ A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this value set, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the value set (business identifier)
    :param str version: Business version of the value set
    :param str name: Name for this value set (computer friendly)
    :param str title: Name for this value set (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the value set
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for value set (if applicable)
    :param bool immutable: Indicates whether or not any change to the content logical definition may occur
    :param str purpose: Why this value set is defined
    :param str copyright: Use and/or publishing restrictions
    :param Compose compose: Content logical definition of the value set (CLD)
    :param Expansion expansion: Used when the value set is "expanded"
    """

    resourceType: str = "ValueSet"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    identifier: list["Identifier"] = None
    
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
    
    immutable: bool = None
    
    purpose: str = None
    
    copyright: str = None
    
    compose: "Compose" = None
    
    expansion: "Expansion" = None
    