"""
Generated class for Expression. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.Extension import *
from fhan.models.R4.Element import *




@dataclass
class Expression(Element):
    """ Base StructureDefinition for Expression Type: A expression that is evaluated in a specified context and returns a value. The context of use of the expression must specify the context in which the expression is evaluated, and how the result of the expression is used.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str description: Natural language description of the condition
    :param str name: Short name assigned to expression for reuse
    :param str language: text/cql | text/fhirpath | application/x-fhir-query | etc.
    :param str expression: Expression in specified language
    :param str reference: Where the expression is found
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    description: str = None
    
    name: str = None
    
    language: str = None
    
    expression: str = None
    
    reference: str = None
    