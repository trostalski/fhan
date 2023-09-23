"""
Generated class for MedicinalProductPharmaceutical. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    status: "CodeableConcept" = CodeableConcept()
    

    
        
    
        
    
    
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    tissue: "CodeableConcept" = CodeableConcept()
    value: "Quantity" = Quantity()
    
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    withdrawalPeriod: list[WithdrawalPeriod] = WithdrawalPeriod() 
    

  
    
    
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    code: "CodeableConcept" = CodeableConcept()
    firstDose: "Quantity" = Quantity()
    maxSingleDose: "Quantity" = Quantity()
    maxDosePerDay: "Quantity" = Quantity()
    maxDosePerTreatmentPeriod: "Ratio" = Ratio()
    maxTreatmentPeriod: "Duration" = Duration()
    targetSpecies: list[TargetSpecies] = TargetSpecies() 
    

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

    resourceType: str = "MedicinalProductPharmaceutical"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    administrableDoseForm: "CodeableConcept" = CodeableConcept()
    
    unitOfPresentation: "CodeableConcept" = CodeableConcept()
    
    ingredient: list[Reference] = Reference() 
    
    device: list[Reference] = Reference() 
    
    characteristics: list[Characteristics] = Characteristics() 
    
    routeOfAdministration: list[RouteOfAdministration] = RouteOfAdministration() 
    