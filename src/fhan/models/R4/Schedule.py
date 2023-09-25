"""
Generated class for Schedule. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Schedule(DomainResource):
    """ A container for slots of time that may be available for booking appointments.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this item
    :param bool active: Whether this schedule is in active use
    :param list['CodeableConcept'] serviceCategory: High-level category
    :param list['CodeableConcept'] serviceType: Specific service
    :param list['CodeableConcept'] specialty: Type of specialty needed
    :param list['Reference'] actor: Resource(s) that availability information is being provided for
    :param 'Period' planningHorizon: Period of time covered by schedule
    :param str comment: Comments on availability
    """
    def __init__(self, resourceType: str = "Schedule",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  active: bool = None,  serviceCategory: list['CodeableConcept'] = None,  serviceType: list['CodeableConcept'] = None,  specialty: list['CodeableConcept'] = None,  actor: list['Reference'] = None,  planningHorizon: 'Period' = None,  comment: str = None, ):
        self.resourceType: str = resourceType or "Schedule"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.active: bool = active 
        self.serviceCategory: list['CodeableConcept'] = serviceCategory or []
        self.serviceType: list['CodeableConcept'] = serviceType or []
        self.specialty: list['CodeableConcept'] = specialty or []
        self.actor: list['Reference'] = actor or []
        self.planningHorizon: 'Period' = planningHorizon 
        self.comment: str = comment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Schedule":
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