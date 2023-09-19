"""
Generated class for TestScript. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.Narrative import *
from fhan.models.R4.Resource import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Reference import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *


@dataclass
class TestScript:
    """
    A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    origin: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    index: int = None
    
    profile: "Coding" = None
    
    destination: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    index: int = None
    
    profile: "Coding" = None
    
    metadata: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    description: str = None
    
    capability: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    required: bool = None
    
    validated: bool = None
    
    description: str = None
    
    origin: int = None
    
    destination: int = None
    
    link: str = None
    
    capabilities: str = None
    
    fixture: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    autocreate: bool = None
    
    autodelete: bool = None
    
    resource: "Reference" = None
    
    profile: "Reference" = None
    
    variable: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    defaultValue: str = None
    
    description: str = None
    
    expression: str = None
    
    headerField: str = None
    
    hint: str = None
    
    path: str = None
    
    sourceId: str = None
    
    setup: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    action: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    operation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "Coding" = None
    
    resource: str = None
    
    label: str = None
    
    description: str = None
    
    accept: str = None
    
    contentType: str = None
    
    destination: int = None
    
    encodeRequestUrl: bool = None
    
    method: str = None
    
    origin: int = None
    
    params: str = None
    
    requestHeader: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    field: str = None
    
    value: str = None
    
    requestId: str = None
    
    responseId: str = None
    
    sourceId: str = None
    
    targetId: str = None
    
    url: str = None
    
    assert: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    label: str = None
    
    description: str = None
    
    direction: str = None
    
    compareToSourceId: str = None
    
    compareToSourceExpression: str = None
    
    compareToSourcePath: str = None
    
    contentType: str = None
    
    expression: str = None
    
    headerField: str = None
    
    minimumId: str = None
    
    navigationLinks: bool = None
    
    operator: str = None
    
    path: str = None
    
    requestMethod: str = None
    
    requestURL: str = None
    
    resource: str = None
    
    response: str = None
    
    responseCode: str = None
    
    sourceId: str = None
    
    validateProfileId: str = None
    
    value: str = None
    
    warningOnly: bool = None
    
    test: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    description: str = None
    
    action: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    operation: "BackboneElement" = None
    
    assert: "BackboneElement" = None
    
    teardown: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    action: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    operation: "BackboneElement" = None
    