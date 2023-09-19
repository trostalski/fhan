"""
Generated class for Flag. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Flag:
    """ Prospective warnings of potential issues when providing care to the patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: active | inactive | entered-in-error
    :param CodeableConcept category: Clinical, administrative, etc
    :param CodeableConcept code: Coded or textual message to display to user
    :param Reference subject: Who/What is flag about?
    :param Period period: Time period when flag is active
    :param Reference encounter: Alert relevant during encounter
    :param Reference author: Flag creator
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    period: "Period" = None
    
    encounter: "Reference" = None
    
    author: "Reference" = None
    