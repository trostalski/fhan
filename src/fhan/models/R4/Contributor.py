"""
Generated class for Contributor. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Contributor(ModelBase):
    """ Base StructureDefinition for Contributor Type: A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str type: author | editor | reviewer | endorser
    :param str name: Who contributed the content
    :param list['ContactDetail'] contact: Contact details of the contributor
    """
    def __init__(self, resourceType: str = "Contributor",  id: str = None,  extension: list['Extension'] = None,  type: str = None,  name: str = None,  contact: list['ContactDetail'] = None, ):
        self.resourceType: str = resourceType or "Contributor"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.name: str = name 
        self.contact: list['ContactDetail'] = contact or []
        