"""
Generated class for Endpoint. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

@dataclass
class Endpoint(ModelBase):
    """ The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
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
    :param Coding connectionType: Protocol/Profile/Standard to be used with this endpoint connection
    :param str name: A name that this endpoint can be identified by
    :param Reference managingOrganization: Organization that manages this endpoint (might not be the organization that exposes the endpoint)
    :param ContactPoint contact: Contact details for source (e.g. troubleshooting)
    :param Period period: Interval the endpoint is expected to be operational
    :param CodeableConcept payloadType: The type of content that may be used at this endpoint (e.g. XDS Discharge summaries)
    :param str payloadMimeType: Mimetype to send. If not specified, the content could be anything (including no payload, if the connectionType defined this)
    :param str address: The technical base address for connecting to this endpoint
    :param str header: Usage depends on the channel type
    """

    resourceType: str = "Endpoint"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    connectionType: "Coding" = Coding()
    
    name: str = None
    
    managingOrganization: "Reference" = Reference()
    
    contact: list[ContactPoint] = ContactPoint() 
    
    period: "Period" = Period()
    
    payloadType: list[CodeableConcept] = CodeableConcept() 
    
    payloadMimeType: str = None
    
    address: str = None
    
    header: str = None
    