"""
Generated class for ServiceRequest. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Range import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase
@dataclass
class ServiceRequest(ModelBase):
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
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param CodeableConcept category: Classification of service
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if service/procedure should not be performed
    :param CodeableConcept code: What is being requested/ordered
    :param CodeableConcept orderDetail: Additional order information
    :param Quantity quantityQuantity: Service amount
    :param Reference subject: Individual or Entity the service is ordered for
    :param Reference encounter: Encounter in which the request was created
    :param str occurrenceDateTime: When service should occur
    :param bool asNeededBoolean: Preconditions for service
    :param str authoredOn: Date request signed
    :param Reference requester: Who/what is requesting service
    :param CodeableConcept performerType: Performer role
    :param Reference performer: Requested performer
    :param CodeableConcept locationCode: Requested location
    :param Reference locationReference: Requested location
    :param CodeableConcept reasonCode: Explanation/Justification for procedure or service
    :param Reference reasonReference: Explanation/Justification for service or service
    :param Reference insurance: Associated insurance coverage
    :param Reference supportingInfo: Additional clinical information
    :param Reference specimen: Procedure Samples
    :param CodeableConcept bodySite: Location on Body
    :param Annotation note: Comments
    :param str patientInstruction: Patient or consumer-oriented instructions
    :param Reference relevantHistory: Request provenance
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    basedOn: list["Reference"] = None
    
    replaces: list["Reference"] = None
    
    requisition: "Identifier" = None
    
    status: str = None
    
    intent: str = None
    
    category: list["CodeableConcept"] = None
    
    priority: str = None
    
    doNotPerform: bool = None
    
    code: "CodeableConcept" = None
    
    orderDetail: list["CodeableConcept"] = None
    
    quantityQuantity: "Quantity" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrenceDateTime: str = None
    
    asNeededBoolean: bool = None
    
    authoredOn: str = None
    
    requester: "Reference" = None
    
    performerType: "CodeableConcept" = None
    
    performer: list["Reference"] = None
    
    locationCode: list["CodeableConcept"] = None
    
    locationReference: list["Reference"] = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    insurance: list["Reference"] = None
    
    supportingInfo: list["Reference"] = None
    
    specimen: list["Reference"] = None
    
    bodySite: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    
    patientInstruction: str = None
    
    relevantHistory: list["Reference"] = None
    