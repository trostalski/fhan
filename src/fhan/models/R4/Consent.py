"""
Generated class for Consent. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Consent(ModelBase):
    """ A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier for this record (external references)
    :param str status: draft | proposed | active | rejected | inactive | entered-in-error
    :param CodeableConcept scope: Which of the four areas this resource covers (extensible)
    :param CodeableConcept category: Classification of the consent statement - for indexing/retrieval
    :param Reference patient: Who the consent applies to
    :param str dateTime: When this Consent was created or indexed
    :param Reference performer: Who is agreeing to the policy and rules
    :param Reference organization: Custodian of the consent
    :param Attachment sourceAttachment: Source from which this consent is taken
    :param Reference sourceAttachment: Source from which this consent is taken
    :param BackboneElement policy: Policies covered by this consent
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str authority: Enforcement source for policy
    :param str uri: Specific policy covered by this consent
    :param CodeableConcept policyRule: Regulation that this consents to
    :param BackboneElement verification: Consent Verified by patient or family
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool verified: Has been verified
    :param Reference verifiedWith: Person who verified
    :param str verificationDate: When consent verified
    :param BackboneElement provision: Constraints to the base Consent.policyRule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: deny | permit
    :param Period period: Timeframe for this rule
    :param BackboneElement actor: Who|what controlled by this rule (or group, by role)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: How the actor is involved
    :param Reference reference: Resource for the actor (or group, by role)
    :param CodeableConcept action: Actions controlled by this rule
    :param Coding securityLabel: Security Labels that define affected resources
    :param Coding purpose: Context of activities covered by this rule
    :param Coding _class: e.g. Resource Type, Profile, CDA, etc.
    :param CodeableConcept code: e.g. LOINC or SNOMED CT code, etc. in the content
    :param Period dataPeriod: Timeframe for data controlled by this rule
    :param BackboneElement data: Data controlled by this rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str meaning: instance | related | dependents | authoredby
    :param Reference reference: The actual data reference
    :param BackboneElement provision: Constraints to the base Consent.policyRule
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    scope: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    dateTime: str = None
    
    performer: "Reference" = None
    
    organization: "Reference" = None
    
    sourceAttachment: "Attachment" = None
    
    sourceAttachment: "Reference" = None
    
    policy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    authority: str = None
    
    uri: str = None
    
    policyRule: "CodeableConcept" = None
    
    verification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    verified: bool = None
    
    verifiedWith: "Reference" = None
    
    verificationDate: str = None
    
    provision: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    period: "Period" = None
    
    actor: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    reference: "Reference" = None
    
    action: "CodeableConcept" = None
    
    securityLabel: "Coding" = None
    
    purpose: "Coding" = None
    
    _class: "Coding" = None
    
    code: "CodeableConcept" = None
    
    dataPeriod: "Period" = None
    
    data: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    meaning: str = None
    
    reference: "Reference" = None
    
    provision: "BackboneElement" = None
    