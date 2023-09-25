"""
Generated class for MedicinalProductManufactured. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class MedicinalProductManufactured(DomainResource):
    """ The manufactured item as contained in the packaged medicinal product.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'CodeableConcept' manufacturedDoseForm: Dose form as manufactured and before any transformation into the pharmaceutical product
    :param 'CodeableConcept' unitOfPresentation: The “real world” units in which the quantity of the manufactured item is described
    :param 'Quantity' quantity: The quantity or "count number" of the manufactured item
    :param list['Reference'] manufacturer: Manufacturer of the item (Note that this should be named "manufacturer" but it currently causes technical issues)
    :param list['Reference'] ingredient: Ingredient
    :param 'ProdCharacteristic' physicalCharacteristics: Dimensions, color etc.
    :param list['CodeableConcept'] otherCharacteristics: Other codeable characteristics
    """
    def __init__(self, resourceType: str = "MedicinalProductManufactured",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  manufacturedDoseForm: 'CodeableConcept' = None,  unitOfPresentation: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  manufacturer: list['Reference'] = None,  ingredient: list['Reference'] = None,  physicalCharacteristics: 'ProdCharacteristic' = None,  otherCharacteristics: list['CodeableConcept'] = None, ):
        self.resourceType: str = resourceType or "MedicinalProductManufactured"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.manufacturedDoseForm: 'CodeableConcept' = manufacturedDoseForm 
        self.unitOfPresentation: 'CodeableConcept' = unitOfPresentation 
        self.quantity: 'Quantity' = quantity 
        self.manufacturer: list['Reference'] = manufacturer or []
        self.ingredient: list['Reference'] = ingredient or []
        self.physicalCharacteristics: 'ProdCharacteristic' = physicalCharacteristics 
        self.otherCharacteristics: list['CodeableConcept'] = otherCharacteristics or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductManufactured":
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