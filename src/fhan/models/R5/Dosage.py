"""
Generated class for Dosage. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Element import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Range import *


@dataclass
class Dosage:
    """ Dosage Type: Indicates how the medication is/was taken or should be taken by the patient.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: The order of the dosage instructions
    :param str text: Free text dosage instructions e.g. SIG
    :param CodeableConcept additionalInstruction: Supplemental instruction or warnings to the patient - e.g. "with meals", "may cause drowsiness"
    :param str patientInstruction: Patient or consumer oriented instructions
    :param Timing timing: When medication should be administered
    :param bool asNeeded: Take "as needed"
    :param CodeableConcept asNeededFor: Take "as needed" (for x)
    :param CodeableConcept site: Body site to administer to
    :param CodeableConcept route: How drug should enter body
    :param CodeableConcept method: Technique for administering medication
    :param Element doseAndRate: Amount of medication administered, to be administered or typical amount to be administered
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param CodeableConcept type: The kind of dose or rate specified
    :param Range doseRange: Amount of medication per dose
    :param Quantity doseRange: Amount of medication per dose
    :param Ratio rateRatio: Amount of medication per unit of time
    :param Range rateRatio: Amount of medication per unit of time
    :param Quantity rateRatio: Amount of medication per unit of time
    :param Ratio maxDosePerPeriod: Upper limit on medication per unit of time
    :param Quantity maxDosePerAdministration: Upper limit on medication per administration
    :param Quantity maxDosePerLifetime: Upper limit on medication per lifetime of the patient
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    sequence: int = None
    
    text: str = None
    
    additionalInstruction: "CodeableConcept" = None
    
    patientInstruction: str = None
    
    timing: "Timing" = None
    
    asNeeded: bool = None
    
    asNeededFor: "CodeableConcept" = None
    
    site: "CodeableConcept" = None
    
    route: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    doseAndRate: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    doseRange: "Range" = None
    
    doseRange: "Quantity" = None
    
    rateRatio: "Ratio" = None
    
    rateRatio: "Range" = None
    
    rateRatio: "Quantity" = None
    
    maxDosePerPeriod: "Ratio" = None
    
    maxDosePerAdministration: "Quantity" = None
    
    maxDosePerLifetime: "Quantity" = None
    