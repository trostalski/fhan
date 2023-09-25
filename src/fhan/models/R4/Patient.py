"""
Generated class for Patient. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Meta import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Address import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Contact(ModelBase):
    """A contact party (e.g. guardian, partner, friend) for the patient.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] relationship: The kind of relationship
    :param 'HumanName' name: A name associated with the contact person
    :param list['ContactPoint'] telecom: A contact detail for the person
    :param 'Address' address: Address for the contact person
    :param str gender: male | female | other | unknown
    :param 'Reference' organization: Organization that is associated with the contact
    :param 'Period' period: The period during which this contact person or organization is valid to be contacted relating to this patient
    """

    def __init__(
        self,
        id: str = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        relationship: list["CodeableConcept"] = None,
        name: "HumanName" = None,
        telecom: list["ContactPoint"] = None,
        address: "Address" = None,
        gender: str = None,
        organization: "Reference" = None,
        period: "Period" = None,
    ):
        self.id: str = id
        self.extension: list["Extension"] = extension or []
        self.modifierExtension: list["Extension"] = modifierExtension or []
        self.relationship: list["CodeableConcept"] = relationship or []
        self.name: "HumanName" = name
        self.telecom: list["ContactPoint"] = telecom or []
        self.address: "Address" = address
        self.gender: str = gender
        self.organization: "Reference" = organization
        self.period: "Period" = period

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
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


class Communication(ModelBase):
    """A language which may be used to communicate with the patient about his or her health.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' language: The language which can be used to communicate with the patient about his or her health
    :param bool preferred: Language preference indicator
    """

    def __init__(
        self,
        id: str = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        language: "CodeableConcept" = None,
        preferred: bool = None,
    ):
        self.id: str = id
        self.extension: list["Extension"] = extension or []
        self.modifierExtension: list["Extension"] = modifierExtension or []
        self.language: "CodeableConcept" = language
        self.preferred: bool = preferred

    @classmethod
    def from_dict(cls, data: dict) -> "Communication":
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


class Link(ModelBase):
    """Link to another patient resource that concerns the same actual patient.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' other: The other patient or related person resource that the link refers to
    :param str type: replaced-by | replaces | refer | seealso
    """

    def __init__(
        self,
        id: str = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        other: "Reference" = None,
        type: str = None,
    ):
        self.id: str = id
        self.extension: list["Extension"] = extension or []
        self.modifierExtension: list["Extension"] = modifierExtension or []
        self.other: "Reference" = other
        self.type: str = type

    @classmethod
    def from_dict(cls, data: dict) -> "Link":
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


class Patient(DomainResource):
    """Demographics and other administrative information about an individual or animal receiving care or other health-related services.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: An identifier for this patient
    :param bool active: Whether this patient's record is in active use
    :param list['HumanName'] name: A name associated with the patient
    :param list['ContactPoint'] telecom: A contact detail for the individual
    :param str gender: male | female | other | unknown
    :param str birthDate: The date of birth for the individual
    :param bool deceasedBoolean: Indicates if the individual is deceased or not
    :param str deceasedDateTime: Indicates if the individual is deceased or not
    :param list['Address'] address: An address for the individual
    :param 'CodeableConcept' maritalStatus: Marital (civil) status of a patient
    :param bool multipleBirthBoolean: Whether patient is part of a multiple birth
    :param int multipleBirthInteger: Whether patient is part of a multiple birth
    :param list['Attachment'] photo: Image of the patient
    :param list['Contact'] contact: A contact party (e.g. guardian, partner, friend) for the patient
    :param list['Communication'] communication: A language which may be used to communicate with the patient about his or her health
    :param list['Reference'] generalPractitioner: Patient's nominated primary care provider
    :param 'Reference' managingOrganization: Organization that is the custodian of the patient record
    :param list['Link'] link: Link to another patient resource that concerns the same actual person
    """

    def __init__(
        self,
        resourceType: str = "Patient",
        id: str = None,
        meta: "Meta" = None,
        implicitRules: str = None,
        language: str = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        identifier: list["Identifier"] = None,
        active: bool = None,
        name: list["HumanName"] = None,
        telecom: list["ContactPoint"] = None,
        gender: str = None,
        birthDate: str = None,
        deceasedBoolean: bool = None,
        deceasedDateTime: str = None,
        address: list["Address"] = None,
        maritalStatus: "CodeableConcept" = None,
        multipleBirthBoolean: bool = None,
        multipleBirthInteger: int = None,
        photo: list["Attachment"] = None,
        contact: list["Contact"] = None,
        communication: list["Communication"] = None,
        generalPractitioner: list["Reference"] = None,
        managingOrganization: "Reference" = None,
        link: list["Link"] = None,
    ):
        self.resourceType: str = resourceType or "Patient"
        self.id: str = id
        self.meta: "Meta" = meta
        self.implicitRules: str = implicitRules
        self.language: str = language
        self.text: "Narrative" = text
        self.contained: list["Resource"] = contained or []
        self.extension: list["Extension"] = extension or []
        self.modifierExtension: list["Extension"] = modifierExtension or []
        self.identifier: list["Identifier"] = identifier or []
        self.active: bool = active
        self.name: list["HumanName"] = name or []
        self.telecom: list["ContactPoint"] = telecom or []
        self.gender: str = gender
        self.birthDate: str = birthDate
        self.deceasedBoolean: bool = deceasedBoolean
        self.deceasedDateTime: str = deceasedDateTime
        self.address: list["Address"] = address or []
        self.maritalStatus: "CodeableConcept" = maritalStatus
        self.multipleBirthBoolean: bool = multipleBirthBoolean
        self.multipleBirthInteger: int = multipleBirthInteger
        self.photo: list["Attachment"] = photo or []
        self.contact: list["Contact"] = contact or []
        self.communication: list["Communication"] = communication or []
        self.generalPractitioner: list["Reference"] = generalPractitioner or []
        self.managingOrganization: "Reference" = managingOrganization
        self.link: list["Link"] = link or []

    @classmethod
    def from_dict(cls, data: dict) -> "Patient":
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
