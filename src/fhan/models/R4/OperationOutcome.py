"""
Generated class for OperationOutcome. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Issue(Element):
    """ An error, warning, or information message that results from a system action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str severity: fatal | error | warning | information
    :param str code: Error or warning code
    :param CodeableConcept details: Additional details about the error
    :param str diagnostics: Additional diagnostic information about the issue
    :param str location: Deprecated: Path of element(s) related to issue
    :param str expression: FHIRPath of element(s) related to issue
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    severity: str = None
    
    code: str = None
    details: "CodeableConcept" = None
    
    diagnostics: str = None
    
    location: str = None
    
    expression: str = None
    
@dataclass
class OperationOutcome(ModelBase):
    """ A collection of error, warning, or information messages that result from a system action.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Issue issue: A single issue associated with the action
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    issue: list["Issue"] = None
    