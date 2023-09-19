"""
Generated class for PractitionerRole. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Availability import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class PractitionerRole:
    """ A specific set of Roles/Locations/specialties/services that a practitioner may perform, or has performed at an organization during a period of time.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers for a role/location
    :param bool active: Whether this practitioner role record is in active use
    :param Period period: The period during which the practitioner is authorized to perform in these role(s)
    :param Reference practitioner: Practitioner that provides services for the organization
    :param Reference organization: Organization where the roles are available
    :param CodeableConcept code: Roles which this practitioner may perform
    :param CodeableConcept specialty: Specific specialty of the practitioner
    :param Reference location: Location(s) where the practitioner provides care
    :param Reference healthcareService: Healthcare services provided for this role's Organization/Location(s)
    :param ExtendedContactDetail contact: Official contact details relating to this PractitionerRole
    :param CodeableConcept characteristic: Collection of characteristics (attributes)
    :param CodeableConcept communication: A language the practitioner (in this role) can use in patient communication
    :param Availability availability: Times the Practitioner is available at this location and/or healthcare service (including exceptions)
    :param Reference endpoint: Endpoints for interacting with the practitioner in this role
    
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
    
    practitioner: "Reference" = None
    
    organization: "Reference" = None
    
    code: "CodeableConcept" = None
    
    specialty: "CodeableConcept" = None
    
    location: "Reference" = None
    
    healthcareService: "Reference" = None
    
    contact: "ExtendedContactDetail" = None
    
    characteristic: "CodeableConcept" = None
    
    communication: "CodeableConcept" = None
    
    availability: "Availability" = None
    
    endpoint: "Reference" = None
    