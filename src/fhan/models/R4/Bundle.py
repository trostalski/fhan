"""
Generated class for Bundle. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Link(Element):
    """ A series of links that provide context to this bundle.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relation: See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1
    :param str url: Reference details for the link
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    relation: str = None
    
    url: str = None
    

    
        
    
    
@dataclass
class Search(Element):
    """ Information about the search process that lead to the creation of this entry.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include | outcome - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    mode: str = None
    
    score: float = None
    

    
    
@dataclass
class Request(Element):
    """ Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache currency
    :param str ifModifiedSince: For managing cache currency
    :param str ifMatch: For managing update contention
    :param str ifNoneExist: For conditional creates
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    method: str = None
    
    url: str = None
    
    ifNoneMatch: str = None
    
    ifModifiedSince: str = None
    
    ifMatch: str = None
    
    ifNoneExist: str = None
    

    
    
@dataclass
class Response(Element):
    """ Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: Status response code (text optional)
    :param str location: The location (if the operation returns a location)
    :param str etag: The Etag for the resource (if relevant)
    :param str lastModified: Server's date time modified
    :param Resource outcome: OperationOutcome with hints and warnings (for batch/transaction)
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    status: str = None
    
    location: str = None
    
    etag: str = None
    
    lastModified: str = None
    outcome: "Resource" = None
    

  
    
    
@dataclass
class Entry(Element):
    """ An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str fullUrl: URI for resource (Absolute URL server address or URI for UUID/OID)
    :param Resource resource: A resource in the bundle
    :param Search search: Search related information
    :param Request request: Additional execution information (transaction/batch/history)
    :param Response response: Results of execution (transaction/batch/history)
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    fullUrl: str = None
    resource: "Resource" = None
    search: "Search" = None
    request: "Request" = None
    response: "Response" = None
    

@dataclass
class Bundle(ModelBase):
    """ A container for a collection of resources.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Identifier identifier: Persistent identifier for the bundle
    :param str type: document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection
    :param str timestamp: When the bundle was assembled
    :param int total: If search, the total number of matches
    :param Link link: Links related to this Bundle
    :param Entry entry: Entry in the bundle - will have a resource or information
    :param Signature signature: Digital Signature
    """

    resourceType: str = "Bundle"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    identifier: "Identifier" = None
    
    type: str = None
    
    timestamp: str = None
    
    total: int = None
    
    link: list["Link"] = None
    
    entry: list["Entry"] = None
    
    signature: "Signature" = None
    