"""
Generated class for MedicationStatement. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Adherence(BaseModel):
    """ Indicates whether the medication is or is not being consumed or administered.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of adherence
    :param CodeableConcept reason: Details of the reason for the current use of the medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  reason:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.reason = reason 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationStatement":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicationStatement(DomainResource):
    """ A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the patient may be taking the medication now or has taken the medication in the past or will be taking the medication in the future.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay.   The medication information may come from sources such as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or other party maintains. 

The primary difference between a medicationstatement and a medicationadministration is that the medication administration has complete administration information and is based on actual administration information from the person who administered the medication.  A medicationstatement is often, if not always, less specific.  There is no required date/time when the medication was administered, in fact we only know that a source has reported the patient is taking this medication, where details such as time, quantity, or rate or even medication product may be incomplete or missing or less precise.  As stated earlier, the Medication Statement information may come from the patient's memory, from a prescription bottle or from a list of medications the patient, clinician or other party maintains.  Medication administration is more formal and is not missing detailed information.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param Reference partOf: Part of referenced event
    :param str status: recorded | entered-in-error | draft
    :param CodeableConcept category: Type of medication statement
    :param CodeableReference medication: What medication was taken
    :param Reference subject: Who is/was taking  the medication
    :param Reference encounter: Encounter associated with MedicationStatement
    :param str effectiveDateTime: The date/time or interval when the medication is/was/will be taken
    :param Period effectivePeriod: The date/time or interval when the medication is/was/will be taken
    :param Timing effectiveTiming: The date/time or interval when the medication is/was/will be taken
    :param str dateAsserted: When the usage was asserted?
    :param Reference informationSource: Person or organization that provided the information about the taking of this medication
    :param Reference derivedFrom: Link to information used to derive the MedicationStatement
    :param CodeableReference reason: Reason for why the medication is being/was taken
    :param Annotation note: Further information about the usage
    :param Reference relatedClinicalInformation: Link to information relevant to the usage of a medication
    :param str renderedDosageInstruction: Full representation of the dosage instructions
    :param Dosage dosage: Details of how medication is/was taken or should be taken
    :param Adherence adherence: Indicates whether the medication is or is not being consumed or administered
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "medication": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "effectiveTiming": {"class_name": "Timing", "is_contained": False},
        
        
        
        "informationSource": {"class_name": "Reference", "is_contained": False},
        
        
        "derivedFrom": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "relatedClinicalInformation": {"class_name": "Reference", "is_contained": False},
        
        
        
        "dosage": {"class_name": "Dosage", "is_contained": False},
        
        
        "adherence": {"class_name": "Adherence", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  partOf:  list['Reference']  = None,  status:  'str'  = None,  category:  list['CodeableConcept']  = None,  medication:  'CodeableReference'  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  effectiveDateTime:  'str'  = None,  effectivePeriod:  'Period'  = None,  effectiveTiming:  'Timing'  = None,  dateAsserted:  'str'  = None,  informationSource:  list['Reference']  = None,  derivedFrom:  list['Reference']  = None,  reason:  list['CodeableReference']  = None,  note:  list['Annotation']  = None,  relatedClinicalInformation:  list['Reference']  = None,  renderedDosageInstruction:  'str'  = None,  dosage:  list['Dosage']  = None,  adherence:  'Adherence'  = None, ):
        self.resourceType = resourceType or "MedicationStatement"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.partOf = partOf or []
        self.status = status 
        self.category = category or []
        self.medication = medication 
        self.subject = subject 
        self.encounter = encounter 
        self.effectiveDateTime = effectiveDateTime 
        self.effectivePeriod = effectivePeriod 
        self.effectiveTiming = effectiveTiming 
        self.dateAsserted = dateAsserted 
        self.informationSource = informationSource or []
        self.derivedFrom = derivedFrom or []
        self.reason = reason or []
        self.note = note or []
        self.relatedClinicalInformation = relatedClinicalInformation or []
        self.renderedDosageInstruction = renderedDosageInstruction 
        self.dosage = dosage or []
        self.adherence = adherence 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationStatement":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationStatement":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()