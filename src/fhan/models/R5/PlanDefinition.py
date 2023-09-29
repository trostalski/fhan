"""
Generated class for PlanDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Period import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.TriggerDefinition import *
from fhan.models.R5.Expression import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Range import *
from fhan.models.R5.Age import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Timing import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Coding import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Target(BaseModel):
    """ Indicates what should be done and within what timeframe.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept measure: The parameter whose value is to be tracked
    :param Quantity detailQuantity: The target value to be achieved
    :param Range detailRange: The target value to be achieved
    :param CodeableConcept detailCodeableConcept: The target value to be achieved
    :param str detailString: The target value to be achieved
    :param bool detailBoolean: The target value to be achieved
    :param int detailInteger: The target value to be achieved
    :param Ratio detailRatio: The target value to be achieved
    :param Duration due: Reach goal within
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "measure": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "detailQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "detailRange": {"class_name": "Range", "is_contained": False},
        
        
        "detailCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "detailRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        "due": {"class_name": "Duration", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  measure:  'CodeableConcept'  = None,  detailQuantity:  'Quantity'  = None,  detailRange:  'Range'  = None,  detailCodeableConcept:  'CodeableConcept'  = None,  detailString:  'str'  = None,  detailBoolean:  'bool'  = None,  detailInteger:  'int'  = None,  detailRatio:  'Ratio'  = None,  due:  'Duration'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.measure = measure 
        self.detailQuantity = detailQuantity 
        self.detailRange = detailRange 
        self.detailCodeableConcept = detailCodeableConcept 
        self.detailString = detailString 
        self.detailBoolean = detailBoolean 
        self.detailInteger = detailInteger 
        self.detailRatio = detailRatio 
        self.due = due 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Goal(BaseModel):
    """ A goal describes an expected outcome that activities within the plan are intended to achieve. For example, weight loss, restoring an activity of daily living, obtaining herd immunity via immunization, meeting a process improvement objective, meeting the acceptance criteria for a test as specified by a quality specification, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: E.g. Treatment, dietary, behavioral
    :param CodeableConcept description: Code or text describing the goal
    :param CodeableConcept priority: high-priority | medium-priority | low-priority
    :param CodeableConcept start: When goal pursuit begins
    :param CodeableConcept addresses: What does the goal address
    :param RelatedArtifact documentation: Supporting documentation for the goal
    :param Target target: Target outcome for the goal
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "description": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "priority": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "start": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "addresses": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "documentation": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "target": {"class_name": "Target", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  category:  'CodeableConcept'  = None,  description:  'CodeableConcept'  = None,  priority:  'CodeableConcept'  = None,  start:  'CodeableConcept'  = None,  addresses:  list['CodeableConcept']  = None,  documentation:  list['RelatedArtifact']  = None,  target:  list['Target']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.category = category 
        self.description = description 
        self.priority = priority 
        self.start = start 
        self.addresses = addresses or []
        self.documentation = documentation or []
        self.target = target or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Option(BaseModel):
    """ The characteristics of the candidates that could serve as the actor.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "typeReference": {"class_name": "Reference", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  typeCanonical:  'str'  = None,  typeReference:  'Reference'  = None,  role:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.typeCanonical = typeCanonical 
        self.typeReference = typeReference 
        self.role = role 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Actor(BaseModel):
    """ Actors represent the individuals or groups involved in the execution of the defined set of activities.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: User-visible title
    :param str description: Describes the actor
    :param Option option: Who or what can be this actor
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "option": {"class_name": "Option", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  title:  'str'  = None,  description:  'str'  = None,  option:  list['Option']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title 
        self.description = description 
        self.option = option or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Condition(BaseModel):
    """ An expression that describes applicability criteria or start/stop conditions for the action.:param str id: Unique id for inter-element referencing
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
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
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
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
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
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class RelatedAction(BaseModel):
    """ A relationship to another action such as "before" or "30-60 minutes after start of".:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str targetId: What action is this related to
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
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Participant(BaseModel):
    """ Indicates who should participate in performing the action described.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actorId: What actor
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent
    :param CodeableConcept function: E.g. Author, Reviewer, Witness, etc
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        "typeReference": {"class_name": "Reference", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  actorId:  'str'  = None,  type:  'str'  = None,  typeCanonical:  'str'  = None,  typeReference:  'Reference'  = None,  role:  'CodeableConcept'  = None,  function:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.actorId = actorId 
        self.type = type 
        self.typeCanonical = typeCanonical 
        self.typeReference = typeReference 
        self.role = role 
        self.function = function 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
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
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Action(BaseModel):
    """ An action or group of actions to be taken as part of the plan. For example, in clinical care, an action would be to prescribe a particular indicated medication, or perform a particular test as appropriate. In pharmaceutical quality, an action would be the test that needs to be performed on a drug product as defined in the quality specification.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for the action in the PlanDefinition
    :param str prefix: User-visible prefix for the action (e.g. 1. or A.)
    :param str title: User-visible title
    :param str description: Brief description of the action
    :param str textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system
    :param str priority: routine | urgent | asap | stat
    :param CodeableConcept code: Code representing the meaning of the action or sub-actions
    :param CodeableConcept reason: Why the action should be performed
    :param RelatedArtifact documentation: Supporting documentation for the intended performer of the action
    :param str goalId: What goals this action supports
    :param CodeableConcept subjectCodeableConcept: Type of individual the action is focused on
    :param Reference subjectReference: Type of individual the action is focused on
    :param str subjectCanonical: Type of individual the action is focused on
    :param TriggerDefinition trigger: When the action should be triggered
    :param Condition condition: Whether or not the action is applicable
    :param Input input: Input data requirements
    :param Output output: Output data definition
    :param RelatedAction relatedAction: Relationship to another action
    :param Age timingAge: When the action should take place
    :param Duration timingDuration: When the action should take place
    :param Range timingRange: When the action should take place
    :param Timing timingTiming: When the action should take place
    :param CodeableReference location: Where it should happen
    :param Participant participant: Who should participate in the action
    :param CodeableConcept type: create | update | remove | fire-event
    :param str groupingBehavior: visual-group | logical-group | sentence-group
    :param str selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
    :param str requiredBehavior: must | could | must-unless-documented
    :param str precheckBehavior: yes | no
    :param str cardinalityBehavior: single | multiple
    :param str definitionCanonical: Description of the activity to be performed
    :param str definitionUri: Description of the activity to be performed
    :param str transform: Transform to apply the template
    :param DynamicValue dynamicValue: Dynamic aspects of the definition
    :param Action action: A sub-action
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "documentation": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        
        "subjectCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        "trigger": {"class_name": "TriggerDefinition", "is_contained": False},
        
        
        "condition": {"class_name": "Condition", "is_contained": True},
        
        
        "input": {"class_name": "Input", "is_contained": True},
        
        
        "output": {"class_name": "Output", "is_contained": True},
        
        
        "relatedAction": {"class_name": "RelatedAction", "is_contained": True},
        
        
        "timingAge": {"class_name": "Age", "is_contained": False},
        
        
        "timingDuration": {"class_name": "Duration", "is_contained": False},
        
        
        "timingRange": {"class_name": "Range", "is_contained": False},
        
        
        "timingTiming": {"class_name": "Timing", "is_contained": False},
        
        
        "location": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        
        
        
        "dynamicValue": {"class_name": "DynamicValue", "is_contained": True},
        
        
        "action": {"class_name": "Action", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  prefix:  'str'  = None,  title:  'str'  = None,  description:  'str'  = None,  textEquivalent:  'str'  = None,  priority:  'str'  = None,  code:  'CodeableConcept'  = None,  reason:  list['CodeableConcept']  = None,  documentation:  list['RelatedArtifact']  = None,  goalId:  list['str']  = None,  subjectCodeableConcept:  'CodeableConcept'  = None,  subjectReference:  'Reference'  = None,  subjectCanonical:  'str'  = None,  trigger:  list['TriggerDefinition']  = None,  condition:  list['Condition']  = None,  input:  list['Input']  = None,  output:  list['Output']  = None,  relatedAction:  list['RelatedAction']  = None,  timingAge:  'Age'  = None,  timingDuration:  'Duration'  = None,  timingRange:  'Range'  = None,  timingTiming:  'Timing'  = None,  location:  'CodeableReference'  = None,  participant:  list['Participant']  = None,  type:  'CodeableConcept'  = None,  groupingBehavior:  'str'  = None,  selectionBehavior:  'str'  = None,  requiredBehavior:  'str'  = None,  precheckBehavior:  'str'  = None,  cardinalityBehavior:  'str'  = None,  definitionCanonical:  'str'  = None,  definitionUri:  'str'  = None,  transform:  'str'  = None,  dynamicValue:  list['DynamicValue']  = None,  action:  list['Action']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.prefix = prefix 
        self.title = title 
        self.description = description 
        self.textEquivalent = textEquivalent 
        self.priority = priority 
        self.code = code 
        self.reason = reason or []
        self.documentation = documentation or []
        self.goalId = goalId or []
        self.subjectCodeableConcept = subjectCodeableConcept 
        self.subjectReference = subjectReference 
        self.subjectCanonical = subjectCanonical 
        self.trigger = trigger or []
        self.condition = condition or []
        self.input = input or []
        self.output = output or []
        self.relatedAction = relatedAction or []
        self.timingAge = timingAge 
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
        self.definitionCanonical = definitionCanonical 
        self.definitionUri = definitionUri 
        self.transform = transform 
        self.dynamicValue = dynamicValue or []
        self.action = action or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class PlanDefinition(DomainResource):
    """ This resource allows for the definition of various types of plans as a sharable, consumable, and executable artifact. The resource is general enough to support the description of a broad range of clinical and non-clinical artifacts such as clinical decision support rules, order sets, protocols, and drug quality specifications.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this plan definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the plan definition
    :param str version: Business version of the plan definition
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this plan definition (computer friendly)
    :param str title: Name for this plan definition (human friendly)
    :param str subtitle: Subordinate title of the plan definition
    :param CodeableConcept type: order-set | clinical-protocol | eca-rule | workflow-definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the plan definition is focused on
    :param Reference subjectReference: Type of individual the plan definition is focused on
    :param str subjectCanonical: Type of individual the plan definition is focused on
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the plan definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for plan definition (if applicable)
    :param str purpose: Why this plan definition is defined
    :param str usage: Describes the clinical usage of the plan
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the plan definition was approved by publisher
    :param str lastReviewDate: When the plan definition was last reviewed by the publisher
    :param Period effectivePeriod: When the plan definition is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations
    :param str library: Logic used by the plan definition
    :param Goal goal: What the plan is trying to accomplish
    :param Actor actor: Actors within the plan
    :param Action action: Action defined by the plan
    :param bool asNeededBoolean: Preconditions for service
    :param CodeableConcept asNeededCodeableConcept: Preconditions for service
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
        
        
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "subjectCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        
        "goal": {"class_name": "Goal", "is_contained": True},
        
        
        "actor": {"class_name": "Actor", "is_contained": True},
        
        
        "action": {"class_name": "Action", "is_contained": True},
        
        
        
        "asNeededCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  subtitle:  'str'  = None,  type:  'CodeableConcept'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  subjectCodeableConcept:  'CodeableConcept'  = None,  subjectReference:  'Reference'  = None,  subjectCanonical:  'str'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  usage:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  topic:  list['CodeableConcept']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  library:  list['str']  = None,  goal:  list['Goal']  = None,  actor:  list['Actor']  = None,  action:  list['Action']  = None,  asNeededBoolean:  'bool'  = None,  asNeededCodeableConcept:  'CodeableConcept'  = None, ):
        self.resourceType = resourceType or "PlanDefinition"
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
        self.subtitle = subtitle 
        self.type = type 
        self.status = status 
        self.experimental = experimental 
        self.subjectCodeableConcept = subjectCodeableConcept 
        self.subjectReference = subjectReference 
        self.subjectCanonical = subjectCanonical 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.usage = usage 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.topic = topic or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatedArtifact = relatedArtifact or []
        self.library = library or []
        self.goal = goal or []
        self.actor = actor or []
        self.action = action or []
        self.asNeededBoolean = asNeededBoolean 
        self.asNeededCodeableConcept = asNeededCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "PlanDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "PlanDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()