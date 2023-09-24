"""
Generated class for MedicationKnowledge. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Money import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class RelatedMedicationKnowledge(ModelBase):
    """ Associated or related knowledge about a medication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Category of medicationKnowledge
    :param list['Reference'] reference: Associated documentation about the associated medication knowledge
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  reference: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.reference: list['Reference'] = reference or []
        

    
    

class Monograph(ModelBase):
    """ Associated documentation about the medication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The category of medication document
    :param 'Reference' source: Associated documentation about the medication
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  source: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.source: 'Reference' = source 
        

    
    

class Ingredient(ModelBase):
    """ Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param bool isActive: Active ingredient indicator
    :param 'Ratio' strength: Quantity of ingredient present
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  itemCodeableConcept: 'CodeableConcept' = None,  isActive: bool = None,  strength: 'Ratio' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.isActive: bool = isActive 
        self.strength: 'Ratio' = strength 
        

    
    

class Cost(ModelBase):
    """ The price of the medication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The category of the cost information
    :param str source: The source or owner for the price information
    :param 'Money' cost: The price of the medication
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  source: str = None,  cost: 'Money' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.source: str = source 
        self.cost: 'Money' = cost 
        

    
    

class MonitoringProgram(ModelBase):
    """ The program under which the medication is reviewed.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  name: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.name: str = name 
        

    
        
    
    

class Dosage(ModelBase):
    """ Dosage for the medication for the specific guidelines.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Type of dosage
    :param list['Dosage'] dosage: Dosage for the medication for the specific guidelines
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  dosage: list['Dosage'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.dosage: list['Dosage'] = dosage or []
        

    
    

class PatientCharacteristics(ModelBase):
    """ Characteristics of the patient that are relevant to the administration guidelines (for example, height, weight, gender, etc.).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param str value: The specific characteristic
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  characteristicCodeableConcept: 'CodeableConcept' = None,  value: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.characteristicCodeableConcept: 'CodeableConcept' = characteristicCodeableConcept 
        self.value: str = value or []
        

  
    
    

