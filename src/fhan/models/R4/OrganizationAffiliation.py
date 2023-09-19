"""
Generated class for OrganizationAffiliation. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase


@dataclass
class OrganizationAffiliation(ModelBase):
    """ Defines an affiliation/assotiation/relationship between 2 distinct oganizations, that is not a part-of relationship/sub-division relationship.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifiers that are specific to this role
    :param bool active: Whether this organization affiliation record is in active use
    :param Period period: The period during which the participatingOrganization is affiliated with the primary organization
    :param Reference organization: Organization where the role is available
    :param Reference participatingOrganization: Organization that provides/performs the role (e.g. providing services or is a member of)
    :param Reference network: Health insurance provider network in which the participatingOrganization provides the role's services (if defined) at the indicated locations (if defined)
    :param CodeableConcept code: Definition of the role the participatingOrganization plays
    :param CodeableConcept specialty: Specific specialty of the participatingOrganization in the context of the role
    :param Reference location: The location(s) at which the role occurs
    :param Reference healthcareService: Healthcare services provided through the role
    :param ContactPoint telecom: Contact details at the participatingOrganization relevant to this Affiliation
    :param Reference endpoint: Technical endpoints providing access to services operated for this role
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
    
    active: bool = None
    
    period: "Period" = None
    
    organization: "Reference" = None
    
    participatingOrganization: "Reference" = None
    
    network: "Reference" = None
    
    code: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    location: "Reference" = None
    
    healthcareService: "Reference" = None
    
    telecom: "ContactPoint" = None
    
    endpoint: "Reference" = None
    