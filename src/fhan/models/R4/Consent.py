"""
Generated class for Consent. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Coding import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Policy(ModelBase):
    """ The references to the policies that are included in this consent scope. Policies may be organizational, but are often defined jurisdictionally, or in law.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str authority: Enforcement source for policy
    :param str uri: Specific policy covered by this consent
    :param 'CodeableConcept' policyRule: Regulation that this consents to
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  authority: str = None,  uri: str = None,  policyRule: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.authority: str = authority 
        self.uri: str = uri 
        self.policyRule: 'CodeableConcept' = policyRule 
        

    
    

class Verification(ModelBase):
    """ Whether a treatment instruction (e.g. artificial respiration yes or no) was verified with the patient, his/her family or another authorized person.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool verified: Has been verified
    :param 'Reference' verifiedWith: Person who verified
    :param str verificationDate: When consent verified
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  verified: bool = None,  verifiedWith: 'Reference' = None,  verificationDate: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.verified: bool = verified 
        self.verifiedWith: 'Reference' = verifiedWith 
        self.verificationDate: str = verificationDate 
        

    
        
    
    

class Actor(ModelBase):
    """ Who or what is controlled by this rule. Use group to identify a set of actors by some property they share (e.g. 'admitting officers').:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' role: How the actor is involved
    :param 'Reference' reference: Resource for the actor (or group, by role)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  role: 'CodeableConcept' = None,  reference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.role: 'CodeableConcept' = role 
        self.reference: 'Reference' = reference 
        

    
    

class Data(ModelBase):
    """ The resources controlled by this rule if specific resources are referenced.:param 'Period' dataPeriod: Timeframe for data controlled by this rule
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str meaning: instance | related | dependents | authoredby
    :param 'Reference' reference: The actual data reference
    """
    def __init__(self,  dataPeriod: 'Period' = None,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  meaning: str = None,  reference: 'Reference' = None, ):
        self.dataPeriod: 'Period' = dataPeriod 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.meaning: str = meaning 
        self.reference: 'Reference' = reference 
        

  
    
    

class Provision(ModelBase):
    """ An exception to the base policy of this consent. An exception can be an addition or removal of access permissions.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: deny | permit
    :param 'Period' period: Timeframe for this rule
    :param list['Actor'] actor: Who|what controlled by this rule (or group, by role)
    :param list['CodeableConcept'] action: Actions controlled by this rule
    :param list['Coding'] securityLabel: Security Labels that define affected resources
    :param list['Coding'] purpose: Context of activities covered by this rule
    :param list['Coding'] _class: e.g. Resource Type, Profile, CDA, etc.
    :param list['CodeableConcept'] code: e.g. LOINC or SNOMED CT code, etc. in the content
    :param 'Period' dataPeriod: Timeframe for data controlled by this rule
    :param list['Data'] data: Data controlled by this rule
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  period: 'Period' = None,  actor: list['Actor'] = None,  action: list['CodeableConcept'] = None,  securityLabel: list['Coding'] = None,  purpose: list['Coding'] = None,  _class: list['Coding'] = None,  code: list['CodeableConcept'] = None,  dataPeriod: 'Period' = None,  data: list['Data'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.period: 'Period' = period 
        self.actor: list['Actor'] = actor or []
        self.action: list['CodeableConcept'] = action or []
        self.securityLabel: list['Coding'] = securityLabel or []
        self.purpose: list['Coding'] = purpose or []
        self._class: list['Coding'] = _class or []
        self.code: list['CodeableConcept'] = code or []
        self.dataPeriod: 'Period' = dataPeriod 
        self.data: list['Data'] = data or []
        

class Consent(DomainResource):
    """ A record of a healthcare consumer’s  choices, which permits or denies identified recipient(s) or recipient role(s) to perform one or more actions within a given policy context, for specific purposes and periods of time.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Identifier for this record (external references)
    :param str status: draft | proposed | active | rejected | inactive | entered-in-error
    :param 'CodeableConcept' scope: Which of the four areas this resource covers (extensible)
    :param list['CodeableConcept'] category: Classification of the consent statement - for indexing/retrieval
    :param 'Reference' patient: Who the consent applies to
    :param str dateTime: When this Consent was created or indexed
    :param list['Reference'] performer: Who is agreeing to the policy and rules
    :param list['Reference'] organization: Custodian of the consent
    :param 'Attachment' sourceAttachment: Source from which this consent is taken
    :param list['Policy'] policy: Policies covered by this consent
    :param list['Verification'] verification: Consent Verified by patient or family
    :param 'Provision' provision: Constraints to the base Consent.policyRule
    """
    def __init__(self, resourceType: str = "Consent",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  scope: 'CodeableConcept' = None,  category: list['CodeableConcept'] = None,  patient: 'Reference' = None,  dateTime: str = None,  performer: list['Reference'] = None,  organization: list['Reference'] = None,  sourceAttachment: 'Attachment' = None,  policy: list['Policy'] = None,  verification: list['Verification'] = None,  provision: 'Provision' = None, ):
        self.resourceType: str = resourceType or "Consent"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.scope: 'CodeableConcept' = scope 
        self.category: list['CodeableConcept'] = category or []
        self.patient: 'Reference' = patient 
        self.dateTime: str = dateTime 
        self.performer: list['Reference'] = performer or []
        self.organization: list['Reference'] = organization or []
        self.sourceAttachment: 'Attachment' = sourceAttachment 
        self.policy: list['Policy'] = policy or []
        self.verification: list['Verification'] = verification or []
        self.provision: 'Provision' = provision 
        