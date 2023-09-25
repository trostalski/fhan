"""
Generated class for Coding. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Coding(ModelBase):
    """ Base StructureDefinition for Coding Type: A reference to a code defined by a terminology system.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str system: Identity of the terminology system
    :param str version: Version of the system - if relevant
    :param str code: Symbol in syntax defined by the system
    :param str display: Representation defined by the system
    :param bool userSelected: If this coding was chosen directly by the user
    """
    def __init__(self, resourceType: str = "Coding",  id: str = None,  extension: list['Extension'] = None,  system: str = None,  version: str = None,  code: str = None,  display: str = None,  userSelected: bool = None, ):
        self.resourceType: str = resourceType or "Coding"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.system: str = system 
        self.version: str = version 
        self.code: str = code 
        self.display: str = display 
        self.userSelected: bool = userSelected 
        