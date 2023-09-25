"""
Generated class for Immunization. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Performer(ModelBase):
    """ Indicates who performed the immunization event.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' function: What type of performance was done
    :param 'Reference' actor: Individual or organization who was performing
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


    
    

class Education(ModelBase):
    """ Educational material presented to the patient (or guardian) at the time of vaccine administration.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str documentType: Educational material document identifier
    :param str reference: Educational material reference pointer
    :param str publicationDate: Educational material publication date
    :param str presentationDate: Educational material presentation date
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  documentType: str = None,  reference: str = None,  publicationDate: str = None,  presentationDate: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.documentType: str = documentType 
        self.reference: str = reference 
        self.publicationDate: str = publicationDate 
        self.presentationDate: str = presentationDate 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Education":
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


    
    

class Reaction(ModelBase):
    """ Categorical data indicating that an adverse event is associated in time to an immunization.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str date: When reaction started
    :param 'Reference' detail: Additional information on reaction
    :param bool reported: Indicates self-reported reaction
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  date: str = None,  detail: 'Reference' = None,  reported: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.date: str = date 
        self.detail: 'Reference' = detail 
        self.reported: bool = reported 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Reaction":
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


    
    

class ProtocolApplied(ModelBase):
    """ The protocol (set of recommendations) being followed by the provider who administered the dose.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str series: Name of vaccine series
    :param 'Reference' authority: Who is responsible for publishing the recommendations
    :param list['CodeableConcept'] targetDisease: Vaccine preventatable disease being targetted
    :param int doseNumberPositiveInt: Dose number within series
    :param str doseNumberString: Dose number within series
    :param int seriesDosesPositiveInt: Recommended number of doses for immunity
    :param str seriesDosesString: Recommended number of doses for immunity
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  series: str = None,  authority: 'Reference' = None,  targetDisease: list['CodeableConcept'] = None,  doseNumberPositiveInt: int = None,  doseNumberString: str = None,  seriesDosesPositiveInt: int = None,  seriesDosesString: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.series: str = series 
        self.authority: 'Reference' = authority 
        self.targetDisease: list['CodeableConcept'] = targetDisease or []
        self.doseNumberPositiveInt: int = doseNumberPositiveInt 
        self.doseNumberString: str = doseNumberString 
        self.seriesDosesPositiveInt: int = seriesDosesPositiveInt 
        self.seriesDosesString: str = seriesDosesString 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ProtocolApplied":
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


class Immunization(DomainResource):
    """ Describes the event of a patient being administered a vaccine or a record of an immunization as reported by a patient, a clinician or another party.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier
    :param str status: completed | entered-in-error | not-done
    :param 'CodeableConcept' statusReason: Reason not done
    :param 'CodeableConcept' vaccineCode: Vaccine product administered
    :param 'Reference' patient: Who was immunized
    :param 'Reference' encounter: Encounter immunization was part of
    :param str occurrenceDateTime: Vaccine administration date
    :param str occurrenceString: Vaccine administration date
    :param str recorded: When the immunization was first captured in the subject's record
    :param bool primarySource: Indicates context the data was recorded in
    :param 'CodeableConcept' reportOrigin: Indicates the source of a secondarily reported record
    :param 'Reference' location: Where immunization occurred
    :param 'Reference' manufacturer: Vaccine manufacturer
    :param str lotNumber: Vaccine lot number
    :param str expirationDate: Vaccine expiration date
    :param 'CodeableConcept' site: Body site vaccine  was administered
    :param 'CodeableConcept' route: How vaccine entered body
    :param 'Quantity' doseQuantity: Amount of vaccine administered
    :param list['Performer'] performer: Who performed event
    :param list['Annotation'] note: Additional immunization notes
    :param list['CodeableConcept'] reasonCode: Why immunization occurred
    :param list['Reference'] reasonReference: Why immunization occurred
    :param bool isSubpotent: Dose potency
    :param list['CodeableConcept'] subpotentReason: Reason for being subpotent
    :param list['Education'] education: Educational material presented to patient
    :param list['CodeableConcept'] programEligibility: Patient eligibility for a vaccination program
    :param 'CodeableConcept' fundingSource: Funding source for the vaccine
    :param list['Reaction'] reaction: Details of a reaction that follows immunization
    :param list['ProtocolApplied'] protocolApplied: Protocol followed by the provider
    """
    def __init__(self, resourceType: str = "Immunization",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  vaccineCode: 'CodeableConcept' = None,  patient: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  occurrenceString: str = None,  recorded: str = None,  primarySource: bool = None,  reportOrigin: 'CodeableConcept' = None,  location: 'Reference' = None,  manufacturer: 'Reference' = None,  lotNumber: str = None,  expirationDate: str = None,  site: 'CodeableConcept' = None,  route: 'CodeableConcept' = None,  doseQuantity: 'Quantity' = None,  performer: list['Performer'] = None,  note: list['Annotation'] = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  isSubpotent: bool = None,  subpotentReason: list['CodeableConcept'] = None,  education: list['Education'] = None,  programEligibility: list['CodeableConcept'] = None,  fundingSource: 'CodeableConcept' = None,  reaction: list['Reaction'] = None,  protocolApplied: list['ProtocolApplied'] = None, ):
        self.resourceType: str = resourceType or "Immunization"
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
        self.statusReason: 'CodeableConcept' = statusReason 
        self.vaccineCode: 'CodeableConcept' = vaccineCode 
        self.patient: 'Reference' = patient 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.occurrenceString: str = occurrenceString 
        self.recorded: str = recorded 
        self.primarySource: bool = primarySource 
        self.reportOrigin: 'CodeableConcept' = reportOrigin 
        self.location: 'Reference' = location 
        self.manufacturer: 'Reference' = manufacturer 
        self.lotNumber: str = lotNumber 
        self.expirationDate: str = expirationDate 
        self.site: 'CodeableConcept' = site 
        self.route: 'CodeableConcept' = route 
        self.doseQuantity: 'Quantity' = doseQuantity 
        self.performer: list['Performer'] = performer or []
        self.note: list['Annotation'] = note or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.isSubpotent: bool = isSubpotent 
        self.subpotentReason: list['CodeableConcept'] = subpotentReason or []
        self.education: list['Education'] = education or []
        self.programEligibility: list['CodeableConcept'] = programEligibility or []
        self.fundingSource: 'CodeableConcept' = fundingSource 
        self.reaction: list['Reaction'] = reaction or []
        self.protocolApplied: list['ProtocolApplied'] = protocolApplied or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Immunization":
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