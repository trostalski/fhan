"""
Generated class for VerificationResult. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Timing import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class PrimarySource(Element):
    """ Information about the primary source(s) involved in validation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference who: Reference to the primary source
    :param CodeableConcept type: Type of primary source (License Board; Primary Education; Continuing Education; Postal Service; Relationship owner; Registration Authority; legal source; issuing source; authoritative source)
    :param CodeableConcept communicationMethod: Method for exchanging information with the primary source
    :param CodeableConcept validationStatus: successful | failed | unknown
    :param str validationDate: When the target was validated against the primary source
    :param CodeableConcept canPushUpdates: yes | no | undetermined
    :param CodeableConcept pushTypeAvailable: specific | any | source
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    who: "Reference" = Reference()
    type: list[CodeableConcept] = CodeableConcept() 
    communicationMethod: list[CodeableConcept] = CodeableConcept() 
    validationStatus: "CodeableConcept" = CodeableConcept()
    
    validationDate: str = None
    canPushUpdates: "CodeableConcept" = CodeableConcept()
    pushTypeAvailable: list[CodeableConcept] = CodeableConcept() 
    

    
    
@dataclass
class Attestation(Element):
    """ Information about the entity attesting to information.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference who: The individual or organization attesting to information
    :param Reference onBehalfOf: When the who is asserting on behalf of another (organization or individual)
    :param CodeableConcept communicationMethod: The method by which attested information was submitted/retrieved
    :param str date: The date the information was attested to
    :param str sourceIdentityCertificate: A digital identity certificate associated with the attestation source
    :param str proxyIdentityCertificate: A digital identity certificate associated with the proxy entity submitting attested information on behalf of the attestation source
    :param Signature proxySignature: Proxy signature
    :param Signature sourceSignature: Attester signature
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    who: "Reference" = Reference()
    onBehalfOf: "Reference" = Reference()
    communicationMethod: "CodeableConcept" = CodeableConcept()
    
    date: str = None
    
    sourceIdentityCertificate: str = None
    
    proxyIdentityCertificate: str = None
    proxySignature: "Signature" = Signature()
    sourceSignature: "Signature" = Signature()
    

    
    
@dataclass
class Validator(Element):
    """ Information about the entity validating information.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference organization: Reference to the organization validating information
    :param str identityCertificate: A digital identity certificate associated with the validator
    :param Signature attestationSignature: Validator signature
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    organization: "Reference" = Reference()
    
    identityCertificate: str = None
    attestationSignature: "Signature" = Signature()
    

@dataclass
class VerificationResult(ModelBase):
    """ Describes validation requirements, source(s), status and dates for one or more elements.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference target: A resource that was validated
    :param str targetLocation: The fhirpath location(s) within the resource that was validated
    :param CodeableConcept need: none | initial | periodic
    :param str status: attested | validated | in-process | req-revalid | val-fail | reval-fail
    :param str statusDate: When the validation status was updated
    :param CodeableConcept validationType: nothing | primary | multiple
    :param CodeableConcept validationProcess: The primary process by which the target is validated (edit check; value set; primary source; multiple sources; standalone; in context)
    :param Timing frequency: Frequency of revalidation
    :param str lastPerformed: The date/time validation was last completed (including failed validations)
    :param str nextScheduled: The date when target is next validated, if appropriate
    :param CodeableConcept failureAction: fatal | warn | rec-only | none
    :param PrimarySource primarySource: Information about the primary source(s) involved in validation
    :param Attestation attestation: Information about the entity attesting to information
    :param Validator validator: Information about the entity validating information
    """

    resourceType: str = "VerificationResult"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    target: list[Reference] = Reference() 
    
    targetLocation: str = None
    
    need: "CodeableConcept" = CodeableConcept()
    
    status: str = None
    
    statusDate: str = None
    
    validationType: "CodeableConcept" = CodeableConcept()
    
    validationProcess: list[CodeableConcept] = CodeableConcept() 
    
    frequency: "Timing" = Timing()
    
    lastPerformed: str = None
    
    nextScheduled: str = None
    
    failureAction: "CodeableConcept" = CodeableConcept()
    
    primarySource: list[PrimarySource] = PrimarySource() 
    
    attestation: "Attestation" = Attestation()
    
    validator: list[Validator] = Validator() 
    