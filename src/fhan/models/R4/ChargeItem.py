"""
Generated class for ChargeItem. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Money import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Performer(ModelBase):
    """ Indicates who or what performed or participated in the charged service.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' function: What type of performance was done
    :param 'Reference' actor: Individual who was performing
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  function: 'CodeableConcept' = None,  actor: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.function: 'CodeableConcept' = function 
        self.actor: 'Reference' = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Performer":
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
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
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


class ChargeItem(DomainResource):
    """ The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for item
    :param str definitionUri: Defining information about the code of this charge item
    :param str definitionCanonical: Resource defining the code of this ChargeItem
    :param str status: planned | billable | not-billable | aborted | billed | entered-in-error | unknown
    :param list['Reference'] partOf: Part of referenced ChargeItem
    :param 'CodeableConcept' code: A code that identifies the charge, like a billing code
    :param 'Reference' subject: Individual service was done for/to
    :param 'Reference' context: Encounter / Episode associated with event
    :param str occurrenceDateTime: When the charged service was applied
    :param 'Period' occurrencePeriod: When the charged service was applied
    :param 'Timing' occurrenceTiming: When the charged service was applied
    :param list['Performer'] performer: Who performed charged service
    :param 'Reference' performingOrganization: Organization providing the charged service
    :param 'Reference' requestingOrganization: Organization requesting the charged service
    :param 'Reference' costCenter: Organization that has ownership of the (potential, future) revenue
    :param 'Quantity' quantity: Quantity of which the charge item has been serviced
    :param list['CodeableConcept'] bodysite: Anatomical location, if relevant
    :param float factorOverride: Factor overriding the associated rules
    :param 'Money' priceOverride: Price overriding the associated rules
    :param str overrideReason: Reason for overriding the list price/factor
    :param 'Reference' enterer: Individual who was entering
    :param str enteredDate: Date the charge item was entered
    :param list['CodeableConcept'] reason: Why was the charged  service rendered?
    :param list['Reference'] service: Which rendered service is being charged?
    :param 'Reference' productReference: Product charged
    :param 'CodeableConcept' productCodeableConcept: Product charged
    :param list['Reference'] account: Account to place this charge
    :param list['Annotation'] note: Comments made about the ChargeItem
    :param list['Reference'] supportingInformation: Further information supporting this charge
    """
    def __init__(self, resourceType: str = "ChargeItem",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  definitionUri: str = None,  definitionCanonical: str = None,  status: str = None,  partOf: list['Reference'] = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  context: 'Reference' = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  performer: list['Performer'] = None,  performingOrganization: 'Reference' = None,  requestingOrganization: 'Reference' = None,  costCenter: 'Reference' = None,  quantity: 'Quantity' = None,  bodysite: list['CodeableConcept'] = None,  factorOverride: float = None,  priceOverride: 'Money' = None,  overrideReason: str = None,  enterer: 'Reference' = None,  enteredDate: str = None,  reason: list['CodeableConcept'] = None,  service: list['Reference'] = None,  productReference: 'Reference' = None,  productCodeableConcept: 'CodeableConcept' = None,  account: list['Reference'] = None,  note: list['Annotation'] = None,  supportingInformation: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "ChargeItem"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.definitionUri: str = definitionUri or []
        self.definitionCanonical: str = definitionCanonical or []
        self.status: str = status 
        self.partOf: list['Reference'] = partOf or []
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.context: 'Reference' = context 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.performer: list['Performer'] = performer or []
        self.performingOrganization: 'Reference' = performingOrganization 
        self.requestingOrganization: 'Reference' = requestingOrganization 
        self.costCenter: 'Reference' = costCenter 
        self.quantity: 'Quantity' = quantity 
        self.bodysite: list['CodeableConcept'] = bodysite or []
        self.factorOverride: float = factorOverride 
        self.priceOverride: 'Money' = priceOverride 
        self.overrideReason: str = overrideReason 
        self.enterer: 'Reference' = enterer 
        self.enteredDate: str = enteredDate 
        self.reason: list['CodeableConcept'] = reason or []
        self.service: list['Reference'] = service or []
        self.productReference: 'Reference' = productReference 
        self.productCodeableConcept: 'CodeableConcept' = productCodeableConcept 
        self.account: list['Reference'] = account or []
        self.note: list['Annotation'] = note or []
        self.supportingInformation: list['Reference'] = supportingInformation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ChargeItem":
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
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
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