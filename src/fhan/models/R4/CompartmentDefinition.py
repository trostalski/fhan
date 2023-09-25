"""
Generated class for CompartmentDefinition. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.DomainResource import *


    
    

class Resource(ModelBase):
    """ Information about how a resource is related to the compartment.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Name of resource type
    :param str param: Search Parameter Name, or chained parameters
    :param str documentation: Additional documentation about the resource and compartment
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: str = None,  param: str = None,  documentation: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: str = code 
        self.param: str = param or []
        self.documentation: str = documentation 
        

class CompartmentDefinition(DomainResource):
    """ A compartment definition that defines how resources are accessed on a server.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this compartment definition, represented as a URI (globally unique)
    :param str version: Business version of the compartment definition
    :param str name: Name for this compartment definition (computer friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the compartment definition
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param str purpose: Why this compartment definition is defined
    :param str code: Patient | Encounter | RelatedPerson | Practitioner | Device
    :param bool search: Whether the search syntax is supported
    :param list['Resource'] resource: How a resource is related to the compartment
    """
    def __init__(self, resourceType: str = "CompartmentDefinition",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  version: str = None,  name: str = None,  status: str = None,  experimental: bool = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  purpose: str = None,  code: str = None,  search: bool = None,  resource: list['Resource'] = None, ):
        self.resourceType: str = resourceType or "CompartmentDefinition"
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
        self.status: str = status 
        self.experimental: bool = experimental 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.purpose: str = purpose 
        self.code: str = code 
        self.search: bool = search 
        self.resource: list['Resource'] = resource or []
        