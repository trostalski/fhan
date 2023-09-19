"""
Generated class for ServiceRequest. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class ServiceRequest:
    """ A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers assigned to this order
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param Reference basedOn: What request fulfills
    :param Reference replaces: What request replaces
    :param Identifier requisition: Composite Request ID
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order +
    :param CodeableConcept category: Classification of service
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if service/procedure should not be performed
    :param CodeableReference code: What is being requested/ordered
    :param BackboneElement orderDetail: Additional order information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference parameterFocus: The context of the order details by reference
    :param BackboneElement parameter: The parameter details for the service being requested
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The detail of the order being requested
    :param Quantity valueQuantity: The value for the order detail
    :param Ratio valueQuantity: The value for the order detail
    :param Range valueQuantity: The value for the order detail
    :param bool valueQuantity: The value for the order detail
    :param CodeableConcept valueQuantity: The value for the order detail
    :param str valueQuantity: The value for the order detail
    :param Period valueQuantity: The value for the order detail
    :param Quantity quantityQuantity: Service amount
    :param Ratio quantityQuantity: Service amount
    :param Range quantityQuantity: Service amount
    :param Reference subject: Individual or Entity the service is ordered for
    :param Reference focus: What the service request is about, when it is not about the subject of record
    :param Reference encounter: Encounter in which the request was created
    :param str occurrencedateTime: When service should occur
    :param Period occurrencedateTime: When service should occur
    :param Timing occurrencedateTime: When service should occur
    :param bool asNeededboolean: Preconditions for service
    :param CodeableConcept asNeededboolean: Preconditions for service
    :param str authoredOn: Date request signed
    :param Reference requester: Who/what is requesting service
    :param CodeableConcept performerType: Performer role
    :param Reference performer: Requested performer
    :param CodeableReference location: Requested location
    :param CodeableReference reason: Explanation/Justification for procedure or service
    :param Reference insurance: Associated insurance coverage
    :param CodeableReference supportingInfo: Additional clinical information
    :param Reference specimen: Procedure Samples
    :param CodeableConcept bodySite: Coded location on Body
    :param Reference bodyStructure: BodyStructure-based location on the body
    :param Annotation note: Comments
    :param BackboneElement patientInstruction: Patient or consumer-oriented instructions
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str instructionmarkdown: Patient or consumer-oriented instructions
    :param Reference instructionmarkdown: Patient or consumer-oriented instructions
    :param Reference relevantHistory: Request provenance
    
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: "Reference" = None
    
    replaces: "Reference" = None
    
    requisition: "Identifier" = None
    
    status: str = None
    
    intent: str = None
    
    category: "CodeableConcept" = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    code: "CodeableReference" = None
    
    orderDetail: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    parameterFocus: "CodeableReference" = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "Ratio" = None
    
    valueQuantity: "Range" = None
    
    valueQuantity: bool = None
    
    valueQuantity: "CodeableConcept" = None
    
    valueQuantity: str = None
    
    valueQuantity: "Period" = None
    
    quantityQuantity: "Quantity" = None
    
    quantityQuantity: "Ratio" = None
    
    quantityQuantity: "Range" = None
    
    subject: "Reference" = None
    
    focus: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    asNeededboolean: bool = None
    
    asNeededboolean: "CodeableConcept" = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    performer: "Reference" = None
    
    location: "CodeableReference" = None
    
    reason: "CodeableReference" = None
    
    insurance: "Reference" = None
    
    supportingInfo: "CodeableReference" = None
    
    specimen: "Reference" = None
    
    bodySite: "CodeableConcept" = None
    
    bodyStructure: "Reference" = None
    
    note: "Annotation" = None
    
    patientInstruction: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    instructionmarkdown: str = None
    
    instructionmarkdown: "Reference" = None
    
    relevantHistory: "Reference" = None
    