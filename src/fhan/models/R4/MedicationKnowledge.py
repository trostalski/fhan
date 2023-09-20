"""
Generated class for MedicationKnowledge. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Duration import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Money import *
from fhan.models.generator_models import ModelBase

@dataclass
class relatedMedicationKnowledge(Element):
    """ Associated or related knowledge about a medication.
    :param BackboneElement relatedMedicationKnowledge: Associated or related medication information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of medicationKnowledge
    :param Reference reference: Associated documentation about the associated medication knowledge
    """
    relatedMedicationKnowledge: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    reference: list["Reference"] = None
    
@dataclass
class monograph(Element):
    """ Associated documentation about the medication.
    :param BackboneElement monograph: Associated documentation about the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of medication document
    :param Reference source: Associated documentation about the medication
    """
    monograph: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    source: "Reference" = None
    
@dataclass
class ingredient(Element):
    """ Identifies a particular constituent of interest in the product.
    :param BackboneElement ingredient: Active or inactive ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param Reference itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param bool isActive: Active ingredient indicator
    :param Ratio strength: Quantity of ingredient present
    """
    ingredient: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    itemCodeableConcept: "CodeableConcept" = None
    
    itemCodeableConcept: "Reference" = None
    
    isActive: bool = None
    
    strength: "Ratio" = None
    
@dataclass
class cost(Element):
    """ The price of the medication.
    :param BackboneElement cost: The pricing of the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of the cost information
    :param str source: The source or owner for the price information
    :param Money cost: The price of the medication
    """
    cost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    source: str = None
    
    cost: "Money" = None
    
@dataclass
class monitoringProgram(Element):
    """ The program under which the medication is reviewed.
    :param BackboneElement monitoringProgram: Program under which a medication is reviewed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    """
    monitoringProgram: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    name: str = None
    
@dataclass
class administrationGuidelines(Element):
    """ Guidelines for the administration of the medication.
    :param BackboneElement administrationGuidelines: Guidelines for administration of the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement dosage: Dosage for the medication for the specific guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of dosage
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    :param CodeableConcept indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param Reference indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param BackboneElement patientCharacteristics: Characteristics of the patient that are relevant to the administration guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param Quantity characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param str value: The specific characteristic
    """
    administrationGuidelines: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    dosage: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    dosage: list["Dosage"] = None
    
    indicationCodeableConcept: "CodeableConcept" = None
    
    indicationCodeableConcept: "Reference" = None
    
    patientCharacteristics: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    characteristicCodeableConcept: "CodeableConcept" = None
    
    characteristicCodeableConcept: "Quantity" = None
    
    value: str = None
    
@dataclass
class dosage(Element):
    """ Dosage for the medication for the specific guidelines.
    :param BackboneElement dosage: Dosage for the medication for the specific guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of dosage
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    """
    dosage: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    dosage: list["Dosage"] = None
    
@dataclass
class patientCharacteristics(Element):
    """ Characteristics of the patient that are relevant to the administration guidelines (for example, height, weight, gender, etc.).
    :param BackboneElement patientCharacteristics: Characteristics of the patient that are relevant to the administration guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param Quantity characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param str value: The specific characteristic
    """
    patientCharacteristics: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    characteristicCodeableConcept: "CodeableConcept" = None
    
    characteristicCodeableConcept: "Quantity" = None
    
    value: str = None
    
@dataclass
class medicineClassification(Element):
    """ Categorization of the medication within a formulary or classification system.
    :param BackboneElement medicineClassification: Categorization of the medication within a formulary or classification system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param CodeableConcept classification: Specific category assigned to the medication
    """
    medicineClassification: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    classification: list["CodeableConcept"] = None
    
@dataclass
class packaging(Element):
    """ Information that only applies to packages (not products).
    :param BackboneElement packaging: Details about packaged medications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code that defines the specific type of packaging that the medication can be found in
    :param Quantity quantity: The number of product units the package would contain if fully loaded
    """
    packaging: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
@dataclass
class drugCharacteristic(Element):
    """ Specifies descriptive properties of the medicine, such as color, shape, imprints, etc.
    :param BackboneElement drugCharacteristic: Specifies descriptive properties of the medicine
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic of medication
    :param CodeableConcept valueCodeableConcept: Description of the characteristic
    :param str valueCodeableConcept: Description of the characteristic
    :param Quantity valueCodeableConcept: Description of the characteristic
    :param str valueCodeableConcept: Description of the characteristic
    """
    drugCharacteristic: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
@dataclass
class regulatory(Element):
    """ Regulatory information about a medication.
    :param BackboneElement regulatory: Regulatory information about a medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference regulatoryAuthority: Specifies the authority of the regulation
    :param BackboneElement substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    :param BackboneElement schedule: Specifies the schedule of a medication in jurisdiction
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept schedule: Specifies the specific drug schedule
    :param BackboneElement maxDispense: The maximum number of units of the medication that can be dispensed in a period
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The maximum number of units of the medication that can be dispensed
    :param Duration period: The period that applies to the maximum number of units
    """
    regulatory: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    regulatoryAuthority: "Reference" = None
    
    substitution: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    allowed: bool = None
    
    schedule: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    schedule: "CodeableConcept" = None
    
    maxDispense: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    quantity: "Quantity" = None
    
    period: "Duration" = None
    
@dataclass
class substitution(Element):
    """ Specifies if changes are allowed when dispensing a medication from a regulatory perspective.
    :param BackboneElement substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    """
    substitution: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    allowed: bool = None
    
@dataclass
class schedule(Element):
    """ Specifies the schedule of a medication in jurisdiction.
    :param BackboneElement schedule: Specifies the schedule of a medication in jurisdiction
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept schedule: Specifies the specific drug schedule
    """
    schedule: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    schedule: "CodeableConcept" = None
    
@dataclass
class maxDispense(Element):
    """ The maximum number of units of the medication that can be dispensed in a period.
    :param BackboneElement maxDispense: The maximum number of units of the medication that can be dispensed in a period
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The maximum number of units of the medication that can be dispensed
    :param Duration period: The period that applies to the maximum number of units
    """
    maxDispense: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    quantity: "Quantity" = None
    
    period: "Duration" = None
    
@dataclass
class kinetics(Element):
    """ The time course of drug absorption, distribution, metabolism and excretion of a medication from the body.
    :param BackboneElement kinetics: The time course of drug absorption, distribution, metabolism and excretion of a medication from the body
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity areaUnderCurve: The drug concentration measured at certain discrete points in time
    :param Quantity lethalDose50: The median lethal dose of a drug
    :param Duration halfLifePeriod: Time required for concentration in the body to decrease by half
    """
    kinetics: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    areaUnderCurve: list["Quantity"] = None
    
    lethalDose50: list["Quantity"] = None
    
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
    :param BackboneElement relatedMedicationKnowledge: Associated or related medication information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of medicationKnowledge
    :param Reference reference: Associated documentation about the associated medication knowledge
    :param Reference associatedMedication: A medication resource that is associated with this medication
    :param CodeableConcept productType: Category of the medication or product
    :param BackboneElement monograph: Associated documentation about the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of medication document
    :param Reference source: Associated documentation about the medication
    :param BackboneElement ingredient: Active or inactive ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param Reference itemCodeableConcept: Medication(s) or substance(s) contained in the medication
    :param bool isActive: Active ingredient indicator
    :param Ratio strength: Quantity of ingredient present
    :param str preparationInstruction: The instructions for preparing the medication
    :param CodeableConcept intendedRoute: The intended or approved route of administration
    :param BackboneElement cost: The pricing of the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of the cost information
    :param str source: The source or owner for the price information
    :param Money cost: The price of the medication
    :param BackboneElement monitoringProgram: Program under which a medication is reviewed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    :param BackboneElement administrationGuidelines: Guidelines for administration of the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement dosage: Dosage for the medication for the specific guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of dosage
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    :param CodeableConcept indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param Reference indicationCodeableConcept: Indication for use that apply to the specific administration guidelines
    :param BackboneElement patientCharacteristics: Characteristics of the patient that are relevant to the administration guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param Quantity characteristicCodeableConcept: Specific characteristic that is relevant to the administration guideline
    :param str value: The specific characteristic
    :param BackboneElement medicineClassification: Categorization of the medication within a formulary or classification system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param CodeableConcept classification: Specific category assigned to the medication
    :param BackboneElement packaging: Details about packaged medications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code that defines the specific type of packaging that the medication can be found in
    :param Quantity quantity: The number of product units the package would contain if fully loaded
    :param BackboneElement drugCharacteristic: Specifies descriptive properties of the medicine
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic of medication
    :param CodeableConcept valueCodeableConcept: Description of the characteristic
    :param str valueCodeableConcept: Description of the characteristic
    :param Quantity valueCodeableConcept: Description of the characteristic
    :param str valueCodeableConcept: Description of the characteristic
    :param Reference contraindication: Potential clinical issue with or between medication(s)
    :param BackboneElement regulatory: Regulatory information about a medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference regulatoryAuthority: Specifies the authority of the regulation
    :param BackboneElement substitution: Specifies if changes are allowed when dispensing a medication from a regulatory perspective
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Specifies the type of substitution allowed
    :param bool allowed: Specifies if regulation allows for changes in the medication when dispensing
    :param BackboneElement schedule: Specifies the schedule of a medication in jurisdiction
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept schedule: Specifies the specific drug schedule
    :param BackboneElement maxDispense: The maximum number of units of the medication that can be dispensed in a period
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The maximum number of units of the medication that can be dispensed
    :param Duration period: The period that applies to the maximum number of units
    :param BackboneElement kinetics: The time course of drug absorption, distribution, metabolism and excretion of a medication from the body
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity areaUnderCurve: The drug concentration measured at certain discrete points in time
    :param Quantity lethalDose50: The median lethal dose of a drug
    :param Duration halfLifePeriod: Time required for concentration in the body to decrease by half
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
    
    relatedMedicationKnowledge: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    reference: list["Reference"] = None
    
    associatedMedication: list["Reference"] = None
    
    productType: list["CodeableConcept"] = None
    
    monograph: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    source: "Reference" = None
    
    ingredient: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    itemCodeableConcept: "CodeableConcept" = None
    
    itemCodeableConcept: "Reference" = None
    
    isActive: bool = None
    
    strength: "Ratio" = None
    
    preparationInstruction: str = None
    
    intendedRoute: list["CodeableConcept"] = None
    
    cost: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    source: str = None
    
    cost: "Money" = None
    
    monitoringProgram: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    name: str = None
    
    administrationGuidelines: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    dosage: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    dosage: list["Dosage"] = None
    
    indicationCodeableConcept: "CodeableConcept" = None
    
    indicationCodeableConcept: "Reference" = None
    
    patientCharacteristics: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    characteristicCodeableConcept: "CodeableConcept" = None
    
    characteristicCodeableConcept: "Quantity" = None
    
    value: str = None
    
    medicineClassification: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    classification: list["CodeableConcept"] = None
    
    packaging: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    drugCharacteristic: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    contraindication: list["Reference"] = None
    
    regulatory: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    regulatoryAuthority: "Reference" = None
    
    substitution: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    allowed: bool = None
    
    schedule: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    schedule: "CodeableConcept" = None
    
    maxDispense: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    quantity: "Quantity" = None
    
    period: "Duration" = None
    
    kinetics: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    areaUnderCurve: list["Quantity"] = None
    
    lethalDose50: list["Quantity"] = None
    
    halfLifePeriod: "Duration" = None
    