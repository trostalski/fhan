"""
Generated class for NamingSystem. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.DomainResource import *


    
    

class UniqueId(ModelBase):
    """ Indicates how the system may be identified when referenced in electronic exchange.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: oid | uuid | uri | other
    :param str value: The unique identifier
    :param bool preferred: Is this the id that should be used for this type
    :param str comment: Notes about identifier usage
    :param 'Period' period: When is identifier valid?
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  value: str = None,  preferred: bool = None,  comment: str = None,  period: 'Period' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.value: str = value 
        self.preferred: bool = preferred 
        self.comment: str = comment 
        self.period: 'Period' = period 
        

class NamingSystem(DomainResource):
    """ A curated namespace that issues unique symbols within that namespace for the identification of concepts, people, devices, etc.  Represents a "System" used within the Identifier and Coding data types.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param str name: Name for this naming system (computer friendly)
    :param str status: draft | active | retired | unknown
    :param str kind: codesystem | identifier | root
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param list['ContactDetail'] contact: Contact details for the publisher
    :param str responsible: Who maintains system namespace?
    :param 'CodeableConcept' type: e.g. driver,  provider,  patient, bank etc.
    :param str description: Natural language description of the naming system
    :param list['UsageContext'] useContext: The context that the content is intended to support
    :param list['CodeableConcept'] jurisdiction: Intended jurisdiction for naming system (if applicable)
    :param str usage: How/where is it used
    :param list['UniqueId'] uniqueId: Unique identifiers used for system
    """
    def __init__(self, resourceType: str = "NamingSystem",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  name: str = None,  status: str = None,  kind: str = None,  date: str = None,  publisher: str = None,  contact: list['ContactDetail'] = None,  responsible: str = None,  type: 'CodeableConcept' = None,  description: str = None,  useContext: list['UsageContext'] = None,  jurisdiction: list['CodeableConcept'] = None,  usage: str = None,  uniqueId: list['UniqueId'] = None, ):
        self.resourceType: str = resourceType or "NamingSystem"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.name: str = name 
        self.status: str = status 
        self.kind: str = kind 
        self.date: str = date 
        self.publisher: str = publisher 
        self.contact: list['ContactDetail'] = contact or []
        self.responsible: str = responsible 
        self.type: 'CodeableConcept' = type 
        self.description: str = description 
        self.useContext: list['UsageContext'] = useContext or []
        self.jurisdiction: list['CodeableConcept'] = jurisdiction or []
        self.usage: str = usage 
        self.uniqueId: list['UniqueId'] = uniqueId or []
        