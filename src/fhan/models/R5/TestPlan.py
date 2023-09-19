"""
Generated class for TestPlan. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class TestPlan:
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
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
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
    :param BackboneElement dependency: The required criteria to execute the test plan - e.g. preconditions, previous tests
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of the dependency criterium
    :param Reference predecessor: Link to predecessor test plans
    :param str exitCriteria: The threshold or criteria for the test plan to be considered successfully executed - narrative
    :param BackboneElement testCase: The test cases that constitute this plan
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: Sequence of test case in the test plan
    :param Reference scope: The scope or artifact covered by the case
    :param BackboneElement dependency: Required criteria to execute the test case
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of the criteria
    :param Reference predecessor: Link to predecessor test plans
    :param BackboneElement testRun: The actual test to be executed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str narrative: The narrative description of the tests
    :param BackboneElement script: The test cases in a structured language e.g. gherkin, Postman, or FHIR TestScript
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept language: The language for the test cases e.g. 'gherkin', 'testscript'
    :param str sourcestring: The actual content of the cases - references to TestScripts or externally defined content
    :param Reference sourcestring: The actual content of the cases - references to TestScripts or externally defined content
    :param BackboneElement testData: The test data used in the test case
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: The type of test data description, e.g. 'synthea'
    :param Reference content: The actual test resources when they exist
    :param str sourcestring: Pointer to a definition of test resources - narrative or structured e.g. synthetic data generation, etc
    :param Reference sourcestring: Pointer to a definition of test resources - narrative or structured e.g. synthetic data generation, etc
    :param BackboneElement assertion: Test assertions or expectations
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Assertion type - for example 'informative' or 'required' 
    :param CodeableReference object: The focus or object of the assertion
    :param CodeableReference result: The actual result assertion
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    copyrightLabel: str = None
    
    category: "CodeableConcept" = None
    
    scope: "Reference" = None
    
    testTools: str = None
    
    dependency: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    predecessor: "Reference" = None
    
    exitCriteria: str = None
    
    testCase: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    scope: "Reference" = None
    
    dependency: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    predecessor: "Reference" = None
    
    testRun: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    narrative: str = None
    
    script: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: "CodeableConcept" = None
    
    sourcestring: str = None
    
    sourcestring: "Reference" = None
    
    testData: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "Coding" = None
    
    content: "Reference" = None
    
    sourcestring: str = None
    
    sourcestring: "Reference" = None
    
    assertion: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    object: "CodeableReference" = None
    
    result: "CodeableReference" = None
    