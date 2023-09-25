"""
Generated class for Reference. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class Reference(ModelBase):
    """ Base StructureDefinition for Reference Type: A reference from one resource to another.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str reference: Literal reference, Relative, internal or absolute URL
    :param str type: Type the reference refers to (e.g. "Patient")
    :param 'Identifier' identifier: Logical reference, when literal reference is not known
    :param str display: Text alternative for the resource
    """
    def __init__(self, resourceType: str = "Reference",  id: str = None,  extension: list['Extension'] = None,  reference: str = None,  type: str = None,  identifier: 'Identifier' = None,  display: str = None, ):
        self.resourceType: str = resourceType or "Reference"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.reference: str = reference 
        self.type: str = type 
        self.identifier: 'Identifier' = identifier 
        self.display: str = display 
        