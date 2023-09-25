"""
Generated class for SubstanceSpecification. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Range import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Moiety(ModelBase):
    """ Moiety, for structural modifications.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' role: Role that the moiety is playing
    :param 'Identifier' identifier: Identifier by which this moiety substance is known
    :param str name: Textual name for this moiety substance
    :param 'CodeableConcept' stereochemistry: Stereochemistry type
    :param 'CodeableConcept' opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula
    :param 'Quantity' amountQuantity: Quantitative value for this moiety
    :param str amountString: Quantitative value for this moiety
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  role: 'CodeableConcept' = None,  identifier: 'Identifier' = None,  name: str = None,  stereochemistry: 'CodeableConcept' = None,  opticalActivity: 'CodeableConcept' = None,  molecularFormula: str = None,  amountQuantity: 'Quantity' = None,  amountString: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.role: 'CodeableConcept' = role 
        self.identifier: 'Identifier' = identifier 
        self.name: str = name 
        self.stereochemistry: 'CodeableConcept' = stereochemistry 
        self.opticalActivity: 'CodeableConcept' = opticalActivity 
        self.molecularFormula: str = molecularFormula 
        self.amountQuantity: 'Quantity' = amountQuantity 
        self.amountString: str = amountString 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Moiety":
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


    
    

class Property(ModelBase):
    """ General specifications for this substance, including how it is related to other substances.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' category: A category for this property, e.g. Physical, Chemical, Enzymatic
    :param 'CodeableConcept' code: Property type e.g. viscosity, pH, isoelectric point
    :param str parameters: Parameters that were used in the measurement of a property (e.g. for viscosity: measured at 20C with a pH of 7.1)
    :param 'Reference' definingSubstanceReference: A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol)
    :param 'CodeableConcept' definingSubstanceCodeableConcept: A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol)
    :param 'Quantity' amountQuantity: Quantitative value for this property
    :param str amountString: Quantitative value for this property
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  category: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  parameters: str = None,  definingSubstanceReference: 'Reference' = None,  definingSubstanceCodeableConcept: 'CodeableConcept' = None,  amountQuantity: 'Quantity' = None,  amountString: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.category: 'CodeableConcept' = category 
        self.code: 'CodeableConcept' = code 
        self.parameters: str = parameters 
        self.definingSubstanceReference: 'Reference' = definingSubstanceReference 
        self.definingSubstanceCodeableConcept: 'CodeableConcept' = definingSubstanceCodeableConcept 
        self.amountQuantity: 'Quantity' = amountQuantity 
        self.amountString: str = amountString 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Property":
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


    
        
    
        
    
    

class MolecularWeight(ModelBase):
    """ The molecular weight or weight range (for proteins, polymers or nucleic acids).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' method: The method by which the molecular weight was determined
    :param 'CodeableConcept' type: Type of molecular weight such as exact, average (also known as. number average), weight average
    :param 'Quantity' amount: Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  method: 'CodeableConcept' = None,  type: 'CodeableConcept' = None,  amount: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.method: 'CodeableConcept' = method 
        self.type: 'CodeableConcept' = type 
        self.amount: 'Quantity' = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularWeight":
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


  
    
    

class Isotope(ModelBase):
    """ Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Substance identifier for each non-natural or radioisotope
    :param 'CodeableConcept' name: Substance name for each non-natural or radioisotope
    :param 'CodeableConcept' substitution: The type of isotopic substitution present in a single substance
    :param 'Quantity' halfLife: Half life - for a non-natural nuclide
    :param 'MolecularWeight' molecularWeight: The molecular weight or weight range (for proteins, polymers or nucleic acids)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  name: 'CodeableConcept' = None,  substitution: 'CodeableConcept' = None,  halfLife: 'Quantity' = None,  molecularWeight: 'MolecularWeight' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.name: 'CodeableConcept' = name 
        self.substitution: 'CodeableConcept' = substitution 
        self.halfLife: 'Quantity' = halfLife 
        self.molecularWeight: 'MolecularWeight' = molecularWeight 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Isotope":
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


    
    

class Representation(ModelBase):
    """ Molecular structural representation.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The type of structure (e.g. Full, Partial, Representative)
    :param str representation: The structural representation as text string in a format e.g. InChI, SMILES, MOLFILE, CDX
    :param 'Attachment' attachment: An attached file with the structural representation
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  representation: str = None,  attachment: 'Attachment' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.representation: str = representation 
        self.attachment: 'Attachment' = attachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Representation":
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


  
    
    

