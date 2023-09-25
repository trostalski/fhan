"""
Generated class for DeviceRequest. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Range import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Timing import *
from fhan.models.R4.DomainResource import *


    
    

class Parameter(ModelBase):
    """ Specific parameters for the ordered item.  For example, the prism value for lenses.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Device detail
    :param 'CodeableConcept' valueCodeableConcept: Value of detail
    :param 'Quantity' valueQuantity: Value of detail
    :param 'Range' valueRange: Value of detail
    :param bool valueBoolean: Value of detail
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueBoolean: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueRange: 'Range' = valueRange 
        self.valueBoolean: bool = valueBoolean 
        

class DeviceRequest(DomainResource):
    """ Represents a request for a patient to employ a medical device. The device may be an implantable device, or an external assistive device, such as a walker.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Request identifier
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param list['Reference'] basedOn: What request fulfills
    :param list['Reference'] priorRequest: What request replaces
    :param 'Identifier' groupIdentifier: Identifier of composite request
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param 'Reference' codeReference: Device requested
    :param 'CodeableConcept' codeCodeableConcept: Device requested
    :param list['Parameter'] parameter: Device details
    :param 'Reference' subject: Focus of request
    :param 'Reference' encounter: Encounter motivating request
    :param str occurrenceDateTime: Desired time or schedule for use
    :param 'Period' occurrencePeriod: Desired time or schedule for use
    :param 'Timing' occurrenceTiming: Desired time or schedule for use
    :param str authoredOn: When recorded
    :param 'Reference' requester: Who/what is requesting diagnostics
    :param 'CodeableConcept' performerType: Filler role
    :param 'Reference' performer: Requested Filler
    :param list['CodeableConcept'] reasonCode: Coded Reason for request
    :param list['Reference'] reasonReference: Linked Reason for request
    :param list['Reference'] insurance: Associated insurance coverage
    :param list['Reference'] supportingInfo: Additional clinical information
    :param list['Annotation'] note: Notes or comments
    :param list['Reference'] relevantHistory: Request provenance
    """
    def __init__(self, resourceType: str = "DeviceRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: list['Reference'] = None,  priorRequest: list['Reference'] = None,  groupIdentifier: 'Identifier' = None,  status: str = None,  intent: str = None,  priority: str = None,  codeReference: 'Reference' = None,  codeCodeableConcept: 'CodeableConcept' = None,  parameter: list['Parameter'] = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  authoredOn: str = None,  requester: 'Reference' = None,  performerType: 'CodeableConcept' = None,  performer: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  insurance: list['Reference'] = None,  supportingInfo: list['Reference'] = None,  note: list['Annotation'] = None,  relevantHistory: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "DeviceRequest"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: str = instantiatesCanonical or []
        self.instantiatesUri: str = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.priorRequest: list['Reference'] = priorRequest or []
        self.groupIdentifier: 'Identifier' = groupIdentifier 
        self.status: str = status 
        self.intent: str = intent 
        self.priority: str = priority 
        self.codeReference: 'Reference' = codeReference 
        self.codeCodeableConcept: 'CodeableConcept' = codeCodeableConcept 
        self.parameter: list['Parameter'] = parameter or []
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.authoredOn: str = authoredOn 
        self.requester: 'Reference' = requester 
        self.performerType: 'CodeableConcept' = performerType 
        self.performer: 'Reference' = performer 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.insurance: list['Reference'] = insurance or []
        self.supportingInfo: list['Reference'] = supportingInfo or []
        self.note: list['Annotation'] = note or []
        self.relevantHistory: list['Reference'] = relevantHistory or []
        