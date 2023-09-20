"""
Generated class for Organization. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.HumanName import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Address import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class contact(Element):
    """ Contact for the organization for a certain purpose.
    :param BackboneElement contact: Contact for the organization for a certain purpose
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: A name associated with the contact
    :param ContactPoint telecom: Contact details (telephone, email, etc.)  for a contact
    :param Address address: Visiting or postal addresses for the contact
    """
    contact: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    purpose: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: list["ContactPoint"] = None
    
    address: "Address" = None
    


@dataclass
class Organization(ModelBase):
    """ A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action.  Includes companies, institutions, corporations, departments, community groups, healthcare practice groups, payer/insurer, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifies this organization  across multiple systems
    :param bool active: Whether the organization's record is still in active use
    :param CodeableConcept type: Kind of organization
    :param str name: Name used for the organization
    :param str alias: A list of alternate names that the organization is known as, or was known as in the past
    :param ContactPoint telecom: A contact detail for the organization
    :param Address address: An address for the organization
    :param Reference partOf: The organization of which this organization forms a part
    :param BackboneElement contact: Contact for the organization for a certain purpose
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept purpose: The type of contact
    :param HumanName name: A name associated with the contact
    :param ContactPoint telecom: Contact details (telephone, email, etc.)  for a contact
    :param Address address: Visiting or postal addresses for the contact
    :param Reference endpoint: Technical endpoints providing access to services operated for the organization
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    active: bool = None
    
    type: list["CodeableConcept"] = None
    
    name: str = None
    
    alias: str = None
    
    telecom: list["ContactPoint"] = None
    
    address: list["Address"] = None
    
    partOf: "Reference" = None
    
    contact: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    purpose: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: list["ContactPoint"] = None
    
    address: "Address" = None
    
    endpoint: list["Reference"] = None
    