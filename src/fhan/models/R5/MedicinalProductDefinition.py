"""
Generated class for MedicinalProductDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.MarketingStatus import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Contact(BaseModel):
    """ A product specific contact, person (in a role), or an organization.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Allows the contact to be classified, for example QPPV, Pharmacovigilance Enquiry Information
    :param Reference contact: A product specific contact, person (in a role), or an organization
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "contact": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  contact:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.contact = contact 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Part(BaseModel):
    """ Coding words or phrases of the name.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str part: A fragment of a product name
    :param CodeableConcept type: Identifying type for this part of the name (e.g. strength part)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  part:  'str'  = None,  type:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.part = part 
        self.type = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Usage(BaseModel):
    """ Country and jurisdiction where the name applies, and associated language.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept country: Country code for where this name applies
    :param CodeableConcept jurisdiction: Jurisdiction code for where this name applies
    :param CodeableConcept language: Language code for this name
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "country": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  country:  'CodeableConcept'  = None,  jurisdiction:  'CodeableConcept'  = None,  language:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.country = country 
        self.jurisdiction = jurisdiction 
        self.language = language 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Name(BaseModel):
    """ The product's name, including full name and possibly coded parts.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str productName: The full product name
    :param CodeableConcept type: Type of product name, such as rINN, BAN, Proprietary, Non-Proprietary
    :param Part part: Coding words or phrases of the name
    :param Usage usage: Country and jurisdiction where the name applies
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "part": {"class_name": "Part", "is_contained": True},
        
        
        "usage": {"class_name": "Usage", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  productName:  'str'  = None,  type:  'CodeableConcept'  = None,  part:  list['Part']  = None,  usage:  list['Usage']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.productName = productName 
        self.type = type 
        self.part = part or []
        self.usage = usage or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class CrossReference(BaseModel):
    """ Reference to another product, e.g. for linking authorised to investigational product, or a virtual product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference product: Reference to another product, e.g. for linking authorised to investigational product
    :param CodeableConcept type: The type of relationship, for instance branded to generic or virtual to actual product
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "product": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  product:  'CodeableReference'  = None,  type:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.product = product 
        self.type = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Operation(BaseModel):
    """ A manufacturing or administrative process or step associated with (or performed on) the medicinal product.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference type: The type of manufacturing operation e.g. manufacturing itself, re-packaging
    :param Period effectiveDate: Date range of applicability
    :param Reference organization: The organization responsible for the particular process, e.g. the manufacturer or importer
    :param CodeableConcept confidentialityIndicator: Specifies whether this process is considered proprietary or confidential
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "effectiveDate": {"class_name": "Period", "is_contained": False},
        
        
        "organization": {"class_name": "Reference", "is_contained": False},
        
        
        "confidentialityIndicator": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableReference'  = None,  effectiveDate:  'Period'  = None,  organization:  list['Reference']  = None,  confidentialityIndicator:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.effectiveDate = effectiveDate 
        self.organization = organization or []
        self.confidentialityIndicator = confidentialityIndicator 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Characteristic(BaseModel):
    """ Allows the key product features to be recorded, such as "sugar free", "modified release", "parallel import".:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param str valueMarkdown: A value for the characteristic
    :param Quantity valueQuantity: A value for the characteristic
    :param int valueInteger: A value for the characteristic
    :param str valueDate: A value for the characteristic
    :param bool valueBoolean: A value for the characteristic
    :param Attachment valueAttachment: A value for the characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueMarkdown:  'str'  = None,  valueQuantity:  'Quantity'  = None,  valueInteger:  'int'  = None,  valueDate:  'str'  = None,  valueBoolean:  'bool'  = None,  valueAttachment:  'Attachment'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueMarkdown = valueMarkdown 
        self.valueQuantity = valueQuantity 
        self.valueInteger = valueInteger 
        self.valueDate = valueDate 
        self.valueBoolean = valueBoolean 
        self.valueAttachment = valueAttachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MedicinalProductDefinition(DomainResource):
    """ Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use, drug catalogs, to support prescribing, adverse events management etc.).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this product. Could be an MPID
    :param CodeableConcept type: Regulatory type, e.g. Investigational or Authorized
    :param CodeableConcept domain: If this medicine applies to human or veterinary uses
    :param str version: A business identifier relating to a specific version of the product
    :param CodeableConcept status: The status within the lifecycle of this product record
    :param str statusDate: The date at which the given status became applicable
    :param str description: General description of this product
    :param CodeableConcept combinedPharmaceuticalDoseForm: The dose form for a single part product, or combined form of a multiple part product
    :param CodeableConcept route: The path by which the product is taken into or makes contact with the body
    :param str indication: Description of indication(s) for this product, used when structured indications are not required
    :param CodeableConcept legalStatusOfSupply: The legal status of supply of the medicinal product as classified by the regulator
    :param CodeableConcept additionalMonitoringIndicator: Whether the Medicinal Product is subject to additional monitoring for regulatory reasons
    :param CodeableConcept specialMeasures: Whether the Medicinal Product is subject to special measures for regulatory reasons
    :param CodeableConcept pediatricUseIndicator: If authorised for use in children
    :param CodeableConcept classification: Allows the product to be classified by various systems
    :param MarketingStatus marketingStatus: Marketing status of the medicinal product, in contrast to marketing authorization
    :param CodeableConcept packagedMedicinalProduct: Package type for the product
    :param Reference comprisedOf: Types of medicinal manufactured items and/or devices that this product consists of, such as tablets, capsule, or syringes
    :param CodeableConcept ingredient: The ingredients of this medicinal product - when not detailed in other resources
    :param CodeableReference impurity: Any component of the drug product which is not the chemical entity defined as the drug substance, or an excipient in the drug product
    :param Reference attachedDocument: Additional documentation about the medicinal product
    :param Reference masterFile: A master file for the medicinal product (e.g. Pharmacovigilance System Master File)
    :param Contact contact: A product specific contact, person (in a role), or an organization
    :param Reference clinicalTrial: Clinical trials or studies that this product is involved in
    :param Coding code: A code that this product is known by, within some formal terminology
    :param Name name: The product's name, including full name and possibly coded parts
    :param CrossReference crossReference: Reference to another product, e.g. for linking authorised to investigational product
    :param Operation operation: A manufacturing or administrative process for the medicinal product
    :param Characteristic characteristic: Key product features such as "sugar free", "modified release"
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "domain": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "combinedPharmaceuticalDoseForm": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "route": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "legalStatusOfSupply": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "additionalMonitoringIndicator": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specialMeasures": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "pediatricUseIndicator": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "marketingStatus": {"class_name": "MarketingStatus", "is_contained": False},
        
        
        "packagedMedicinalProduct": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "comprisedOf": {"class_name": "Reference", "is_contained": False},
        
        
        "ingredient": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "impurity": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "attachedDocument": {"class_name": "Reference", "is_contained": False},
        
        
        "masterFile": {"class_name": "Reference", "is_contained": False},
        
        
        "contact": {"class_name": "Contact", "is_contained": True},
        
        
        "clinicalTrial": {"class_name": "Reference", "is_contained": False},
        
        
        "code": {"class_name": "Coding", "is_contained": False},
        
        
        "name": {"class_name": "Name", "is_contained": True},
        
        
        "crossReference": {"class_name": "CrossReference", "is_contained": True},
        
        
        "operation": {"class_name": "Operation", "is_contained": True},
        
        
        "characteristic": {"class_name": "Characteristic", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  type:  'CodeableConcept'  = None,  domain:  'CodeableConcept'  = None,  version:  'str'  = None,  status:  'CodeableConcept'  = None,  statusDate:  'str'  = None,  description:  'str'  = None,  combinedPharmaceuticalDoseForm:  'CodeableConcept'  = None,  route:  list['CodeableConcept']  = None,  indication:  'str'  = None,  legalStatusOfSupply:  'CodeableConcept'  = None,  additionalMonitoringIndicator:  'CodeableConcept'  = None,  specialMeasures:  list['CodeableConcept']  = None,  pediatricUseIndicator:  'CodeableConcept'  = None,  classification:  list['CodeableConcept']  = None,  marketingStatus:  list['MarketingStatus']  = None,  packagedMedicinalProduct:  list['CodeableConcept']  = None,  comprisedOf:  list['Reference']  = None,  ingredient:  list['CodeableConcept']  = None,  impurity:  list['CodeableReference']  = None,  attachedDocument:  list['Reference']  = None,  masterFile:  list['Reference']  = None,  contact:  list['Contact']  = None,  clinicalTrial:  list['Reference']  = None,  code:  list['Coding']  = None,  name:  list['Name']  = None,  crossReference:  list['CrossReference']  = None,  operation:  list['Operation']  = None,  characteristic:  list['Characteristic']  = None, ):
        self.resourceType = resourceType or "MedicinalProductDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type 
        self.domain = domain 
        self.version = version 
        self.status = status 
        self.statusDate = statusDate 
        self.description = description 
        self.combinedPharmaceuticalDoseForm = combinedPharmaceuticalDoseForm 
        self.route = route or []
        self.indication = indication 
        self.legalStatusOfSupply = legalStatusOfSupply 
        self.additionalMonitoringIndicator = additionalMonitoringIndicator 
        self.specialMeasures = specialMeasures or []
        self.pediatricUseIndicator = pediatricUseIndicator 
        self.classification = classification or []
        self.marketingStatus = marketingStatus or []
        self.packagedMedicinalProduct = packagedMedicinalProduct or []
        self.comprisedOf = comprisedOf or []
        self.ingredient = ingredient or []
        self.impurity = impurity or []
        self.attachedDocument = attachedDocument or []
        self.masterFile = masterFile or []
        self.contact = contact or []
        self.clinicalTrial = clinicalTrial or []
        self.code = code or []
        self.name = name or []
        self.crossReference = crossReference or []
        self.operation = operation or []
        self.characteristic = characteristic or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MedicinalProductDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MedicinalProductDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()