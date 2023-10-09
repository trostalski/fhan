"""
Generated class for Bundle. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Resource import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Signature import *
from fhan.models.R4.DomainResource import *


class Link(BaseModel):
    """A series of links that provide context to this bundle.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relation: See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1
    :param str url: Reference details for the link
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        relation: "str" = None,
        url: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relation = relation
        self.url = url

    @classmethod
    def from_dict(cls, data: dict) -> "Bundle":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Bundle":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Search(BaseModel):
    """Information about the search process that lead to the creation of this entry.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: match | include | outcome - why this is in the result set
    :param float score: Search ranking (between 0 and 1)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        mode: "str" = None,
        score: "float" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode
        self.score = score

    @classmethod
    def from_dict(cls, data: dict) -> "Bundle":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Bundle":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Request(BaseModel):
    """Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str method: GET | HEAD | POST | PUT | DELETE | PATCH
    :param str url: URL for HTTP equivalent of this entry
    :param str ifNoneMatch: For managing cache currency
    :param str ifModifiedSince: For managing cache currency
    :param str ifMatch: For managing update contention
    :param str ifNoneExist: For conditional creates
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        method: "str" = None,
        url: "str" = None,
        ifNoneMatch: "str" = None,
        ifModifiedSince: "str" = None,
        ifMatch: "str" = None,
        ifNoneExist: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.method = method
        self.url = url
        self.ifNoneMatch = ifNoneMatch
        self.ifModifiedSince = ifModifiedSince
        self.ifMatch = ifMatch
        self.ifNoneExist = ifNoneExist

    @classmethod
    def from_dict(cls, data: dict) -> "Bundle":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Bundle":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Response(BaseModel):
    """Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str status: Status response code (text optional)
    :param str location: The location (if the operation returns a location)
    :param str etag: The Etag for the resource (if relevant)
    :param str lastModified: Server's date time modified
    :param Resource outcome: OperationOutcome with hints and warnings (for batch/transaction)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "outcome": {"class_name": "Resource", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        status: "str" = None,
        location: "str" = None,
        etag: "str" = None,
        lastModified: "str" = None,
        outcome: "Resource" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.status = status
        self.location = location
        self.etag = etag
        self.lastModified = lastModified
        self.outcome = outcome

    @classmethod
    def from_dict(cls, data: dict) -> "Bundle":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Bundle":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Entry(BaseModel):
    """An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Link link: Links related to this entry
    :param str fullUrl: URI for resource (Absolute URL server address or URI for UUID/OID)
    :param Resource resource: A resource in the bundle
    :param Search search: Search related information
    :param Request request: Additional execution information (transaction/batch/history)
    :param Response response: Results of execution (transaction/batch/history)
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "link": {"class_name": "Link", "is_contained": True},
        "resource": {"class_name": "Resource", "is_contained": False},
        "search": {"class_name": "Search", "is_contained": True},
        "request": {"class_name": "Request", "is_contained": True},
        "response": {"class_name": "Response", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        link: list["Link"] = None,
        fullUrl: "str" = None,
        resource: "Resource" = None,
        search: "Search" = None,
        request: "Request" = None,
        response: "Response" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.link = link or []
        self.fullUrl = fullUrl
        self.resource = resource
        self.search = search
        self.request = request
        self.response = response

    @classmethod
    def from_dict(cls, data: dict) -> "Bundle":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Bundle":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Bundle(DomainResource):
    """A container for a collection of resources.
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

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "link": {"class_name": "Link", "is_contained": True},
        "entry": {"class_name": "Entry", "is_contained": True},
        "signature": {"class_name": "Signature", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        identifier: "Identifier" = None,
        type: "str" = None,
        timestamp: "str" = None,
        total: "int" = None,
        link: list["Link"] = None,
        entry: list["Entry"] = None,
        signature: "Signature" = None,
    ):
        self.resourceType = resourceType or "Bundle"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.identifier = identifier
        self.type = type
        self.timestamp = timestamp
        self.total = total
        self.link = link or []
        self.entry = entry or []
        self.signature = signature

    @classmethod
    def from_dict(cls, data: dict) -> "Bundle":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "Bundle":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
