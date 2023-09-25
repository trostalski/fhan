"""
Generated class for MedicinalProduct. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class NamePart(ModelBase):
    """ Coding words or phrases of the name.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str part: A fragment of a product name
    :param 'Coding' type: Idenifying type for this part of the name (e.g. strength part)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  part: str = None,  type: 'Coding' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.part: str = part 
        self.type: 'Coding' = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "NamePart":
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


    
    

class CountryLanguage(ModelBase):
    """ Country where the name applies.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' country: Country code for where this name applies
    :param 'CodeableConcept' jurisdiction: Jurisdiction code for where this name applies
    :param 'CodeableConcept' language: Language code for this name
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  country: 'CodeableConcept' = None,  jurisdiction: 'CodeableConcept' = None,  language: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.country: 'CodeableConcept' = country 
        self.jurisdiction: 'CodeableConcept' = jurisdiction 
        self.language: 'CodeableConcept' = language 
        

    @classmethod
    def from_dict(cls, data: dict) -> "CountryLanguage":
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


  
    
    

class Name(ModelBase):
    """ The product's name, including full name and possibly coded parts.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str productName: The full product name
    :param list['NamePart'] namePart: Coding words or phrases of the name
    :param list['CountryLanguage'] countryLanguage: Country where the name applies
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  productName: str = None,  namePart: list['NamePart'] = None,  countryLanguage: list['CountryLanguage'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.productName: str = productName 
        self.namePart: list['NamePart'] = namePart or []
        self.countryLanguage: list['CountryLanguage'] = countryLanguage or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Name":
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


    
    

class ManufacturingBusinessOperation(ModelBase):
    """ An operation applied to the product, for manufacturing or adminsitrative purpose.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' operationType: The type of manufacturing operation
    :param 'Identifier' authorisationReferenceNumber: Regulatory authorization reference number
    :param str effectiveDate: Regulatory authorization date
    :param 'CodeableConcept' confidentialityIndicator: To indicate if this proces is commercially confidential
    :param list['Reference'] manufacturer: The manufacturer or establishment associated with the process
    :param 'Reference' regulator: A regulator which oversees the operation
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  operationType: 'CodeableConcept' = None,  authorisationReferenceNumber: 'Identifier' = None,  effectiveDate: str = None,  confidentialityIndicator: 'CodeableConcept' = None,  manufacturer: list['Reference'] = None,  regulator: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.operationType: 'CodeableConcept' = operationType 
        self.authorisationReferenceNumber: 'Identifier' = authorisationReferenceNumber 
        self.effectiveDate: str = effectiveDate 
        self.confidentialityIndicator: 'CodeableConcept' = confidentialityIndicator 
        self.manufacturer: list['Reference'] = manufacturer or []
        self.regulator: 'Reference' = regulator 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ManufacturingBusinessOperation":
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


    
    

class SpecialDesignation(ModelBase):
    """ Indicates if the medicinal product has an orphan designation for the treatment of a rare disease.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Identifier'] identifier: Identifier for the designation, or procedure number
    :param 'CodeableConcept' type: The type of special designation, e.g. orphan drug, minor use
    :param 'CodeableConcept' intendedUse: The intended use of the product, e.g. prevention, treatment
    :param 'CodeableConcept' indicationCodeableConcept: Condition for which the medicinal use applies
    :param 'Reference' indicationReference: Condition for which the medicinal use applies
    :param 'CodeableConcept' status: For example granted, pending, expired or withdrawn
    :param str date: Date when the designation was granted
    :param 'CodeableConcept' species: Animal species for which this applies
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  type: 'CodeableConcept' = None,  intendedUse: 'CodeableConcept' = None,  indicationCodeableConcept: 'CodeableConcept' = None,  indicationReference: 'Reference' = None,  status: 'CodeableConcept' = None,  date: str = None,  species: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.type: 'CodeableConcept' = type 
        self.intendedUse: 'CodeableConcept' = intendedUse 
        self.indicationCodeableConcept: 'CodeableConcept' = indicationCodeableConcept 
        self.indicationReference: 'Reference' = indicationReference 
        self.status: 'CodeableConcept' = status 
        self.date: str = date 
        self.species: 'CodeableConcept' = species 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SpecialDesignation":
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


class MedicinalProduct(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier for this product. Could be an MPID
    :param 'CodeableConcept' type: Regulatory type, e.g. Investigational or Authorized
    :param 'Coding' domain: If this medicine applies to human or veterinary uses
    :param 'CodeableConcept' combinedPharmaceuticalDoseForm: The dose form for a single part product, or combined form of a multiple part product
    :param 'CodeableConcept' legalStatusOfSupply: The legal status of supply of the medicinal product as classified by the regulator
    :param 'CodeableConcept' additionalMonitoringIndicator: Whether the Medicinal Product is subject to additional monitoring for regulatory reasons
    :param str specialMeasures: Whether the Medicinal Product is subject to special measures for regulatory reasons
    :param 'CodeableConcept' paediatricUseIndicator: If authorised for use in children
    :param list['CodeableConcept'] productClassification: Allows the product to be classified by various systems
    :param list['MarketingStatus'] marketingStatus: Marketing status of the medicinal product, in contrast to marketing authorizaton
    :param list['Reference'] pharmaceuticalProduct: Pharmaceutical aspects of product
    :param list['Reference'] packagedMedicinalProduct: Package representation for the product
    :param list['Reference'] attachedDocument: Supporting documentation, typically for regulatory submission
    :param list['Reference'] masterFile: A master file for to the medicinal product (e.g. Pharmacovigilance System Master File)
    :param list['Reference'] contact: A product specific contact, person (in a role), or an organization
    :param list['Reference'] clinicalTrial: Clinical trials or studies that this product is involved in
    :param list['Name'] name: The product's name, including full name and possibly coded parts
    :param list['Identifier'] crossReference: Reference to another product, e.g. for linking authorised to investigational product
    :param list['ManufacturingBusinessOperation'] manufacturingBusinessOperation: An operation applied to the product, for manufacturing or adminsitrative purpose
    :param list['SpecialDesignation'] specialDesignation: Indicates if the medicinal product has an orphan designation for the treatment of a rare disease
    """
    def __init__(self, resourceType: str = "MedicinalProduct",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  type: 'CodeableConcept' = None,  domain: 'Coding' = None,  combinedPharmaceuticalDoseForm: 'CodeableConcept' = None,  legalStatusOfSupply: 'CodeableConcept' = None,  additionalMonitoringIndicator: 'CodeableConcept' = None,  specialMeasures: str = None,  paediatricUseIndicator: 'CodeableConcept' = None,  productClassification: list['CodeableConcept'] = None,  marketingStatus: list['MarketingStatus'] = None,  pharmaceuticalProduct: list['Reference'] = None,  packagedMedicinalProduct: list['Reference'] = None,  attachedDocument: list['Reference'] = None,  masterFile: list['Reference'] = None,  contact: list['Reference'] = None,  clinicalTrial: list['Reference'] = None,  name: list['Name'] = None,  crossReference: list['Identifier'] = None,  manufacturingBusinessOperation: list['ManufacturingBusinessOperation'] = None,  specialDesignation: list['SpecialDesignation'] = None, ):
        self.resourceType: str = resourceType or "MedicinalProduct"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.type: 'CodeableConcept' = type 
        self.domain: 'Coding' = domain 
        self.combinedPharmaceuticalDoseForm: 'CodeableConcept' = combinedPharmaceuticalDoseForm 
        self.legalStatusOfSupply: 'CodeableConcept' = legalStatusOfSupply 
        self.additionalMonitoringIndicator: 'CodeableConcept' = additionalMonitoringIndicator 
        self.specialMeasures: str = specialMeasures or []
        self.paediatricUseIndicator: 'CodeableConcept' = paediatricUseIndicator 
        self.productClassification: list['CodeableConcept'] = productClassification or []
        self.marketingStatus: list['MarketingStatus'] = marketingStatus or []
        self.pharmaceuticalProduct: list['Reference'] = pharmaceuticalProduct or []
        self.packagedMedicinalProduct: list['Reference'] = packagedMedicinalProduct or []
        self.attachedDocument: list['Reference'] = attachedDocument or []
        self.masterFile: list['Reference'] = masterFile or []
        self.contact: list['Reference'] = contact or []
        self.clinicalTrial: list['Reference'] = clinicalTrial or []
        self.name: list['Name'] = name or []
        self.crossReference: list['Identifier'] = crossReference or []
        self.manufacturingBusinessOperation: list['ManufacturingBusinessOperation'] = manufacturingBusinessOperation or []
        self.specialDesignation: list['SpecialDesignation'] = specialDesignation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProduct":
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