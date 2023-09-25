"""
Generated class for Organization. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Address import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Contact(ModelBase):
    """ Contact for the organization for a certain purpose.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' purpose: The type of contact
    :param 'HumanName' name: A name associated with the contact
    :param list['ContactPoint'] telecom: Contact details (telephone, email, etc.)  for a contact
    :param 'Address' address: Visiting or postal addresses for the contact
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  purpose: 'CodeableConcept' = None,  name: 'HumanName' = None,  telecom: list['ContactPoint'] = None,  address: 'Address' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.purpose: 'CodeableConcept' = purpose 
        self.name: 'HumanName' = name 
        self.telecom: list['ContactPoint'] = telecom or []
        self.address: 'Address' = address 
        

class Organization(DomainResource):
    """ A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Identifies this organization  across multiple systems
    :param bool active: Whether the organization's record is still in active use
    :param list['CodeableConcept'] type: Kind of organization
    :param str name: Name used for the organization
    :param str alias: A list of alternate names that the organization is known as, or was known as in the past
    :param list['ContactPoint'] telecom: A contact detail for the organization
    :param list['Address'] address: An address for the organization
    :param 'Reference' partOf: The organization of which this organization forms a part
    :param list['Contact'] contact: Contact for the organization for a certain purpose
    :param list['Reference'] endpoint: Technical endpoints providing access to services operated for the organization
    """
    def __init__(self, resourceType: str = "Organization",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  active: bool = None,  type: list['CodeableConcept'] = None,  name: str = None,  alias: str = None,  telecom: list['ContactPoint'] = None,  address: list['Address'] = None,  partOf: 'Reference' = None,  contact: list['Contact'] = None,  endpoint: list['Reference'] = None, ):
        self.resourceType: str = resourceType or "Organization"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.active: bool = active 
        self.type: list['CodeableConcept'] = type or []
        self.name: str = name 
        self.alias: str = alias or []
        self.telecom: list['ContactPoint'] = telecom or []
        self.address: list['Address'] = address or []
        self.partOf: 'Reference' = partOf 
        self.contact: list['Contact'] = contact or []
        self.endpoint: list['Reference'] = endpoint or []
        