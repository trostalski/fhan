"""
Generated class for Bundle. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Signature import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Identifier import *


@dataclass
class Bundle:
    """ This profile holds all the requirements and constraints related to a FHIR history bundle.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Identifier identifier: Persistent identifier for the bundle
    :param str type: document | message | transaction | transaction-response | batch | batch-response | history | searchset | collection | subscription-notification
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
    :param str fullUrl: URI for resource (e.g. the absolute URL server address, URI for UUID/OID, etc.)
    :param Resource resource: A resource in the bundle
    :param BackboneElement search: Search related information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    :param BackboneElement request: Additional execution information (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache validation
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
    :param BackboneElement entry:put: Entry in the bundle - will have a resource or information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links related to this Bundle
    :param str fullUrl: URI for resource (e.g. the absolute URL server address, URI for UUID/OID, etc.)
    :param Resource resource: A resource in the bundle
    :param BackboneElement search: Search related information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    :param BackboneElement request: Additional execution information (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache validation
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
    :param BackboneElement entry:post: Entry in the bundle - will have a resource or information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links related to this Bundle
    :param str fullUrl: URI for resource (e.g. the absolute URL server address, URI for UUID/OID, etc.)
    :param Resource resource: A resource in the bundle
    :param BackboneElement search: Search related information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    :param BackboneElement request: Additional execution information (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache validation
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
    :param BackboneElement entry:get: Entry in the bundle - will have a resource or information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links related to this Bundle
    :param str fullUrl: URI for resource (e.g. the absolute URL server address, URI for UUID/OID, etc.)
    :param Resource resource: A resource in the bundle
    :param BackboneElement search: Search related information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    :param BackboneElement request: Additional execution information (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache validation
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
    :param BackboneElement entry:delete: Entry in the bundle - will have a resource or information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links related to this Bundle
    :param str fullUrl: URI for resource (e.g. the absolute URL server address, URI for UUID/OID, etc.)
    :param Resource resource: A resource in the bundle
    :param BackboneElement search: Search related information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    :param BackboneElement request: Additional execution information (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache validation
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
    :param BackboneElement entry:patch: Entry in the bundle - will have a resource or information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links related to this Bundle
    :param str fullUrl: URI for resource (e.g. the absolute URL server address, URI for UUID/OID, etc.)
    :param Resource resource: A resource in the bundle
    :param BackboneElement search: Search related information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    :param BackboneElement request: Additional execution information (transaction/batch/history)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache validation
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
    :param Resource issues: Issues with the Bundle
    
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
    
    entry:put: "BackboneElement" = None
    
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
    
    entry:post: "BackboneElement" = None
    
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
    
    entry:get: "BackboneElement" = None
    
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
    
    entry:delete: "BackboneElement" = None
    
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
    
    entry:patch: "BackboneElement" = None
    
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
    
    issues: "Resource" = None
    