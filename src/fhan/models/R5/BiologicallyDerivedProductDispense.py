"""
Generated class for BiologicallyDerivedProductDispense. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Performer(BaseModel):
    """ Indicates who or what performed an action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Identifies the function of the performer during the dispense
    :param Reference actor: Who performed the action
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  function:  'CodeableConcept'  = None,  actor:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.function = function 
        self.actor = actor 
        

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProductDispense":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProductDispense":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class BiologicallyDerivedProductDispense(DomainResource):
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
    :param Performer performer: Indicates who or what performed an action
    :param Reference location: Where the dispense occurred
    :param Quantity quantity: Amount dispensed
    :param str preparedDate: When product was selected/matched
    :param str whenHandedOver: When the product was dispatched
    :param Reference destination: Where the product was dispatched to
    :param Annotation note: Additional notes
    :param str usageInstruction: Specific instructions for use
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        
        "originRelationshipType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "product": {"class_name": "Reference", "is_contained": False},
        
        
        "patient": {"class_name": "Reference", "is_contained": False},
        
        
        "matchStatus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        "destination": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  basedOn:  list['Reference']  = None,  partOf:  list['Reference']  = None,  status:  'str'  = None,  originRelationshipType:  'CodeableConcept'  = None,  product:  'Reference'  = None,  patient:  'Reference'  = None,  matchStatus:  'CodeableConcept'  = None,  performer:  list['Performer']  = None,  location:  'Reference'  = None,  quantity:  'Quantity'  = None,  preparedDate:  'str'  = None,  whenHandedOver:  'str'  = None,  destination:  'Reference'  = None,  note:  list['Annotation']  = None,  usageInstruction:  'str'  = None, ):
        self.resourceType = resourceType or "BiologicallyDerivedProductDispense"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.basedOn = basedOn or []
        self.partOf = partOf or []
        self.status = status 
        self.originRelationshipType = originRelationshipType 
        self.product = product 
        self.patient = patient 
        self.matchStatus = matchStatus 
        self.performer = performer or []
        self.location = location 
        self.quantity = quantity 
        self.preparedDate = preparedDate 
        self.whenHandedOver = whenHandedOver 
        self.destination = destination 
        self.note = note or []
        self.usageInstruction = usageInstruction 
        

    @classmethod
    def from_dict(cls, data: dict) -> "BiologicallyDerivedProductDispense":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "BiologicallyDerivedProductDispense":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()