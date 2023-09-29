"""
Generated class for GraphDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Node(BaseModel):
    """ Potential target for the link.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str nodeId: Internal ID - target for link references
    :param str description: Why this node is specified
    :param str type: Type of resource this link refers to
    :param str profile: Profile for the target resource
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  nodeId:  'str'  = None,  description:  'str'  = None,  type:  'str'  = None,  profile:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.nodeId = nodeId 
        self.description = description 
        self.type = type 
        self.profile = profile 
        

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Compartment(BaseModel):
    """ Compartment Consistency Rules.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str use: where | requires
    :param str rule: identical | matching | different | custom
    :param str code: Patient | Encounter | RelatedPerson | Practitioner | Device | EpisodeOfCare
    :param str expression: Custom rule, as a FHIRPath expression
    :param str description: Documentation for FHIRPath expression
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  use:  'str'  = None,  rule:  'str'  = None,  code:  'str'  = None,  expression:  'str'  = None,  description:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.use = use 
        self.rule = rule 
        self.code = code 
        self.expression = expression 
        self.description = description 
        

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Link(BaseModel):
    """ Links this graph makes rules about.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Why this link is specified
    :param int min: Minimum occurrences for this link
    :param str max: Maximum occurrences for this link
    :param str sourceId: Source Node for this link
    :param str path: Path in the resource that contains the link
    :param str sliceName: Which slice (if profiled)
    :param str targetId: Target Node for this link
    :param str params: Criteria for reverse lookup
    :param Compartment compartment: Compartment Consistency Rules
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        
        
        
        "compartment": {"class_name": "Compartment", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  min:  'int'  = None,  max:  'str'  = None,  sourceId:  'str'  = None,  path:  'str'  = None,  sliceName:  'str'  = None,  targetId:  'str'  = None,  params:  'str'  = None,  compartment:  list['Compartment']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.min = min 
        self.max = max 
        self.sourceId = sourceId 
        self.path = path 
        self.sliceName = sliceName 
        self.targetId = targetId 
        self.params = params 
        self.compartment = compartment or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class GraphDefinition(DomainResource):
    """ A formal computable definition of a graph of resources - that is, a coherent set of resources that form a graph by following references. The Graph Definition resource defines a set and makes rules about the set.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this graph definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the GraphDefinition (business identifier)
    :param str version: Business version of the graph definition
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this graph definition (computer friendly)
    :param str title: Name for this graph definition (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the graph definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for graph definition (if applicable)
    :param str purpose: Why this graph definition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str start: Starting Node
    :param Node node: Potential target for the link
    :param Link link: Links this graph makes rules about
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        "node": {"class_name": "Node", "is_contained": True},
        
        
        "link": {"class_name": "Link", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  start:  'str'  = None,  node:  list['Node']  = None,  link:  list['Link']  = None, ):
        self.resourceType = resourceType or "GraphDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.status = status 
        self.experimental = experimental 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.start = start 
        self.node = node or []
        self.link = link or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "GraphDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GraphDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()