class AdministrationGuidelines(ModelBase):
    """ Guidelines for the administration of the medication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Dosage'] dosage: Dosage for the medication for the specific guidelines
    :param 'CodeableConcept' indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param list['PatientCharacteristics'] patientCharacteristics: Characteristics of the patient that are relevant to the administration guidelines
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  dosage: list['Dosage'] = None,  indicationCodeableConcept: 'CodeableConcept' = None,  patientCharacteristics: list['PatientCharacteristics'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.dosage: list['Dosage'] = dosage or []
        self.indicationCodeableConcept: 'CodeableConcept' = indicationCodeableConcept 
        self.patientCharacteristics: list['PatientCharacteristics'] = patientCharacteristics or []
        

    
    

class MedicineClassification(ModelBase):
    """ Categorization of the medication within a formulary or classification system.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param list['CodeableConcept'] classification: Specific category assigned to the medication
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  classification: list['CodeableConcept'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.classification: list['CodeableConcept'] = classification or []
        

    
    

class Packaging(ModelBase):
    """ Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: A code that defines the specific type of packaging that the medication can be found in
    :param 'Quantity' quantity: The number of product units the package would contain if fully loaded
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  quantity: 'Quantity' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.quantity: 'Quantity' = quantity 
        

    
    

class DrugCharacteristic(ModelBase):
    """ Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Code specifying the type of characteristic of medication
    :param 'CodeableConcept' valueCodeableConcept: Description of the characteristic
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  valueCodeableConcept: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        

    
        
    
    

class Substitution(ModelBase):
    """ Specifies if changes are allowed when dispensing a medication from a regulatory perspective.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  allowed: bool = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.allowed: bool = allowed 
        

    
    

class Schedule(ModelBase):
    """ Specifies the schedule of a medication in jurisdiction.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' schedule: Specifies the specific drug schedule
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  schedule: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.schedule: 'CodeableConcept' = schedule 
        

    
    

class MaxDispense(ModelBase):
    """ The maximum number of units of the medication that can be dispensed in a period.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Quantity' quantity: The maximum number of units of the medication that can be dispensed
    :param 'Duration' period: The period that applies to the maximum number of units
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  quantity: 'Quantity' = None,  period: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.quantity: 'Quantity' = quantity 
        self.period: 'Duration' = period 
        

  
    
    

class Regulatory(ModelBase):
    """ Regulatory information about a medication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Reference' regulatoryAuthority: Specifies the authority of the regulation
    :param list['Substitution'] substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param list['Schedule'] schedule: Specifies the schedule of a medication in jurisdiction
    :param 'MaxDispense' maxDispense: The maximum number of units of the medication that can be dispensed in a period
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  regulatoryAuthority: 'Reference' = None,  substitution: list['Substitution'] = None,  schedule: list['Schedule'] = None,  maxDispense: 'MaxDispense' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.regulatoryAuthority: 'Reference' = regulatoryAuthority 
        self.substitution: list['Substitution'] = substitution or []
        self.schedule: list['Schedule'] = schedule or []
        self.maxDispense: 'MaxDispense' = maxDispense 
        

    
    

class Kinetics(ModelBase):
    """ The time course of drug absorption, distribution, metabolism and excretion of a medication from the body.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Quantity'] areaUnderCurve: The drug concentration measured at certain discrete points in time
    :param list['Quantity'] lethalDose50: The median lethal dose of a drug
    :param 'Duration' halfLifePeriod: Time required for concentration in the body to decrease by half
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  areaUnderCurve: list['Quantity'] = None,  lethalDose50: list['Quantity'] = None,  halfLifePeriod: 'Duration' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.areaUnderCurve: list['Quantity'] = areaUnderCurve or []
        self.lethalDose50: list['Quantity'] = lethalDose50 or []
        self.halfLifePeriod: 'Duration' = halfLifePeriod 
        

class MedicationKnowledge(DomainResource):
    """ Information about a medication that is used to support knowledge.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'CodeableConcept' code: Code that identifies this medication
    :param str status: active | inactive | entered-in-error
    :param 'Reference' manufacturer: Manufacturer of the item
    :param 'CodeableConcept' doseForm: powder | tablets | capsule +
    :param 'Quantity' amount: Amount of drug in package
    :param str synonym: Additional names for a medication
    :param list['RelatedMedicationKnowledge'] relatedMedicationKnowledge: Associated or related medication information
    :param list['Reference'] associatedMedication: A medication resource that is associated with this medication
    :param list['CodeableConcept'] productType: Category of the medication or product
    :param list['Monograph'] monograph: Associated documentation about the medication
    :param list['Ingredient'] ingredient: Active or inactive ingredient
    :param str preparationInstruction: The instructions for preparing the medication
    :param list['CodeableConcept'] intendedRoute: The intended or approved route of administration
    :param list['Cost'] cost: The pricing of the medication
    :param list['MonitoringProgram'] monitoringProgram: Program under which a medication is reviewed
    :param list['AdministrationGuidelines'] administrationGuidelines: Guidelines for administration of the medication
    :param list['MedicineClassification'] medicineClassification: Categorization of the medication within a formulary or classification system
    :param 'Packaging' packaging: Details about packaged medications
    :param list['DrugCharacteristic'] drugCharacteristic: Specifies descriptive properties of the medicine
    :param list['Reference'] contraindication: Potential clinical issue with or between medication(s)
    :param list['Regulatory'] regulatory: Regulatory information about a medication
    :param list['Kinetics'] kinetics: The time course of drug absorption, distribution, metabolism and excretion of a medication from the body
    """
    def __init__(self, resourceType: str = "MedicationKnowledge",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  status: str = None,  manufacturer: 'Reference' = None,  doseForm: 'CodeableConcept' = None,  amount: 'Quantity' = None,  synonym: str = None,  relatedMedicationKnowledge: list['RelatedMedicationKnowledge'] = None,  associatedMedication: list['Reference'] = None,  productType: list['CodeableConcept'] = None,  monograph: list['Monograph'] = None,  ingredient: list['Ingredient'] = None,  preparationInstruction: str = None,  intendedRoute: list['CodeableConcept'] = None,  cost: list['Cost'] = None,  monitoringProgram: list['MonitoringProgram'] = None,  administrationGuidelines: list['AdministrationGuidelines'] = None,  medicineClassification: list['MedicineClassification'] = None,  packaging: 'Packaging' = None,  drugCharacteristic: list['DrugCharacteristic'] = None,  contraindication: list['Reference'] = None,  regulatory: list['Regulatory'] = None,  kinetics: list['Kinetics'] = None, ):
        self.resourceType: str = resourceType or "MedicationKnowledge"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.status: str = status 
        self.manufacturer: 'Reference' = manufacturer 
        self.doseForm: 'CodeableConcept' = doseForm 
        self.amount: 'Quantity' = amount 
        self.synonym: str = synonym or []
        self.relatedMedicationKnowledge: list['RelatedMedicationKnowledge'] = relatedMedicationKnowledge or []
        self.associatedMedication: list['Reference'] = associatedMedication or []
        self.productType: list['CodeableConcept'] = productType or []
        self.monograph: list['Monograph'] = monograph or []
        self.ingredient: list['Ingredient'] = ingredient or []
        self.preparationInstruction: str = preparationInstruction 
        self.intendedRoute: list['CodeableConcept'] = intendedRoute or []
        self.cost: list['Cost'] = cost or []
        self.monitoringProgram: list['MonitoringProgram'] = monitoringProgram or []
        self.administrationGuidelines: list['AdministrationGuidelines'] = administrationGuidelines or []
        self.medicineClassification: list['MedicineClassification'] = medicineClassification or []
        self.packaging: 'Packaging' = packaging 
        self.drugCharacteristic: list['DrugCharacteristic'] = drugCharacteristic or []
        self.contraindication: list['Reference'] = contraindication or []
        self.regulatory: list['Regulatory'] = regulatory or []
        self.kinetics: list['Kinetics'] = kinetics or []
        