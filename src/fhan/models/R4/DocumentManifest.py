"""
Generated class for DocumentManifest. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Related(ModelBase):
    """ Related identifiers or resources associated with the DocumentManifest.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Identifiers of things that are related
    :param 'Reference' ref: Related Resource
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  ref: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.ref: 'Reference' = ref 
        

class DocumentManifest(DomainResource):
    """ A collection of documents compiled for a purpose together with metadata that applies to the collection.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' masterIdentifier: Unique Identifier for the set of documents
    :param list['Identifier'] identifier: Other identifiers for the manifest
    :param str status: current | superseded | entered-in-error
    :param 'CodeableConcept' type: Kind of document set
    :param 'Reference' subject: The subject of the set of documents
    :param str created: When this document manifest created
    :param list['Reference'] author: Who and/or what authored the DocumentManifest
    :param list['Reference'] recipient: Intended to get notified about this set of documents
    :param str source: The source system/application/software
    :param str description: Human-readable description (title)
    :param list['Reference'] content: Items in manifest
    :param list['Related'] related: Related things
    """
    def __init__(self, resourceType: str = "DocumentManifest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  masterIdentifier: 'Identifier' = None,  identifier: list['Identifier'] = None,  status: str = None,  type: 'CodeableConcept' = None,  subject: 'Reference' = None,  created: str = None,  author: list['Reference'] = None,  recipient: list['Reference'] = None,  source: str = None,  description: str = None,  content: list['Reference'] = None,  related: list['Related'] = None, ):
        self.resourceType: str = resourceType or "DocumentManifest"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.masterIdentifier: 'Identifier' = masterIdentifier 
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.type: 'CodeableConcept' = type 
        self.subject: 'Reference' = subject 
        self.created: str = created 
        self.author: list['Reference'] = author or []
        self.recipient: list['Reference'] = recipient or []
        self.source: str = source 
        self.description: str = description 
        self.content: list['Reference'] = content or []
        self.related: list['Related'] = related or []
        