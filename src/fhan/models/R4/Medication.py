"""
Generated class for Medication. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class ingredient(Element):
    """ Identifies a particular constituent of interest in the product.
    :param BackboneElement ingredient: Active or inactive ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: The actual ingredient or content
    :param Reference itemCodeableConcept: The actual ingredient or content
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
class batch(Element):
    """ Information that only applies to packages (not products).
    :param BackboneElement batch: Details about packaged medications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lotNumber: Identifier assigned to batch
    :param str expirationDate: When batch will expire
    """
    batch: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    lotNumber: str = None
    
    expirationDate: str = None
    


@dataclass
class Medication(ModelBase):
    """ This resource is primarily used for the identification and definition of a medication for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this medication
    :param CodeableConcept code: Codes that identify this medication
    :param str status: active | inactive | entered-in-error
    :param Reference manufacturer: Manufacturer of the item
    :param CodeableConcept form: powder | tablets | capsule +
    :param Ratio amount: Amount of drug in package
    :param BackboneElement ingredient: Active or inactive ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept itemCodeableConcept: The actual ingredient or content
    :param Reference itemCodeableConcept: The actual ingredient or content
    :param bool isActive: Active ingredient indicator
    :param Ratio strength: Quantity of ingredient present
    :param BackboneElement batch: Details about packaged medications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lotNumber: Identifier assigned to batch
    :param str expirationDate: When batch will expire
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
    
    code: "CodeableConcept" = None
    
    status: str = None
    
    manufacturer: "Reference" = None
    
    form: "CodeableConcept" = None
    
    amount: "Ratio" = None
    
    ingredient: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    itemCodeableConcept: "CodeableConcept" = None
    
    itemCodeableConcept: "Reference" = None
    
    isActive: bool = None
    
    strength: "Ratio" = None
    
    batch: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    lotNumber: str = None
    
    expirationDate: str = None
    