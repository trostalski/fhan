"""
Generated class for Dosage. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Element import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Range import *
from fhan.models.R5.Timing import *
from fhan.models.generator_models import BaseModel

    
    

class DoseAndRate(BaseModel):
    """ Depending on the resource,this is the amount of medication administered, to  be administered or typical amount to be administered.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param CodeableConcept type: The kind of dose or rate specified
    :param Range doseRange: Amount of medication per dose
    :param Quantity doseQuantity: Amount of medication per dose
    :param Ratio rateRatio: Amount of medication per unit of time
    :param Range rateRange: Amount of medication per unit of time
    :param Quantity rateQuantity: Amount of medication per unit of time
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "doseRange": {"class_name": "Range", "is_contained": False},
        
        
        "doseQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "rateRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        "rateRange": {"class_name": "Range", "is_contained": False},
        
        
        "rateQuantity": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  doseRange:  'Range'  = None,  doseQuantity:  'Quantity'  = None,  rateRatio:  'Ratio'  = None,  rateRange:  'Range'  = None,  rateQuantity:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.type = type 
        self.doseRange = doseRange 
        self.doseQuantity = doseQuantity 
        self.rateRatio = rateRatio 
        self.rateRange = rateRange 
        self.rateQuantity = rateQuantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Dosage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Dosage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Dosage(BaseModel):
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
    :param DoseAndRate doseAndRate: Amount of medication administered, to be administered or typical amount to be administered
    :param Ratio maxDosePerPeriod: Upper limit on medication per unit of time
    :param Quantity maxDosePerAdministration: Upper limit on medication per administration
    :param Quantity maxDosePerLifetime: Upper limit on medication per lifetime of the patient
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "additionalInstruction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "timing": {"class_name": "Timing", "is_contained": False},
        
        
        
        "asNeededFor": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "site": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "route": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "doseAndRate": {"class_name": "DoseAndRate", "is_contained": True},
        
        
        "maxDosePerPeriod": {"class_name": "Ratio", "is_contained": False},
        
        
        "maxDosePerAdministration": {"class_name": "Quantity", "is_contained": False},
        
        
        "maxDosePerLifetime": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  sequence:  'int'  = None,  text:  'str'  = None,  additionalInstruction:  list['CodeableConcept']  = None,  patientInstruction:  'str'  = None,  timing:  'Timing'  = None,  asNeeded:  'bool'  = None,  asNeededFor:  list['CodeableConcept']  = None,  site:  'CodeableConcept'  = None,  route:  'CodeableConcept'  = None,  method:  'CodeableConcept'  = None,  doseAndRate:  list['DoseAndRate']  = None,  maxDosePerPeriod:  list['Ratio']  = None,  maxDosePerAdministration:  'Quantity'  = None,  maxDosePerLifetime:  'Quantity'  = None, ):
        self.resourceType = resourceType or "Dosage"
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.sequence = sequence 
        self.text = text 
        self.additionalInstruction = additionalInstruction or []
        self.patientInstruction = patientInstruction 
        self.timing = timing 
        self.asNeeded = asNeeded 
        self.asNeededFor = asNeededFor or []
        self.site = site 
        self.route = route 
        self.method = method 
        self.doseAndRate = doseAndRate or []
        self.maxDosePerPeriod = maxDosePerPeriod or []
        self.maxDosePerAdministration = maxDosePerAdministration 
        self.maxDosePerLifetime = maxDosePerLifetime 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Dosage":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Dosage":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()