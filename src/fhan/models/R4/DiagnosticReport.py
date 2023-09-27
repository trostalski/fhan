"""
Generated class for DiagnosticReport. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


    
    

class Media(BaseModel):
    """ A list of key images associated with this report. The images are generally created during the diagnostic process, and may be directly of the patient, or of treated specimens (i.e. slides of interest).:param str id: Unique id for inter-element referencing
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str comment: Comment about the image (e.g. explanation)
    :param 'Reference' link: Reference to the image source
    """
    def __init__(self,  id: str = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  comment: str = None,  link: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.comment: str = comment 
        self.link: 'Reference' = link 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Media":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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


class DiagnosticReport(DomainResource):
    """ The findings and interpretation of diagnostic  tests performed on patients, groups of patients, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting and provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: Business identifier for report
    :param 'Reference' basedOn: What was requested
    :param str status: registered | partial | preliminary | final +
    :param 'CodeableConcept' category: Service category
    :param 'CodeableConcept' code: Name/Code for this diagnostic report
    :param 'Reference' subject: The subject of the report - usually, but not always, the patient
    :param 'Reference' encounter: Health care event when test ordered
    :param str effectiveDateTime: Clinically relevant time/time-period for report
    :param 'Period' effectivePeriod: Clinically relevant time/time-period for report
    :param str issued: DateTime this version was made
    :param 'Reference' performer: Responsible Diagnostic Service
    :param 'Reference' resultsInterpreter: Primary result interpreter
    :param 'Reference' specimen: Specimens this report is based on
    :param 'Reference' result: Observations
    :param 'Reference' imagingStudy: Reference to full details of imaging associated with the diagnostic report
    :param 'Media' media: Key images associated with this report
    :param str conclusion: Clinical conclusion (interpretation) of test results
    :param 'CodeableConcept' conclusionCode: Codes for the clinical conclusion of test results
    :param 'Attachment' presentedForm: Entire report as issued
    """
    def __init__(self, resourceType: str = "DiagnosticReport",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  basedOn: 'Reference' = None,  status: str = None,  category: 'CodeableConcept' = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  effectiveDateTime: str = None,  effectivePeriod: 'Period' = None,  issued: str = None,  performer: 'Reference' = None,  resultsInterpreter: 'Reference' = None,  specimen: 'Reference' = None,  result: 'Reference' = None,  imagingStudy: 'Reference' = None,  media: 'Media' = None,  conclusion: str = None,  conclusionCode: 'CodeableConcept' = None,  presentedForm: 'Attachment' = None, ):
        self.resourceType: str = resourceType or "DiagnosticReport"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.basedOn: list['Reference'] = basedOn or []
        self.status: str = status 
        self.category: list['CodeableConcept'] = category or []
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.effectiveDateTime: str = effectiveDateTime 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.issued: str = issued 
        self.performer: list['Reference'] = performer or []
        self.resultsInterpreter: list['Reference'] = resultsInterpreter or []
        self.specimen: list['Reference'] = specimen or []
        self.result: list['Reference'] = result or []
        self.imagingStudy: list['Reference'] = imagingStudy or []
        self.media: list['Media'] = media or []
        self.conclusion: str = conclusion 
        self.conclusionCode: list['CodeableConcept'] = conclusionCode or []
        self.presentedForm: list['Attachment'] = presentedForm or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "DiagnosticReport":
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
                # Check if the class is a subclass of BaseModel
                if inspect.isclass(model_class) and issubclass(model_class, BaseModel):
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