"""
Generated class for Bundle. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Meta import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement link: Links related to this Bundle
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relation: See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1
    :param str url: Reference details for the link
    :param BackboneElement entry: Entry in the bundle - will have a resource or information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links related to this Bundle
    :param str fullUrl: URI for resource (Absolute URL server address or URI for UUID/OID)
    :param Resource resource: A resource in the bundle
    :param BackboneElement search: Search related information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include | outcome - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    :param BackboneElement request: Additional execution information (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache currency
    :param str ifModifiedSince: For managing cache currency
    :param str ifMatch: For managing update contention
    :param str ifNoneExist: For conditional creates
    :param BackboneElement response: Results of execution (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: Status response code (text optional)
    :param str location: The location (if the operation returns a location)
    :param str etag: The Etag for the resource (if relevant)
    :param str lastModified: Server's date time modified
    :param Resource outcome: OperationOutcome with hints and warnings (for batch/transaction)
    :param Signature signature: Digital Signature
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    identifier: "Identifier" = None
    
    type: str = None
    
    timestamp: str = None
    
    total: int = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relation: str = None
    
    url: str = None
    
    entry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    link: "BackboneElement" = None
    
    fullUrl: str = None
    
    resource: "Resource" = None
    
    search: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    score: float = None
    
    request: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    method: str = None
    
    url: str = None
    
    ifNoneMatch: str = None
    
    ifModifiedSince: str = None
    
    ifMatch: str = None
    
    ifNoneExist: str = None
    
    response: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    status: str = None
    
    location: str = None
    
    etag: str = None
    
    lastModified: str = None
    
    outcome: "Resource" = None
    
    signature: "Signature" = None
    