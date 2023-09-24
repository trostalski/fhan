"""
Generated class for Annotation. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import ModelBase

class Annotation(ModelBase):
    """ Base StructureDefinition for Annotation Type: A  text note which also  contains information about who made the statement and when.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param 'Reference' authorReference: Individual responsible for the annotation
    :param str time: When the annotation was made
    :param str text: The annotation  - text content (as markdown)
    """
    def __init__(self, resourceType: str = "Annotation",  id: str = None,  extension: list['Extension'] = None,  authorReference: 'Reference' = None,  time: str = None,  text: str = None, ):
        self.resourceType: str = resourceType or "Annotation"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.authorReference: 'Reference' = authorReference 
        self.time: str = time 
        self.text: str = text 
        