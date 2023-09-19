"""
Generated class for MedicinalProductPharmaceutical. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class MedicinalProductPharmaceutical(ModelBase):
    """ A pharmaceutical product described in terms of its composition and dose form.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier for the pharmaceutical medicinal product
    :param CodeableConcept administrableDoseForm: The administrable dose form, after necessary reconstitution
    :param CodeableConcept unitOfPresentation: Todo
    :param Reference ingredient: Ingredient
    :param Reference device: Accompanying device
    :param BackboneElement characteristics: Characteristics e.g. a products onset of action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: A coded characteristic
    :param CodeableConcept status: The status of characteristic e.g. assigned or pending
    :param BackboneElement routeOfAdministration: The path by which the pharmaceutical product is taken into or makes contact with the body
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the route
    :param Quantity firstDose: The first dose (dose quantity) administered in humans can be specified, for a product under investigation, using a numerical value and its unit of measurement
    :param Quantity maxSingleDose: The maximum single dose that can be administered as per the protocol of a clinical trial can be specified using a numerical value and its unit of measurement
    :param Quantity maxDosePerDay: The maximum dose per day (maximum dose quantity to be administered in any one 24-h period) that can be administered as per the protocol referenced in the clinical trial authorisation
    :param Ratio maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered as per the protocol referenced in the clinical trial authorisation
    :param Duration maxTreatmentPeriod: The maximum treatment period during which an Investigational Medicinal Product can be administered as per the protocol referenced in the clinical trial authorisation
    :param BackboneElement targetSpecies: A species for which this route applies
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the species
    :param BackboneElement withdrawalPeriod: A species specific time during which consumption of animal product is not appropriate
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept tissue: Coded expression for the type of tissue for which the withdrawal period applues, e.g. meat, milk
    :param Quantity value: A value for the time
    :param str supportingInformation: Extra information about the withdrawal period
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
    
    administrableDoseForm: "CodeableConcept" = None
    
    unitOfPresentation: "CodeableConcept" = None
    
    ingredient: "Reference" = None
    
    device: "Reference" = None
    
    characteristics: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    routeOfAdministration: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    firstDose: "Quantity" = None
    
    maxSingleDose: "Quantity" = None
    
    maxDosePerDay: "Quantity" = None
    
    maxDosePerTreatmentPeriod: "Ratio" = None
    
    maxTreatmentPeriod: "Duration" = None
    
    targetSpecies: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    withdrawalPeriod: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    tissue: "CodeableConcept" = None
    
    value: "Quantity" = None
    
    supportingInformation: str = None
    