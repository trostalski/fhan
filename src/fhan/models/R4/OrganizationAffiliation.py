"""
Generated class for OrganizationAffiliation. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class OrganizationAffiliation(DomainResource):
    """ Defines an affiliation/assotiation/relationship between 2 distinct oganizations, that is not a part-of relationship/sub-division relationship.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifiers that are specific to this role
    :param bool active: Whether this organization affiliation record is in active use
    :param 'Period' period: The period during which the participatingOrganization is affiliated with the primary organization
    :param 'Reference' organization: Organization where the role is available
    :param 'Reference' participatingOrganization: Organization that provides/performs the role (e.g. providing services or is a member of)
    :param list['Reference'] network: Health insurance provider network in which the participatingOrganization provides the role's services (if defined) at the indicated locations (if defined)
    :param list['CodeableConcept'] code: Definition of the role the participatingOrganization plays
    :param list['CodeableConcept'] specialty: Specific specialty of the participatingOrganization in the context of the role
    :param list['Reference'] location: The location(s) at which the role occurs
    :param list['Reference'] healthcareService: Healthcare services provided through the role
    :param list['ContactPoint'] telecom: Contact details at the participatingOrganization relevant to this Affiliation
    :param list['Reference'] endpoint: Technical endpoints providing access to services operated for this role
    """
    def __init__(self, resourceType: str = "OrganizationAffiliation",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  active: bool = None,  period: 'Period' = None,  organization: 'Reference' = None,  participatingOrganization: 'Reference' = None,  network: list['Reference'] = None,  code: list['CodeableConcept'] = None,  specialty: list['CodeableConcept'] = None,  location: list['Reference'] = None,  healthcareService: list['Reference'] = None,  telecom: list['ContactPoint'] = None,  endpoint: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "OrganizationAffiliation"
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
        self.period: 'Period' = period 
        self.organization: 'Reference' = organization 
        self.participatingOrganization: 'Reference' = participatingOrganization 
        self.network: list['Reference'] = network or []
        self.code: list['CodeableConcept'] = code or []
        self.specialty: list['CodeableConcept'] = specialty or []
        self.location: list['Reference'] = location or []
        self.healthcareService: list['Reference'] = healthcareService or []
        self.telecom: list['ContactPoint'] = telecom or []
        self.endpoint: list['Reference'] = endpoint or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "OrganizationAffiliation":
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