"""
Generated class for CareTeam. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class CareTeam:
    """ The Care Team includes all the people and organizations who plan to participate in the coordination and delivery of care.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Ids for this team
    :param str status: proposed | active | suspended | inactive | entered-in-error
    :param CodeableConcept category: Type of team
    :param str name: Name of the team, such as crisis assessment team
    :param Reference subject: Who care team is for
    :param Period period: Time period team covers
    :param BackboneElement participant: Members of the team
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Type of involvement
    :param Reference member: Who is involved
    :param Reference onBehalfOf: Organization of the practitioner
    :param Period coveragePeriod: When the member is generally available within this care team
    :param Timing coveragePeriod: When the member is generally available within this care team
    :param CodeableReference reason: Why the care team exists
    :param Reference managingOrganization: Organization responsible for the care team
    :param ContactPoint telecom: A contact detail for the care team (that applies to all members)
    :param Annotation note: Comments made about the CareTeam
    
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
    
    name: str = None
    
    subject: "Reference" = None
    
    period: "Period" = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    member: "Reference" = None
    
    onBehalfOf: "Reference" = None
    
    coveragePeriod: "Period" = None
    
    coveragePeriod: "Timing" = None
    
    reason: "CodeableReference" = None
    
    managingOrganization: "Reference" = None
    
    telecom: "ContactPoint" = None
    
    note: "Annotation" = None
    