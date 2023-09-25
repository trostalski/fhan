"""
Generated class for MedicinalProductAuthorization. 
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
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class JurisdictionalAuthorization(ModelBase):
    """ Authorization in areas within a country.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Identifier'] identifier: The assigned number for the marketing authorization
    :param 'CodeableConcept' country: Country of authorization
    :param list['CodeableConcept'] jurisdiction: Jurisdiction within a country
    :param 'CodeableConcept' legalStatusOfSupply: The legal status of supply in a jurisdiction or region
    :param 'Period' validityPeriod: The start and expected end date of the authorization
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  country: 'CodeableConcept' = None,  jurisdiction: list['CodeableConcept'] = None,  legalStatusOfSupply: 'CodeableConcept' = None,  validityPeriod: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.country: 'CodeableConcept' = country 
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.legalStatusOfSupply: 'CodeableConcept' = legalStatusOfSupply 
        self.validityPeriod: 'Period' = validityPeriod 
        

    @classmethod
    def from_dict(cls, data: dict) -> "JurisdictionalAuthorization":
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


    
    

class Procedure(ModelBase):
    """ The regulatory procedure for granting or amending a marketing authorization.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Identifier for this procedure
    :param 'CodeableConcept' type: Type of procedure
    :param 'Period' datePeriod: Date of procedure
    :param str dateDateTime: Date of procedure
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  type: 'CodeableConcept' = None,  datePeriod: 'Period' = None,  dateDateTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.type: 'CodeableConcept' = type 
        self.datePeriod: 'Period' = datePeriod 
        self.dateDateTime: str = dateDateTime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Procedure":
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


    
    

class Application(ModelBase):
    """ The regulatory procedure for granting or amending a marketing authorization.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Identifier for this procedure
    :param 'CodeableConcept' type: Type of procedure
    :param 'Period' datePeriod: Date of procedure
    :param str dateDateTime: Date of procedure
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  type: 'CodeableConcept' = None,  datePeriod: 'Period' = None,  dateDateTime: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.type: 'CodeableConcept' = type 
        self.datePeriod: 'Period' = datePeriod 
        self.dateDateTime: str = dateDateTime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Application":
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


class MedicinalProductAuthorization(DomainResource):
    """ The regulatory authorization of a medicinal product.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier for the marketing authorization, as assigned by a regulator
    :param 'Reference' subject: The medicinal product that is being authorized
    :param list['CodeableConcept'] country: The country in which the marketing authorization has been granted
    :param list['CodeableConcept'] jurisdiction: Jurisdiction within a country
    :param 'CodeableConcept' status: The status of the marketing authorization
    :param str statusDate: The date at which the given status has become applicable
    :param str restoreDate: The date when a suspended the marketing or the marketing authorization of the product is anticipated to be restored
    :param 'Period' validityPeriod: The beginning of the time period in which the marketing authorization is in the specific status shall be specified A complete date consisting of day, month and year shall be specified using the ISO 8601 date format
    :param 'Period' dataExclusivityPeriod: A period of time after authorization before generic product applicatiosn can be submitted
    :param str dateOfFirstAuthorization: The date when the first authorization was granted by a Medicines Regulatory Agency
    :param str internationalBirthDate: Date of first marketing authorization for a company's new medicinal product in any country in the World
    :param 'CodeableConcept' legalBasis: The legal framework against which this authorization is granted
    :param list['JurisdictionalAuthorization'] jurisdictionalAuthorization: Authorization in areas within a country
    :param 'Reference' holder: Marketing Authorization Holder
    :param 'Reference' regulator: Medicines Regulatory Agency
    :param 'Procedure' procedure: The regulatory procedure for granting or amending a marketing authorization
    :param 'Application' application: The regulatory procedure for granting or amending a marketing authorization
    """
    def __init__(self, resourceType: str = "MedicinalProductAuthorization",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  subject: 'Reference' = None,  country: list['CodeableConcept'] = None,  jurisdiction: list['CodeableConcept'] = None,  status: 'CodeableConcept' = None,  statusDate: str = None,  restoreDate: str = None,  validityPeriod: 'Period' = None,  dataExclusivityPeriod: 'Period' = None,  dateOfFirstAuthorization: str = None,  internationalBirthDate: str = None,  legalBasis: 'CodeableConcept' = None,  jurisdictionalAuthorization: list['JurisdictionalAuthorization'] = None,  holder: 'Reference' = None,  regulator: 'Reference' = None,  procedure: 'Procedure' = None,  application: 'Application' = None, ):
        self.resourceType: str = resourceType or "MedicinalProductAuthorization"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.subject: 'Reference' = subject 
        self.country: list['CodeableConcept'] = country or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.status: 'CodeableConcept' = status 
        self.statusDate: str = statusDate 
        self.restoreDate: str = restoreDate 
        self.validityPeriod: 'Period' = validityPeriod 
        self.dataExclusivityPeriod: 'Period' = dataExclusivityPeriod 
        self.dateOfFirstAuthorization: str = dateOfFirstAuthorization 
        self.internationalBirthDate: str = internationalBirthDate 
        self.legalBasis: 'CodeableConcept' = legalBasis 
        self.jurisdictionalAuthorization: list['JurisdictionalAuthorization'] = jurisdictionalAuthorization or []
        self.holder: 'Reference' = holder 
        self.regulator: 'Reference' = regulator 
        self.procedure: 'Procedure' = procedure 
        self.application: 'Application' = application 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductAuthorization":
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