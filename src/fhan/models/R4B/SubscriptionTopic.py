"""
Generated class for SubscriptionTopic. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *


@dataclass
class SubscriptionTopic:
    """
    Describes a stream of resource state changes identified by trigger criteria and annotated with labels useful to filter projections from this topic.
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
    
    title: str = None
    
    derivedFrom: str = None
    
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
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    resourceTrigger: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    resource: str = None
    
    supportedInteraction: str = None
    
    queryCriteria: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    previous: str = None
    
    resultForCreate: str = None
    
    current: str = None
    
    resultForDelete: str = None
    
    requireBoth: bool = None
    
    fhirPathCriteria: str = None
    
    eventTrigger: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    event: "CodeableConcept" = None
    
    resource: str = None
    
    canFilterBy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    resource: str = None
    
    filterParameter: str = None
    
    filterDefinition: str = None
    
    modifier: str = None
    
    notificationShape: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    resource: str = None
    
    include: str = None
    
    revInclude: str = None
    