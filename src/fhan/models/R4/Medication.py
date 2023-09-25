"""
Generated class for Medication. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.DomainResource import *


    
    

class Ingredient(ModelBase):
    """ Identifies a particular constituent of interest in the product.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' itemCodeableConcept: The actual ingredient or content
    :param 'Reference' itemReference: The actual ingredient or content
    :param bool isActive: Active ingredient indicator
    :param 'Ratio' strength: Quantity of ingredient present
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  itemCodeableConcept: 'CodeableConcept' = None,  itemReference: 'Reference' = None,  isActive: bool = None,  strength: 'Ratio' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.itemReference: 'Reference' = itemReference 
        self.isActive: bool = isActive 
        self.strength: 'Ratio' = strength 
        

    
    

class Batch(ModelBase):
    """ Information that only applies to packages (not products).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str lotNumber: Identifier assigned to batch
    :param str expirationDate: When batch will expire
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  lotNumber: str = None,  expirationDate: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.lotNumber: str = lotNumber 
        self.expirationDate: str = expirationDate 
        

class Medication(DomainResource):
    """ This resource is primarily used for the identification and definition of a medication for the purposes of prescribing, dispensing, and administering a medication as well as for making statements about medication use.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier for this medication
    :param 'CodeableConcept' code: Codes that identify this medication
    :param str status: active | inactive | entered-in-error
    :param 'Reference' manufacturer: Manufacturer of the item
    :param 'CodeableConcept' form: powder | tablets | capsule +
    :param 'Ratio' amount: Amount of drug in package
    :param list['Ingredient'] ingredient: Active or inactive ingredient
    :param 'Batch' batch: Details about packaged medications
    """
    def __init__(self, resourceType: str = "Medication",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  code: 'CodeableConcept' = None,  status: str = None,  manufacturer: 'Reference' = None,  form: 'CodeableConcept' = None,  amount: 'Ratio' = None,  ingredient: list['Ingredient'] = None,  batch: 'Batch' = None, ):
        self.resourceType: str = resourceType or "Medication"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.code: 'CodeableConcept' = code 
        self.status: str = status 
        self.manufacturer: 'Reference' = manufacturer 
        self.form: 'CodeableConcept' = form 
        self.amount: 'Ratio' = amount 
        self.ingredient: list['Ingredient'] = ingredient or []
        self.batch: 'Batch' = batch 
        