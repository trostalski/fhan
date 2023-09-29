"""
Generated class for Measure. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Expression import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Term(BaseModel):
    """ Provides a description of an individual term used within the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: What term?
    :param str definition: Meaning of the term
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  definition:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.definition = definition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Measure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Measure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Population(BaseModel):
    """ A population criteria for the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for population in measure
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param str description: The human readable description of this population criteria
    :param Expression criteria: The criteria that defines this population
    :param Reference groupDefinition: A group resource that defines this population
    :param str inputPopulationId: Which population
    :param CodeableConcept aggregateMethod: Aggregation method for a measure score (e.g. sum, average, median, minimum, maximum, count)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "criteria": {"class_name": "Expression", "is_contained": False},
        
        
        "groupDefinition": {"class_name": "Reference", "is_contained": False},
        
        
        
        "aggregateMethod": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  description:  'str'  = None,  criteria:  'Expression'  = None,  groupDefinition:  'Reference'  = None,  inputPopulationId:  'str'  = None,  aggregateMethod:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.description = description 
        self.criteria = criteria 
        self.groupDefinition = groupDefinition 
        self.inputPopulationId = inputPopulationId 
        self.aggregateMethod = aggregateMethod 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Measure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Measure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Component(BaseModel):
    """ A component of the stratifier criteria for the measure report, specified as either the name of a valid CQL expression defined within a referenced library or a valid FHIR Resource Path.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for stratifier component in measure
    :param CodeableConcept code: Meaning of the stratifier component
    :param str description: The human readable description of this stratifier component
    :param Expression criteria: Component of how the measure should be stratified
    :param Reference groupDefinition: A group resource that defines this population
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "criteria": {"class_name": "Expression", "is_contained": False},
        
        
        "groupDefinition": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  description:  'str'  = None,  criteria:  'Expression'  = None,  groupDefinition:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.description = description 
        self.criteria = criteria 
        self.groupDefinition = groupDefinition 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Measure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Measure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Stratifier(BaseModel):
    """ The stratifier criteria for the measure report, specified as either the name of a valid CQL expression defined within a referenced library or a valid FHIR Resource Path.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for stratifier in measure
    :param CodeableConcept code: Meaning of the stratifier
    :param str description: The human readable description of this stratifier
    :param Expression criteria: How the measure should be stratified
    :param Reference groupDefinition: A group resource that defines this population
    :param Component component: Stratifier criteria component for the measure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "criteria": {"class_name": "Expression", "is_contained": False},
        
        
        "groupDefinition": {"class_name": "Reference", "is_contained": False},
        
        
        "component": {"class_name": "Component", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  description:  'str'  = None,  criteria:  'Expression'  = None,  groupDefinition:  'Reference'  = None,  component:  list['Component']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.description = description 
        self.criteria = criteria 
        self.groupDefinition = groupDefinition 
        self.component = component or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Measure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Measure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Group(BaseModel):
    """ A group of population criteria for the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for group in measure
    :param CodeableConcept code: Meaning of the group
    :param str description: Summary description
    :param CodeableConcept type: process | outcome | structure | patient-reported-outcome | composite
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param Reference subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str basis: Population basis
    :param CodeableConcept scoring: proportion | ratio | continuous-variable | cohort
    :param CodeableConcept scoringUnit: What units?
    :param str rateAggregation: How is rate aggregation performed for this measure
    :param CodeableConcept improvementNotation: increase | decrease
    :param str library: Logic used by the measure group
    :param Population population: Population criteria
    :param Stratifier stratifier: Stratifier criteria for the measure
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subjectCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        "scoring": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "scoringUnit": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "improvementNotation": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "population": {"class_name": "Population", "is_contained": True},
        
        
        "stratifier": {"class_name": "Stratifier", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  description:  'str'  = None,  type:  list['CodeableConcept']  = None,  subjectCodeableConcept:  'CodeableConcept'  = None,  subjectReference:  'Reference'  = None,  basis:  'str'  = None,  scoring:  'CodeableConcept'  = None,  scoringUnit:  'CodeableConcept'  = None,  rateAggregation:  'str'  = None,  improvementNotation:  'CodeableConcept'  = None,  library:  list['str']  = None,  population:  list['Population']  = None,  stratifier:  list['Stratifier']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.description = description 
        self.type = type or []
        self.subjectCodeableConcept = subjectCodeableConcept 
        self.subjectReference = subjectReference 
        self.basis = basis 
        self.scoring = scoring 
        self.scoringUnit = scoringUnit 
        self.rateAggregation = rateAggregation 
        self.improvementNotation = improvementNotation 
        self.library = library or []
        self.population = population or []
        self.stratifier = stratifier or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Measure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Measure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class SupplementalData(BaseModel):
    """ The supplemental data criteria for the measure report, specified as either the name of a valid CQL expression within a referenced library, or a valid FHIR Resource Path.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Unique id for supplementalData in measure
    :param CodeableConcept code: Meaning of the supplemental data
    :param CodeableConcept usage: supplemental-data | risk-adjustment-factor
    :param str description: The human readable description of this supplemental data
    :param Expression criteria: Expression describing additional data to be reported
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "usage": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "criteria": {"class_name": "Expression", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  usage:  list['CodeableConcept']  = None,  description:  'str'  = None,  criteria:  'Expression'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.usage = usage or []
        self.description = description 
        self.criteria = criteria 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Measure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Measure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Measure(DomainResource):
    """ The Measure resource provides the definition of a quality measure.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this measure, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the measure
    :param str version: Business version of the measure
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this measure (computer friendly)
    :param str title: Name for this measure (human friendly)
    :param str subtitle: Subordinate title of the measure
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param Reference subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str basis: Population basis
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the measure
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for measure (if applicable)
    :param str purpose: Why this measure is defined
    :param str usage: Describes the clinical usage of the measure
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the measure was approved by publisher
    :param str lastReviewDate: When the measure was last reviewed by the publisher
    :param Period effectivePeriod: When the measure is expected to be used
    :param CodeableConcept topic: The category of the measure, such as Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param str library: Logic used by the measure
    :param str disclaimer: Disclaimer for use of the measure or its referenced content
    :param CodeableConcept scoring: proportion | ratio | continuous-variable | cohort
    :param CodeableConcept scoringUnit: What units?
    :param CodeableConcept compositeScoring: opportunity | all-or-nothing | linear | weighted
    :param CodeableConcept type: process | outcome | structure | patient-reported-outcome | composite
    :param str riskAdjustment: How risk adjustment is applied for this measure
    :param str rateAggregation: How is rate aggregation performed for this measure
    :param str rationale: Detailed description of why the measure exists
    :param str clinicalRecommendationStatement: Summary of clinical guidelines
    :param CodeableConcept improvementNotation: increase | decrease
    :param Term term: Defined terms used in the measure documentation
    :param str guidance: Additional guidance for implementers (deprecated)
    :param Group group: Population criteria group
    :param SupplementalData supplementalData: What other data should be reported with the measure
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
        
        
        
        
        
        
        
        "subjectCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
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
        
        
        
        
        "scoring": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "scoringUnit": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "compositeScoring": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        "improvementNotation": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "term": {"class_name": "Term", "is_contained": True},
        
        
        
        "group": {"class_name": "Group", "is_contained": True},
        
        
        "supplementalData": {"class_name": "SupplementalData", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  subtitle:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  subjectCodeableConcept:  'CodeableConcept'  = None,  subjectReference:  'Reference'  = None,  basis:  'str'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  usage:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  topic:  list['CodeableConcept']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  library:  list['str']  = None,  disclaimer:  'str'  = None,  scoring:  'CodeableConcept'  = None,  scoringUnit:  'CodeableConcept'  = None,  compositeScoring:  'CodeableConcept'  = None,  type:  list['CodeableConcept']  = None,  riskAdjustment:  'str'  = None,  rateAggregation:  'str'  = None,  rationale:  'str'  = None,  clinicalRecommendationStatement:  'str'  = None,  improvementNotation:  'CodeableConcept'  = None,  term:  list['Term']  = None,  guidance:  'str'  = None,  group:  list['Group']  = None,  supplementalData:  list['SupplementalData']  = None, ):
        self.resourceType = resourceType or "Measure"
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
        self.subtitle = subtitle 
        self.status = status 
        self.experimental = experimental 
        self.subjectCodeableConcept = subjectCodeableConcept 
        self.subjectReference = subjectReference 
        self.basis = basis 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.usage = usage 
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
        self.library = library or []
        self.disclaimer = disclaimer 
        self.scoring = scoring 
        self.scoringUnit = scoringUnit 
        self.compositeScoring = compositeScoring 
        self.type = type or []
        self.riskAdjustment = riskAdjustment 
        self.rateAggregation = rateAggregation 
        self.rationale = rationale 
        self.clinicalRecommendationStatement = clinicalRecommendationStatement 
        self.improvementNotation = improvementNotation 
        self.term = term or []
        self.guidance = guidance 
        self.group = group or []
        self.supplementalData = supplementalData or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Measure":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Measure":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()