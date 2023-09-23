"""
Generated class for DocumentManifest. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Related(Element):
    """ Related identifiers or resources associated with the DocumentManifest.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifiers of things that are related
    :param Reference ref: Related Resource
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    identifier: "Identifier" = Identifier()
    ref: "Reference" = Reference()
    

@dataclass
class DocumentManifest(ModelBase):
    """ A collection of documents compiled for a purpose together with metadata that applies to the collection.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier masterIdentifier: Unique Identifier for the set of documents
    :param Identifier identifier: Other identifiers for the manifest
    :param str status: current | superseded | entered-in-error
    :param CodeableConcept type: Kind of document set
    :param Reference subject: The subject of the set of documents
    :param str created: When this document manifest created
    :param Reference author: Who and/or what authored the DocumentManifest
    :param Reference recipient: Intended to get notified about this set of documents
    :param str source: The source system/application/software
    :param str description: Human-readable description (title)
    :param Reference content: Items in manifest
    :param Related related: Related things
    """

    resourceType: str = "DocumentManifest"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    masterIdentifier: "Identifier" = Identifier()
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    type: "CodeableConcept" = CodeableConcept()
    
    subject: "Reference" = Reference()
    
    created: str = None
    
    author: list[Reference] = Reference() 
    
    recipient: list[Reference] = Reference() 
    
    source: str = None
    
    description: str = None
    
    content: list[Reference] = Reference() 
    
    related: list[Related] = Related() 
    