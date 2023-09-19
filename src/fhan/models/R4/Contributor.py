"""
Generated class for Contributor. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *



@dataclass
class Contributor(Element):
    """ Base StructureDefinition for Contributor Type: A contributor to the content of a knowledge asset, including authors, editors, reviewers, and endorsers.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: author | editor | reviewer | endorser
    :param str name: Who contributed the content
    :param ContactDetail contact: Contact details of the contributor
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    name: str = None
    
    contact: "ContactDetail" = None
    