class Structure(ModelBase):
    """ Structural information.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' stereochemistry: Stereochemistry type
    :param 'CodeableConcept' opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula
    :param str molecularFormulaByMoiety: Specified per moiety according to the Hill system, i.e. first C, then H, then alphabetical, each moiety separated by a dot
    :param list['Isotope'] isotope: Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio
    :param list['Reference'] source: Supporting literature
    :param list['Representation'] representation: Molecular structural representation
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  stereochemistry: 'CodeableConcept' = None,  opticalActivity: 'CodeableConcept' = None,  molecularFormula: str = None,  molecularFormulaByMoiety: str = None,  isotope: list['Isotope'] = None,  source: list['Reference'] = None,  representation: list['Representation'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.stereochemistry: 'CodeableConcept' = stereochemistry 
        self.opticalActivity: 'CodeableConcept' = opticalActivity 
        self.molecularFormula: str = molecularFormula 
        self.molecularFormulaByMoiety: str = molecularFormulaByMoiety 
        self.isotope: list['Isotope'] = isotope or []
        self.source: list['Reference'] = source or []
        self.representation: list['Representation'] = representation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Structure":
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


    
    

class Code(ModelBase):
    """ Codes associated with the substance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: The specific code
    :param 'CodeableConcept' status: Status of the code assignment
    :param str statusDate: The date at which the code status is changed as part of the terminology maintenance
    :param str comment: Any comment can be provided in this field, if necessary
    :param list['Reference'] source: Supporting literature
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  statusDate: str = None,  comment: str = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.status: 'CodeableConcept' = status 
        self.statusDate: str = statusDate 
        self.comment: str = comment 
        self.source: list['Reference'] = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Code":
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


    
        
    
    

class Official(ModelBase):
    """ Details of the official nature of this name.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' authority: Which authority uses this official name
    :param 'CodeableConcept' status: The status of the official name
    :param str date: Date of official name change
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  authority: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  date: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.authority: 'CodeableConcept' = authority 
        self.status: 'CodeableConcept' = status 
        self.date: str = date 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Official":
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
    """ Names applicable to this substance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The actual name
    :param 'CodeableConcept' type: Name type
    :param 'CodeableConcept' status: The status of the name
    :param bool preferred: If this is the preferred name for this substance
    :param list['CodeableConcept'] language: Language of the name
    :param list['CodeableConcept'] domain: The use context of this name for example if there is a different name a drug active ingredient as opposed to a food colour additive
    :param list['CodeableConcept'] jurisdiction: The jurisdiction where this name applies
    :param list['Official'] official: Details of the official nature of this name
    :param list['Reference'] source: Supporting literature
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  type: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  preferred: bool = None,  language: list['CodeableConcept'] = None,  domain: list['CodeableConcept'] = None,  jurisdiction: list['CodeableConcept'] = None,  official: list['Official'] = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.type: 'CodeableConcept' = type 
        self.status: 'CodeableConcept' = status 
        self.preferred: bool = preferred 
        self.language: list['CodeableConcept'] = language or []
        self.domain: list['CodeableConcept'] = domain or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.official: list['Official'] = official or []
        self.source: list['Reference'] = source or []
        

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


    
        
    
    

