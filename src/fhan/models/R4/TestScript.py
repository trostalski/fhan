"""
Generated class for TestScript. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.generator_models import ModelBase

@dataclass
class origin(Element):
    """ An abstract server used in operations within this test script in the origin element.
    :param BackboneElement origin: An abstract server representing a client or sender in a message exchange
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract origin server starting at 1
    :param Coding profile: FHIR-Client | FHIR-SDC-FormFiller
    """
    origin: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    index: int = None
    
    profile: "Coding" = None
    
@dataclass
class destination(Element):
    """ An abstract server used in operations within this test script in the destination element.
    :param BackboneElement destination: An abstract server representing a destination or receiver in a message exchange
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract destination server starting at 1
    :param Coding profile: FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-SDC-FormProcessor
    """
    destination: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    index: int = None
    
    profile: "Coding" = None
    
@dataclass
class metadata(Element):
    """ The required capability must exist and are assumed to function correctly on the FHIR server being tested.
    :param BackboneElement metadata: Required capability that is assumed to function correctly on the FHIR server being tested
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links to the FHIR specification
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: URL to the specification
    :param str description: Short description
    :param BackboneElement capability: Capabilities  that are assumed to function correctly on the FHIR server being tested
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool required: Are the capabilities required?
    :param bool validated: Are the capabilities validated?
    :param str description: The expected capabilities of the server
    :param int origin: Which origin server these requirements apply to
    :param int destination: Which server these requirements apply to
    :param str link: Links to the FHIR specification
    :param str capabilities: Required Capability Statement
    """
    metadata: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    link: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    description: str = None
    
    capability: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    required: bool = None
    
    validated: bool = None
    
    description: str = None
    
    origin: int = None
    
    destination: int = None
    
    link: str = None
    
    capabilities: str = None
    
@dataclass
class link(Element):
    """ A link to the FHIR specification that this test is covering.
    :param BackboneElement link: Links to the FHIR specification
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: URL to the specification
    :param str description: Short description
    """
    link: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    description: str = None
    
@dataclass
class capability(Element):
    """ Capabilities that must exist and are assumed to function correctly on the FHIR server being tested.
    :param BackboneElement capability: Capabilities  that are assumed to function correctly on the FHIR server being tested
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool required: Are the capabilities required?
    :param bool validated: Are the capabilities validated?
    :param str description: The expected capabilities of the server
    :param int origin: Which origin server these requirements apply to
    :param int destination: Which server these requirements apply to
    :param str link: Links to the FHIR specification
    :param str capabilities: Required Capability Statement
    """
    capability: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    required: bool = None
    
    validated: bool = None
    
    description: str = None
    
    origin: int = None
    
    destination: int = None
    
    link: str = None
    
    capabilities: str = None
    
@dataclass
class fixture(Element):
    """ Fixture in the test script - by reference (uri). All fixtures are required for the test script to execute.
    :param BackboneElement fixture: Fixture in the test script - by reference (uri)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool autocreate: Whether or not to implicitly create the fixture during setup
    :param bool autodelete: Whether or not to implicitly delete the fixture during teardown
    :param Reference resource: Reference of the resource
    """
    fixture: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    autocreate: bool = None
    
    autodelete: bool = None
    
    resource: "Reference" = None
    
@dataclass
class variable(Element):
    """ Variable is set based either on element value in response body or on header field value in the response headers.
    :param BackboneElement variable: Placeholder for evaluated elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Descriptive name for this variable
    :param str defaultValue: Default, hard-coded, or user-defined value for this variable
    :param str description: Natural language description of the variable
    :param str expression: The FHIRPath expression against the fixture body
    :param str headerField: HTTP header field name for source
    :param str hint: Hint help text for default value to enter
    :param str path: XPath or JSONPath against the fixture body
    :param str sourceId: Fixture Id of source expression or headerField within this variable
    """
    variable: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    defaultValue: str = None
    
    description: str = None
    
    expression: str = None
    
    headerField: str = None
    
    hint: str = None
    
    path: str = None
    
    sourceId: str = None
    
@dataclass
class setup(Element):
    """ A series of required setup operations before tests are executed.
    :param BackboneElement setup: A series of required setup operations before tests are executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: A setup operation or assert to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The setup operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The operation code type that will be executed
    :param str resource: Resource type
    :param str label: Tracking/logging operation label
    :param str description: Tracking/reporting operation description
    :param str accept: Mime type to accept in the payload of the response, with charset etc.
    :param str contentType: Mime type of the request payload contents, with charset etc.
    :param int destination: Server responding to the request
    :param bool encodeRequestUrl: Whether or not to send the request url in encoded format
    :param str method: delete | get | options | patch | post | put | head
    :param int origin: Server initiating the request
    :param str params: Explicitly defined path parameters
    :param BackboneElement requestHeader: Each operation can have one or more header elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str label: Tracking/logging assertion label
    :param str description: Tracking/reporting assertion description
    :param str direction: response | request
    :param str compareToSourceId: Id of the source fixture to be evaluated
    :param str compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture
    :param str compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture
    :param str contentType: Mime type to compare against the 'Content-Type' header
    :param str expression: The FHIRPath expression to be evaluated
    :param str headerField: HTTP header field name
    :param str minimumId: Fixture Id of minimum content resource
    :param bool navigationLinks: Perform validation on navigation links?
    :param str operator: equals | notEquals | in | notIn | greaterThan | lessThan | empty | notEmpty | contains | notContains | eval
    :param str path: XPath or JSONPath expression
    :param str requestMethod: delete | get | options | patch | post | put | head
    :param str requestURL: Request URL comparison value
    :param str resource: Resource type
    :param str response: okay | created | noContent | notModified | bad | forbidden | notFound | methodNotAllowed | conflict | gone | preconditionFailed | unprocessable
    :param str responseCode: HTTP response code to test
    :param str sourceId: Fixture Id of source expression or headerField
    :param str validateProfileId: Profile Id of validation profile reference
    :param str value: The value to compare to
    :param bool warningOnly: Will this assert produce a warning only on error?
    :param BackboneElement operation: The setup operation to perform
    :param BackboneElement _assert: The assertion to perform
    :param BackboneElement operation: The setup operation to perform
    """
    setup: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "Coding" = None
    
    resource: str = None
    
    label: str = None
    
    description: str = None
    
    accept: str = None
    
    contentType: str = None
    
    destination: int = None
    
    encodeRequestUrl: bool = None
    
    method: str = None
    
    origin: int = None
    
    params: str = None
    
    requestHeader: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    field: str = None
    
    value: str = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    label: str = None
    
    description: str = None
    
    direction: str = None
    
    compareToSourceId: str = None
    
    compareToSourceExpression: str = None
    
    compareToSourcePath: str = None
    
    contentType: str = None
    
    expression: str = None
    
    headerField: str = None
    
    minimumId: str = None
    
    navigationLinks: bool = None
    
    operator: str = None
    
    path: str = None
    
    requestMethod: str = None
    
    requestURL: str = None
    
    resource: str = None
    
    response: str = None
    
    responseCode: str = None
    
    sourceId: str = None
    
    validateProfileId: str = None
    
    value: str = None
    
    warningOnly: bool = None
    
    operation: "BackboneElement" = None
    
    _assert: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class action(Element):
    """ Action would contain either an operation or an assertion.
    :param BackboneElement action: A setup operation or assert to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The setup operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The operation code type that will be executed
    :param str resource: Resource type
    :param str label: Tracking/logging operation label
    :param str description: Tracking/reporting operation description
    :param str accept: Mime type to accept in the payload of the response, with charset etc.
    :param str contentType: Mime type of the request payload contents, with charset etc.
    :param int destination: Server responding to the request
    :param bool encodeRequestUrl: Whether or not to send the request url in encoded format
    :param str method: delete | get | options | patch | post | put | head
    :param int origin: Server initiating the request
    :param str params: Explicitly defined path parameters
    :param BackboneElement requestHeader: Each operation can have one or more header elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str label: Tracking/logging assertion label
    :param str description: Tracking/reporting assertion description
    :param str direction: response | request
    :param str compareToSourceId: Id of the source fixture to be evaluated
    :param str compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture
    :param str compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture
    :param str contentType: Mime type to compare against the 'Content-Type' header
    :param str expression: The FHIRPath expression to be evaluated
    :param str headerField: HTTP header field name
    :param str minimumId: Fixture Id of minimum content resource
    :param bool navigationLinks: Perform validation on navigation links?
    :param str operator: equals | notEquals | in | notIn | greaterThan | lessThan | empty | notEmpty | contains | notContains | eval
    :param str path: XPath or JSONPath expression
    :param str requestMethod: delete | get | options | patch | post | put | head
    :param str requestURL: Request URL comparison value
    :param str resource: Resource type
    :param str response: okay | created | noContent | notModified | bad | forbidden | notFound | methodNotAllowed | conflict | gone | preconditionFailed | unprocessable
    :param str responseCode: HTTP response code to test
    :param str sourceId: Fixture Id of source expression or headerField
    :param str validateProfileId: Profile Id of validation profile reference
    :param str value: The value to compare to
    :param bool warningOnly: Will this assert produce a warning only on error?
    :param BackboneElement operation: The setup operation to perform
    :param BackboneElement _assert: The assertion to perform
    :param BackboneElement operation: The setup operation to perform
    """
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "Coding" = None
    
    resource: str = None
    
    label: str = None
    
    description: str = None
    
    accept: str = None
    
    contentType: str = None
    
    destination: int = None
    
    encodeRequestUrl: bool = None
    
    method: str = None
    
    origin: int = None
    
    params: str = None
    
    requestHeader: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    field: str = None
    
    value: str = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    label: str = None
    
    description: str = None
    
    direction: str = None
    
    compareToSourceId: str = None
    
    compareToSourceExpression: str = None
    
    compareToSourcePath: str = None
    
    contentType: str = None
    
    expression: str = None
    
    headerField: str = None
    
    minimumId: str = None
    
    navigationLinks: bool = None
    
    operator: str = None
    
    path: str = None
    
    requestMethod: str = None
    
    requestURL: str = None
    
    resource: str = None
    
    response: str = None
    
    responseCode: str = None
    
    sourceId: str = None
    
    validateProfileId: str = None
    
    value: str = None
    
    warningOnly: bool = None
    
    operation: "BackboneElement" = None
    
    _assert: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class operation(Element):
    """ The operation to perform.
    :param BackboneElement operation: The setup operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The operation code type that will be executed
    :param str resource: Resource type
    :param str label: Tracking/logging operation label
    :param str description: Tracking/reporting operation description
    :param str accept: Mime type to accept in the payload of the response, with charset etc.
    :param str contentType: Mime type of the request payload contents, with charset etc.
    :param int destination: Server responding to the request
    :param bool encodeRequestUrl: Whether or not to send the request url in encoded format
    :param str method: delete | get | options | patch | post | put | head
    :param int origin: Server initiating the request
    :param str params: Explicitly defined path parameters
    :param BackboneElement requestHeader: Each operation can have one or more header elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    :param BackboneElement operation: The setup operation to perform
    :param BackboneElement operation: The setup operation to perform
    """
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "Coding" = None
    
    resource: str = None
    
    label: str = None
    
    description: str = None
    
    accept: str = None
    
    contentType: str = None
    
    destination: int = None
    
    encodeRequestUrl: bool = None
    
    method: str = None
    
    origin: int = None
    
    params: str = None
    
    requestHeader: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    field: str = None
    
    value: str = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    
    operation: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class requestHeader(Element):
    """ Header elements would be used to set HTTP headers.
    :param BackboneElement requestHeader: Each operation can have one or more header elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    """
    requestHeader: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    field: str = None
    
    value: str = None
    
@dataclass
class _assert(Element):
    """ Evaluates the results of previous operations to determine if the server under test behaves appropriately.
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str label: Tracking/logging assertion label
    :param str description: Tracking/reporting assertion description
    :param str direction: response | request
    :param str compareToSourceId: Id of the source fixture to be evaluated
    :param str compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture
    :param str compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture
    :param str contentType: Mime type to compare against the 'Content-Type' header
    :param str expression: The FHIRPath expression to be evaluated
    :param str headerField: HTTP header field name
    :param str minimumId: Fixture Id of minimum content resource
    :param bool navigationLinks: Perform validation on navigation links?
    :param str operator: equals | notEquals | in | notIn | greaterThan | lessThan | empty | notEmpty | contains | notContains | eval
    :param str path: XPath or JSONPath expression
    :param str requestMethod: delete | get | options | patch | post | put | head
    :param str requestURL: Request URL comparison value
    :param str resource: Resource type
    :param str response: okay | created | noContent | notModified | bad | forbidden | notFound | methodNotAllowed | conflict | gone | preconditionFailed | unprocessable
    :param str responseCode: HTTP response code to test
    :param str sourceId: Fixture Id of source expression or headerField
    :param str validateProfileId: Profile Id of validation profile reference
    :param str value: The value to compare to
    :param bool warningOnly: Will this assert produce a warning only on error?
    :param BackboneElement _assert: The assertion to perform
    """
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    label: str = None
    
    description: str = None
    
    direction: str = None
    
    compareToSourceId: str = None
    
    compareToSourceExpression: str = None
    
    compareToSourcePath: str = None
    
    contentType: str = None
    
    expression: str = None
    
    headerField: str = None
    
    minimumId: str = None
    
    navigationLinks: bool = None
    
    operator: str = None
    
    path: str = None
    
    requestMethod: str = None
    
    requestURL: str = None
    
    resource: str = None
    
    response: str = None
    
    responseCode: str = None
    
    sourceId: str = None
    
    validateProfileId: str = None
    
    value: str = None
    
    warningOnly: bool = None
    
    _assert: "BackboneElement" = None
    
@dataclass
class test(Element):
    """ A test in this script.
    :param BackboneElement test: A test in this script
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param BackboneElement action: A test operation or assert to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    test: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    description: str = None
    
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
@dataclass
class action(Element):
    """ Action would contain either an operation or an assertion.
    :param BackboneElement action: A test operation or assert to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
@dataclass
class operation(Element):
    """ The operation to perform.
    :param BackboneElement operation: The setup operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The operation code type that will be executed
    :param str resource: Resource type
    :param str label: Tracking/logging operation label
    :param str description: Tracking/reporting operation description
    :param str accept: Mime type to accept in the payload of the response, with charset etc.
    :param str contentType: Mime type of the request payload contents, with charset etc.
    :param int destination: Server responding to the request
    :param bool encodeRequestUrl: Whether or not to send the request url in encoded format
    :param str method: delete | get | options | patch | post | put | head
    :param int origin: Server initiating the request
    :param str params: Explicitly defined path parameters
    :param BackboneElement requestHeader: Each operation can have one or more header elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    :param BackboneElement operation: The setup operation to perform
    :param BackboneElement operation: The setup operation to perform
    """
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "Coding" = None
    
    resource: str = None
    
    label: str = None
    
    description: str = None
    
    accept: str = None
    
    contentType: str = None
    
    destination: int = None
    
    encodeRequestUrl: bool = None
    
    method: str = None
    
    origin: int = None
    
    params: str = None
    
    requestHeader: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    field: str = None
    
    value: str = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    
    operation: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class _assert(Element):
    """ Evaluates the results of previous operations to determine if the server under test behaves appropriately.
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str label: Tracking/logging assertion label
    :param str description: Tracking/reporting assertion description
    :param str direction: response | request
    :param str compareToSourceId: Id of the source fixture to be evaluated
    :param str compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture
    :param str compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture
    :param str contentType: Mime type to compare against the 'Content-Type' header
    :param str expression: The FHIRPath expression to be evaluated
    :param str headerField: HTTP header field name
    :param str minimumId: Fixture Id of minimum content resource
    :param bool navigationLinks: Perform validation on navigation links?
    :param str operator: equals | notEquals | in | notIn | greaterThan | lessThan | empty | notEmpty | contains | notContains | eval
    :param str path: XPath or JSONPath expression
    :param str requestMethod: delete | get | options | patch | post | put | head
    :param str requestURL: Request URL comparison value
    :param str resource: Resource type
    :param str response: okay | created | noContent | notModified | bad | forbidden | notFound | methodNotAllowed | conflict | gone | preconditionFailed | unprocessable
    :param str responseCode: HTTP response code to test
    :param str sourceId: Fixture Id of source expression or headerField
    :param str validateProfileId: Profile Id of validation profile reference
    :param str value: The value to compare to
    :param bool warningOnly: Will this assert produce a warning only on error?
    :param BackboneElement _assert: The assertion to perform
    """
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    label: str = None
    
    description: str = None
    
    direction: str = None
    
    compareToSourceId: str = None
    
    compareToSourceExpression: str = None
    
    compareToSourcePath: str = None
    
    contentType: str = None
    
    expression: str = None
    
    headerField: str = None
    
    minimumId: str = None
    
    navigationLinks: bool = None
    
    operator: str = None
    
    path: str = None
    
    requestMethod: str = None
    
    requestURL: str = None
    
    resource: str = None
    
    response: str = None
    
    responseCode: str = None
    
    sourceId: str = None
    
    validateProfileId: str = None
    
    value: str = None
    
    warningOnly: bool = None
    
    _assert: "BackboneElement" = None
    
@dataclass
class teardown(Element):
    """ A series of operations required to clean up after all the tests are executed (successfully or otherwise).
    :param BackboneElement teardown: A series of required clean up steps
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: One or more teardown operations to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    teardown: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
@dataclass
class action(Element):
    """ The teardown action will only contain an operation.
    :param BackboneElement action: One or more teardown operations to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
@dataclass
class operation(Element):
    """ The operation to perform.
    :param BackboneElement operation: The setup operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The operation code type that will be executed
    :param str resource: Resource type
    :param str label: Tracking/logging operation label
    :param str description: Tracking/reporting operation description
    :param str accept: Mime type to accept in the payload of the response, with charset etc.
    :param str contentType: Mime type of the request payload contents, with charset etc.
    :param int destination: Server responding to the request
    :param bool encodeRequestUrl: Whether or not to send the request url in encoded format
    :param str method: delete | get | options | patch | post | put | head
    :param int origin: Server initiating the request
    :param str params: Explicitly defined path parameters
    :param BackboneElement requestHeader: Each operation can have one or more header elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    :param BackboneElement operation: The setup operation to perform
    :param BackboneElement operation: The setup operation to perform
    """
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "Coding" = None
    
    resource: str = None
    
    label: str = None
    
    description: str = None
    
    accept: str = None
    
    contentType: str = None
    
    destination: int = None
    
    encodeRequestUrl: bool = None
    
    method: str = None
    
    origin: int = None
    
    params: str = None
    
    requestHeader: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    field: str = None
    
    value: str = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    
    operation: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    


@dataclass
class TestScript(ModelBase):
    """ A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this test script, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the test script
    :param str version: Business version of the test script
    :param str name: Name for this test script (computer friendly)
    :param str title: Name for this test script (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the test script
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for test script (if applicable)
    :param str purpose: Why this test script is defined
    :param str copyright: Use and/or publishing restrictions
    :param BackboneElement origin: An abstract server representing a client or sender in a message exchange
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract origin server starting at 1
    :param Coding profile: FHIR-Client | FHIR-SDC-FormFiller
    :param BackboneElement destination: An abstract server representing a destination or receiver in a message exchange
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract destination server starting at 1
    :param Coding profile: FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-SDC-FormProcessor
    :param BackboneElement metadata: Required capability that is assumed to function correctly on the FHIR server being tested
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement link: Links to the FHIR specification
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: URL to the specification
    :param str description: Short description
    :param BackboneElement capability: Capabilities  that are assumed to function correctly on the FHIR server being tested
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool required: Are the capabilities required?
    :param bool validated: Are the capabilities validated?
    :param str description: The expected capabilities of the server
    :param int origin: Which origin server these requirements apply to
    :param int destination: Which server these requirements apply to
    :param str link: Links to the FHIR specification
    :param str capabilities: Required Capability Statement
    :param BackboneElement fixture: Fixture in the test script - by reference (uri)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool autocreate: Whether or not to implicitly create the fixture during setup
    :param bool autodelete: Whether or not to implicitly delete the fixture during teardown
    :param Reference resource: Reference of the resource
    :param Reference profile: Reference of the validation profile
    :param BackboneElement variable: Placeholder for evaluated elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Descriptive name for this variable
    :param str defaultValue: Default, hard-coded, or user-defined value for this variable
    :param str description: Natural language description of the variable
    :param str expression: The FHIRPath expression against the fixture body
    :param str headerField: HTTP header field name for source
    :param str hint: Hint help text for default value to enter
    :param str path: XPath or JSONPath against the fixture body
    :param str sourceId: Fixture Id of source expression or headerField within this variable
    :param BackboneElement setup: A series of required setup operations before tests are executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: A setup operation or assert to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The setup operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The operation code type that will be executed
    :param str resource: Resource type
    :param str label: Tracking/logging operation label
    :param str description: Tracking/reporting operation description
    :param str accept: Mime type to accept in the payload of the response, with charset etc.
    :param str contentType: Mime type of the request payload contents, with charset etc.
    :param int destination: Server responding to the request
    :param bool encodeRequestUrl: Whether or not to send the request url in encoded format
    :param str method: delete | get | options | patch | post | put | head
    :param int origin: Server initiating the request
    :param str params: Explicitly defined path parameters
    :param BackboneElement requestHeader: Each operation can have one or more header elements
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str label: Tracking/logging assertion label
    :param str description: Tracking/reporting assertion description
    :param str direction: response | request
    :param str compareToSourceId: Id of the source fixture to be evaluated
    :param str compareToSourceExpression: The FHIRPath expression to evaluate against the source fixture
    :param str compareToSourcePath: XPath or JSONPath expression to evaluate against the source fixture
    :param str contentType: Mime type to compare against the 'Content-Type' header
    :param str expression: The FHIRPath expression to be evaluated
    :param str headerField: HTTP header field name
    :param str minimumId: Fixture Id of minimum content resource
    :param bool navigationLinks: Perform validation on navigation links?
    :param str operator: equals | notEquals | in | notIn | greaterThan | lessThan | empty | notEmpty | contains | notContains | eval
    :param str path: XPath or JSONPath expression
    :param str requestMethod: delete | get | options | patch | post | put | head
    :param str requestURL: Request URL comparison value
    :param str resource: Resource type
    :param str response: okay | created | noContent | notModified | bad | forbidden | notFound | methodNotAllowed | conflict | gone | preconditionFailed | unprocessable
    :param str responseCode: HTTP response code to test
    :param str sourceId: Fixture Id of source expression or headerField
    :param str validateProfileId: Profile Id of validation profile reference
    :param str value: The value to compare to
    :param bool warningOnly: Will this assert produce a warning only on error?
    :param BackboneElement test: A test in this script
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param BackboneElement action: A test operation or assert to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The setup operation to perform
    :param BackboneElement _assert: The assertion to perform
    :param BackboneElement teardown: A series of required clean up steps
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: One or more teardown operations to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The setup operation to perform
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
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
    
    purpose: str = None
    
    copyright: str = None
    
    origin: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    index: int = None
    
    profile: "Coding" = None
    
    destination: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    index: int = None
    
    profile: "Coding" = None
    
    metadata: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    link: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    description: str = None
    
    capability: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    required: bool = None
    
    validated: bool = None
    
    description: str = None
    
    origin: int = None
    
    destination: int = None
    
    link: str = None
    
    capabilities: str = None
    
    fixture: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    autocreate: bool = None
    
    autodelete: bool = None
    
    resource: "Reference" = None
    
    profile: list["Reference"] = None
    
    variable: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    defaultValue: str = None
    
    description: str = None
    
    expression: str = None
    
    headerField: str = None
    
    hint: str = None
    
    path: str = None
    
    sourceId: str = None
    
    setup: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "Coding" = None
    
    resource: str = None
    
    label: str = None
    
    description: str = None
    
    accept: str = None
    
    contentType: str = None
    
    destination: int = None
    
    encodeRequestUrl: bool = None
    
    method: str = None
    
    origin: int = None
    
    params: str = None
    
    requestHeader: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    field: str = None
    
    value: str = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    label: str = None
    
    description: str = None
    
    direction: str = None
    
    compareToSourceId: str = None
    
    compareToSourceExpression: str = None
    
    compareToSourcePath: str = None
    
    contentType: str = None
    
    expression: str = None
    
    headerField: str = None
    
    minimumId: str = None
    
    navigationLinks: bool = None
    
    operator: str = None
    
    path: str = None
    
    requestMethod: str = None
    
    requestURL: str = None
    
    resource: str = None
    
    response: str = None
    
    responseCode: str = None
    
    sourceId: str = None
    
    validateProfileId: str = None
    
    value: str = None
    
    warningOnly: bool = None
    
    test: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    description: str = None
    
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    operation: "BackboneElement" = None
    
    _assert: "BackboneElement" = None
    
    teardown: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    operation: "BackboneElement" = None
    