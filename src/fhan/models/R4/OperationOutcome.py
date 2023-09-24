"""
Generated class for OperationOutcome. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class Issue(ModelBase):
    """ An error, warning, or information message that results from a system action.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str severity: fatal | error | warning | information
    :param str code: Error or warning code
    :param 'CodeableConcept' details: Additional details about the error
    :param str diagnostics: Additional diagnostic information about the issue
    :param str location: Deprecated: Path of element(s) related to issue
    :param str expression: FHIRPath of element(s) related to issue
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  severity: str = None,  code: str = None,  details: 'CodeableConcept' = None,  diagnostics: str = None,  location: str = None,  expression: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.severity: str = severity 
        self.code: str = code 
        self.details: 'CodeableConcept' = details 
        self.diagnostics: str = diagnostics 
        self.location: str = location or []
        self.expression: str = expression or []
        

class OperationOutcome(DomainResource):
    """ A collection of error, warning, or information messages that result from a system action.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Issue'] issue: A single issue associated with the action
    """
    def __init__(self, resourceType: str = "OperationOutcome",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  issue: list['Issue'] = None, ):
        self.resourceType: str = resourceType or "OperationOutcome"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.issue: list['Issue'] = issue or []
        