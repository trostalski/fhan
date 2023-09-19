"""
Generated class for Endpoint. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class Endpoint:
    """
    The technical details of an endpoint that can be used for electronic services, such as for web services providing XDS.b or a REST endpoint for another FHIR server. This may include any security context information.
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
    
    connectionType: "Coding" = None
    
    name: str = None
    
    managingOrganization: "Reference" = None
    
    contact: "ContactPoint" = None
    
    period: "Period" = None
    
    payloadType: "CodeableConcept" = None
    
    payloadMimeType: str = None
    
    address: str = None
    
    header: str = None
    