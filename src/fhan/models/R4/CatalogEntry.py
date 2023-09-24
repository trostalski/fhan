"""
Generated class for CatalogEntry. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class RelatedEntry(ModelBase):
    """ Used for example, to point to a substance, or to a device used to administer a medication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relationtype: triggers | is-replaced-by
    :param 'Reference' item: The reference to the related item
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  relationtype: str = None,  item: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.relationtype: str = relationtype 
        self.item: 'Reference' = item 
        

class CatalogEntry(DomainResource):
    """ Catalog entries are wrappers that contextualize items included in a catalog.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique identifier of the catalog item
    :param 'CodeableConcept' type: The type of item - medication, device, service, protocol or other
    :param bool orderable: Whether the entry represents an orderable item
    :param 'Reference' referencedItem: The item that is being defined
    :param list['Identifier'] additionalIdentifier: Any additional identifier(s) for the catalog item, in the same granularity or concept
    :param list['CodeableConcept'] classification: Classification (category or class) of the item entry
    :param str status: draft | active | retired | unknown
    :param 'Period' validityPeriod: The time period in which this catalog entry is expected to be active
    :param str validTo: The date until which this catalog entry is expected to be active
    :param str lastUpdated: When was this catalog last updated
    :param list['CodeableConcept'] additionalCharacteristic: Additional characteristics of the catalog entry
    :param list['CodeableConcept'] additionalClassification: Additional classification of the catalog entry
    :param list['RelatedEntry'] relatedEntry: An item that this catalog entry is related to
    """
    def __init__(self, resourceType: str = "CatalogEntry",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  type: 'CodeableConcept' = None,  orderable: bool = None,  referencedItem: 'Reference' = None,  additionalIdentifier: list['Identifier'] = None,  classification: list['CodeableConcept'] = None,  status: str = None,  validityPeriod: 'Period' = None,  validTo: str = None,  lastUpdated: str = None,  additionalCharacteristic: list['CodeableConcept'] = None,  additionalClassification: list['CodeableConcept'] = None,  relatedEntry: list['RelatedEntry'] = None, ):
        self.resourceType: str = resourceType or "CatalogEntry"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.type: 'CodeableConcept' = type 
        self.orderable: bool = orderable 
        self.referencedItem: 'Reference' = referencedItem 
        self.additionalIdentifier: list['Identifier'] = additionalIdentifier or []
        self.classification: list['CodeableConcept'] = classification or []
        self.status: str = status 
        self.validityPeriod: 'Period' = validityPeriod 
        self.validTo: str = validTo 
        self.lastUpdated: str = lastUpdated 
        self.additionalCharacteristic: list['CodeableConcept'] = additionalCharacteristic or []
        self.additionalClassification: list['CodeableConcept'] = additionalClassification or []
        self.relatedEntry: list['RelatedEntry'] = relatedEntry or []
        