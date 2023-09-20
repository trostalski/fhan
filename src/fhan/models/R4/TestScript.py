"""
Generated class for TestScript. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Origin(Element):
    """ An abstract server used in operations within this test script in the origin element.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract origin server starting at 1
    :param Coding profile: FHIR-Client | FHIR-SDC-FormFiller
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    index: int = None
    profile: "Coding" = None
    

    
    
@dataclass
class Destination(Element):
    """ An abstract server used in operations within this test script in the destination element.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int index: The index of the abstract destination server starting at 1
    :param Coding profile: FHIR-Server | FHIR-SDC-FormManager | FHIR-SDC-FormReceiver | FHIR-SDC-FormProcessor
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    index: int = None
    profile: "Coding" = None
    

    
        
    
    
@dataclass
class Link(Element):
    """ A link to the FHIR specification that this test is covering.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: URL to the specification
    :param str description: Short description
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    url: str = None
    
    description: str = None
    

    
    
@dataclass
class Capability(Element):
    """ Capabilities that must exist and are assumed to function correctly on the FHIR server being tested.:param str id: Unique id for inter-element referencing
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
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    required: bool = None
    
    validated: bool = None
    
    description: str = None
    
    origin: int = None
    
    destination: int = None
    
    link: str = None
    
    capabilities: str = None
    
  
    
    
@dataclass
class Metadata(Element):
    """ The required capability must exist and are assumed to function correctly on the FHIR server being tested.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Link link: Links to the FHIR specification
    :param Capability capability: Capabilities  that are assumed to function correctly on the FHIR server being tested
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    link: list[Link] = None
    capability: list[Capability] = None
    

    
    
@dataclass
class Fixture(Element):
    """ Fixture in the test script - by reference (uri). All fixtures are required for the test script to execute.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool autocreate: Whether or not to implicitly create the fixture during setup
    :param bool autodelete: Whether or not to implicitly delete the fixture during teardown
    :param Reference resource: Reference of the resource
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    autocreate: bool = None
    
    autodelete: bool = None
    resource: "Reference" = None
    

    
    
@dataclass
class Variable(Element):
    """ Variable is set based either on element value in response body or on header field value in the response headers.:param str id: Unique id for inter-element referencing
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
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    
    defaultValue: str = None
    
    description: str = None
    
    expression: str = None
    
    headerField: str = None
    
    hint: str = None
    
    path: str = None
    
    sourceId: str = None
    

    
        
    
        
    
        
    
    
@dataclass
class RequestHeader(Element):
    """ Header elements would be used to set HTTP headers.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str field: HTTP header field name
    :param str value: HTTP headerfield value
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    field: str = None
    
    value: str = None
    
  
    
    
@dataclass
class Operation(Element):
    """ The operation to perform.:param str id: Unique id for inter-element referencing
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
    :param RequestHeader requestHeader: Each operation can have one or more header elements
    :param str requestId: Fixture Id of mapped request
    :param str responseId: Fixture Id of mapped response
    :param str sourceId: Fixture Id of body for PUT and POST requests
    :param str targetId: Id of fixture used for extracting the [id],  [type], and [vid] for GET requests
    :param str url: Request URL
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
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
    requestHeader: list[RequestHeader] = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    

    
    
@dataclass
class _assert(Element):
    """ Evaluates the results of previous operations to determine if the server under test behaves appropriately.:param str id: Unique id for inter-element referencing
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
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
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
    
  
    
    
@dataclass
class Action(Element):
    """ Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The setup operation to perform
    :param _assert _assert: The assertion to perform
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    operation: "Operation" = None
    _assert: "_assert" = None
    
  
    
    
@dataclass
class Setup(Element):
    """ A series of required setup operations before tests are executed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: A setup operation or assert to perform
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    action: list[Action] = None
    

    
        
    
    
@dataclass
class Action(Element):
    """ Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
  
    
    
@dataclass
class Test(Element):
    """ A test in this script.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param Action action: A test operation or assert to perform
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    
    description: str = None
    action: list[Action] = None
    

    
        
    
    
@dataclass
class Action(Element):
    """ The teardown action will only contain an operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
  
    
    
@dataclass
class Teardown(Element):
    """ A series of operations required to clean up after all the tests are executed (successfully or otherwise).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: One or more teardown operations to perform
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    action: list[Action] = None
    
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
    :param Origin origin: An abstract server representing a client or sender in a message exchange
    :param Destination destination: An abstract server representing a destination or receiver in a message exchange
    :param Metadata metadata: Required capability that is assumed to function correctly on the FHIR server being tested
    :param Fixture fixture: Fixture in the test script - by reference (uri)
    :param Reference profile: Reference of the validation profile
    :param Variable variable: Placeholder for evaluated elements
    :param Setup setup: A series of required setup operations before tests are executed
    :param Test test: A test in this script
    :param Teardown teardown: A series of required clean up steps
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
    
    origin: list["Origin"] = None
    
    destination: list["Destination"] = None
    
    metadata: "Metadata" = None
    
    fixture: list["Fixture"] = None
    
    profile: list["Reference"] = None
    
    variable: list["Variable"] = None
    
    setup: "Setup" = None
    
    test: list["Test"] = None
    
    teardown: "Teardown" = None
    