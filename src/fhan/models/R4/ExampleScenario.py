"""
Generated class for ExampleScenario. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.DomainResource import *


    
    

class Actor(ModelBase):
    """ Actor participating in the resource.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actorId: ID or acronym of the actor
    :param str type: person | entity
    :param str name: The name of the actor as shown in the page
    :param str description: The description of the actor
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  actorId: str = None,  type: str = None,  name: str = None,  description: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.actorId: str = actorId 
        self.type: str = type 
        self.name: str = name 
        self.description: str = description 
        

    
        
    
    

class Version(ModelBase):
    """ A specific version of the resource.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str versionId: The identifier of a specific version of a resource
    :param str description: The description of the resource version
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  versionId: str = None,  description: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.versionId: str = versionId 
        self.description: str = description 
        

    
    

class ContainedInstance(ModelBase):
    """ Resources contained in the instance (e.g. the observations contained in a bundle).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  resourceId: str = None,  versionId: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.resourceId: str = resourceId 
        self.versionId: str = versionId 
        

    
    

class Request(ModelBase):
    """ Resources contained in the instance (e.g. the observations contained in a bundle).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  resourceId: str = None,  versionId: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.resourceId: str = resourceId 
        self.versionId: str = versionId 
        

    
    

class Response(ModelBase):
    """ Resources contained in the instance (e.g. the observations contained in a bundle).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  resourceId: str = None,  versionId: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.resourceId: str = resourceId 
        self.versionId: str = versionId 
        

  
    
    

class Instance(ModelBase):
    """ Each resource and each version that is present in the workflow.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: The id of the resource for referencing
    :param str resourceType: The type of the resource
    :param str name: A short name for the resource instance
    :param str description: Human-friendly description of the resource instance
    :param list['Version'] version: A specific version of the resource
    :param list['ContainedInstance'] containedInstance: Resources contained in the instance
    :param list['Request'] request: Resources contained in the instance
    :param list['Response'] response: Resources contained in the instance
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  resourceId: str = None,  resourceType: str = None,  name: str = None,  description: str = None,  version: list['Version'] = None,  containedInstance: list['ContainedInstance'] = None,  request: list['Request'] = None,  response: list['Response'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.resourceId: str = resourceId 
        self.resourceType: str = resourceType 
        self.name: str = name 
        self.description: str = description 
        self.version: list['Version'] = version or []
        self.containedInstance: list['ContainedInstance'] = containedInstance or []
        self.request: list['Request'] = request or []
        self.response: list['Response'] = response or []
        

    
        
    
        
    
    

class Operation(ModelBase):
    """ Each interaction or action.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  number: str = None,  type: str = None,  name: str = None,  initiator: str = None,  receiver: str = None,  description: str = None,  initiatorActive: bool = None,  receiverActive: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.number: str = number 
        self.type: str = type 
        self.name: str = name 
        self.initiator: str = initiator 
        self.receiver: str = receiver 
        self.description: str = description 
        self.initiatorActive: bool = initiatorActive 
        self.receiverActive: bool = receiverActive 
        

    
    

class Alternative(ModelBase):
    """ Indicates an alternative step that can be taken instead of the operations on the base step in exceptional/atypical circumstances.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  title: str = None,  description: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.title: str = title 
        self.description: str = description 
        

  
    
    

class Step(ModelBase):
    """ Each step of the process.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool pause: If there is a pause in the flow
    :param 'Operation' operation: Each interaction or action
    :param list['Alternative'] alternative: Alternate non-typical step action
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  pause: bool = None,  operation: 'Operation' = None,  alternative: list['Alternative'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.pause: bool = pause 
        self.operation: 'Operation' = operation 
        self.alternative: list['Alternative'] = alternative or []
        

  
    
    

class Process(ModelBase):
    """ Each major process - a group of operations.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: The diagram title of the group of operations
    :param str description: A longer description of the group of operations
    :param str preConditions: Description of initial status before the process starts
    :param str postConditions: Description of final status after the process ends
    :param list['Step'] step: Each step of the process
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  title: str = None,  description: str = None,  preConditions: str = None,  postConditions: str = None,  step: list['Step'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.title: str = title 
        self.description: str = description 
        self.preConditions: str = preConditions 
        self.postConditions: str = postConditions 
        self.step: list['Step'] = step or []
        

class ExampleScenario(DomainResource):
    """ Example of workflow instance.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this example scenario, represented as a URI (globally unique)
    :param list['Identifier'] identifier: Additional identifier for the example scenario
    :param str version: Business version of the example scenario
    :param str name: Name for this example scenario (computer friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for example scenario (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str purpose: The purpose of the example, e.g. to illustrate a scenario
    :param list['Actor'] actor: Actor participating in the resource
    :param list['Instance'] instance: Each resource and each version that is present in the workflow
    :param list['Process'] process: Each major process - a group of operations
    :param str workflow: Another nested workflow
    """
    def __init__(self, resourceType: str = "ExampleScenario",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  url: str = None,  identifier: list['Identifier'] = None,  version: str = None,  name: str = None,  status: str = None,  experimental: bool = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  copyright: str = None,  purpose: str = None,  actor: list['Actor'] = None,  instance: list['Instance'] = None,  process: list['Process'] = None,  workflow: str = None, ):
        self.resourceType: str = resourceType or "ExampleScenario"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.url: str = url 
        self.identifier: list['Identifier'] = identifier or []
        self.version: str = version 
        self.name: str = name 
        self.status: str = status 
        self.experimental: bool = experimental 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.copyright: str = copyright 
        self.purpose: str = purpose 
        self.actor: list['Actor'] = actor or []
        self.instance: list['Instance'] = instance or []
        self.process: list['Process'] = process or []
        self.workflow: str = workflow or []
        