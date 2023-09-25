"""
Generated class for GuidanceResponse. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class GuidanceResponse(DomainResource):
    """ A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' requestIdentifier: The identifier of the request associated with this response, if any
    :param list['Identifier'] identifier: Business identifier
    :param str moduleUri: What guidance was requested
    :param str moduleCanonical: What guidance was requested
    :param 'CodeableConcept' moduleCodeableConcept: What guidance was requested
    :param str status: success | data-requested | data-required | in-progress | failure | entered-in-error
    :param 'Reference' subject: Patient the request was performed for
    :param 'Reference' encounter: Encounter during which the response was returned
    :param str occurrenceDateTime: When the guidance response was processed
    :param 'Reference' performer: Device returning the guidance
    :param list['CodeableConcept'] reasonCode: Why guidance is needed
    :param list['Reference'] reasonReference: Why guidance is needed
    :param list['Annotation'] note: Additional notes about the response
    :param list['Reference'] evaluationMessage: Messages resulting from the evaluation of the artifact or artifacts
    :param 'Reference' outputParameters: The output parameters of the evaluation, if any
    :param 'Reference' result: Proposed actions, if any
    :param list['DataRequirement'] dataRequirement: Additional required data
    """
    def __init__(self, resourceType: str = "GuidanceResponse",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  requestIdentifier: 'Identifier' = None,  identifier: list['Identifier'] = None,  moduleUri: str = None,  moduleCanonical: str = None,  moduleCodeableConcept: 'CodeableConcept' = None,  status: str = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  occurrenceDateTime: str = None,  performer: 'Reference' = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  note: list['Annotation'] = None,  evaluationMessage: list['Reference'] = None,  outputParameters: 'Reference' = None,  result: 'Reference' = None,  dataRequirement: list['DataRequirement'] = None, ):
        self.resourceType: str = resourceType or "GuidanceResponse"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.requestIdentifier: 'Identifier' = requestIdentifier 
        self.identifier: list['Identifier'] = identifier or []
        self.moduleUri: str = moduleUri 
        self.moduleCanonical: str = moduleCanonical 
        self.moduleCodeableConcept: 'CodeableConcept' = moduleCodeableConcept 
        self.status: str = status 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.performer: 'Reference' = performer 
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        self.evaluationMessage: list['Reference'] = evaluationMessage or []
        self.outputParameters: 'Reference' = outputParameters 
        self.result: 'Reference' = result 
        self.dataRequirement: list['DataRequirement'] = dataRequirement or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "GuidanceResponse":
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