class Official(ModelBase):
    """ Details of the official nature of this name.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' authority: Which authority uses this official name
    :param 'CodeableConcept' status: The status of the official name
    :param str date: Date of official name change
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  authority: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  date: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.authority: 'CodeableConcept' = authority 
        self.status: 'CodeableConcept' = status 
        self.date: str = date 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Official":
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


  
    
    

class Synonym(ModelBase):
    """ Names applicable to this substance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The actual name
    :param 'CodeableConcept' type: Name type
    :param 'CodeableConcept' status: The status of the name
    :param bool preferred: If this is the preferred name for this substance
    :param list['CodeableConcept'] language: Language of the name
    :param list['CodeableConcept'] domain: The use context of this name for example if there is a different name a drug active ingredient as opposed to a food colour additive
    :param list['CodeableConcept'] jurisdiction: The jurisdiction where this name applies
    :param list['Official'] official: Details of the official nature of this name
    :param list['Reference'] source: Supporting literature
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  type: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  preferred: bool = None,  language: list['CodeableConcept'] = None,  domain: list['CodeableConcept'] = None,  jurisdiction: list['CodeableConcept'] = None,  official: list['Official'] = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.type: 'CodeableConcept' = type 
        self.status: 'CodeableConcept' = status 
        self.preferred: bool = preferred 
        self.language: list['CodeableConcept'] = language or []
        self.domain: list['CodeableConcept'] = domain or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.official: list['Official'] = official or []
        self.source: list['Reference'] = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Synonym":
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


    
        
    
    

class Official(ModelBase):
    """ Details of the official nature of this name.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' authority: Which authority uses this official name
    :param 'CodeableConcept' status: The status of the official name
    :param str date: Date of official name change
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  authority: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  date: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.authority: 'CodeableConcept' = authority 
        self.status: 'CodeableConcept' = status 
        self.date: str = date 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Official":
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


  
    
    

class Translation(ModelBase):
    """ Names applicable to this substance.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The actual name
    :param 'CodeableConcept' type: Name type
    :param 'CodeableConcept' status: The status of the name
    :param bool preferred: If this is the preferred name for this substance
    :param list['CodeableConcept'] language: Language of the name
    :param list['CodeableConcept'] domain: The use context of this name for example if there is a different name a drug active ingredient as opposed to a food colour additive
    :param list['CodeableConcept'] jurisdiction: The jurisdiction where this name applies
    :param list['Official'] official: Details of the official nature of this name
    :param list['Reference'] source: Supporting literature
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  type: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  preferred: bool = None,  language: list['CodeableConcept'] = None,  domain: list['CodeableConcept'] = None,  jurisdiction: list['CodeableConcept'] = None,  official: list['Official'] = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.type: 'CodeableConcept' = type 
        self.status: 'CodeableConcept' = status 
        self.preferred: bool = preferred 
        self.language: list['CodeableConcept'] = language or []
        self.domain: list['CodeableConcept'] = domain or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.official: list['Official'] = official or []
        self.source: list['Reference'] = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Translation":
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


    
    

