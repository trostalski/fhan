"""
Generated class for MedicationKnowledge. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Money import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class RelatedMedicationKnowledge(BaseModel):
    """ Associated or related medications. For example, if the medication is a branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g. Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this would link to a branded product (e.g. Crestor.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of medicationKnowledge
    :param Reference reference: Associated documentation about the associated medication knowledge
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  reference:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.reference = reference or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Monograph(BaseModel):
    """ Associated documentation about the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of medication document
    :param Reference source: Associated documentation about the medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "source": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  source:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.source = source 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Cost(BaseModel):
    """ The price of the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period effectiveDate: The date range for which the cost is effective
    :param CodeableConcept type: The category of the cost information
    :param str source: The source or owner for the price information
    :param Money costMoney: The price or category of the cost of the medication
    :param CodeableConcept costCodeableConcept: The price or category of the cost of the medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "effectiveDate": {"class_name": "Period", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "costMoney": {"class_name": "Money", "is_contained": False},
        
        
        "costCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  effectiveDate:  list['Period']  = None,  type:  'CodeableConcept'  = None,  source:  'str'  = None,  costMoney:  'Money'  = None,  costCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.effectiveDate = effectiveDate or []
        self.type = type 
        self.source = source 
        self.costMoney = costMoney 
        self.costCodeableConcept = costCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class MonitoringProgram(BaseModel):
    """ The program under which the medication is reviewed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  name:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.name = name 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class Dosage(BaseModel):
    """ Dosage for the medication for the specific guidelines.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of dosage for a medication
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "dosage": {"class_name": "Dosage", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  dosage:  list['Dosage']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.dosage = dosage or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class PatientCharacteristic(BaseModel):
    """ Characteristics of the patient that are relevant to the administration guidelines (for example, height, weight, gender, etc.).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Categorization of specific characteristic that is relevant to the administration guideline
    :param CodeableConcept valueCodeableConcept: The specific characteristic
    :param Quantity valueQuantity: The specific characteristic
    :param Range valueRange: The specific characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class DosingGuideline(BaseModel):
    """ The guidelines for the dosage of the medication for the indication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept treatmentIntent: Intention of the treatment
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    :param CodeableConcept administrationTreatment: Type of treatment the guideline applies to
    :param PatientCharacteristic patientCharacteristic: Characteristics of the patient that are relevant to the administration guidelines
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "treatmentIntent": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "dosage": {"class_name": "Dosage", "is_contained": True},
        
        
        "administrationTreatment": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "patientCharacteristic": {"class_name": "PatientCharacteristic", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  treatmentIntent:  'CodeableConcept'  = None,  dosage:  list['Dosage']  = None,  administrationTreatment:  'CodeableConcept'  = None,  patientCharacteristic:  list['PatientCharacteristic']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.treatmentIntent = treatmentIntent 
        self.dosage = dosage or []
        self.administrationTreatment = administrationTreatment 
        self.patientCharacteristic = patientCharacteristic or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class IndicationGuideline(BaseModel):
    """ Guidelines or protocols that are applicable for the administration of the medication based on indication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference indication: Indication for use that applies to the specific administration guideline
    :param DosingGuideline dosingGuideline: Guidelines for dosage of the medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "indication": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "dosingGuideline": {"class_name": "DosingGuideline", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  indication:  list['CodeableReference']  = None,  dosingGuideline:  list['DosingGuideline']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.indication = indication or []
        self.dosingGuideline = dosingGuideline or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class MedicineClassification(BaseModel):
    """ Categorization of the medication within a formulary or classification system.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param str sourceString: The source of the classification
    :param str sourceUri: The source of the classification
    :param CodeableConcept classification: Specific category assigned to the medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  sourceString:  'str'  = None,  sourceUri:  'str'  = None,  classification:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.sourceString = sourceString 
        self.sourceUri = sourceUri 
        self.classification = classification or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Packaging(BaseModel):
    """ Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Cost cost: Cost of the packaged medication
    :param Reference packagedProduct: The packaged medication that is being priced
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "cost": {"class_name": "Cost", "is_contained": True},
        
        
        "packagedProduct": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  cost:  list['Cost']  = None,  packagedProduct:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.cost = cost or []
        self.packagedProduct = packagedProduct 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class EnvironmentalSetting(BaseModel):
    """ Describes a setting/value on the environment for the adequate storage of the medication and other substances.  Environment settings may involve temperature, humidity, or exposure to light.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Categorization of the setting
    :param Quantity valueQuantity: Value of the setting
    :param Range valueRange: Value of the setting
    :param CodeableConcept valueCodeableConcept: Value of the setting
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueCodeableConcept = valueCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class StorageGuideline(BaseModel):
    """ Information on how the medication should be stored, for example, refrigeration temperatures and length of stability at a given temperature.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str reference: Reference to additional information
    :param Annotation note: Additional storage notes
    :param Duration stabilityDuration: Duration remains stable
    :param EnvironmentalSetting environmentalSetting: Setting or value of environment for adequate storage
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "stabilityDuration": {"class_name": "Duration", "is_contained": False},
        
        
        "environmentalSetting": {"class_name": "EnvironmentalSetting", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  reference:  'str'  = None,  note:  list['Annotation']  = None,  stabilityDuration:  'Duration'  = None,  environmentalSetting:  list['EnvironmentalSetting']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.reference = reference 
        self.note = note or []
        self.stabilityDuration = stabilityDuration 
        self.environmentalSetting = environmentalSetting or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Substitution(BaseModel):
    """ Specifies if changes are allowed when dispensing a medication from a regulatory perspective.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  allowed:  'bool'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.allowed = allowed 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class MaxDispense(BaseModel):
    """ The maximum number of units of the medication that can be dispensed in a period.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The maximum number of units of the medication that can be dispensed
    :param Duration period: The period that applies to the maximum number of units
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "period": {"class_name": "Duration", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  quantity:  'Quantity'  = None,  period:  'Duration'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.quantity = quantity 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Regulatory(BaseModel):
    """ Regulatory information about a medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference regulatoryAuthority: Specifies the authority of the regulation
    :param Substitution substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param CodeableConcept schedule: Specifies the schedule of a medication in jurisdiction
    :param MaxDispense maxDispense: The maximum number of units of the medication that can be dispensed in a period
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "regulatoryAuthority": {"class_name": "Reference", "is_contained": False},
        
        
        "substitution": {"class_name": "Substitution", "is_contained": True},
        
        
        "schedule": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "maxDispense": {"class_name": "MaxDispense", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  regulatoryAuthority:  'Reference'  = None,  substitution:  list['Substitution']  = None,  schedule:  list['CodeableConcept']  = None,  maxDispense:  'MaxDispense'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.regulatoryAuthority = regulatoryAuthority 
        self.substitution = substitution or []
        self.schedule = schedule or []
        self.maxDispense = maxDispense 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Ingredient(BaseModel):
    """ Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: Substances contained in the medication
    :param CodeableConcept type: A code that defines the type of ingredient, active, base, etc
    :param Ratio strengthRatio: Quantity of ingredient present
    :param CodeableConcept strengthCodeableConcept: Quantity of ingredient present
    :param Quantity strengthQuantity: Quantity of ingredient present
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "item": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "strengthRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        "strengthCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "strengthQuantity": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  item:  'CodeableReference'  = None,  type:  'CodeableConcept'  = None,  strengthRatio:  'Ratio'  = None,  strengthCodeableConcept:  'CodeableConcept'  = None,  strengthQuantity:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.item = item 
        self.type = type 
        self.strengthRatio = strengthRatio 
        self.strengthCodeableConcept = strengthCodeableConcept 
        self.strengthQuantity = strengthQuantity 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class DrugCharacteristic(BaseModel):
    """ Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic of medication
    :param CodeableConcept valueCodeableConcept: Description of the characteristic
    :param str valueString: Description of the characteristic
    :param Quantity valueQuantity: Description of the characteristic
    :param str valueBase64Binary: Description of the characteristic
    :param Attachment valueAttachment: Description of the characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueString:  'str'  = None,  valueQuantity:  'Quantity'  = None,  valueBase64Binary:  'str'  = None,  valueAttachment:  'Attachment'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueString = valueString 
        self.valueQuantity = valueQuantity 
        self.valueBase64Binary = valueBase64Binary 
        self.valueAttachment = valueAttachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Definitional(BaseModel):
    """ Along with the link to a Medicinal Product Definition resource, this information provides common definitional elements that are needed to understand the specific medication that is being described.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference definition: Definitional resources that provide more information about this medication
    :param CodeableConcept doseForm: powder | tablets | capsule +
    :param CodeableConcept intendedRoute: The intended or approved route of administration
    :param Ingredient ingredient: Active or inactive ingredient
    :param DrugCharacteristic drugCharacteristic: Specifies descriptive properties of the medicine
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "definition": {"class_name": "Reference", "is_contained": False},
        
        
        "doseForm": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "intendedRoute": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "ingredient": {"class_name": "Ingredient", "is_contained": True},
        
        
        "drugCharacteristic": {"class_name": "DrugCharacteristic", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  definition:  list['Reference']  = None,  doseForm:  'CodeableConcept'  = None,  intendedRoute:  list['CodeableConcept']  = None,  ingredient:  list['Ingredient']  = None,  drugCharacteristic:  list['DrugCharacteristic']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.definition = definition or []
        self.doseForm = doseForm 
        self.intendedRoute = intendedRoute or []
        self.ingredient = ingredient or []
        self.drugCharacteristic = drugCharacteristic or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicationKnowledge(DomainResource):
    """ Information about a medication that is used to support knowledge.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this medication
    :param CodeableConcept code: Code that identifies this medication
    :param str status: active | entered-in-error | inactive
    :param Reference author: Creator or owner of the knowledge or information about the medication
    :param CodeableConcept intendedJurisdiction: Codes that identify the different jurisdictions for which the information of this resource was created
    :param str name: A name associated with the medication being described
    :param RelatedMedicationKnowledge relatedMedicationKnowledge: Associated or related medication information
    :param Reference associatedMedication: The set of medication resources that are associated with this medication
    :param CodeableConcept productType: Category of the medication or product
    :param Monograph monograph: Associated documentation about the medication
    :param str preparationInstruction: The instructions for preparing the medication
    :param Cost cost: The pricing of the medication
    :param MonitoringProgram monitoringProgram: Program under which a medication is reviewed
    :param IndicationGuideline indicationGuideline: Guidelines or protocols for administration of the medication for an indication
    :param MedicineClassification medicineClassification: Categorization of the medication within a formulary or classification system
    :param Packaging packaging: Details about packaged medications
    :param Reference clinicalUseIssue: Potential clinical issue with or between medication(s)
    :param StorageGuideline storageGuideline: How the medication should be stored
    :param Regulatory regulatory: Regulatory information about a medication
    :param Definitional definitional: Minimal definition information about the medication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "author": {"class_name": "Reference", "is_contained": False},
        
        
        "intendedJurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "relatedMedicationKnowledge": {"class_name": "RelatedMedicationKnowledge", "is_contained": True},
        
        
        "associatedMedication": {"class_name": "Reference", "is_contained": False},
        
        
        "productType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "monograph": {"class_name": "Monograph", "is_contained": True},
        
        
        
        "cost": {"class_name": "Cost", "is_contained": True},
        
        
        "monitoringProgram": {"class_name": "MonitoringProgram", "is_contained": True},
        
        
        "indicationGuideline": {"class_name": "IndicationGuideline", "is_contained": True},
        
        
        "medicineClassification": {"class_name": "MedicineClassification", "is_contained": True},
        
        
        "packaging": {"class_name": "Packaging", "is_contained": True},
        
        
        "clinicalUseIssue": {"class_name": "Reference", "is_contained": False},
        
        
        "storageGuideline": {"class_name": "StorageGuideline", "is_contained": True},
        
        
        "regulatory": {"class_name": "Regulatory", "is_contained": True},
        
        
        "definitional": {"class_name": "Definitional", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  code:  'CodeableConcept'  = None,  status:  'str'  = None,  author:  'Reference'  = None,  intendedJurisdiction:  list['CodeableConcept']  = None,  name:  list['str']  = None,  relatedMedicationKnowledge:  list['RelatedMedicationKnowledge']  = None,  associatedMedication:  list['Reference']  = None,  productType:  list['CodeableConcept']  = None,  monograph:  list['Monograph']  = None,  preparationInstruction:  'str'  = None,  cost:  list['Cost']  = None,  monitoringProgram:  list['MonitoringProgram']  = None,  indicationGuideline:  list['IndicationGuideline']  = None,  medicineClassification:  list['MedicineClassification']  = None,  packaging:  list['Packaging']  = None,  clinicalUseIssue:  list['Reference']  = None,  storageGuideline:  list['StorageGuideline']  = None,  regulatory:  list['Regulatory']  = None,  definitional:  'Definitional'  = None, ):
        self.resourceType = resourceType or "MedicationKnowledge"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.code = code 
        self.status = status 
        self.author = author 
        self.intendedJurisdiction = intendedJurisdiction or []
        self.name = name or []
        self.relatedMedicationKnowledge = relatedMedicationKnowledge or []
        self.associatedMedication = associatedMedication or []
        self.productType = productType or []
        self.monograph = monograph or []
        self.preparationInstruction = preparationInstruction 
        self.cost = cost or []
        self.monitoringProgram = monitoringProgram or []
        self.indicationGuideline = indicationGuideline or []
        self.medicineClassification = medicineClassification or []
        self.packaging = packaging or []
        self.clinicalUseIssue = clinicalUseIssue or []
        self.storageGuideline = storageGuideline or []
        self.regulatory = regulatory or []
        self.definitional = definitional 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicationKnowledge":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicationKnowledge":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()