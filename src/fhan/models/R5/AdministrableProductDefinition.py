"""
Generated class for AdministrableProductDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class AdministrableProductDefinition:
    """ A medicinal product in the final form which is suitable for administering to a patient (after any mixing of multiple components, dissolution etc. has been performed).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier for the administrable product
    :param str status: draft | active | retired | unknown
    :param Reference formOf: References a product from which one or more of the constituent parts of that product can be prepared and used as described by this administrable product
    :param CodeableConcept administrableDoseForm: The dose form of the final product after necessary reconstitution or processing
    :param CodeableConcept unitOfPresentation: The presentation type in which this item is given to a patient. e.g. for a spray - 'puff'
    :param Reference producedFrom: Indicates the specific manufactured items that are part of the 'formOf' product that are used in the preparation of this specific administrable form
    :param CodeableConcept ingredient: The ingredients of this administrable medicinal product. This is only needed if the ingredients are not specified either using ManufacturedItemDefiniton, or using by incoming references from the Ingredient resource
    :param Reference device: A device that is integral to the medicinal product, in effect being considered as an "ingredient" of the medicinal product
    :param str description: A general description of the product, when in its final form, suitable for administration e.g. effervescent blue liquid, to be swallowed
    :param BackboneElement property: Characteristics e.g. a product's onset of action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param Quantity valueCodeableConcept: A value for the characteristic
    :param str valueCodeableConcept: A value for the characteristic
    :param bool valueCodeableConcept: A value for the characteristic
    :param str valueCodeableConcept: A value for the characteristic
    :param Attachment valueCodeableConcept: A value for the characteristic
    :param Reference valueCodeableConcept: A value for the characteristic
    :param CodeableConcept status: The status of characteristic e.g. assigned or pending
    :param BackboneElement routeOfAdministration: The path by which the product is taken into or makes contact with the body
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the route
    :param Quantity firstDose: The first dose (dose quantity) administered can be specified for the product
    :param Quantity maxSingleDose: The maximum single dose that can be administered
    :param Quantity maxDosePerDay: The maximum dose quantity to be administered in any one 24-h period
    :param Ratio maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered
    :param Duration maxTreatmentPeriod: The maximum treatment period during which the product can be administered
    :param BackboneElement targetSpecies: A species for which this route applies
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the species
    :param BackboneElement withdrawalPeriod: A species specific time during which consumption of animal product is not appropriate
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept tissue: The type of tissue for which the withdrawal period applies, e.g. meat, milk
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
    
    status: str = None
    
    formOf: "Reference" = None
    
    administrableDoseForm: "CodeableConcept" = None
    
    unitOfPresentation: "CodeableConcept" = None
    
    producedFrom: "Reference" = None
    
    ingredient: "CodeableConcept" = None
    
    device: "Reference" = None
    
    description: str = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Attachment" = None
    
    valueCodeableConcept: "Reference" = None
    
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
    