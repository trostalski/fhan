"""
Generated class for NamingSystem. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Period import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class UniqueId(Element):
    """ Indicates how the system may be identified when referenced in electronic exchange.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: oid | uuid | uri | other
    :param str value: The unique identifier
    :param bool preferred: Is this the id that should be used for this type
    :param str comment: Notes about identifier usage
    :param Period period: When is identifier valid?
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    type: str = None
    
    value: str = None
    
    preferred: bool = None
    
    comment: str = None
    period: "Period" = None
    

@dataclass
class NamingSystem(ModelBase):
    """ A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc.  Represents a "System" used within the Identifier and Coding data types.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str name: Name for this naming system (computer friendly)
    :param str status: draft | active | retired | unknown
    :param str kind: codesystem | identifier | root
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str responsible: Who maintains system namespace?
    :param CodeableConcept type: e.g. driver,  provider,  patient, bank etc.
    :param str description: Natural language description of the naming system
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for naming system (if applicable)
    :param str usage: How/where is it used
    :param UniqueId uniqueId: Unique identifiers used for system
    """

    resourceType: str = "NamingSystem"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    status: str = None
    
    kind: str = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    responsible: str = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    usage: str = None
    
    uniqueId: list["UniqueId"] = None
    