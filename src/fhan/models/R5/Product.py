"""
Generated class for Product. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Element import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Product:
    """ Logical Model: A pattern to be followed by resources that represent a product used in healthcare, for clinical or operational purposes.
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: A category or class of the product
    :param CodeableConcept code: A code designating a specific type of product
    :param Reference manufacturer: Manufacturer, representative or officially responsible for the product
    :param Element instance: One or several physical instances or occurrences of the product
    :param Quantity quantity: The amount of items
    :param Identifier identifier: The identifier for the physical instance, typically a serial number
    :param str lotNumber: The identification of the batch or lot of the product
    :param str expiry: The expiry date or date and time for the product
    :param Reference subject: Individual the product is associated with, or which has used the product
    :param Annotation note: Comments made about the product
    
    """
    status: str = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    manufacturer: "Reference" = None
    
    instance: "Element" = None
    
    quantity: "Quantity" = None
    
    identifier: "Identifier" = None
    
    lotNumber: str = None
    
    expiry: str = None
    
    subject: "Reference" = None
    
    note: "Annotation" = None
    