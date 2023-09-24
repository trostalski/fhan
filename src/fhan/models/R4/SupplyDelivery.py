"""
Generated class for SupplyDelivery. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class SuppliedItem(Element):
    """ The item that is being delivered or has been supplied.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity quantity: Amount dispensed
    :param CodeableConcept itemCodeableConcept: Medication, Substance, or Device supplied
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    quantity:  "Quantity" = Quantity()
    
    itemCodeableConcept:  "CodeableConcept" = CodeableConcept()
    

@dataclass
class SupplyDelivery(ModelBase):
    """ Record of delivery of what is supplied.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param Reference basedOn: Fulfills plan, proposal or order
    :param Reference partOf: Part of referenced event
    :param str status: in-progress | completed | abandoned | entered-in-error
    :param Reference patient: Patient for whom the item is supplied
    :param CodeableConcept type: Category of dispense event
    :param SuppliedItem suppliedItem: The item that is delivered or supplied
    :param str occurrenceDateTime: When event occurred
    :param Reference supplier: Dispenser
    :param Reference destination: Where the Supply was sent
    :param Reference receiver: Who collected the Supply
    """

    resourceType: str = "SupplyDelivery"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    basedOn: list["Reference"] = None
    
    partOf: list["Reference"] = None
    
    status: str = None
    
    patient: "Reference" = None
    
    type: "CodeableConcept" = None
    
    suppliedItem: "SuppliedItem" = None
    
    occurrenceDateTime: str = None
    
    supplier: "Reference" = None
    
    destination: "Reference" = None
    
    receiver: list["Reference"] = None
    