"""
Generated class for Medication. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Medication:
    """ This resource is primarily used for the identification and definition of a medication, including ingredients, for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.
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
    :param Reference marketingAuthorizationHolder: Organization that has authorization to market medication
    :param CodeableConcept doseForm: powder | tablets | capsule +
    :param Quantity totalVolume: When the specified product code does not infer a package size, this is the specific amount of drug in the product
    :param BackboneElement ingredient: Active or inactive ingredient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference item: The ingredient (substance or medication) that the ingredient.strength relates to
    :param bool isActive: Active ingredient indicator
    :param Ratio strengthRatio: Quantity of ingredient present
    :param CodeableConcept strengthRatio: Quantity of ingredient present
    :param Quantity strengthRatio: Quantity of ingredient present
    :param BackboneElement batch: Details about packaged medications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lotNumber: Identifier assigned to batch
    :param str expirationDate: When batch will expire
    :param Reference definition: Knowledge about this medication
    
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
    
    marketingAuthorizationHolder: "Reference" = None
    
    doseForm: "CodeableConcept" = None
    
    totalVolume: "Quantity" = None
    
    ingredient: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    item: "CodeableReference" = None
    
    isActive: bool = None
    
    strengthRatio: "Ratio" = None
    
    strengthRatio: "CodeableConcept" = None
    
    strengthRatio: "Quantity" = None
    
    batch: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    lotNumber: str = None
    
    expirationDate: str = None
    
    definition: "Reference" = None
    