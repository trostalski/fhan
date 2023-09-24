"""
Generated class for TestReport. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Participant(ModelBase):
    """ A participant in the test execution, either the execution engine, a client, or a server.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: test-engine | client | server
    :param str uri: The uri of the participant. An absolute URL is preferred
    :param str display: The display name of the participant
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  uri: str = None,  display: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.uri: str = uri 
        self.display: str = display 
        

    
        
    
        
    
    

class Operation(ModelBase):
    """ The operation performed.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  result: str = None,  message: str = None,  detail: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.result: str = result 
        self.message: str = message 
        self.detail: str = detail 
        

    
    

class _assert(ModelBase):
    """ The results of the assertion performed on the previous operations.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  result: str = None,  message: str = None,  detail: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.result: str = result 
        self.message: str = message 
        self.detail: str = detail 
        

  
    
    

class Action(ModelBase):
    """ Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Operation' operation: The operation to perform
    :param '_assert' _assert: The assertion to perform
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  operation: 'Operation' = None,  _assert: '_assert' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.operation: 'Operation' = operation 
        self._assert: '_assert' = _assert 
        

  
    
    

class Setup(ModelBase):
    """ The results of the series of required setup operations before the tests were executed.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Action'] action: A setup operation or assert that was executed
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  action: list['Action'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.action: list['Action'] = action or []
        

    
        
    
    

class Action(ModelBase):
    """ Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        

  
    
    

class Test(ModelBase):
    """ A test executed from the test script.:param 'Reference' testScript: Reference to the  version-specific TestScript that was executed to produce this TestReport
    :param str tester: Name of the tester producing this report (Organization or individual)
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param list['Action'] action: A test operation or assert that was performed
    """
    def __init__(self,  testScript: 'Reference' = None,  tester: str = None,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  description: str = None,  action: list['Action'] = None, ):
        self.testScript: 'Reference' = testScript 
        self.tester: str = tester 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.description: str = description 
        self.action: list['Action'] = action or []
        

    
        
    
    

class Action(ModelBase):
    """ The teardown action will only contain an operation.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        

  
    
    

class Teardown(ModelBase):
    """ The results of the series of operations required to clean up after all the tests were executed (successfully or otherwise).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Action'] action: One or more teardown operations performed
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  action: list['Action'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.action: list['Action'] = action or []
        

class TestReport(DomainResource):
    """ A summary of information based on the results of executing a TestScript.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: External identifier
    :param str name: Informal name of the executed TestScript
    :param str status: completed | in-progress | waiting | stopped | entered-in-error
    :param 'Reference' testScript: Reference to the  version-specific TestScript that was executed to produce this TestReport
    :param str result: pass | fail | pending
    :param float score: The final score (percentage of tests passed) resulting from the execution of the TestScript
    :param str tester: Name of the tester producing this report (Organization or individual)
    :param str issued: When the TestScript was executed and this TestReport was generated
    :param list['Participant'] participant: A participant in the test execution, either the execution engine, a client, or a server
    :param 'Setup' setup: The results of the series of required setup operations before the tests were executed
    :param list['Test'] test: A test executed from the test script
    :param 'Teardown' teardown: The results of running the series of required clean up steps
    """
    def __init__(self, resourceType: str = "TestReport",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  name: str = None,  status: str = None,  testScript: 'Reference' = None,  result: str = None,  score: float = None,  tester: str = None,  issued: str = None,  participant: list['Participant'] = None,  setup: 'Setup' = None,  test: list['Test'] = None,  teardown: 'Teardown' = None, ):
        self.resourceType: str = resourceType or "TestReport"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.name: str = name 
        self.status: str = status 
        self.testScript: 'Reference' = testScript 
        self.result: str = result 
        self.score: float = score 
        self.tester: str = tester 
        self.issued: str = issued 
        self.participant: list['Participant'] = participant or []
        self.setup: 'Setup' = setup 
        self.test: list['Test'] = test or []
        self.teardown: 'Teardown' = teardown 
        