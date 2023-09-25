"""
Generated class for Dosage. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Range import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase

    
    

class DoseAndRate(ModelBase):
    """ The amount of medication administered.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'CodeableConcept' type: The kind of dose or rate specified
    :param 'Range' doseRange: Amount of medication per dose
    :param 'Quantity' doseQuantity: Amount of medication per dose
    :param 'Ratio' rateRatio: Amount of medication per unit of time
    :param 'Range' rateRange: Amount of medication per unit of time
    :param 'Quantity' rateQuantity: Amount of medication per unit of time
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  type: 'CodeableConcept' = None,  doseRange: 'Range' = None,  doseQuantity: 'Quantity' = None,  rateRatio: 'Ratio' = None,  rateRange: 'Range' = None,  rateQuantity: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: 'CodeableConcept' = type 
        self.doseRange: 'Range' = doseRange 
        self.doseQuantity: 'Quantity' = doseQuantity 
        self.rateRatio: 'Ratio' = rateRatio 
        self.rateRange: 'Range' = rateRange 
        self.rateQuantity: 'Quantity' = rateQuantity 
        

class Dosage(ModelBase):
    """ Base StructureDefinition for Dosage Type: Indicates how the medication is/was taken or should be taken by the patient.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int sequence: The order of the dosage instructions
    :param str text: Free text dosage instructions e.g. SIG
    :param list['CodeableConcept'] additionalInstruction: Supplemental instruction or warnings to the patient - e.g. "with meals", "may cause drowsiness"
    :param str patientInstruction: Patient or consumer oriented instructions
    :param 'Timing' timing: When medication should be administered
    :param bool asNeededBoolean: Take "as needed" (for x)
    :param 'CodeableConcept' asNeededCodeableConcept: Take "as needed" (for x)
    :param 'CodeableConcept' site: Body site to administer to
    :param 'CodeableConcept' route: How drug should enter body
    :param 'CodeableConcept' method: Technique for administering medication
    :param list['DoseAndRate'] doseAndRate: Amount of medication administered
    :param 'Ratio' maxDosePerPeriod: Upper limit on medication per unit of time
    :param 'Quantity' maxDosePerAdministration: Upper limit on medication per administration
    :param 'Quantity' maxDosePerLifetime: Upper limit on medication per lifetime of the patient
    """
    def __init__(self, resourceType: str = "Dosage",  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  sequence: int = None,  text: str = None,  additionalInstruction: list['CodeableConcept'] = None,  patientInstruction: str = None,  timing: 'Timing' = None,  asNeededBoolean: bool = None,  asNeededCodeableConcept: 'CodeableConcept' = None,  site: 'CodeableConcept' = None,  route: 'CodeableConcept' = None,  method: 'CodeableConcept' = None,  doseAndRate: list['DoseAndRate'] = None,  maxDosePerPeriod: 'Ratio' = None,  maxDosePerAdministration: 'Quantity' = None,  maxDosePerLifetime: 'Quantity' = None, ):
        self.resourceType: str = resourceType or "Dosage"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.sequence: int = sequence 
        self.text: str = text 
        self.additionalInstruction: list['CodeableConcept'] = additionalInstruction or []
        self.patientInstruction: str = patientInstruction 
        self.timing: 'Timing' = timing 
        self.asNeededBoolean: bool = asNeededBoolean 
        self.asNeededCodeableConcept: 'CodeableConcept' = asNeededCodeableConcept 
        self.site: 'CodeableConcept' = site 
        self.route: 'CodeableConcept' = route 
        self.method: 'CodeableConcept' = method 
        self.doseAndRate: list['DoseAndRate'] = doseAndRate or []
        self.maxDosePerPeriod: 'Ratio' = maxDosePerPeriod 
        self.maxDosePerAdministration: 'Quantity' = maxDosePerAdministration 
        self.maxDosePerLifetime: 'Quantity' = maxDosePerLifetime 
        