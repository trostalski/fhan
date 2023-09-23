"""
Generated class for TestReport. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Participant(Element):
    """ A participant in the test execution, either the execution engine, a client, or a server.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: test-engine | client | server
    :param str uri: The uri of the participant. An absolute URL is preferred
    :param str display: The display name of the participant
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    type: str = None
    
    uri: str = None
    
    display: str = None
    

    
        
    
        
    
    
@dataclass
class Operation(Element):
    """ The operation performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    

    
    
@dataclass
class _assert(Element):
    """ The results of the assertion performed on the previous operations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    result: str = None
    
    message: str = None
    
    detail: str = None
    

  
    
    
@dataclass
class Action(Element):
    """ Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The operation to perform
    :param _assert _assert: The assertion to perform
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    operation: "Operation" = Operation()
    _assert: "_assert" = _assert()
    

  
    
    
@dataclass
class Setup(Element):
    """ The results of the series of required setup operations before the tests were executed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: A setup operation or assert that was executed
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    action: list[Action] = Action() 
    

    
        
    
    
@dataclass
class Action(Element):
    """ Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    

  
    
    
@dataclass
class Test(Element):
    """ A test executed from the test script.:param Reference testScript: Reference to the  version-specific TestScript that was executed to produce this TestReport
    :param str tester: Name of the tester producing this report (Organization or individual)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param Action action: A test operation or assert that was performed
    """testScript: "Reference" = Reference()
    
    tester: str = None
    
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    name: str = None
    
    description: str = None
    action: list[Action] = Action() 
    

    
        
    
    
@dataclass
class Action(Element):
    """ The teardown action will only contain an operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    

  
    
    
@dataclass
class Teardown(Element):
    """ The results of the series of operations required to clean up after all the tests were executed (successfully or otherwise).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: One or more teardown operations performed
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    action: list[Action] = Action() 
    

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
    :param Participant participant: A participant in the test execution, either the execution engine, a client, or a server
    :param Setup setup: The results of the series of required setup operations before the tests were executed
    :param Test test: A test executed from the test script
    :param Teardown teardown: The results of running the series of required clean up steps
    """

    resourceType: str = "TestReport"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: "Identifier" = Identifier()
    
    name: str = None
    
    status: str = None
    
    testScript: "Reference" = Reference()
    
    result: str = None
    
    score: float = None
    
    tester: str = None
    
    issued: str = None
    
    participant: list[Participant] = Participant() 
    
    setup: "Setup" = Setup()
    
    test: list[Test] = Test() 
    
    teardown: "Teardown" = Teardown()
    