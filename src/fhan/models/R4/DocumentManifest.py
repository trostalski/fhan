"""
Generated class for DocumentManifest. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement related: Related things
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifiers of things that are related
    :param Reference ref: Related Resource
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    masterIdentifier: "Identifier" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    created: str = None
    
    author: "Reference" = None
    
    recipient: "Reference" = None
    
    source: str = None
    
    description: str = None
    
    content: "Reference" = None
    
    related: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    ref: "Reference" = None
    