"""
Generated class for DataRequirement. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Element import *
from fhan.models.R4.Duration import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import ModelBase

    
    

class CodeFilter(ModelBase):
    """ Code filters specify additional constraints on the data, specifying the value set of interest for a particular element of the data. Each code filter defines an additional constraint on the data, i.e. code filters are AND'ed, not OR'ed.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: A code-valued attribute to filter on
    :param str searchParam: A coded (token) parameter to search on
    :param str valueSet: Valueset for the filter
    :param list['Coding'] code: What code is expected
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  searchParam: str = None,  valueSet: str = None,  code: list['Coding'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.searchParam: str = searchParam 
        self.valueSet: str = valueSet 
        self.code: list['Coding'] = code or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "CodeFilter":
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


    
    

class DateFilter(ModelBase):
    """ Date filters specify additional constraints on the data in terms of the applicable date range for specific elements. Each date filter specifies an additional constraint on the data, i.e. date filters are AND'ed, not OR'ed.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: A date-valued attribute to filter on
    :param str searchParam: A date valued parameter to search on
    :param str valueDateTime: The value of the filter, as a Period, DateTime, or Duration value
    :param 'Period' valuePeriod: The value of the filter, as a Period, DateTime, or Duration value
    :param 'Duration' valueDuration: The value of the filter, as a Period, DateTime, or Duration value
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  searchParam: str = None,  valueDateTime: str = None,  valuePeriod: 'Period' = None,  valueDuration: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.searchParam: str = searchParam 
        self.valueDateTime: str = valueDateTime 
        self.valuePeriod: 'Period' = valuePeriod 
        self.valueDuration: 'Duration' = valueDuration 
        

    @classmethod
    def from_dict(cls, data: dict) -> "DateFilter":
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


    
    

class Sort(ModelBase):
    """ Specifies the order of the results to be returned.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: The name of the attribute to perform the sort
    :param str direction: ascending | descending
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  direction: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.direction: str = direction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Sort":
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


class DataRequirement(ModelBase):
    """ Base StructureDefinition for DataRequirement Type: Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str type: The type of the required data
    :param str profile: The profile of the required data
    :param 'CodeableConcept' subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param 'Reference' subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str mustSupport: Indicates specific structure elements that are referenced by the knowledge module
    :param list['CodeFilter'] codeFilter: What codes are expected
    :param list['DateFilter'] dateFilter: What dates/date ranges are expected
    :param int limit: Number of results
    :param list['Sort'] sort: Order of the results
    """
    def __init__(self, resourceType: str = "DataRequirement",  id: str = None,  extension: list['Extension'] = None,  type: str = None,  profile: str = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  mustSupport: str = None,  codeFilter: list['CodeFilter'] = None,  dateFilter: list['DateFilter'] = None,  limit: int = None,  sort: list['Sort'] = None, ):
        self.resourceType: str = resourceType or "DataRequirement"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.profile: str = profile or []
        self.subjectCodeableConcept: 'CodeableConcept' = subjectCodeableConcept 
        self.subjectReference: 'Reference' = subjectReference 
        self.mustSupport: str = mustSupport or []
        self.codeFilter: list['CodeFilter'] = codeFilter or []
        self.dateFilter: list['DateFilter'] = dateFilter or []
        self.limit: int = limit 
        self.sort: list['Sort'] = sort or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DataRequirement":
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