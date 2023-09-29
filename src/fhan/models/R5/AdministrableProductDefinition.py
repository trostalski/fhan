"""
Generated class for AdministrableProductDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Property(BaseModel):
    """ Characteristics e.g. a product's onset of action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param Quantity valueQuantity: A value for the characteristic
    :param str valueDate: A value for the characteristic
    :param bool valueBoolean: A value for the characteristic
    :param str valueMarkdown: A value for the characteristic
    :param Attachment valueAttachment: A value for the characteristic
    :param Reference valueReference: A value for the characteristic
    :param CodeableConcept status: The status of characteristic e.g. assigned or pending
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        
        "valueReference": {"class_name": "Reference", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueDate:  'str'  = None,  valueBoolean:  'bool'  = None,  valueMarkdown:  'str'  = None,  valueAttachment:  'Attachment'  = None,  valueReference:  'Reference'  = None,  status:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueDate = valueDate 
        self.valueBoolean = valueBoolean 
        self.valueMarkdown = valueMarkdown 
        self.valueAttachment = valueAttachment 
        self.valueReference = valueReference 
        self.status = status 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdministrableProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdministrableProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class WithdrawalPeriod(BaseModel):
    """ A species specific time during which consumption of animal product is not appropriate.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept tissue: The type of tissue for which the withdrawal period applies, e.g. meat, milk
    :param Quantity value: A value for the time
    :param str supportingInformation: Extra information about the withdrawal period
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "tissue": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "value": {"class_name": "Quantity", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  tissue:  'CodeableConcept'  = None,  value:  'Quantity'  = None,  supportingInformation:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.tissue = tissue 
        self.value = value 
        self.supportingInformation = supportingInformation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdministrableProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdministrableProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class TargetSpecies(BaseModel):
    """ A species for which this route applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the species
    :param WithdrawalPeriod withdrawalPeriod: A species specific time during which consumption of animal product is not appropriate
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "withdrawalPeriod": {"class_name": "WithdrawalPeriod", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  withdrawalPeriod:  list['WithdrawalPeriod']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.withdrawalPeriod = withdrawalPeriod or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdministrableProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdministrableProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class RouteOfAdministration(BaseModel):
    """ The path by which the product is taken into or makes contact with the body. In some regions this is referred to as the licenced or approved route. RouteOfAdministration cannot be used when the 'formOf' product already uses MedicinalProductDefinition.route (and vice versa).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Coded expression for the route
    :param Quantity firstDose: The first dose (dose quantity) administered can be specified for the product
    :param Quantity maxSingleDose: The maximum single dose that can be administered
    :param Quantity maxDosePerDay: The maximum dose quantity to be administered in any one 24-h period
    :param Ratio maxDosePerTreatmentPeriod: The maximum dose per treatment period that can be administered
    :param Duration maxTreatmentPeriod: The maximum treatment period during which the product can be administered
    :param TargetSpecies targetSpecies: A species for which this route applies
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "firstDose": {"class_name": "Quantity", "is_contained": False},
        
        
        "maxSingleDose": {"class_name": "Quantity", "is_contained": False},
        
        
        "maxDosePerDay": {"class_name": "Quantity", "is_contained": False},
        
        
        "maxDosePerTreatmentPeriod": {"class_name": "Ratio", "is_contained": False},
        
        
        "maxTreatmentPeriod": {"class_name": "Duration", "is_contained": False},
        
        
        "targetSpecies": {"class_name": "TargetSpecies", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  firstDose:  'Quantity'  = None,  maxSingleDose:  'Quantity'  = None,  maxDosePerDay:  'Quantity'  = None,  maxDosePerTreatmentPeriod:  'Ratio'  = None,  maxTreatmentPeriod:  'Duration'  = None,  targetSpecies:  list['TargetSpecies']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.firstDose = firstDose 
        self.maxSingleDose = maxSingleDose 
        self.maxDosePerDay = maxDosePerDay 
        self.maxDosePerTreatmentPeriod = maxDosePerTreatmentPeriod 
        self.maxTreatmentPeriod = maxTreatmentPeriod 
        self.targetSpecies = targetSpecies or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdministrableProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdministrableProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class AdministrableProductDefinition(DomainResource):
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
    :param Property property: Characteristics e.g. a product's onset of action
    :param RouteOfAdministration routeOfAdministration: The path by which the product is taken into or makes contact with the body
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "formOf": {"class_name": "Reference", "is_contained": False},
        
        
        "administrableDoseForm": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "unitOfPresentation": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "producedFrom": {"class_name": "Reference", "is_contained": False},
        
        
        "ingredient": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "routeOfAdministration": {"class_name": "RouteOfAdministration", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  formOf:  list['Reference']  = None,  administrableDoseForm:  'CodeableConcept'  = None,  unitOfPresentation:  'CodeableConcept'  = None,  producedFrom:  list['Reference']  = None,  ingredient:  list['CodeableConcept']  = None,  device:  'Reference'  = None,  description:  'str'  = None,  property:  list['Property']  = None,  routeOfAdministration:  list['RouteOfAdministration']  = None, ):
        self.resourceType = resourceType or "AdministrableProductDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.formOf = formOf or []
        self.administrableDoseForm = administrableDoseForm 
        self.unitOfPresentation = unitOfPresentation 
        self.producedFrom = producedFrom or []
        self.ingredient = ingredient or []
        self.device = device 
        self.description = description 
        self.property = property or []
        self.routeOfAdministration = routeOfAdministration or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "AdministrableProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "AdministrableProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()