"""
Generated class for SubscriptionTopic. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *


@dataclass
class SubscriptionTopic:
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
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
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
    :param BackboneElement resourceTrigger: Definition of a resource-based trigger for the subscription topic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Text representation of the resource trigger
    :param str resource: Data Type or Resource (reference to definition) for this trigger definition
    :param str supportedInteraction: create | update | delete
    :param BackboneElement queryCriteria: Query based trigger rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str previous: Rule applied to previous resource state
    :param str resultForCreate: test-passes | test-fails
    :param str current: Rule applied to current resource state
    :param str resultForDelete: test-passes | test-fails
    :param bool requireBoth: Both must be true flag
    :param str fhirPathCriteria: FHIRPath based trigger rule
    :param BackboneElement eventTrigger: Event definitions the SubscriptionTopic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Text representation of the event trigger
    :param CodeableConcept event: Event which can trigger a notification from the SubscriptionTopic
    :param str resource: Data Type or Resource (reference to definition) for this trigger definition
    :param BackboneElement canFilterBy: Properties by which a Subscription can filter notifications from the SubscriptionTopic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of this filter parameter
    :param str resource: URL of the triggering Resource that this filter applies to
    :param str filterParameter: Human-readable and computation-friendly name for a filter parameter usable by subscriptions on this topic, via Subscription.filterBy.filterParameter
    :param str filterDefinition: Canonical URL for a filterParameter definition
    :param str comparator: eq | ne | gt | lt | ge | le | sa | eb | ap
    :param str modifier: missing | exact | contains | not | text | in | not-in | below | above | type | identifier | of-type | code-text | text-advanced | iterate
    :param BackboneElement notificationShape: Properties for describing the shape of notifications generated by this topic
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resource: URL of the Resource that is the focus (main) resource in a notification shape
    :param str include: Include directives, rooted in the resource for this shape
    :param str revInclude: Reverse include directives, rooted in the resource for this shape
    
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
    
    copyrightLabel: str = None
    
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
    
    comparator: str = None
    
    modifier: str = None
    
    notificationShape: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    resource: str = None
    
    include: str = None
    
    revInclude: str = None
    