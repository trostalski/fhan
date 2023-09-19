"""
Generated class for MedicationKnowledge. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class MedicationKnowledge:
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
    :param BackboneElement relatedMedicationKnowledge: Associated or related medication information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of medicationKnowledge
    :param Reference reference: Associated documentation about the associated medication knowledge
    :param Reference associatedMedication: The set of medication resources that are associated with this medication
    :param CodeableConcept productType: Category of the medication or product
    :param BackboneElement monograph: Associated documentation about the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The category of medication document
    :param Reference source: Associated documentation about the medication
    :param str preparationInstruction: The instructions for preparing the medication
    :param BackboneElement cost: The pricing of the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period effectiveDate: The date range for which the cost is effective
    :param CodeableConcept type: The category of the cost information
    :param str source: The source or owner for the price information
    :param Money costMoney: The price or category of the cost of the medication
    :param CodeableConcept costMoney: The price or category of the cost of the medication
    :param BackboneElement monitoringProgram: Program under which a medication is reviewed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Type of program under which the medication is monitored
    :param str name: Name of the reviewing program
    :param BackboneElement indicationGuideline: Guidelines or protocols for administration of the medication for an indication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference indication: Indication for use that applies to the specific administration guideline
    :param BackboneElement dosingGuideline: Guidelines for dosage of the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept treatmentIntent: Intention of the treatment
    :param BackboneElement dosage: Dosage for the medication for the specific guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Category of dosage for a medication
    :param Dosage dosage: Dosage for the medication for the specific guidelines
    :param CodeableConcept administrationTreatment: Type of treatment the guideline applies to
    :param BackboneElement patientCharacteristic: Characteristics of the patient that are relevant to the administration guidelines
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Categorization of specific characteristic that is relevant to the administration guideline
    :param CodeableConcept valueCodeableConcept: The specific characteristic
    :param Quantity valueCodeableConcept: The specific characteristic
    :param Range valueCodeableConcept: The specific characteristic
    :param BackboneElement medicineClassification: Categorization of the medication within a formulary or classification system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of category for the medication (for example, therapeutic classification, therapeutic sub-classification)
    :param str sourcestring: The source of the classification
    :param str sourcestring: The source of the classification
    :param CodeableConcept classification: Specific category assigned to the medication
    :param BackboneElement packaging: Details about packaged medications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement cost: The pricing of the medication
    :param Reference packagedProduct: The packaged medication that is being priced
    :param Reference clinicalUseIssue: Potential clinical issue with or between medication(s)
    :param BackboneElement storageGuideline: How the medication should be stored
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str reference: Reference to additional information
    :param Annotation note: Additional storage notes
    :param Duration stabilityDuration: Duration remains stable
    :param BackboneElement environmentalSetting: Setting or value of environment for adequate storage
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Categorization of the setting
    :param Quantity valueQuantity: Value of the setting
    :param Range valueQuantity: Value of the setting
    :param CodeableConcept valueQuantity: Value of the setting
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
    :param CodeableConcept schedule: Specifies the schedule of a medication in jurisdiction
    :param BackboneElement maxDispense: The maximum number of units of the medication that can be dispensed in a period
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: The maximum number of units of the medication that can be dispensed
    :param Duration period: The period that applies to the maximum number of units
    :param BackboneElement definitional: Minimal definition information about the medication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference definition: Definitional resources that provide more information about this medication
    :param CodeableConcept doseForm: powder | tablets | capsule +
    :param CodeableConcept intendedRoute: The intended or approved route of administration
    :param BackboneElement ingredient: Active or inactive ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: Substances contained in the medication
    :param CodeableConcept type: A code that defines the type of ingredient, active, base, etc
    :param Ratio strengthRatio: Quantity of ingredient present
    :param CodeableConcept strengthRatio: Quantity of ingredient present
    :param Quantity strengthRatio: Quantity of ingredient present
    :param BackboneElement drugCharacteristic: Specifies descriptive properties of the medicine
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Code specifying the type of characteristic of medication
    :param CodeableConcept valueCodeableConcept: Description of the characteristic
    :param str valueCodeableConcept: Description of the characteristic
    :param Quantity valueCodeableConcept: Description of the characteristic
    :param str valueCodeableConcept: Description of the characteristic
    :param Attachment valueCodeableConcept: Description of the characteristic
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    code: "CodeableConcept" = None
    
    status: str = None
    
    author: "Reference" = None
    
    intendedJurisdiction: "CodeableConcept" = None
    
    name: str = None
    
    relatedMedicationKnowledge: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    reference: "Reference" = None
    
    associatedMedication: "Reference" = None
    
    productType: "CodeableConcept" = None
    
    monograph: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    source: "Reference" = None
    
    preparationInstruction: str = None
    
    cost: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    effectiveDate: "Period" = None
    
    type: "CodeableConcept" = None
    
    source: str = None
    
    costMoney: "Money" = None
    
    costMoney: "CodeableConcept" = None
    
    monitoringProgram: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    name: str = None
    
    indicationGuideline: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    indication: "CodeableReference" = None
    
    dosingGuideline: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    treatmentIntent: "CodeableConcept" = None
    
    dosage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    dosage: "Dosage" = None
    
    administrationTreatment: "CodeableConcept" = None
    
    patientCharacteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: "Range" = None
    
    medicineClassification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    sourcestring: str = None
    
    sourcestring: str = None
    
    classification: "CodeableConcept" = None
    
    packaging: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    cost: "BackboneElement" = None
    
    packagedProduct: "Reference" = None
    
    clinicalUseIssue: "Reference" = None
    
    storageGuideline: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    reference: str = None
    
    note: "Annotation" = None
    
    stabilityDuration: "Duration" = None
    
    environmentalSetting: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "Range" = None
    
    valueQuantity: "CodeableConcept" = None
    
    regulatory: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    regulatoryAuthority: "Reference" = None
    
    substitution: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    allowed: bool = None
    
    schedule: "CodeableConcept" = None
    
    maxDispense: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    quantity: "Quantity" = None
    
    period: "Duration" = None
    
    definitional: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    definition: "Reference" = None
    
    doseForm: "CodeableConcept" = None
    
    intendedRoute: "CodeableConcept" = None
    
    ingredient: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    item: "CodeableReference" = None
    
    type: "CodeableConcept" = None
    
    strengthRatio: "Ratio" = None
    
    strengthRatio: "CodeableConcept" = None
    
    strengthRatio: "Quantity" = None
    
    drugCharacteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Attachment" = None
    