"""
Generated class for Definition. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.UsageContext import *
from fhan.models.generator_models import ModelBase

class Definition(ModelBase):
    """ Logical Model: A pattern to be followed by resources that represent a specific proposal, plan and/or order for some sort of action or service.
    :param str url: Logical canonical URL to reference this {{title}} (globally unique)
    :param 'Identifier' identifier: Business Identifier for {{title}}
    :param str version: Business version of the {{title}}
    :param str title: Name for this {{title}} (Human friendly)
    :param str derivedFromCanonical: Based on FHIR protocol or definition
    :param str derivedFromUri: Based on external protocol or definition
    :param str partOf: Part of referenced definition
    :param str replaces: Request(s) replaced by this request
    :param str status: draft | active | retired | unknown
    :param bool experimental: If for testing purposes, not real usage
    :param 'CodeableConcept' subjectCodeableConcept: Type of individual the defined service is for
    :param 'Reference' subjectReference: Type of individual the defined service is for
    :param str date: Date status first applied
    :param 'Reference' publisher: The name of the individual or organization that published the {{title}}
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str description: Natural language description of the {{title}}
    :param list['UsageContext'] useContext: Content intends to support these contexts
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for {{title}} (if applicable)
    :param str purpose: Why this {{title}} is defined
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When {{title}} approved by publisher
    :param str lastReviewDate: Last review date for the {{title}}
    :param 'Period' effectivePeriod: The effective date range for the {{title}}
    :param 'CodeableConcept' performerType: Desired kind of service performer
    """
    def __init__(self, resourceType: str = "Definition",  url: str = None,  identifier: 'Identifier' = None,  version: str = None,  title: str = None,  derivedFromCanonical: str = None,  derivedFromUri: str = None,  partOf: str = None,  replaces: str = None,  status: str = None,  experimental: bool = None,  subjectCodeableConcept: 'CodeableConcept' = None,  subjectReference: 'Reference' = None,  date: str = None,  publisher: 'Reference' = None,  contact: list['ContactDetail'] = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  purpose: str = None,  copyright: str = None,  approvalDate: str = None,  lastReviewDate: str = None,  effectivePeriod: 'Period' = None,  performerType: 'CodeableConcept' = None, ):
        self.resourceType: str = resourceType or "Definition"
        self.url: str = url 
        self.identifier: 'Identifier' = identifier 
        self.version: str = version 
        self.title: str = title 
        self.derivedFromCanonical: str = derivedFromCanonical or []
        self.derivedFromUri: str = derivedFromUri or []
        self.partOf: str = partOf or []
        self.replaces: str = replaces or []
        self.status: str = status 
        self.experimental: bool = experimental 
        self.subjectCodeableConcept: 'CodeableConcept' = subjectCodeableConcept 
        self.subjectReference: 'Reference' = subjectReference 
        self.date: str = date 
        self.publisher: 'Reference' = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.purpose: str = purpose 
        self.copyright: str = copyright 
        self.approvalDate: str = approvalDate 
        self.lastReviewDate: str = lastReviewDate 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.performerType: 'CodeableConcept' = performerType 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Definition":
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