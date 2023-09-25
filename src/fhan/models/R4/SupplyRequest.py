"""
Generated class for SupplyRequest. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Parameter(ModelBase):
    """ Specific parameters for the ordered item.  For example, the size of the indicated item.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Item detail
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
        

    @classmethod
    def from_dict(cls, data: dict) -> "Parameter":
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


class SupplyRequest(DomainResource):
    """ A record of a request for a medication, substance or device used in the healthcare setting.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for SupplyRequest
    :param str status: draft | active | suspended +
    :param 'CodeableConcept' category: The kind of supply (central, non-stock, etc.)
    :param str priority: routine | urgent | asap | stat
    :param 'CodeableConcept' itemCodeableConcept: Medication, Substance, or Device requested to be supplied
    :param 'Reference' itemReference: Medication, Substance, or Device requested to be supplied
    :param 'Quantity' quantity: The requested amount of the item indicated
    :param list['Parameter'] parameter: Ordered item details
    :param str occurrenceDateTime: When the request should be fulfilled
    :param 'Period' occurrencePeriod: When the request should be fulfilled
    :param 'Timing' occurrenceTiming: When the request should be fulfilled
    :param str authoredOn: When the request was made
    :param 'Reference' requester: Individual making the request
    :param list['Reference'] supplier: Who is intended to fulfill the request
    :param list['CodeableConcept'] reasonCode: The reason why the supply item was requested
    :param list['Reference'] reasonReference: The reason why the supply item was requested
    :param 'Reference' deliverFrom: The origin of the supply
    :param 'Reference' deliverTo: The destination of the supply
    """
    def __init__(self, resourceType: str = "SupplyRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  category: 'CodeableConcept' = None,  priority: str = None,  itemCodeableConcept: 'CodeableConcept' = None,  itemReference: 'Reference' = None,  quantity: 'Quantity' = None,  parameter: list['Parameter'] = None,  occurrenceDateTime: str = None,  occurrencePeriod: 'Period' = None,  occurrenceTiming: 'Timing' = None,  authoredOn: str = None,  requester: 'Reference' = None,  supplier: list['Reference'] = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  deliverFrom: 'Reference' = None,  deliverTo: 'Reference' = None, ):
        self.resourceType: str = resourceType or "SupplyRequest"
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
        self.category: 'CodeableConcept' = category 
        self.priority: str = priority 
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.itemReference: 'Reference' = itemReference 
        self.quantity: 'Quantity' = quantity 
        self.parameter: list['Parameter'] = parameter or []
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrencePeriod: 'Period' = occurrencePeriod 
        self.occurrenceTiming: 'Timing' = occurrenceTiming 
        self.authoredOn: str = authoredOn 
        self.requester: 'Reference' = requester 
        self.supplier: list['Reference'] = supplier or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.deliverFrom: 'Reference' = deliverFrom 
        self.deliverTo: 'Reference' = deliverTo 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SupplyRequest":
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