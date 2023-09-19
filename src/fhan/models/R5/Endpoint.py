"""
Generated class for Endpoint. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Endpoint:
    """ The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b, a REST endpoint for another FHIR server, or a s/Mime email address. This may include any security context information.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifies this endpoint across multiple systems
    :param str status: active | suspended | error | off | entered-in-error | test
    :param CodeableConcept connectionType: Protocol/Profile/Standard to be used with this endpoint connection
    :param str name: A name that this endpoint can be identified by
    :param str description: Additional details about the endpoint that could be displayed as further information to identify the description beyond its name
    :param CodeableConcept environmentType: The type of environment(s) exposed at this endpoint
    :param Reference managingOrganization: Organization that manages this endpoint (might not be the organization that exposes the endpoint)
    :param ContactPoint contact: Contact details for source (e.g. troubleshooting)
    :param Period period: Interval the endpoint is expected to be operational
    :param BackboneElement payload: Set of payloads that are provided by this endpoint
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
    :param str mimeType: Mimetype to send. If not specified, the content could be anything (including no payload, if the connectionType defined this)
    :param str address: The technical base address for connecting to this endpoint
    :param str header: Usage depends on the channel type
    
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
    
    connectionType: "CodeableConcept" = None
    
    name: str = None
    
    description: str = None
    
    environmentType: "CodeableConcept" = None
    
    managingOrganization: "Reference" = None
    
    contact: "ContactPoint" = None
    
    period: "Period" = None
    
    payload: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    mimeType: str = None
    
    address: str = None
    
    header: str = None
    