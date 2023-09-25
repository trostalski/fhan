"""
Generated class for CareTeam. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Participant(ModelBase):
    """ Identifies all people and organizations who are expected to be involved in the care team.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['CodeableConcept'] role: Type of involvement
    :param 'Reference' member: Who is involved
    :param 'Reference' onBehalfOf: Organization of the practitioner
    :param 'Period' period: Time period of participant
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  role: list['CodeableConcept'] = None,  member: 'Reference' = None,  onBehalfOf: 'Reference' = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.role: list['CodeableConcept'] = role or []
        self.member: 'Reference' = member 
        self.onBehalfOf: 'Reference' = onBehalfOf 
        self.period: 'Period' = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Participant":
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


class CareTeam(DomainResource):
    """ The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care for a patient.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: External Ids for this team
    :param str status: proposed | active | suspended | inactive | entered-in-error
    :param list['CodeableConcept'] category: Type of team
    :param str name: Name of the team, such as crisis assessment team
    :param 'Reference' subject: Who care team is for
    :param 'Reference' encounter: Encounter created as part of
    :param 'Period' period: Time period team covers
    :param list['Participant'] participant: Members of the team
    :param list['CodeableConcept'] reasonCode: Why the care team exists
    :param list['Reference'] reasonReference: Why the care team exists
    :param list['Reference'] managingOrganization: Organization responsible for the care team
    :param list['ContactPoint'] telecom: A contact detail for the care team (that applies to all members)
    :param list['Annotation'] note: Comments made about the CareTeam
    """
    def __init__(self, resourceType: str = "CareTeam",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  category: list['CodeableConcept'] = None,  name: str = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  period: 'Period' = None,  participant: list['Participant'] = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  managingOrganization: list['Reference'] = None,  telecom: list['ContactPoint'] = None,  note: list['Annotation'] = None, ):
        self.resourceType: str = resourceType or "CareTeam"
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
        self.category: list['CodeableConcept'] = category or []
        self.name: str = name 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.period: 'Period' = period 
        self.participant: list['Participant'] = participant or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.managingOrganization: list['Reference'] = managingOrganization or []
        self.telecom: list['ContactPoint'] = telecom or []
        self.note: list['Annotation'] = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "CareTeam":
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