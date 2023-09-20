"""
Generated class for MedicinalProductPharmaceutical. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Characteristics(Element):
    """ Characteristics e.g. a products onset of action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: A coded characteristic
    :param CodeableConcept status: The status of characteristic e.g. assigned or pending
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    status: "CodeableConcept" = None
    

    
        
    
        
    
    
@dataclass
class WithdrawalPeriod(Element):
    """ A species specific time during which consumption of animal product is not appropriate.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept tissue: Coded expression for the type of tissue for which the withdrawal period applues, e.g. meat, milk
    :param Quantity value: A value for the time
    :param str supportingInformation: Extra information about the withdrawal period
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    tissue: "CodeableConcept" = None
    value: "Quantity" = None
    
    supportingInformation: str = None
    
  
    
    
@dataclass
class TargetSpecies(Element):
    """ A species for which this route applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the species
    :param WithdrawalPeriod withdrawalPeriod: A species specific time during which consumption of animal product is not appropriate
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    withdrawalPeriod: list[WithdrawalPeriod] = None
    
  
    
    
@dataclass
class RouteOfAdministration(Element):
    """ The path by which the pharmaceutical product is taken into or makes contact with the body.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the route
    :param Quantity firstDose: The first dose (dose quantity) administered in humans can be specified, for a product under investigation, using a numerical value and its unit of measurement
    :param Quantity maxSingleDose: The maximum single dose that can be administered as per the protocol of a clinical trial can be specified using a numerical value and its unit of measurement
    :param Quantity maxDosePerDay: The maximum dose per day (maximum dose quantity to be administered in any one 24-h period) that can be administered as per the protocol referenced in the clinical trial authorisation
    :param Ratio maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered as per the protocol referenced in the clinical trial authorisation
    :param Duration maxTreatmentPeriod: The maximum treatment period during which an Investigational Medicinal Product can be administered as per the protocol referenced in the clinical trial authorisation
    :param TargetSpecies targetSpecies: A species for which this route applies
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    firstDose: "Quantity" = None
    maxSingleDose: "Quantity" = None
    maxDosePerDay: "Quantity" = None
    maxDosePerTreatmentPeriod: "Ratio" = None
    maxTreatmentPeriod: "Duration" = None
    targetSpecies: list[TargetSpecies] = None
    
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
    :param Characteristics characteristics: Characteristics e.g. a products onset of action
    :param RouteOfAdministration routeOfAdministration: The path by which the pharmaceutical product is taken into or makes contact with the body
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
    
    administrableDoseForm: "CodeableConcept" = None
    
    unitOfPresentation: "CodeableConcept" = None
    
    ingredient: list["Reference"] = None
    
    device: list["Reference"] = None
    
    characteristics: list["Characteristics"] = None
    
    routeOfAdministration: list["RouteOfAdministration"] = None
    