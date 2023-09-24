"""
Generated class for SupplyRequest. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Range import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Timing import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Parameter(ModelBase):
    """ Specific parameters for the ordered item.  For example, the size of the indicated item.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' code: Item detail
    :param 'CodeableConcept' valueCodeableConcept: Value of detail
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: 'CodeableConcept' = None,  valueCodeableConcept: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: 'CodeableConcept' = code 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        

class SupplyRequest(DomainResource):
    """ A record of a request for a medication, substance or device used in the healthcare setting.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for SupplyRequest
    :param str status: draft | active | suspended +
    :param 'CodeableConcept' category: The kind of supply (central, non-stock, etc.)
    :param str priority: routine | urgent | asap | stat
    :param 'CodeableConcept' itemCodeableConcept: Medication, Substance, or Device requested to be supplied
    :param 'Quantity' quantity: The requested amount of the item indicated
    :param list['Parameter'] parameter: Ordered item details
    :param str occurrenceDateTime: When the request should be fulfilled
    :param str authoredOn: When the request was made
    :param 'Reference' requester: Individual making the request
    :param list['Reference'] supplier: Who is intended to fulfill the request
    :param list['CodeableConcept'] reasonCode: The reason why the supply item was requested
    :param list['Reference'] reasonReference: The reason why the supply item was requested
    :param 'Reference' deliverFrom: The origin of the supply
    :param 'Reference' deliverTo: The destination of the supply
    """
    def __init__(self, resourceType: str = "SupplyRequest",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  category: 'CodeableConcept' = None,  priority: str = None,  itemCodeableConcept: 'CodeableConcept' = None,  quantity: 'Quantity' = None,  parameter: list['Parameter'] = None,  occurrenceDateTime: str = None,  authoredOn: str = None,  requester: 'Reference' = None,  supplier: list['Reference'] = None,  reasonCode: list['CodeableConcept'] = None,  reasonReference: list['Reference'] = None,  deliverFrom: 'Reference' = None,  deliverTo: 'Reference' = None, ):
        self.resourceType: str = resourceType or "SupplyRequest"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.category: 'CodeableConcept' = category 
        self.priority: str = priority 
        self.itemCodeableConcept: 'CodeableConcept' = itemCodeableConcept 
        self.quantity: 'Quantity' = quantity 
        self.parameter: list['Parameter'] = parameter or []
        self.occurrenceDateTime: str = occurrenceDateTime 
        self.authoredOn: str = authoredOn 
        self.requester: 'Reference' = requester 
        self.supplier: list['Reference'] = supplier or []
        self.reasonCode: list['CodeableConcept'] = reasonCode or []
        self.reasonReference: list['Reference'] = reasonReference or []
        self.deliverFrom: 'Reference' = deliverFrom 
        self.deliverTo: 'Reference' = deliverTo 
        