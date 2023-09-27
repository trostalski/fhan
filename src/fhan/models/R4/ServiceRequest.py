"""
Generated class for ServiceRequest. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Meta import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class ServiceRequest(DomainResource):
    """ A record of a request for service such as diagnostic investigations, treatments, or operations to be performed.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Identifiers assigned to this order
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param 'Reference' basedOn: What request fulfills
    :param 'Reference' replaces: What request replaces
    :param 'Identifier' requisition: Composite Request ID
    :param str status: draft | active | on-hold | revoked | completed | entered-in-error | unknown
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param 'CodeableConcept' category: Classification of service
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if service/procedure should not be performed
    :param 'CodeableConcept' code: What is being requested/ordered
    :param 'CodeableConcept' orderDetail: Additional order information
    :param 'Quantity' quantityQuantity: Service amount
    :param 'Ratio' quantityRatio: Service amount
    :param 'Range' quantityRange: Service amount
    :param 'Reference' subject: Individual or Entity the service is ordered for
    :param 'Reference' encounter: Encounter in which the request was created
    :param str occurrenceDateTime: When service should occur
    :param 'Period' occurrencePeriod: When service should occur
    :param 'Timing' occurrenceTiming: When service should occur
    :param bool asNeededBoolean: Preconditions for service
    :param 'CodeableConcept' asNeededCodeableConcept: Preconditions for service
    :param str authoredOn: Date request signed
    :param 'Reference' requester: Who/what is requesting service
    :param 'CodeableConcept' performerType: Performer role
    :param 'Reference' performer: Requested performer
    :param 'CodeableConcept' locationCode: Requested location
    :param 'Reference' locationReference: Requested location
    :param 'CodeableConcept' reasonCode: Explanation/Justification for procedure or service
    :param 'Reference' reasonReference: Explanation/Justification for service or service
    :param 'Reference' insurance: Associated insurance coverage
    :param 'Reference' supportingInfo: Additional clinical information
    :param 'Reference' specimen: Procedure Samples
    :param 'CodeableConcept' bodySite: Location on Body
    :param 'Annotation' note: Comments
    :param str patientInstruction: Patient or consumer-oriented instructions
    :param 'Reference' relevantHistory: Request provenance
    """
    def __init__(self, resourceType: str = "ServiceRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  instantiatesCanonical: str = None,  instantiatesUri: str = None,  basedOn: 'Reference' = None,  replaces: 'Reference' = None,  requisition: 'Identifier' = None,  status: str = None,  intent: str = None,  category: 'CodeableConcept' = None,  priority: str = None,  doNotPerform: bool = None,  code: 'CodeableConcept' = None,  orderDetail: 'CodeableConcept' = None,  quantityQuantity: 'Quantity' = None,  quantityRatio: 'Ratio' = None,  quantityRange: 'Range' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  asNeededBoolean: bool = None,  asNeededCodeableConcept: 'CodeableConcept' = None,  authoredOn: str = None,  requester: 'Reference' = None,  performerType: 'CodeableConcept' = None,  performer: 'Reference' = None,  locationCode: 'CodeableConcept' = None,  locationReference: 'Reference' = None,  reasonCode: 'CodeableConcept' = None,  reasonReference: 'Reference' = None,  insurance: 'Reference' = None,  supportingInfo: 'Reference' = None,  specimen: 'Reference' = None,  bodySite: 'CodeableConcept' = None,  note: 'Annotation' = None,  patientInstruction: str = None,  relevantHistory: 'Reference' = None, ):
        self.resourceType: str = resourceType or "ServiceRequest"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.instantiatesCanonical: list[str] = instantiatesCanonical or []
        self.instantiatesUri: list[str] = instantiatesUri or []
        self.basedOn: list['Reference'] = basedOn or []
        self.replaces: list['Reference'] = replaces or []
        self.requisition: 'Identifier' = requisition 
        self.status: str = status 
        self.intent: str = intent 
        self.category: list['CodeableConcept'] = category or []
        self.priority: str = priority 
        self.doNotPerform: bool = doNotPerform 
        self.code: 'CodeableConcept' = code 
        self.orderDetail: list['CodeableConcept'] = orderDetail or []
        self.quantityQuantity: 'Quantity' = quantityQuantity 
        self.quantityRatio: 'Ratio' = quantityRatio 
        self.quantityRange: 'Range' = quantityRange 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.asNeededBoolean: bool = asNeededBoolean 
        self.asNeededCodeableConcept: 'CodeableConcept' = asNeededCodeableConcept 
        self.authoredOn: str = authoredOn 
        self.requester: 'Reference' = requester 
        self.performerType: 'CodeableConcept' = performerType 
        self.performer: list['Reference'] = performer or []
        self.locationCode: list['CodeableConcept'] = locationCode or []
        self.locationReference: list['Reference'] = locationReference or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.insurance: list['Reference'] = insurance or []
        self.supportingInfo: list['Reference'] = supportingInfo or []
        self.specimen: list['Reference'] = specimen or []
        self.bodySite: list['CodeableConcept'] = bodySite or []
        self.note: list['Annotation'] = note or []
        self.patientInstruction: str = patientInstruction 
        self.relevantHistory: list['Reference'] = relevantHistory or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ServiceRequest":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance