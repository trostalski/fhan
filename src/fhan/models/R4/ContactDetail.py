"""
Generated class for ContactDetail. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactPoint import *
from fhan.models.generator_models import ModelBase

class ContactDetail(ModelBase):
    """ Base StructureDefinition for ContactDetail Type: Specifies contact information for a person or organization.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str name: Name of an individual to contact
    :param list['ContactPoint'] telecom: Contact details for individual or organization
    """
    def __init__(self, resourceType: str = "ContactDetail",  id: str = None,  extension: list['Extension'] = None,  name: str = None,  telecom: list['ContactPoint'] = None, ):
        self.resourceType: str = resourceType or "ContactDetail"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.name: str = name 
        self.telecom: list['ContactPoint'] = telecom or []
        