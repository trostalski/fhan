"""
Generated class for MedicationKnowledge. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Money import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class RelatedMedicationKnowledge(Element):
    """ Associated or related knowledge about a medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of medicationKnowledge
    :param Reference reference: Associated documentation about the associated medication knowledge
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    reference: list[Reference] = None
    

    
    
@dataclass
class Monograph(Element):
    """ Associated documentation about the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of medication document
    :param Reference source: Associated documentation about the medication
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    source: "Reference" = None
    

    
    
@dataclass
class Ingredient(Element):
    """ Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param bool isActive: Active ingredient indicator
    :param Ratio strength: Quantity of ingredient present
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    itemCodeableConcept: "CodeableConcept" = None
    
    isActive: bool = None
    strength: "Ratio" = None
    

    
    
@dataclass
class Cost(Element):
    """ The price of the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of the cost information
    :param str source: The source or owner for the price information
    :param Money cost: The price of the medication
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    
    source: str = None
    cost: "Money" = None
    

    
    
@dataclass
class MonitoringProgram(Element):
    """ The program under which the medication is reviewed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    
    name: str = None
    

    
        
    
    
@dataclass
class Dosage(Element):
    """ Dosage for the medication for the specific guidelines.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of dosage
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    dosage: list[Dosage] = None
    

    
    
@dataclass
class PatientCharacteristics(Element):
    """ Characteristics of the patient that are relevant to the administration guidelines (for example, height, weight, gender, etc.).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param str value: The specific characteristic
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    characteristicCodeableConcept: "CodeableConcept" = None
    
    value: str = None
    
  
    
    
@dataclass
class AdministrationGuidelines(Element):
    """ Guidelines for the administration of the medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    :param CodeableConcept indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param PatientCharacteristics patientCharacteristics: Characteristics of the patient that are relevant to the administration guidelines
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    dosage: list[Dosage] = None
    indicationCodeableConcept: "CodeableConcept" = None
    patientCharacteristics: list[PatientCharacteristics] = None
    

    
    
@dataclass
class MedicineClassification(Element):
    """ Categorization of the medication within a formulary or classification system.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param CodeableConcept classification: Specific category assigned to the medication
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    classification: list[CodeableConcept] = None
    

    
    
@dataclass
class Packaging(Element):
    """ Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code that defines the specific type of packaging that the medication can be found in
    :param Quantity quantity: The number of product units the package would contain if fully loaded
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    quantity: "Quantity" = None
    

    
    
@dataclass
class DrugCharacteristic(Element):
    """ Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic of medication
    :param CodeableConcept valueCodeableConcept: Description of the characteristic
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    valueCodeableConcept: "CodeableConcept" = None
    

    
        
    
    
@dataclass
class Substitution(Element):
    """ Specifies if changes are allowed when dispensing a medication from a regulatory perspective.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    
    allowed: bool = None
    

    
    
@dataclass
class Schedule(Element):
    """ Specifies the schedule of a medication in jurisdiction.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept schedule: Specifies the specific drug schedule
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    schedule: "CodeableConcept" = None
    

    
    
@dataclass
class MaxDispense(Element):
    """ The maximum number of units of the medication that can be dispensed in a period.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The maximum number of units of the medication that can be dispensed
    :param Duration period: The period that applies to the maximum number of units
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    quantity: "Quantity" = None
    period: "Duration" = None
    
  
    
    
@dataclass
class Regulatory(Element):
    """ Regulatory information about a medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference regulatoryAuthority: Specifies the authority of the regulation
    :param Substitution substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param Schedule schedule: Specifies the schedule of a medication in jurisdiction
    :param MaxDispense maxDispense: The maximum number of units of the medication that can be dispensed in a period
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    regulatoryAuthority: "Reference" = None
    substitution: list[Substitution] = None
    schedule: list[Schedule] = None
    maxDispense: "MaxDispense" = None
    

    
    
@dataclass
class Kinetics(Element):
    """ The time course of drug absorption, distribution, metabolism and excretion of a medication from the body.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity areaUnderCurve: The drug concentration measured at certain discrete points in time
    :param Quantity lethalDose50: The median lethal dose of a drug
    :param Duration halfLifePeriod: Time required for concentration in the body to decrease by half
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    areaUnderCurve: list[Quantity] = None
    lethalDose50: list[Quantity] = None
    halfLifePeriod: "Duration" = None
    
@dataclass
class MedicationKnowledge(ModelBase):
    """ Information about a medication that is used to support knowledge.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept code: Code that identifies this medication
    :param str status: active | inactive | entered-in-error
    :param Reference manufacturer: Manufacturer of the item
    :param CodeableConcept doseForm: powder | tablets | capsule +
    :param Quantity amount: Amount of drug in package
    :param str synonym: Additional names for a medication
    :param RelatedMedicationKnowledge relatedMedicationKnowledge: Associated or related medication information
    :param Reference associatedMedication: A medication resource that is associated with this medication
    :param CodeableConcept productType: Category of the medication or product
    :param Monograph monograph: Associated documentation about the medication
    :param Ingredient ingredient: Active or inactive ingredient
    :param str preparationInstruction: The instructions for preparing the medication
    :param CodeableConcept intendedRoute: The intended or approved route of administration
    :param Cost cost: The pricing of the medication
    :param MonitoringProgram monitoringProgram: Program under which a medication is reviewed
    :param AdministrationGuidelines administrationGuidelines: Guidelines for administration of the medication
    :param MedicineClassification medicineClassification: Categorization of the medication within a formulary or classification system
    :param Packaging packaging: Details about packaged medications
    :param DrugCharacteristic drugCharacteristic: Specifies descriptive properties of the medicine
    :param Reference contraindication: Potential clinical issue with or between medication(s)
    :param Regulatory regulatory: Regulatory information about a medication
    :param Kinetics kinetics: The time course of drug absorption, distribution, metabolism and excretion of a medication from the body
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    code: "CodeableConcept" = None
    
    status: str = None
    
    manufacturer: "Reference" = None
    
    doseForm: "CodeableConcept" = None
    
    amount: "Quantity" = None
    
    synonym: str = None
    
    relatedMedicationKnowledge: list["RelatedMedicationKnowledge"] = None
    
    associatedMedication: list["Reference"] = None
    
    productType: list["CodeableConcept"] = None
    
    monograph: list["Monograph"] = None
    
    ingredient: list["Ingredient"] = None
    
    preparationInstruction: str = None
    
    intendedRoute: list["CodeableConcept"] = None
    
    cost: list["Cost"] = None
    
    monitoringProgram: list["MonitoringProgram"] = None
    
    administrationGuidelines: list["AdministrationGuidelines"] = None
    
    medicineClassification: list["MedicineClassification"] = None
    
    packaging: "Packaging" = None
    
    drugCharacteristic: list["DrugCharacteristic"] = None
    
    contraindication: list["Reference"] = None
    
    regulatory: list["Regulatory"] = None
    
    kinetics: list["Kinetics"] = None
    