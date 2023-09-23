"""
Generated class for MedicinalProduct. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.MarketingStatus import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class NamePart(Element):
    """ Coding words or phrases of the name.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str part: A fragment of a product name
    :param Coding type: Idenifying type for this part of the name (e.g. strength part)
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    part: str = None
    type: "Coding" = Coding()
    

    
    
@dataclass
class CountryLanguage(Element):
    """ Country where the name applies.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept country: Country code for where this name applies
    :param CodeableConcept jurisdiction: Jurisdiction code for where this name applies
    :param CodeableConcept language: Language code for this name
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    country: "CodeableConcept" = CodeableConcept()
    jurisdiction: "CodeableConcept" = CodeableConcept()
    language: "CodeableConcept" = CodeableConcept()
    

  
    
    
@dataclass
class Name(Element):
    """ The product's name, including full name and possibly coded parts.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str productName: The full product name
    :param NamePart namePart: Coding words or phrases of the name
    :param CountryLanguage countryLanguage: Country where the name applies
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    productName: str = None
    namePart: list[NamePart] = NamePart() 
    countryLanguage: list[CountryLanguage] = CountryLanguage() 
    

    
    
@dataclass
class ManufacturingBusinessOperation(Element):
    """ An operation applied to the product, for manufacturing or adminsitrative purpose.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept operationType: The type of manufacturing operation
    :param Identifier authorisationReferenceNumber: Regulatory authorization reference number
    :param str effectiveDate: Regulatory authorization date
    :param CodeableConcept confidentialityIndicator: To indicate if this proces is commercially confidential
    :param Reference manufacturer: The manufacturer or establishment associated with the process
    :param Reference regulator: A regulator which oversees the operation
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    operationType: "CodeableConcept" = CodeableConcept()
    authorisationReferenceNumber: "Identifier" = Identifier()
    
    effectiveDate: str = None
    confidentialityIndicator: "CodeableConcept" = CodeableConcept()
    manufacturer: list[Reference] = Reference() 
    regulator: "Reference" = Reference()
    

    
    
@dataclass
class SpecialDesignation(Element):
    """ Indicates if the medicinal product has an orphan designation for the treatment of a rare disease.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier for the designation, or procedure number
    :param CodeableConcept type: The type of special designation, e.g. orphan drug, minor use
    :param CodeableConcept intendedUse: The intended use of the product, e.g. prevention, treatment
    :param CodeableConcept indicationCodeableConcept: Condition for which the medicinal use applies
    :param CodeableConcept status: For example granted, pending, expired or withdrawn
    :param str date: Date when the designation was granted
    :param CodeableConcept species: Animal species for which this applies
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    identifier: list[Identifier] = Identifier() 
    type: "CodeableConcept" = CodeableConcept()
    intendedUse: "CodeableConcept" = CodeableConcept()
    indicationCodeableConcept: "CodeableConcept" = CodeableConcept()
    status: "CodeableConcept" = CodeableConcept()
    
    date: str = None
    species: "CodeableConcept" = CodeableConcept()
    

@dataclass
class MedicinalProduct(ModelBase):
    """ Detailed definition of a medicinal product, typically for uses other than direct patient care (e.g. regulatory use).
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
    :param Coding domain: If this medicine applies to human or veterinary uses
    :param CodeableConcept combinedPharmaceuticalDoseForm: The dose form for a single part product, or combined form of a multiple part product
    :param CodeableConcept legalStatusOfSupply: The legal status of supply of the medicinal product as classified by the regulator
    :param CodeableConcept additionalMonitoringIndicator: Whether the Medicinal Product is subject to additional monitoring for regulatory reasons
    :param str specialMeasures: Whether the Medicinal Product is subject to special measures for regulatory reasons
    :param CodeableConcept paediatricUseIndicator: If authorised for use in children
    :param CodeableConcept productClassification: Allows the product to be classified by various systems
    :param MarketingStatus marketingStatus: Marketing status of the medicinal product, in contrast to marketing authorizaton
    :param Reference pharmaceuticalProduct: Pharmaceutical aspects of product
    :param Reference packagedMedicinalProduct: Package representation for the product
    :param Reference attachedDocument: Supporting documentation, typically for regulatory submission
    :param Reference masterFile: A master file for to the medicinal product (e.g. Pharmacovigilance System Master File)
    :param Reference contact: A product specific contact, person (in a role), or an organization
    :param Reference clinicalTrial: Clinical trials or studies that this product is involved in
    :param Name name: The product's name, including full name and possibly coded parts
    :param Identifier crossReference: Reference to another product, e.g. for linking authorised to investigational product
    :param ManufacturingBusinessOperation manufacturingBusinessOperation: An operation applied to the product, for manufacturing or adminsitrative purpose
    :param SpecialDesignation specialDesignation: Indicates if the medicinal product has an orphan designation for the treatment of a rare disease
    """

    resourceType: str = "MedicinalProduct"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    type: "CodeableConcept" = CodeableConcept()
    
    domain: "Coding" = Coding()
    
    combinedPharmaceuticalDoseForm: "CodeableConcept" = CodeableConcept()
    
    legalStatusOfSupply: "CodeableConcept" = CodeableConcept()
    
    additionalMonitoringIndicator: "CodeableConcept" = CodeableConcept()
    
    specialMeasures: str = None
    
    paediatricUseIndicator: "CodeableConcept" = CodeableConcept()
    
    productClassification: list[CodeableConcept] = CodeableConcept() 
    
    marketingStatus: list[MarketingStatus] = MarketingStatus() 
    
    pharmaceuticalProduct: list[Reference] = Reference() 
    
    packagedMedicinalProduct: list[Reference] = Reference() 
    
    attachedDocument: list[Reference] = Reference() 
    
    masterFile: list[Reference] = Reference() 
    
    contact: list[Reference] = Reference() 
    
    clinicalTrial: list[Reference] = Reference() 
    
    name: list[Name] = Name() 
    
    crossReference: list[Identifier] = Identifier() 
    
    manufacturingBusinessOperation: list[ManufacturingBusinessOperation] = ManufacturingBusinessOperation() 
    
    specialDesignation: list[SpecialDesignation] = SpecialDesignation() 
    