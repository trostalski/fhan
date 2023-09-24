"""
Generated class for ContactPoint. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class ContactPoint(ModelBase):
    """ Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str system: phone | fax | email | pager | url | sms | other
    :param str value: The actual contact point details
    :param str use: home | work | temp | old | mobile - purpose of this contact point
    :param int rank: Specify preferred order of use (1 = highest)
    :param 'Period' period: Time period when the contact point was/is in use
    """
    def __init__(self, resourceType: str = "ContactPoint",  id: str = None,  extension: list['Extension'] = None,  system: str = None,  value: str = None,  use: str = None,  rank: int = None,  period: 'Period' = None, ):
        self.resourceType: str = resourceType or "ContactPoint"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.system: str = system 
        self.value: str = value 
        self.use: str = use 
        self.rank: int = rank 
        self.period: 'Period' = period 
        