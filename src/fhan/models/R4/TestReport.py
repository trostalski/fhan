"""
Generated class for TestReport. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class participant(Element):
    """ A participant in the test execution, either the execution engine, a client, or a server.
    :param BackboneElement participant: A participant in the test execution, either the execution engine, a client, or a server
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: test-engine | client | server
    :param str uri: The uri of the participant. An absolute URL is preferred
    :param str display: The display name of the participant
    """
    participant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    uri: str = None
    
    display: str = None
    
@dataclass
class setup(Element):
    """ The results of the series of required setup operations before the tests were executed.
    :param BackboneElement setup: The results of the series of required setup operations before the tests were executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: A setup operation or assert that was executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement operation: The operation to perform
    :param BackboneElement _assert: The assertion to perform
    :param BackboneElement operation: The operation to perform
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
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    operation: "BackboneElement" = None
    
    _assert: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class action(Element):
    """ Action would contain either an operation or an assertion.
    :param BackboneElement action: A setup operation or assert that was executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement operation: The operation to perform
    :param BackboneElement _assert: The assertion to perform
    :param BackboneElement operation: The operation to perform
    """
    action: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    operation: "BackboneElement" = None
    
    _assert: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class operation(Element):
    """ The operation performed.
    :param BackboneElement operation: The operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement operation: The operation to perform
    :param BackboneElement operation: The operation to perform
    """
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    operation: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class _assert(Element):
    """ The results of the assertion performed on the previous operations.
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement _assert: The assertion to perform
    """
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    _assert: "BackboneElement" = None
    
@dataclass
class test(Element):
    """ A test executed from the test script.
    :param Reference testScript: Reference to the  version-specific TestScript that was executed to produce this TestReport
    :param str tester: Name of the tester producing this report (Organization or individual)
    :param BackboneElement test: A test executed from the test script
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param BackboneElement action: A test operation or assert that was performed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    testScript: "Reference" = None
    
    tester: str = None
    
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
    :param BackboneElement action: A test operation or assert that was performed
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
    """ The operation performed.
    :param BackboneElement operation: The operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement operation: The operation to perform
    :param BackboneElement operation: The operation to perform
    """
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    operation: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    
@dataclass
class _assert(Element):
    """ The results of the assertion performed on the previous operations.
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement _assert: The assertion to perform
    """
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    _assert: "BackboneElement" = None
    
@dataclass
class teardown(Element):
    """ The results of the series of operations required to clean up after all the tests were executed (successfully or otherwise).
    :param BackboneElement teardown: The results of running the series of required clean up steps
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: One or more teardown operations performed
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
    :param BackboneElement action: One or more teardown operations performed
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
    """ The operation performed.
    :param BackboneElement operation: The operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement operation: The operation to perform
    :param BackboneElement operation: The operation to perform
    """
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    operation: "BackboneElement" = None
    
    operation: "BackboneElement" = None
    


@dataclass
class TestReport(ModelBase):
    """ A summary of information based on the results of executing a TestScript.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param str name: Informal name of the executed TestScript
    :param str status: completed | in-progress | waiting | stopped | entered-in-error
    :param Reference testScript: Reference to the  version-specific TestScript that was executed to produce this TestReport
    :param str result: pass | fail | pending
    :param float score: The final score (percentage of tests passed) resulting from the execution of the TestScript
    :param str tester: Name of the tester producing this report (Organization or individual)
    :param str issued: When the TestScript was executed and this TestReport was generated
    :param BackboneElement participant: A participant in the test execution, either the execution engine, a client, or a server
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: test-engine | client | server
    :param str uri: The uri of the participant. An absolute URL is preferred
    :param str display: The display name of the participant
    :param BackboneElement setup: The results of the series of required setup operations before the tests were executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: A setup operation or assert that was executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The operation to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement _assert: The assertion to perform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    :param BackboneElement test: A test executed from the test script
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param BackboneElement action: A test operation or assert that was performed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The operation to perform
    :param BackboneElement _assert: The assertion to perform
    :param BackboneElement teardown: The results of running the series of required clean up steps
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement action: One or more teardown operations performed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement operation: The operation to perform
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: "Identifier" = None
    
    name: str = None
    
    status: str = None
    
    testScript: "Reference" = None
    
    result: str = None
    
    score: float = None
    
    tester: str = None
    
    issued: str = None
    
    participant: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: str = None
    
    uri: str = None
    
    display: str = None
    
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
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
    _assert: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    
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
    