"""
Generated class for MedicationStatement. 
Time: 2023-09-27 15:54:17
"""
from importlib import import_module
import inspect

from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class MedicationStatement(DomainResource):
    """ A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the patient may be taking the medication now or has taken the medication in the past or will be taking the medication in the future.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay.   The medication information may come from sources such as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or other party maintains. 

The primary difference between a medication statement and a medication administration is that the medication administration has complete administration information and is based on actual administration information from the person who administered the medication.  A medication statement is often, if not always, less specific.  There is no required date/time when the medication was administered, in fact we only know that a source has reported the patient is taking this medication, where details such as time, quantity, or rate or even medication product may be incomplete or missing or less precise.  As stated earlier, the medication statement information may come from the patient's memory, from a prescription bottle or from a list of medications the patient, clinician or other party maintains.  Medication administration is more formal and is not missing detailed information.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param 'Resource' contained: Contained, inline Resources
    :param 'Extension' extension: Additional content defined by implementations
    :param 'Extension' modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' identifier: External identifier
    :param 'Reference' basedOn: Fulfils plan, proposal or order
    :param 'Reference' partOf: Part of referenced event
    :param str status: active | completed | entered-in-error | intended | stopped | on-hold | unknown | not-taken
    :param 'CodeableConcept' statusReason: Reason for current status
    :param 'CodeableConcept' category: Type of medication usage
    :param 'CodeableConcept' medicationCodeableConcept: What medication was taken
    :param 'Reference' medicationReference: What medication was taken
    :param 'Reference' subject: Who is/was taking  the medication
    :param 'Reference' context: Encounter / Episode associated with MedicationStatement
    :param str effectiveDateTime: The date/time or interval when the medication is/was/will be taken
    :param 'Period' effectivePeriod: The date/time or interval when the medication is/was/will be taken
    :param str dateAsserted: When the statement was asserted?
    :param 'Reference' informationSource: Person or organization that provided the information about the taking of this medication
    :param 'Reference' derivedFrom: Additional supporting information
    :param 'CodeableConcept' reasonCode: Reason for why the medication is being/was taken
    :param 'Reference' reasonReference: Condition or observation that supports why the medication is being/was taken
    :param 'Annotation' note: Further information about the statement
    :param 'Dosage' dosage: Details of how medication is/was taken or should be taken
    """
    def __init__(self, resourceType: str = "MedicationStatement",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: 'Resource' = None,  extension: 'Extension' = None,  modifierExtension: 'Extension' = None,  identifier: 'Identifier' = None,  basedOn: 'Reference' = None,  partOf: 'Reference' = None,  status: str = None,  statusReason: 'CodeableConcept' = None,  category: 'CodeableConcept' = None,  medicationCodeableConcept: 'CodeableConcept' = None,  medicationReference: 'Reference' = None,  subject: 'Reference' = None,  context: 'Reference' = None,  effectiveDateTime: str = None,  effectivePeriod: 'Period' = None,  dateAsserted: str = None,  informationSource: 'Reference' = None,  derivedFrom: 'Reference' = None,  reasonCode: 'CodeableConcept' = None,  reasonReference: 'Reference' = None,  note: 'Annotation' = None,  dosage: 'Dosage' = None, ):
        self.resourceType: str = resourceType or "MedicationStatement"
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
        self.partOf: list['Reference'] = partOf or []
        self.status: str = status 
        self.statusReason: list['CodeableConcept'] = statusReason or []
        self.category: 'CodeableConcept' = category 
        self.medicationCodeableConcept: 'CodeableConcept' = medicationCodeableConcept 
        self.medicationReference: 'Reference' = medicationReference 
        self.subject: 'Reference' = subject 
        self.context: 'Reference' = context 
        self.effectiveDateTime: str = effectiveDateTime 
        self.effectivePeriod: 'Period' = effectivePeriod 
        self.dateAsserted: str = dateAsserted 
        self.informationSource: 'Reference' = informationSource 
        self.derivedFrom: list['Reference'] = derivedFrom or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.note: list['Annotation'] = note or []
        self.dosage: list['Dosage'] = dosage or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationStatement":
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