"""
Generated class for UsageContext. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Range import *
from fhan.models.R4.Quantity import *
from fhan.models.generator_models import ModelBase

class UsageContext(ModelBase):
    """ Base StructureDefinition for UsageContext Type: Specifies clinical/business/etc. metadata that can be used to retrieve, index and/or categorize an artifact. This metadata can either be specific to the applicable population (e.g., age category, DRG) or the specific context of care (e.g., venue, care setting, provider of care).
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Coding' code: Type of context being specified
    :param 'CodeableConcept' valueCodeableConcept: Value that defines the context
    :param 'Quantity' valueQuantity: Value that defines the context
    :param 'Range' valueRange: Value that defines the context
    :param 'Reference' valueReference: Value that defines the context
    """
    def __init__(self, resourceType: str = "UsageContext",  id: str = None,  extension: list['Extension'] = None,  code: 'Coding' = None,  valueCodeableConcept: 'CodeableConcept' = None,  valueQuantity: 'Quantity' = None,  valueRange: 'Range' = None,  valueReference: 'Reference' = None, ):
        self.resourceType: str = resourceType or "UsageContext"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.code: 'Coding' = code 
        self.valueCodeableConcept: 'CodeableConcept' = valueCodeableConcept 
        self.valueQuantity: 'Quantity' = valueQuantity 
        self.valueRange: 'Range' = valueRange 
        self.valueReference: 'Reference' = valueReference 
        