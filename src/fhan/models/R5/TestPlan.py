"""
Generated class for TestPlan. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Dependency(BaseModel):
    """ The required criteria to execute the test plan - e.g. preconditions, previous tests...:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of the dependency criterium
    :param Reference predecessor: Link to predecessor test plans
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "predecessor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  predecessor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.predecessor = predecessor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Dependency(BaseModel):
    """ The required criteria to execute the test case - e.g. preconditions, previous tests.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of the criteria
    :param Reference predecessor: Link to predecessor test plans
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "predecessor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  predecessor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.predecessor = predecessor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Script(BaseModel):
    """ The test cases in a structured language e.g. gherkin, Postman, or FHIR TestScript.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept language: The language for the test cases e.g. 'gherkin', 'testscript'
    :param str sourceString: The actual content of the cases - references to TestScripts or externally defined content
    :param Reference sourceReference: The actual content of the cases - references to TestScripts or externally defined content
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "sourceReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  language:  'CodeableConcept'  = None,  sourceString:  'str'  = None,  sourceReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.language = language 
        self.sourceString = sourceString 
        self.sourceReference = sourceReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class TestRun(BaseModel):
    """ The actual test to be executed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str narrative: The narrative description of the tests
    :param Script script: The test cases in a structured language e.g. gherkin, Postman, or FHIR TestScript
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "script": {"class_name": "Script", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  narrative:  'str'  = None,  script:  'Script'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.narrative = narrative 
        self.script = script 
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class TestData(BaseModel):
    """ The test data used in the test case.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The type of test data description, e.g. 'synthea'
    :param Reference content: The actual test resources when they exist
    :param str sourceString: Pointer to a definition of test resources - narrative or structured e.g. synthetic data generation, etc
    :param Reference sourceReference: Pointer to a definition of test resources - narrative or structured e.g. synthetic data generation, etc
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "Coding", "is_contained": False},
        
        
        "content": {"class_name": "Reference", "is_contained": False},
        
        
        
        "sourceReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'Coding'  = None,  content:  'Reference'  = None,  sourceString:  'str'  = None,  sourceReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.content = content 
        self.sourceString = sourceString 
        self.sourceReference = sourceReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Assertion(BaseModel):
    """ The test assertions - the expectations of test results from the execution of the test case.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Assertion type - for example 'informative' or 'required' 
    :param CodeableReference object: The focus or object of the assertion
    :param CodeableReference result: The actual result assertion
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "object": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "result": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  list['CodeableConcept']  = None,  object:  list['CodeableReference']  = None,  result:  list['CodeableReference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.object = object or []
        self.result = result or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class TestCase(BaseModel):
    """ The individual test cases that are part of this plan, when they they are made explicit.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Sequence of test case in the test plan
    :param Reference scope: The scope or artifact covered by the case
    :param Dependency dependency: Required criteria to execute the test case
    :param TestRun testRun: The actual test to be executed
    :param TestData testData: The test data used in the test case
    :param Assertion assertion: Test assertions or expectations
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "scope": {"class_name": "Reference", "is_contained": False},
        
        
        "dependency": {"class_name": "Dependency", "is_contained": True},
        
        
        "testRun": {"class_name": "TestRun", "is_contained": True},
        
        
        "testData": {"class_name": "TestData", "is_contained": True},
        
        
        "assertion": {"class_name": "Assertion", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  sequence:  'int'  = None,  scope:  list['Reference']  = None,  dependency:  list['Dependency']  = None,  testRun:  list['TestRun']  = None,  testData:  list['TestData']  = None,  assertion:  list['Assertion']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence 
        self.scope = scope or []
        self.dependency = dependency or []
        self.testRun = testRun or []
        self.testData = testData or []
        self.assertion = assertion or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class TestPlan(DomainResource):
    """ A plan for executing testing on an artifact or specifications
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this test plan, represented as a URI (globally unique)
    :param Identifier identifier: Business identifier identifier for the test plan
    :param str version: Business version of the test plan
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this test plan (computer friendly)
    :param str title: Name for this test plan (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the test plan
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction where the test plan applies (if applicable)
    :param str purpose: Why this test plan is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param CodeableConcept category: The category of the Test Plan - can be acceptance, unit, performance
    :param Reference scope: What is being tested with this Test Plan - a conformance resource, or narrative criteria, or an external reference
    :param str testTools: A description of test tools to be used in the test plan - narrative for now
    :param Dependency dependency: The required criteria to execute the test plan - e.g. preconditions, previous tests
    :param str exitCriteria: The threshold or criteria for the test plan to be considered successfully executed - narrative
    :param TestCase testCase: The test cases that constitute this plan
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "scope": {"class_name": "Reference", "is_contained": False},
        
        
        
        "dependency": {"class_name": "Dependency", "is_contained": True},
        
        
        
        "testCase": {"class_name": "TestCase", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  category:  list['CodeableConcept']  = None,  scope:  list['Reference']  = None,  testTools:  'str'  = None,  dependency:  list['Dependency']  = None,  exitCriteria:  'str'  = None,  testCase:  list['TestCase']  = None, ):
        self.resourceType = resourceType or "TestPlan"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.status = status 
        self.experimental = experimental 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.category = category or []
        self.scope = scope or []
        self.testTools = testTools 
        self.dependency = dependency or []
        self.exitCriteria = exitCriteria 
        self.testCase = testCase or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "TestPlan":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "TestPlan":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()