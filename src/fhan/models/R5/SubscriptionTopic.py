"""
Generated class for SubscriptionTopic. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class QueryCriteria(BaseModel):
    """ The FHIR query based rules that the server should use to determine when to trigger a notification for this subscription topic.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str previous: Rule applied to previous resource state
    :param str resultForCreate: test-passes | test-fails
    :param str current: Rule applied to current resource state
    :param str resultForDelete: test-passes | test-fails
    :param bool requireBoth: Both must be true flag
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  previous:  'str'  = None,  resultForCreate:  'str'  = None,  current:  'str'  = None,  resultForDelete:  'str'  = None,  requireBoth:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.previous = previous 
        self.resultForCreate = resultForCreate 
        self.current = current 
        self.resultForDelete = resultForDelete 
        self.requireBoth = requireBoth 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionTopic":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionTopic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class ResourceTrigger(BaseModel):
    """ A definition of a resource-based event that triggers a notification based on the SubscriptionTopic. The criteria may be just a human readable description and/or a full FHIR search string or FHIRPath expression. Multiple triggers are considered OR joined (e.g., a resource update matching ANY of the definitions will trigger a notification).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Text representation of the resource trigger
    :param str resource: Data Type or Resource (reference to definition) for this trigger definition
    :param str supportedInteraction: create | update | delete
    :param QueryCriteria queryCriteria: Query based trigger rule
    :param str fhirPathCriteria: FHIRPath based trigger rule
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        "queryCriteria": {"class_name": "QueryCriteria", "is_contained": True},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  resource:  'str'  = None,  supportedInteraction:  list['str']  = None,  queryCriteria:  'QueryCriteria'  = None,  fhirPathCriteria:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.resource = resource 
        self.supportedInteraction = supportedInteraction or []
        self.queryCriteria = queryCriteria 
        self.fhirPathCriteria = fhirPathCriteria 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionTopic":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionTopic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class EventTrigger(BaseModel):
    """ Event definition which can be used to trigger the SubscriptionTopic.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Text representation of the event trigger
    :param CodeableConcept event: Event which can trigger a notification from the SubscriptionTopic
    :param str resource: Data Type or Resource (reference to definition) for this trigger definition
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "event": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  event:  'CodeableConcept'  = None,  resource:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.event = event 
        self.resource = resource 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionTopic":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionTopic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class CanFilterBy(BaseModel):
    """ List of properties by which Subscriptions on the SubscriptionTopic can be filtered. May be defined Search Parameters (e.g., Encounter.patient) or parameters defined within this SubscriptionTopic context (e.g., hub.event).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of this filter parameter
    :param str resource: URL of the triggering Resource that this filter applies to
    :param str filterParameter: Human-readable and computation-friendly name for a filter parameter usable by subscriptions on this topic, via Subscription.filterBy.filterParameter
    :param str filterDefinition: Canonical URL for a filterParameter definition
    :param str comparator: eq | ne | gt | lt | ge | le | sa | eb | ap
    :param str modifier: missing | exact | contains | not | text | in | not-in | below | above | type | identifier | of-type | code-text | text-advanced | iterate
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  resource:  'str'  = None,  filterParameter:  'str'  = None,  filterDefinition:  'str'  = None,  comparator:  list['str']  = None,  modifier:  list['str']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.resource = resource 
        self.filterParameter = filterParameter 
        self.filterDefinition = filterDefinition 
        self.comparator = comparator or []
        self.modifier = modifier or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionTopic":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionTopic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class NotificationShape(BaseModel):
    """ List of properties to describe the shape (e.g., resources) included in notifications from this Subscription Topic.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resource: URL of the Resource that is the focus (main) resource in a notification shape
    :param str include: Include directives, rooted in the resource for this shape
    :param str revInclude: Reverse include directives, rooted in the resource for this shape
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  resource:  'str'  = None,  include:  list['str']  = None,  revInclude:  list['str']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.resource = resource 
        self.include = include or []
        self.revInclude = revInclude or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionTopic":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionTopic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubscriptionTopic(DomainResource):
    """ Describes a stream of resource state changes identified by trigger criteria and annotated with labels useful to filter projections from this topic.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this subscription topic, represented as an absolute URI (globally unique)
    :param Identifier identifier: Business identifier for subscription topic
    :param str version: Business version of the subscription topic
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this subscription topic (computer friendly)
    :param str title: Name for this subscription topic (human friendly)
    :param str derivedFrom: Based on FHIR protocol or definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: If for testing purposes, not real usage
    :param str date: Date status first applied
    :param str publisher: The name of the individual or organization that published the SubscriptionTopic
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the SubscriptionTopic
    :param UsageContext useContext: Content intends to support these contexts
    :param CodeableConcept jurisdiction: Intended jurisdiction of the SubscriptionTopic (if applicable)
    :param str purpose: Why this SubscriptionTopic is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When SubscriptionTopic is/was approved by publisher
    :param str lastReviewDate: Date the Subscription Topic was last reviewed by the publisher
    :param Period effectivePeriod: The effective date range for the SubscriptionTopic
    :param ResourceTrigger resourceTrigger: Definition of a resource-based trigger for the subscription topic
    :param EventTrigger eventTrigger: Event definitions the SubscriptionTopic
    :param CanFilterBy canFilterBy: Properties by which a Subscription can filter notifications from the SubscriptionTopic
    :param NotificationShape notificationShape: Properties for describing the shape of notifications generated by this topic
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
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "resourceTrigger": {"class_name": "ResourceTrigger", "is_contained": True},
        
        
        "eventTrigger": {"class_name": "EventTrigger", "is_contained": True},
        
        
        "canFilterBy": {"class_name": "CanFilterBy", "is_contained": True},
        
        
        "notificationShape": {"class_name": "NotificationShape", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  derivedFrom:  list['str']  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  resourceTrigger:  list['ResourceTrigger']  = None,  eventTrigger:  list['EventTrigger']  = None,  canFilterBy:  list['CanFilterBy']  = None,  notificationShape:  list['NotificationShape']  = None, ):
        self.resourceType = resourceType or "SubscriptionTopic"
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
        self.derivedFrom = derivedFrom or []
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
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.resourceTrigger = resourceTrigger or []
        self.eventTrigger = eventTrigger or []
        self.canFilterBy = canFilterBy or []
        self.notificationShape = notificationShape or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubscriptionTopic":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubscriptionTopic":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()