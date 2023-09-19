"""
Generated class for MedicinalProductDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.MarketingStatus import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class MedicinalProductDefinition:
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
    :param BackboneElement contact: A product specific contact, person (in a role), or an organization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Allows the contact to be classified, for example QPPV, Pharmacovigilance Enquiry Information
    :param Reference contact: A product specific contact, person (in a role), or an organization
    :param Reference clinicalTrial: Clinical trials or studies that this product is involved in
    :param Coding code: A code that this product is known by, within some formal terminology
    :param BackboneElement name: The product's name, including full name and possibly coded parts
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str productName: The full product name
    :param CodeableConcept type: Type of product name, such as rINN, BAN, Proprietary, Non-Proprietary
    :param BackboneElement part: Coding words or phrases of the name
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str part: A fragment of a product name
    :param CodeableConcept type: Identifying type for this part of the name (e.g. strength part)
    :param BackboneElement usage: Country and jurisdiction where the name applies
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept country: Country code for where this name applies
    :param CodeableConcept jurisdiction: Jurisdiction code for where this name applies
    :param CodeableConcept language: Language code for this name
    :param BackboneElement crossReference: Reference to another product, e.g. for linking authorised to investigational product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference product: Reference to another product, e.g. for linking authorised to investigational product
    :param CodeableConcept type: The type of relationship, for instance branded to generic or virtual to actual product
    :param BackboneElement operation: A manufacturing or administrative process for the medicinal product
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference type: The type of manufacturing operation e.g. manufacturing itself, re-packaging
    :param Period effectiveDate: Date range of applicability
    :param Reference organization: The organization responsible for the particular process, e.g. the manufacturer or importer
    :param CodeableConcept confidentialityIndicator: Specifies whether this process is considered proprietary or confidential
    :param BackboneElement characteristic: Key product features such as "sugar free", "modified release"
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of characteristic
    :param CodeableConcept valueCodeableConcept: A value for the characteristic
    :param str valueCodeableConcept: A value for the characteristic
    :param Quantity valueCodeableConcept: A value for the characteristic
    :param int valueCodeableConcept: A value for the characteristic
    :param str valueCodeableConcept: A value for the characteristic
    :param bool valueCodeableConcept: A value for the characteristic
    :param Attachment valueCodeableConcept: A value for the characteristic
    
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
    
    type: "CodeableConcept" = None
    
    domain: "CodeableConcept" = None
    
    version: str = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    description: str = None
    
    combinedPharmaceuticalDoseForm: "CodeableConcept" = None
    
    route: "CodeableConcept" = None
    
    indication: str = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    additionalMonitoringIndicator: "CodeableConcept" = None
    
    specialMeasures: "CodeableConcept" = None
    
    pediatricUseIndicator: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    marketingStatus: "MarketingStatus" = None
    
    packagedMedicinalProduct: "CodeableConcept" = None
    
    comprisedOf: "Reference" = None
    
    ingredient: "CodeableConcept" = None
    
    impurity: "CodeableReference" = None
    
    attachedDocument: "Reference" = None
    
    masterFile: "Reference" = None
    
    contact: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    contact: "Reference" = None
    
    clinicalTrial: "Reference" = None
    
    code: "Coding" = None
    
    name: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    productName: str = None
    
    type: "CodeableConcept" = None
    
    part: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    part: str = None
    
    type: "CodeableConcept" = None
    
    usage: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    language: "CodeableConcept" = None
    
    crossReference: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    product: "CodeableReference" = None
    
    type: "CodeableConcept" = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableReference" = None
    
    effectiveDate: "Period" = None
    
    organization: "Reference" = None
    
    confidentialityIndicator: "CodeableConcept" = None
    
    characteristic: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: int = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Attachment" = None
    