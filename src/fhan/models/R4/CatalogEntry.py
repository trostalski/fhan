"""
Generated class for CatalogEntry. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class RelatedEntry(Element):
    """ Used for example, to point to a substance, or to a device used to administer a medication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relationtype: triggers | is-replaced-by
    :param Reference item: The reference to the related item
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    relationtype: str = None
    item: "Reference" = Reference()
    

@dataclass
class CatalogEntry(ModelBase):
    """ Catalog entries are wrappers that contextualize items included in a catalog.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique identifier of the catalog item
    :param CodeableConcept type: The type of item - medication, device, service, protocol or other
    :param bool orderable: Whether the entry represents an orderable item
    :param Reference referencedItem: The item that is being defined
    :param Identifier additionalIdentifier: Any additional identifier(s) for the catalog item, in the same granularity or concept
    :param CodeableConcept classification: Classification (category or class) of the item entry
    :param str status: draft | active | retired | unknown
    :param Period validityPeriod: The time period in which this catalog entry is expected to be active
    :param str validTo: The date until which this catalog entry is expected to be active
    :param str lastUpdated: When was this catalog last updated
    :param CodeableConcept additionalCharacteristic: Additional characteristics of the catalog entry
    :param CodeableConcept additionalClassification: Additional classification of the catalog entry
    :param RelatedEntry relatedEntry: An item that this catalog entry is related to
    """

    resourceType: str = "CatalogEntry"
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
    
    orderable: bool = None
    
    referencedItem: "Reference" = Reference()
    
    additionalIdentifier: list[Identifier] = Identifier() 
    
    classification: list[CodeableConcept] = CodeableConcept() 
    
    status: str = None
    
    validityPeriod: "Period" = Period()
    
    validTo: str = None
    
    lastUpdated: str = None
    
    additionalCharacteristic: list[CodeableConcept] = CodeableConcept() 
    
    additionalClassification: list[CodeableConcept] = CodeableConcept() 
    
    relatedEntry: list[RelatedEntry] = RelatedEntry() 
    