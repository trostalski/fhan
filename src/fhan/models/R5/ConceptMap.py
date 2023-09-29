"""
Generated class for ConceptMap. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Property(BaseModel):
    """ A property defines a slot through which additional information can be provided about a map from source -> target.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies the property on the mappings, and when referred to in the $translate operation
    :param str uri: Formal identifier for the property
    :param str description: Why the property is defined, and/or what it conveys
    :param str type: Coding | string | integer | boolean | dateTime | decimal | code
    :param str system: The CodeSystem from which code values come
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  uri:  'str'  = None,  description:  'str'  = None,  type:  'str'  = None,  system:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.uri = uri 
        self.description = description 
        self.type = type 
        self.system = system 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class AdditionalAttribute(BaseModel):
    """ An additionalAttribute defines an additional data element found in the source or target data model where the data will come from or be mapped to. Some mappings are based on data in addition to the source data element, where codes in multiple fields are combined to a single field (or vice versa).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies this additional attribute through this resource
    :param str uri: Formal identifier for the data element referred to in this attribte
    :param str description: Why the additional attribute is defined, and/or what the data element it refers to is
    :param str type: code | Coding | string | boolean | Quantity
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  uri:  'str'  = None,  description:  'str'  = None,  type:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.uri = uri 
        self.description = description 
        self.type = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
        
    
    

class Property(BaseModel):
    """ A property value for this source -> target mapping.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Reference to ConceptMap.property.code
    :param Coding valueCoding: Value of the property for this concept
    :param str valueString: Value of the property for this concept
    :param int valueInteger: Value of the property for this concept
    :param bool valueBoolean: Value of the property for this concept
    :param str valueDateTime: Value of the property for this concept
    :param float valueDecimal: Value of the property for this concept
    :param str valueCode: Value of the property for this concept
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  valueCoding:  'Coding'  = None,  valueString:  'str'  = None,  valueInteger:  'int'  = None,  valueBoolean:  'bool'  = None,  valueDateTime:  'str'  = None,  valueDecimal:  'float'  = None,  valueCode:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.valueCoding = valueCoding 
        self.valueString = valueString 
        self.valueInteger = valueInteger 
        self.valueBoolean = valueBoolean 
        self.valueDateTime = valueDateTime 
        self.valueDecimal = valueDecimal 
        self.valueCode = valueCode 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class DependsOn(BaseModel):
    """ A set of additional dependencies for this mapping to hold. This mapping is only applicable if the specified data attribute can be resolved, and it has the specified value.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str attribute: A reference to a mapping attribute defined in ConceptMap.additionalAttribute
    :param str valueCode: Value of the referenced data element
    :param Coding valueCoding: Value of the referenced data element
    :param str valueString: Value of the referenced data element
    :param bool valueBoolean: Value of the referenced data element
    :param Quantity valueQuantity: Value of the referenced data element
    :param str valueSet: The mapping depends on a data element with a value from this value set
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "valueCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  attribute:  'str'  = None,  valueCode:  'str'  = None,  valueCoding:  'Coding'  = None,  valueString:  'str'  = None,  valueBoolean:  'bool'  = None,  valueQuantity:  'Quantity'  = None,  valueSet:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.attribute = attribute 
        self.valueCode = valueCode 
        self.valueCoding = valueCoding 
        self.valueString = valueString 
        self.valueBoolean = valueBoolean 
        self.valueQuantity = valueQuantity 
        self.valueSet = valueSet 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Target(BaseModel):
    """ A concept from the target value set that this concept maps to.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Code that identifies the target element
    :param str display: Display for the code
    :param str valueSet: Identifies the set of target concepts
    :param str relationship: related-to | equivalent | source-is-narrower-than-target | source-is-broader-than-target | not-related-to
    :param str comment: Description of status/issues in mapping
    :param Property property: Property value for the source -> target mapping
    :param DependsOn dependsOn: Other properties required for this mapping
    :param Product product: Other data elements that this mapping also produces
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "dependsOn": {"class_name": "DependsOn", "is_contained": True},
        
        
        "product": {"class_name": "Product", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  display:  'str'  = None,  valueSet:  'str'  = None,  relationship:  'str'  = None,  comment:  'str'  = None,  property:  list['Property']  = None,  dependsOn:  list['DependsOn']  = None,  product:  list['Product']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.display = display 
        self.valueSet = valueSet 
        self.relationship = relationship 
        self.comment = comment 
        self.property = property or []
        self.dependsOn = dependsOn or []
        self.product = product or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Element(BaseModel):
    """ Mappings for an individual concept in the source to one or more concepts in the target.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: Identifies element being mapped
    :param str display: Display for the code
    :param str valueSet: Identifies the set of concepts being mapped
    :param bool noMap: No mapping to a target concept for this source concept
    :param Target target: Concept in target system for element
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        "target": {"class_name": "Target", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'str'  = None,  display:  'str'  = None,  valueSet:  'str'  = None,  noMap:  'bool'  = None,  target:  list['Target']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.display = display 
        self.valueSet = valueSet 
        self.noMap = noMap 
        self.target = target or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Unmapped(BaseModel):
    """ What to do when there is no mapping to a target concept from the source concept and ConceptMap.group.element.noMap is not true. This provides the "default" to be applied when there is no target concept mapping specified or the expansion of ConceptMap.group.element.target.valueSet is empty.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: use-source-code | fixed | other-map
    :param str code: Fixed code when mode = fixed
    :param str display: Display for the code
    :param str valueSet: Fixed code set when mode = fixed
    :param str relationship: related-to | equivalent | source-is-narrower-than-target | source-is-broader-than-target | not-related-to
    :param str otherMap: canonical reference to an additional ConceptMap to use for mapping if the source concept is unmapped
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  mode:  'str'  = None,  code:  'str'  = None,  display:  'str'  = None,  valueSet:  'str'  = None,  relationship:  'str'  = None,  otherMap:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.mode = mode 
        self.code = code 
        self.display = display 
        self.valueSet = valueSet 
        self.relationship = relationship 
        self.otherMap = otherMap 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Group(BaseModel):
    """ A group of mappings that all have the same source and target system.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str source: Source system where concepts to be mapped are defined
    :param str target: Target system that the concepts are to be mapped to
    :param Element element: Mappings for a concept from the source set
    :param Unmapped unmapped: What to do when there is no mapping target for the source concept and ConceptMap.group.element.noMap is not true
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "element": {"class_name": "Element", "is_contained": True},
        
        
        "unmapped": {"class_name": "Unmapped", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  source:  'str'  = None,  target:  'str'  = None,  element:  list['Element']  = None,  unmapped:  'Unmapped'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.source = source 
        self.target = target 
        self.element = element or []
        self.unmapped = unmapped 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ConceptMap(DomainResource):
    """ A statement of relationships from one set of concepts to one or more other concepts - either concepts in code systems, or data element/data element concepts, or classes in class models.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this concept map, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the concept map
    :param str version: Business version of the concept map
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this concept map (computer friendly)
    :param str title: Name for this concept map (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the concept map
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for concept map (if applicable)
    :param str purpose: Why this concept map is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the ConceptMap was approved by publisher
    :param str lastReviewDate: When the ConceptMap was last reviewed by the publisher
    :param Period effectivePeriod: When the ConceptMap is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the ConceptMap
    :param ContactDetail editor: Who edited the ConceptMap
    :param ContactDetail reviewer: Who reviewed the ConceptMap
    :param ContactDetail endorser: Who endorsed the ConceptMap
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param Property property: Additional properties of the mapping
    :param AdditionalAttribute additionalAttribute: Definition of an additional attribute to act as a data source or target
    :param str sourceScopeUri: The source value set that contains the concepts that are being mapped
    :param str sourceScopeCanonical: The source value set that contains the concepts that are being mapped
    :param str targetScopeUri: The target value set which provides context for the mappings
    :param str targetScopeCanonical: The target value set which provides context for the mappings
    :param Group group: Same source and target systems
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
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "additionalAttribute": {"class_name": "AdditionalAttribute", "is_contained": True},
        
        
        
        
        
        
        "group": {"class_name": "Group", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  topic:  list['CodeableConcept']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  property:  list['Property']  = None,  additionalAttribute:  list['AdditionalAttribute']  = None,  sourceScopeUri:  'str'  = None,  sourceScopeCanonical:  'str'  = None,  targetScopeUri:  'str'  = None,  targetScopeCanonical:  'str'  = None,  group:  list['Group']  = None, ):
        self.resourceType = resourceType or "ConceptMap"
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
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.topic = topic or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatedArtifact = relatedArtifact or []
        self.property = property or []
        self.additionalAttribute = additionalAttribute or []
        self.sourceScopeUri = sourceScopeUri 
        self.sourceScopeCanonical = sourceScopeCanonical 
        self.targetScopeUri = targetScopeUri 
        self.targetScopeCanonical = targetScopeCanonical 
        self.group = group or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ConceptMap":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ConceptMap":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()