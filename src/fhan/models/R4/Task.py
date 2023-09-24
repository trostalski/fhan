"""
Generated class for Task. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Resource import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Range import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Address import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Distance import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Money import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Age import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Extension import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Count import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Period import *
from fhan.models.R4.Expression import *
from fhan.models.R4.DomainResource import *


    
    

class Restriction(ModelBase):
    """ If the Task.focus is a request resource and the task is seeking fulfillment (i.e. is asking for the request to be actioned), this element identifies any limitations on what parts of the referenced request should be actioned.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int repetitions: How many times to repeat
    :param 'Period' period: When fulfillment sought
    :param list['Reference'] recipient: For whom is fulfillment sought?
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  repetitions: int = None,  period: 'Period' = None,  recipient: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.repetitions: int = repetitions 
        self.period: 'Period' = period 
        self.recipient: list['Reference'] = recipient or []
        

    
    

class Input(ModelBase):
    """ Additional information that may be needed in the execution of the task.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Label for the input
    :param str valueBase64Binary: Content to use in performing the task
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  valueBase64Binary: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueBase64Binary: str = valueBase64Binary 
        

    
    

class Output(ModelBase):
    """ Outputs produced by the Task.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Label for output
    :param str valueBase64Binary: Result of output
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  valueBase64Binary: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueBase64Binary: str = valueBase64Binary 
        

class Task(DomainResource):
    """ A task to be performed.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Task Instance Identifier
    :param str instantiatesCanonical: Formal definition of task
    :param str instantiatesUri: Formal definition of task
    :param list['Reference'] basedOn: Request fulfilled by this task
    :param 'Identifier' groupIdentifier: Requisition or grouper id
    :param list['Reference'] partOf: Composite task
    :param str status: draft | requested | received | accepted | +
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' businessStatus: E.g. "Specimen collected", "IV prepped"
    :param str intent: unknown | proposal | plan | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param 'CodeableConcept' code: Task Type
    :param str description: Human-readable explanation of task
    :param 'Reference' focus: What task is acting on
    :param 'Reference' _for: Beneficiary of the Task
    :param 'Reference' encounter: Healthcare event during which this task originated
    :param 'Period' executionPeriod: Start and end time of execution
    :param str authoredOn: Task Creation Date
    :param str lastModified: Task Last Modified Date
    :param 'Reference' requester: Who is asking for task to be done
    :param list['CodeableConcept'] performerType: Requested performer
    :param 'Reference' owner: Responsible individual
    :param 'Reference' location: Where task occurs
    :param 'CodeableConcept' reasonCode: Why task is needed
    :param 'Reference' reasonReference: Why task is needed
    :param list['Reference'] insurance: Associated insurance coverage
    :param list['Annotation'] note: Comments made about the task
    :param list['Reference'] relevantHistory: Key events in history of the Task
    :param 'Restriction' restriction: Constraints on fulfillment tasks
    :param list['Input'] input: Information used to perform task
    :param list['Output'] output: Information produced as part of task
    """
    def __init__(self, resourceType: str = "Task",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  groupIdentifier: 'Identifier' = None,  partOf: list['Reference'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  businessStatus: 'CodeableConcept' = None,  intent: str = None,  priority: str = None,  code: 'CodeableConcept' = None,  description: str = None,  focus: 'Reference' = None,  _for: 'Reference' = None,  encounter: 'Reference' = None,  executionPeriod: 'Period' = None,  authoredOn: str = None,  lastModified: str = None,  requester: 'Reference' = None,  performerType: list['CodeableConcept'] = None,  owner: 'Reference' = None,  location: 'Reference' = None,  reasonCode: 'CodeableConcept' = None,  reasonReference: 'Reference' = None,  insurance: list['Reference'] = None,  note: list['Annotation'] = None,  relevantHistory: list['Reference'] = None,  restriction: 'Restriction' = None,  input: list['Input'] = None,  output: list['Output'] = None, ):
        self.resourceType: str = resourceType or "Task"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical 
        self.instantiatesUri: str = instantiatesUri 
        self.basedOn: list['Reference'] = basedOn or []
        self.groupIdentifier: 'Identifier' = groupIdentifier 
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.statusReason: 'CodeableConcept' = statusReason 
        self.businessStatus: 'CodeableConcept' = businessStatus 
        self.intent: str = intent 
        self.priority: str = priority 
        self.code: 'CodeableConcept' = code 
        self.description: str = description 
        self.focus: 'Reference' = focus 
        self._for: 'Reference' = _for 
        self.encounter: 'Reference' = encounter 
        self.executionPeriod: 'Period' = executionPeriod 
        self.authoredOn: str = authoredOn 
        self.lastModified: str = lastModified 
        self.requester: 'Reference' = requester 
        self.performerType: list['CodeableConcept'] = performerType or []
        self.owner: 'Reference' = owner 
        self.location: 'Reference' = location 
        self.reasonCode: 'CodeableConcept' = reasonCode 
        self.reasonReference: 'Reference' = reasonReference 
        self.insurance: list['Reference'] = insurance or []
        self.note: list['Annotation'] = note or []
        self.relevantHistory: list['Reference'] = relevantHistory or []
        self.restriction: 'Restriction' = restriction 
        self.input: list['Input'] = input or []
        self.output: list['Output'] = output or []
        