"""
Generated class for Expression. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *


@dataclass
class Expression:
    """
    Base StructureDefinition for Expression Type: A expression that is evaluated in a specified context and returns a value. The context of use of the expression must specify the context in which the expression is evaluated, and how the result of the expression is used.
    """
    id: str = None
    
    extension: "Extension" = None
    
    description: str = None
    
    name: str = None
    
    language: str = None
    
    expression: str = None
    
    reference: str = None
    