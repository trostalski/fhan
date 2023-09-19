"""
Generated class for OperationOutcome. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *


@dataclass
class OperationOutcome:
    """ A collection of error, warning, or information messages that result from a system action.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param BackboneElement issue: A single issue associated with the action
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str severity: fatal | error | warning | information | success
    :param str code: Error or warning code
    :param CodeableConcept details: Additional details about the error
    :param str diagnostics: Additional diagnostic information about the issue
    :param str location: Deprecated: Path of element(s) related to issue
    :param str expression: FHIRPath of element(s) related to issue
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    issue: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    severity: str = None
    
    code: str = None
    
    details: "CodeableConcept" = None
    
    diagnostics: str = None
    
    location: str = None
    
    expression: str = None
    