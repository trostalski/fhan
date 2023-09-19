"""
Generated class for BiologicallyDerivedProductDispense. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class BiologicallyDerivedProductDispense:
    """ A record of dispensation of a biologically derived product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this dispense
    :param Reference basedOn: The order or request that this dispense is fulfilling
    :param Reference partOf: Short description
    :param str status: preparation | in-progress | allocated | issued | unfulfilled | returned | entered-in-error | unknown
    :param CodeableConcept originRelationshipType: Relationship between the donor and intended recipient
    :param Reference product: The BiologicallyDerivedProduct that is dispensed
    :param Reference patient: The intended recipient of the dispensed product
    :param CodeableConcept matchStatus: Indicates the type of matching associated with the dispense
    :param BackboneElement performer: Indicates who or what performed an action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Identifies the function of the performer during the dispense
    :param Reference actor: Who performed the action
    :param Reference location: Where the dispense occurred
    :param Quantity quantity: Amount dispensed
    :param str preparedDate: When product was selected/matched
    :param str whenHandedOver: When the product was dispatched
    :param Reference destination: Where the product was dispatched to
    :param Annotation note: Additional notes
    :param str usageInstruction: Specific instructions for use
    
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
    
    basedOn: "Reference" = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    originRelationshipType: "CodeableConcept" = None
    
    product: "Reference" = None
    
    patient: "Reference" = None
    
    matchStatus: "CodeableConcept" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    location: "Reference" = None
    
    quantity: "Quantity" = None
    
    preparedDate: str = None
    
    whenHandedOver: str = None
    
    destination: "Reference" = None
    
    note: "Annotation" = None
    
    usageInstruction: str = None
    