class Relationship(ModelBase):
    """ A link between this substance and another, with details of the relationship.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' substanceReference: A pointer to another substance, as a resource or just a representational code
    :param 'CodeableConcept' substanceCodeableConcept: A pointer to another substance, as a resource or just a representational code
    :param 'CodeableConcept' relationship: For example "salt to parent", "active moiety", "starting material"
    :param bool isDefining: For example where an enzyme strongly bonds with a particular substance, this is a defining relationship for that enzyme, out of several possible substance relationships
    :param 'Quantity' amountQuantity: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param 'Range' amountRange: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param 'Ratio' amountRatio: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param str amountString: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param 'Ratio' amountRatioLowLimit: For use when the numeric
    :param 'CodeableConcept' amountType: An operator for the amount, for example "average", "approximately", "less than"
    :param list['Reference'] source: Supporting literature
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  substanceReference: 'Reference' = None,  substanceCodeableConcept: 'CodeableConcept' = None,  relationship: 'CodeableConcept' = None,  isDefining: bool = None,  amountQuantity: 'Quantity' = None,  amountRange: 'Range' = None,  amountRatio: 'Ratio' = None,  amountString: str = None,  amountRatioLowLimit: 'Ratio' = None,  amountType: 'CodeableConcept' = None,  source: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.substanceReference: 'Reference' = substanceReference 
        self.substanceCodeableConcept: 'CodeableConcept' = substanceCodeableConcept 
        self.relationship: 'CodeableConcept' = relationship 
        self.isDefining: bool = isDefining 
        self.amountQuantity: 'Quantity' = amountQuantity 
        self.amountRange: 'Range' = amountRange 
        self.amountRatio: 'Ratio' = amountRatio 
        self.amountString: str = amountString 
        self.amountRatioLowLimit: 'Ratio' = amountRatioLowLimit 
        self.amountType: 'CodeableConcept' = amountType 
        self.source: list['Reference'] = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Relationship":
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


class SubstanceSpecification(DomainResource):
    """ The detailed description of a substance, typically at a level beyond what is used for prescribing.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Identifier by which this substance is known
    :param 'CodeableConcept' type: High level categorization, e.g. polymer or nucleic acid
    :param 'CodeableConcept' status: Status of substance within the catalogue e.g. approved
    :param 'CodeableConcept' domain: If the substance applies to only human or veterinary use
    :param str description: Textual description of the substance
    :param list['Reference'] source: Supporting literature
    :param str comment: Textual comment about this record of a substance
    :param list['Moiety'] moiety: Moiety, for structural modifications
    :param list['Property'] property: General specifications for this substance, including how it is related to other substances
    :param 'Reference' referenceInformation: General information detailing this substance
    :param 'Structure' structure: Structural information
    :param list['Code'] code: Codes associated with the substance
    :param list['Name'] name: Names applicable to this substance
    :param list['Synonym'] synonym: Names applicable to this substance
    :param list['Translation'] translation: Names applicable to this substance
    :param list['Relationship'] relationship: A link between this substance and another, with details of the relationship
    :param 'Reference' nucleicAcid: Data items specific to nucleic acids
    :param 'Reference' polymer: Data items specific to polymers
    :param 'Reference' protein: Data items specific to proteins
    :param 'Reference' sourceMaterial: Material or taxonomic/anatomical source for the substance
    """
    def __init__(self, resourceType: str = "SubstanceSpecification",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  type: 'CodeableConcept' = None,  status: 'CodeableConcept' = None,  domain: 'CodeableConcept' = None,  description: str = None,  source: list['Reference'] = None,  comment: str = None,  moiety: list['Moiety'] = None,  property: list['Property'] = None,  referenceInformation: 'Reference' = None,  structure: 'Structure' = None,  code: list['Code'] = None,  name: list['Name'] = None,  synonym: list['Synonym'] = None,  translation: list['Translation'] = None,  relationship: list['Relationship'] = None,  nucleicAcid: 'Reference' = None,  polymer: 'Reference' = None,  protein: 'Reference' = None,  sourceMaterial: 'Reference' = None, ):
        self.resourceType: str = resourceType or "SubstanceSpecification"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.type: 'CodeableConcept' = type 
        self.status: 'CodeableConcept' = status 
        self.domain: 'CodeableConcept' = domain 
        self.description: str = description 
        self.source: list['Reference'] = source or []
        self.comment: str = comment 
        self.moiety: list['Moiety'] = moiety or []
        self.property: list['Property'] = property or []
        self.referenceInformation: 'Reference' = referenceInformation 
        self.structure: 'Structure' = structure 
        self.code: list['Code'] = code or []
        self.name: list['Name'] = name or []
        self.synonym: list['Synonym'] = synonym or []
        self.translation: list['Translation'] = translation or []
        self.relationship: list['Relationship'] = relationship or []
        self.nucleicAcid: 'Reference' = nucleicAcid 
        self.polymer: 'Reference' = polymer 
        self.protein: 'Reference' = protein 
        self.sourceMaterial: 'Reference' = sourceMaterial 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceSpecification":
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