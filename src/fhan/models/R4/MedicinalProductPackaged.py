"""
Generated class for MedicinalProductPackaged. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.ProductShelfLife import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.ProdCharacteristic import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class BatchIdentifier(ModelBase):
    """ Batch numbering.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' outerPackaging: A number appearing on the outer packaging of a specific batch
    :param 'Identifier' immediatePackaging: A number appearing on the immediate packaging (and not the outer packaging)
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  outerPackaging: 'Identifier' = None,  immediatePackaging: 'Identifier' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.outerPackaging: 'Identifier' = outerPackaging 
        self.immediatePackaging: 'Identifier' = immediatePackaging 
        

    
    

class PackageItem(ModelBase):
    """ A packaging item, as a contained for medicine, possibly with other packaging items within.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Identifier'] identifier: Including possibly Data Carrier Identifier
    :param 'CodeableConcept' type: The physical type of the container of the medicine
    :param 'Quantity' quantity: The quantity of this package in the medicinal product, at the current level of packaging. The outermost is always 1
    :param list['CodeableConcept'] material: Material type of the package item
    :param list['CodeableConcept'] alternateMaterial: A possible alternate material for the packaging
    :param list['Reference'] device: A device accompanying a medicinal product
    :param list['Reference'] manufacturedItem: The manufactured item as contained in the packaged medicinal product
    :param 'ProdCharacteristic' physicalCharacteristics: Dimensions, color etc.
    :param list['CodeableConcept'] otherCharacteristics: Other codeable characteristics
    :param list['ProductShelfLife'] shelfLifeStorage: Shelf Life and storage information
    :param list['Reference'] manufacturer: Manufacturer of this Package Item
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  type: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  material: list['CodeableConcept'] = None,  alternateMaterial: list['CodeableConcept'] = None,  device: list['Reference'] = None,  manufacturedItem: list['Reference'] = None,  physicalCharacteristics: 'ProdCharacteristic' = None,  otherCharacteristics: list['CodeableConcept'] = None,  shelfLifeStorage: list['ProductShelfLife'] = None,  manufacturer: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.type: 'CodeableConcept' = type 
        self.quantity: 'Quantity' = quantity 
        self.material: list['CodeableConcept'] = material or []
        self.alternateMaterial: list['CodeableConcept'] = alternateMaterial or []
        self.device: list['Reference'] = device or []
        self.manufacturedItem: list['Reference'] = manufacturedItem or []
        self.physicalCharacteristics: 'ProdCharacteristic' = physicalCharacteristics 
        self.otherCharacteristics: list['CodeableConcept'] = otherCharacteristics or []
        self.shelfLifeStorage: list['ProductShelfLife'] = shelfLifeStorage or []
        self.manufacturer: list['Reference'] = manufacturer or []
        

class MedicinalProductPackaged(DomainResource):
    """ A medicinal product in a container or package.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique identifier
    :param list['Reference'] subject: The product with this is a pack for
    :param str description: Textual description
    :param 'CodeableConcept' legalStatusOfSupply: The legal status of supply of the medicinal product as classified by the regulator
    :param list['MarketingStatus'] marketingStatus: Marketing information
    :param 'Reference' marketingAuthorization: Manufacturer of this Package Item
    :param list['Reference'] manufacturer: Manufacturer of this Package Item
    :param list['BatchIdentifier'] batchIdentifier: Batch numbering
    :param list['PackageItem'] packageItem: A packaging item, as a contained for medicine, possibly with other packaging items within
    """
    def __init__(self, resourceType: str = "MedicinalProductPackaged",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  subject: list['Reference'] = None,  description: str = None,  legalStatusOfSupply: 'CodeableConcept' = None,  marketingStatus: list['MarketingStatus'] = None,  marketingAuthorization: 'Reference' = None,  manufacturer: list['Reference'] = None,  batchIdentifier: list['BatchIdentifier'] = None,  packageItem: list['PackageItem'] = None, ):
        self.resourceType: str = resourceType or "MedicinalProductPackaged"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.subject: list['Reference'] = subject or []
        self.description: str = description 
        self.legalStatusOfSupply: 'CodeableConcept' = legalStatusOfSupply 
        self.marketingStatus: list['MarketingStatus'] = marketingStatus or []
        self.marketingAuthorization: 'Reference' = marketingAuthorization 
        self.manufacturer: list['Reference'] = manufacturer or []
        self.batchIdentifier: list['BatchIdentifier'] = batchIdentifier or []
        self.packageItem: list['PackageItem'] = packageItem or []
        