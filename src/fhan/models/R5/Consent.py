"""
Generated class for Consent. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Expression import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Consent:
    """ A record of a healthcare consumer’s  choices  or choices made on their behalf by a third party, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier for this record (external references)
    :param str status: draft | active | inactive | not-done | entered-in-error | unknown
    :param CodeableConcept category: Classification of the consent statement - for indexing/retrieval
    :param Reference subject: Who the consent applies to
    :param str date: Fully executed date of the consent
    :param Period period: Effective period for this Consent
    :param Reference grantor: Who is granting rights according to the policy and rules
    :param Reference grantee: Who is agreeing to the policy and rules
    :param Reference manager: Consent workflow management
    :param Reference controller: Consent Enforcer
    :param Attachment sourceAttachment: Source from which this consent is taken
    :param Reference sourceReference: Source from which this consent is taken
    :param CodeableConcept regulatoryBasis: Regulations establishing base Consent
    :param BackboneElement policyBasis: Computable version of the backing policy
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference reference: Reference backing policy resource
    :param str url: URL to a computable backing policy
    :param Reference policyText: Human Readable Policy
    :param BackboneElement verification: Consent Verified by patient or family
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool verified: Has been verified
    :param CodeableConcept verificationType: Business case of verification
    :param Reference verifiedBy: Person conducting verification
    :param Reference verifiedWith: Person who verified
    :param str verificationDate: When consent verified
    :param str decision: deny | permit
    :param BackboneElement provision: Constraints to the base Consent.policyRule/Consent.policy
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period period: Timeframe for this provision
    :param BackboneElement actor: Who|what controlled by this provision (or group, by role)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: How the actor is involved
    :param Reference reference: Resource for the actor (or group, by role)
    :param CodeableConcept action: Actions controlled by this provision
    :param Coding securityLabel: Security Labels that define affected resources
    :param Coding purpose: Context of activities covered by this provision
    :param Coding documentType: e.g. Resource Type, Profile, CDA, etc
    :param Coding resourceType: e.g. Resource Type, Profile, etc
    :param CodeableConcept code: e.g. LOINC or SNOMED CT code, etc. in the content
    :param Period dataPeriod: Timeframe for data controlled by this provision
    :param BackboneElement data: Data controlled by this provision
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str meaning: instance | related | dependents | authoredby
    :param Reference reference: The actual data reference
    :param Expression expression: A computable expression of the consent
    :param BackboneElement provision: Constraints to the base Consent.policyRule/Consent.policy
    
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
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    date: str = None
    
    period: "Period" = None
    
    grantor: "Reference" = None
    
    grantee: "Reference" = None
    
    manager: "Reference" = None
    
    controller: "Reference" = None
    
    sourceAttachment: "Attachment" = None
    
    sourceReference: "Reference" = None
    
    regulatoryBasis: "CodeableConcept" = None
    
    policyBasis: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: "Reference" = None
    
    url: str = None
    
    policyText: "Reference" = None
    
    verification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    verified: bool = None
    
    verificationType: "CodeableConcept" = None
    
    verifiedBy: "Reference" = None
    
    verifiedWith: "Reference" = None
    
    verificationDate: str = None
    
    decision: str = None
    
    provision: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
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
    
    documentType: "Coding" = None
    
    resourceType: "Coding" = None
    
    code: "CodeableConcept" = None
    
    dataPeriod: "Period" = None
    
    data: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    meaning: str = None
    
    reference: "Reference" = None
    
    expression: "Expression" = None
    
    provision: "BackboneElement" = None
    