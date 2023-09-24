"""
Generated class for HumanName. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class HumanName(ModelBase):
    """ Base StructureDefinition for HumanName Type: A human's name with the ability to identify parts and usage.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str use: usual | official | temp | nickname | anonymous | old | maiden
    :param str text: Text representation of the full name
    :param str family: Family name (often called 'Surname')
    :param str given: Given names (not always 'first'). Includes middle names
    :param str prefix: Parts that come before the name
    :param str suffix: Parts that come after the name
    :param 'Period' period: Time period when name was/is in use
    """
    def __init__(self, resourceType: str = "HumanName",  id: str = None,  extension: list['Extension'] = None,  use: str = None,  text: str = None,  family: str = None,  given: str = None,  prefix: str = None,  suffix: str = None,  period: 'Period' = None, ):
        self.resourceType: str = resourceType or "HumanName"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.use: str = use 
        self.text: str = text 
        self.family: str = family 
        self.given: str = given or []
        self.prefix: str = prefix or []
        self.suffix: str = suffix or []
        self.period: 'Period' = period 
        