"""
Generated class for RequestOrchestration. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Expression import *
from fhan.models.R5.Age import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Condition(BaseModel):
    """ An expression that describes applicability criteria, or start/stop conditions for the action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str kind: applicability | start | stop
    :param Expression expression: Boolean-valued expression
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "expression": {"class_name": "Expression", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  kind:  'str'  = None,  expression:  'Expression'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.kind = kind 
        self.expression = expression 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Input(BaseModel):
    """ Defines input data requirements for the action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: User-visible title
    :param DataRequirement requirement: What data is provided
    :param str relatedData: What data is provided
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "requirement": {"class_name": "DataRequirement", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  title:  'str'  = None,  requirement:  'DataRequirement'  = None,  relatedData:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title 
        self.requirement = requirement 
        self.relatedData = relatedData 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Output(BaseModel):
    """ Defines the outputs of the action, if any.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: User-visible title
    :param DataRequirement requirement: What data is provided
    :param str relatedData: What data is provided
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "requirement": {"class_name": "DataRequirement", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  title:  'str'  = None,  requirement:  'DataRequirement'  = None,  relatedData:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title 
        self.requirement = requirement 
        self.relatedData = relatedData 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class RelatedAction(BaseModel):
    """ A relationship to another action such as "before" or "30-60 minutes after start of".:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str targetId: What action this is related to
    :param str relationship: before | before-start | before-end | concurrent | concurrent-with-start | concurrent-with-end | after | after-start | after-end
    :param str endRelationship: before | before-start | before-end | concurrent | concurrent-with-start | concurrent-with-end | after | after-start | after-end
    :param Duration offsetDuration: Time offset for the relationship
    :param Range offsetRange: Time offset for the relationship
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        "offsetDuration": {"class_name": "Duration", "is_contained": False},
        
        
        "offsetRange": {"class_name": "Range", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  targetId:  'str'  = None,  relationship:  'str'  = None,  endRelationship:  'str'  = None,  offsetDuration:  'Duration'  = None,  offsetRange:  'Range'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.targetId = targetId 
        self.relationship = relationship 
        self.endRelationship = endRelationship 
        self.offsetDuration = offsetDuration 
        self.offsetRange = offsetRange 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Participant(BaseModel):
    """ The participant that should perform or be responsible for this action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent, etc
    :param CodeableConcept function: E.g. Author, Reviewer, Witness, etc
    :param str actorCanonical: Who/what is participating?
    :param Reference actorReference: Who/what is participating?
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "typeReference": {"class_name": "Reference", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "actorReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  typeCanonical:  'str'  = None,  typeReference:  'Reference'  = None,  role:  'CodeableConcept'  = None,  function:  'CodeableConcept'  = None,  actorCanonical:  'str'  = None,  actorReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.typeCanonical = typeCanonical 
        self.typeReference = typeReference 
        self.role = role 
        self.function = function 
        self.actorCanonical = actorCanonical 
        self.actorReference = actorReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class DynamicValue(BaseModel):
    """ Customizations that should be applied to the statically defined resource. For example, if the dosage of a medication must be computed based on the patient's weight, a customization would be used to specify an expression that calculated the weight, and the path on the resource that would contain the result.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param Expression expression: An expression that provides the dynamic value for the customization
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "expression": {"class_name": "Expression", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  path:  'str'  = None,  expression:  'Expression'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.path = path 
        self.expression = expression 
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Action(BaseModel):
    """ The actions, if any, produced by the evaluation of the artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific item from the PlanDefinition
    :param str prefix: User-visible prefix for the action (e.g. 1. or A.)
    :param str title: User-visible title
    :param str description: Short description of the action
    :param str textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: Code representing the meaning of the action or sub-actions
    :param RelatedArtifact documentation: Supporting documentation for the intended performer of the action
    :param Reference goal: What goals
    :param Condition condition: Whether or not the action is applicable
    :param Input input: Input data requirements
    :param Output output: Output data definition
    :param RelatedAction relatedAction: Relationship to another action
    :param str timingDateTime: When the action should take place
    :param Age timingAge: When the action should take place
    :param Period timingPeriod: When the action should take place
    :param Duration timingDuration: When the action should take place
    :param Range timingRange: When the action should take place
    :param Timing timingTiming: When the action should take place
    :param CodeableReference location: Where it should happen
    :param Participant participant: Who should perform the action
    :param CodeableConcept type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param Reference resource: The target of the action
    :param str definitionCanonical: Description of the activity to be performed
    :param str definitionUri: Description of the activity to be performed
    :param str transform: Transform to apply the template
    :param DynamicValue dynamicValue: Dynamic aspects of the definition
    :param Action action: Sub action
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "documentation": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "goal": {"class_name": "Reference", "is_contained": False},
        
        
        "condition": {"class_name": "Condition", "is_contained": True},
        
        
        "input": {"class_name": "Input", "is_contained": True},
        
        
        "output": {"class_name": "Output", "is_contained": True},
        
        
        "relatedAction": {"class_name": "RelatedAction", "is_contained": True},
        
        
        
        "timingAge": {"class_name": "Age", "is_contained": False},
        
        
        "timingPeriod": {"class_name": "Period", "is_contained": False},
        
        
        "timingDuration": {"class_name": "Duration", "is_contained": False},
        
        
        "timingRange": {"class_name": "Range", "is_contained": False},
        
        
        "timingTiming": {"class_name": "Timing", "is_contained": False},
        
        
        "location": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        "resource": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "dynamicValue": {"class_name": "DynamicValue", "is_contained": True},
        
        
        "action": {"class_name": "Action", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  prefix:  'str'  = None,  title:  'str'  = None,  description:  'str'  = None,  textEquivalent:  'str'  = None,  priority:  'str'  = None,  code:  list['CodeableConcept']  = None,  documentation:  list['RelatedArtifact']  = None,  goal:  list['Reference']  = None,  condition:  list['Condition']  = None,  input:  list['Input']  = None,  output:  list['Output']  = None,  relatedAction:  list['RelatedAction']  = None,  timingDateTime:  'str'  = None,  timingAge:  'Age'  = None,  timingPeriod:  'Period'  = None,  timingDuration:  'Duration'  = None,  timingRange:  'Range'  = None,  timingTiming:  'Timing'  = None,  location:  'CodeableReference'  = None,  participant:  list['Participant']  = None,  type:  'CodeableConcept'  = None,  groupingBehavior:  'str'  = None,  selectionBehavior:  'str'  = None,  requiredBehavior:  'str'  = None,  precheckBehavior:  'str'  = None,  cardinalityBehavior:  'str'  = None,  resource:  'Reference'  = None,  definitionCanonical:  'str'  = None,  definitionUri:  'str'  = None,  transform:  'str'  = None,  dynamicValue:  list['DynamicValue']  = None,  action:  list['Action']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.prefix = prefix 
        self.title = title 
        self.description = description 
        self.textEquivalent = textEquivalent 
        self.priority = priority 
        self.code = code or []
        self.documentation = documentation or []
        self.goal = goal or []
        self.condition = condition or []
        self.input = input or []
        self.output = output or []
        self.relatedAction = relatedAction or []
        self.timingDateTime = timingDateTime 
        self.timingAge = timingAge 
        self.timingPeriod = timingPeriod 
        self.timingDuration = timingDuration 
        self.timingRange = timingRange 
        self.timingTiming = timingTiming 
        self.location = location 
        self.participant = participant or []
        self.type = type 
        self.groupingBehavior = groupingBehavior 
        self.selectionBehavior = selectionBehavior 
        self.requiredBehavior = requiredBehavior 
        self.precheckBehavior = precheckBehavior 
        self.cardinalityBehavior = cardinalityBehavior 
        self.resource = resource 
        self.definitionCanonical = definitionCanonical 
        self.definitionUri = definitionUri 
        self.transform = transform 
        self.dynamicValue = dynamicValue or []
        self.action = action or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class RequestOrchestration(DomainResource):
    """ A set of related requests that can be used to capture intended activities that have inter-dependencies such as "give this medication after that one".
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: Fulfills plan, proposal, or order
    :param Reference replaces: Request(s) replaced by this request
    :param Identifier groupIdentifier: Composite request this is part of
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: What's being requested/ordered
    :param Reference subject: Who the request orchestration is about
    :param Reference encounter: Created as part of
    :param str authoredOn: When the request orchestration was authored
    :param Reference author: Device or practitioner that authored the request orchestration
    :param CodeableReference reason: Why the request orchestration is needed
    :param Reference goal: What goals
    :param Annotation note: Additional notes about the response
    :param Action action: Proposed actions, if any
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "replaces": {"class_name": "Reference", "is_contained": False},
        
        
        "groupIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "goal": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "action": {"class_name": "Action", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  instantiatesCanonical:  list['str']  = None,  instantiatesUri:  list['str']  = None,  basedOn:  list['Reference']  = None,  replaces:  list['Reference']  = None,  groupIdentifier:  'Identifier'  = None,  status:  'str'  = None,  intent:  'str'  = None,  priority:  'str'  = None,  code:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  authoredOn:  'str'  = None,  author:  'Reference'  = None,  reason:  list['CodeableReference']  = None,  goal:  list['Reference']  = None,  note:  list['Annotation']  = None,  action:  list['Action']  = None, ):
        self.resourceType = resourceType or "RequestOrchestration"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.instantiatesCanonical = instantiatesCanonical or []
        self.instantiatesUri = instantiatesUri or []
        self.basedOn = basedOn or []
        self.replaces = replaces or []
        self.groupIdentifier = groupIdentifier 
        self.status = status 
        self.intent = intent 
        self.priority = priority 
        self.code = code 
        self.subject = subject 
        self.encounter = encounter 
        self.authoredOn = authoredOn 
        self.author = author 
        self.reason = reason or []
        self.goal = goal or []
        self.note = note or []
        self.action = action or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "RequestOrchestration":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "RequestOrchestration":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()