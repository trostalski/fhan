"""
Generated class for ExampleScenario. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
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


    
    

class Actor(BaseModel):
    """ A system or person who shares or receives an instance within the scenario.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: ID or acronym of the actor
    :param str type: person | system
    :param str title: Label for actor when rendering
    :param str description: Details about actor
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  key:  'str'  = None,  type:  'str'  = None,  title:  'str'  = None,  description:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.key = key 
        self.type = type 
        self.title = title 
        self.description = description 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Version(BaseModel):
    """ Represents the instance as it was at a specific time-point.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: ID or acronym of the version
    :param str title: Label for instance version
    :param str description: Details about version
    :param Reference content: Example instance version data
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        "content": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  key:  'str'  = None,  title:  'str'  = None,  description:  'str'  = None,  content:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.key = key 
        self.title = title 
        self.description = description 
        self.content = content 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ContainedInstance(BaseModel):
    """ References to other instances that can be found within this instance (e.g. the observations contained in a bundle).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str instanceReference: Key of contained instance
    :param str versionReference: Key of contained instance version
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  instanceReference:  'str'  = None,  versionReference:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.instanceReference = instanceReference 
        self.versionReference = versionReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Instance(BaseModel):
    """ A single data collection that is shared as part of the scenario.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str key: ID or acronym of the instance
    :param Coding structureType: Data structure for example
    :param str structureVersion: E.g. 4.0.1
    :param str structureProfileCanonical: Rules instance adheres to
    :param str structureProfileUri: Rules instance adheres to
    :param str title: Label for instance
    :param str description: Human-friendly description of the instance
    :param Reference content: Example instance data
    :param Version version: Snapshot of instance that changes
    :param ContainedInstance containedInstance: Resources contained in the instance
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "structureType": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        "content": {"class_name": "Reference", "is_contained": False},
        
        
        "version": {"class_name": "Version", "is_contained": True},
        
        
        "containedInstance": {"class_name": "ContainedInstance", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  key:  'str'  = None,  structureType:  'Coding'  = None,  structureVersion:  'str'  = None,  structureProfileCanonical:  'str'  = None,  structureProfileUri:  'str'  = None,  title:  'str'  = None,  description:  'str'  = None,  content:  'Reference'  = None,  version:  list['Version']  = None,  containedInstance:  list['ContainedInstance']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.key = key 
        self.structureType = structureType 
        self.structureVersion = structureVersion 
        self.structureProfileCanonical = structureProfileCanonical 
        self.structureProfileUri = structureProfileUri 
        self.title = title 
        self.description = description 
        self.content = content 
        self.version = version or []
        self.containedInstance = containedInstance or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class Operation(BaseModel):
    """ The step represents a single operation invoked on receiver by sender.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding type: Kind of action
    :param str title: Label for step
    :param str initiator: Who starts the operation
    :param str receiver: Who receives the operation
    :param str description: Human-friendly description of the operation
    :param bool initiatorActive: Initiator stays active?
    :param bool receiverActive: Receiver stays active?
    :param Request request: Instance transmitted on invocation
    :param Response response: Instance transmitted on invocation response
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        "request": {"class_name": "Request", "is_contained": True},
        
        
        "response": {"class_name": "Response", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'Coding'  = None,  title:  'str'  = None,  initiator:  'str'  = None,  receiver:  'str'  = None,  description:  'str'  = None,  initiatorActive:  'bool'  = None,  receiverActive:  'bool'  = None,  request:  'Request'  = None,  response:  'Response'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.title = title 
        self.initiator = initiator 
        self.receiver = receiver 
        self.description = description 
        self.initiatorActive = initiatorActive 
        self.receiverActive = receiverActive 
        self.request = request 
        self.response = response 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Alternative(BaseModel):
    """ Indicates an alternative step that can be taken instead of the sub-process, scenario or operation.  E.g. to represent non-happy-path/exceptional/atypical circumstances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: Human-readable description of option
    :param Step step: Alternative action(s)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "step": {"class_name": "Step", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  title:  'str'  = None,  description:  'str'  = None,  step:  list['Step']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title 
        self.description = description 
        self.step = step or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Step(BaseModel):
    """ A significant action that occurs as part of the process.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: Sequential number of the step
    :param Process process: Step is nested process
    :param str workflow: Step is nested workflow
    :param Operation operation: Step is simple action
    :param Alternative alternative: Alternate non-typical step action
    :param bool pause: Pause in the flow?
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "process": {"class_name": "Process", "is_contained": True},
        
        
        
        "operation": {"class_name": "Operation", "is_contained": True},
        
        
        "alternative": {"class_name": "Alternative", "is_contained": True},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  number:  'str'  = None,  process:  'Process'  = None,  workflow:  'str'  = None,  operation:  'Operation'  = None,  alternative:  list['Alternative']  = None,  pause:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.number = number 
        self.process = process 
        self.workflow = workflow 
        self.operation = operation 
        self.alternative = alternative or []
        self.pause = pause 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Process(BaseModel):
    """ A group of operations that represents a significant step within a scenario.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for procss
    :param str description: Human-friendly description of the process
    :param str preConditions: Status before process starts
    :param str postConditions: Status after successful completion
    :param Step step: Event within of the process
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        "step": {"class_name": "Step", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  title:  'str'  = None,  description:  'str'  = None,  preConditions:  'str'  = None,  postConditions:  'str'  = None,  step:  list['Step']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title 
        self.description = description 
        self.preConditions = preConditions 
        self.postConditions = postConditions 
        self.step = step or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ExampleScenario(DomainResource):
    """ A walkthrough of a workflow showing the interaction between systems and the instances shared, possibly including the evolution of instances over time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this example scenario, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the example scenario
    :param str version: Business version of the example scenario
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: To be removed?
    :param str title: Name for this example scenario (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the ExampleScenario
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for example scenario (if applicable)
    :param str purpose: The purpose of the example, e.g. to illustrate a scenario
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param Actor actor: Individual involved in exchange
    :param Instance instance: Data used in the scenario
    :param Process process: Major process within scenario
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
        
        
        
        
        
        "actor": {"class_name": "Actor", "is_contained": True},
        
        
        "instance": {"class_name": "Instance", "is_contained": True},
        
        
        "process": {"class_name": "Process", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  actor:  list['Actor']  = None,  instance:  list['Instance']  = None,  process:  list['Process']  = None, ):
        self.resourceType = resourceType or "ExampleScenario"
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
        self.actor = actor or []
        self.instance = instance or []
        self.process = process or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()