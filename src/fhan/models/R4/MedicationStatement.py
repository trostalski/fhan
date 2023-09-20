"""
Generated class for MedicationStatement. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase
@dataclass
class MedicationStatement(ModelBase):
    """ A record of a medication that is being consumed by a patient.   A MedicationStatement may indicate that the patient may be taking the medication now or has taken the medication in the past or will be taking the medication in the future.  The source of this information can be the patient, significant other (such as a family member or spouse), or a clinician.  A common scenario where this information is captured is during the history taking process during a patient visit or stay.   The medication information may come from sources such as the patient's memory, from a prescription bottle,  or from a list of medications the patient, clinician or other party maintains. 

The primary difference between a medication statement and a medication administration is that the medication administration has complete administration information and is based on actual administration information from the person who administered the medication.  A medication statement is often, if not always, less specific.  There is no required date/time when the medication was administered, in fact we only know that a source has reported the patient is taking this medication, where details such as time, quantity, or rate or even medication product may be incomplete or missing or less precise.  As stated earlier, the medication statement information may come from the patient's memory, from a prescription bottle or from a list of medications the patient, clinician or other party maintains.  Medication administration is more formal and is not missing detailed information.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param Reference basedOn: Fulfils plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param str status: active | completed | entered-in-error | intended | stopped | on-hold | unknown | not-taken
    :param CodeableConcept statusReason: Reason for current status
    :param CodeableConcept category: Type of medication usage
    :param CodeableConcept medicationCodeableConcept: What medication was taken
    :param Reference subject: Who is/was taking  the medication
    :param Reference context: Encounter / Episode associated with MedicationStatement
    :param str effectiveDateTime: The date/time or interval when the medication is/was/will be taken
    :param str dateAsserted: When the statement was asserted?
    :param Reference informationSource: Person or organization that provided the information about the taking of this medication
    :param Reference derivedFrom: Additional supporting information
    :param CodeableConcept reasonCode: Reason for why the medication is being/was taken
    :param Reference reasonReference: Condition or observation that supports why the medication is being/was taken
    :param Annotation note: Further information about the statement
    :param Dosage dosage: Details of how medication is/was taken or should be taken
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    basedOn: list["Reference"] = None
    
    partOf: list["Reference"] = None
    
    status: str = None
    
    statusReason: list["CodeableConcept"] = None
    
    category: "CodeableConcept" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    effectiveDateTime: str = None
    
    dateAsserted: str = None
    
    informationSource: "Reference" = None
    
    derivedFrom: list["Reference"] = None
    
    reasonCode: list["CodeableConcept"] = None
    
    reasonReference: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    dosage: list["Dosage"] = None
    