"""
Generated class for MetadataResource. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class MetadataResource(ModelBase):
    """ Common Ancestor declaration for conformance and knowledge artifact resources.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this metadata resource, represented as a URI (globally unique)
    :param str version: Business version of the metadata resource
    :param str name: Name for this metadata resource (computer friendly)
    :param str title: Name for this metadata resource (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the metadata resource
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for metadata resource (if applicable)
    """
    def __init__(self, resourceType: str = "MetadataResource",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  version: str = None,  name: str = None,  title: str = None,  status: str = None,  experimental: bool = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None, ):
        self.resourceType: str = resourceType or "MetadataResource"
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
        self.title: str = title 
        self.status: str = status 
        self.experimental: bool = experimental 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        