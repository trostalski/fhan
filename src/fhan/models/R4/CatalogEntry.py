"""
Generated class for CatalogEntry. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement relatedEntry: An item that this catalog entry is related to
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str relationtype: triggers | is-replaced-by
    :param Reference item: The reference to the related item
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
    
    orderable: bool = None
    
    referencedItem: "Reference" = None
    
    additionalIdentifier: "Identifier" = None
    
    classification: "CodeableConcept" = None
    
    status: str = None
    
    validityPeriod: "Period" = None
    
    validTo: str = None
    
    lastUpdated: str = None
    
    additionalCharacteristic: "CodeableConcept" = None
    
    additionalClassification: "CodeableConcept" = None
    
    relatedEntry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationtype: str = None
    
    item: "Reference" = None
    