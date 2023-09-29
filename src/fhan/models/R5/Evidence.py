"""
Generated class for Evidence. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class VariableDefinition(BaseModel):
    """ Evidence variable such as population, exposure, or outcome.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: A text description or summary of the variable
    :param Annotation note: Footnotes and/or explanatory notes
    :param CodeableConcept variableRole: population | subpopulation | exposure | referenceExposure | measuredVariable | confounder
    :param Reference observed: Definition of the actual variable related to the statistic(s)
    :param Reference intended: Definition of the intended variable related to the Evidence
    :param CodeableConcept directnessMatch: low | moderate | high | exact
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "variableRole": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "observed": {"class_name": "Reference", "is_contained": False},
        
        
        "intended": {"class_name": "Reference", "is_contained": False},
        
        
        "directnessMatch": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  variableRole:  'CodeableConcept'  = None,  observed:  'Reference'  = None,  intended:  'Reference'  = None,  directnessMatch:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.note = note or []
        self.variableRole = variableRole 
        self.observed = observed 
        self.intended = intended 
        self.directnessMatch = directnessMatch 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class SampleSize(BaseModel):
    """ Number of samples in the statistic.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of sample size for statistic
    :param Annotation note: Footnote or explanatory note about the sample size
    :param int numberOfStudies: Number of contributing studies
    :param int numberOfParticipants: Cumulative number of participants
    :param int knownDataCount: Number of participants with known results for measured variables
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  numberOfStudies:  'int'  = None,  numberOfParticipants:  'int'  = None,  knownDataCount:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.note = note or []
        self.numberOfStudies = numberOfStudies 
        self.numberOfParticipants = numberOfParticipants 
        self.knownDataCount = knownDataCount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class AttributeEstimate(BaseModel):
    """ A statistical attribute of the statistic such as a measure of heterogeneity.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of the attribute estimate
    :param Annotation note: Footnote or explanatory note about the estimate
    :param CodeableConcept type: The type of attribute estimate, e.g., confidence interval or p value
    :param Quantity quantity: The singular quantity of the attribute estimate, for attribute estimates represented as single values; also used to report unit of measure
    :param float level: Level of confidence interval, e.g., 0.95 for 95% confidence interval
    :param Range range: Lower and upper bound values of the attribute estimate
    :param AttributeEstimate attributeEstimate: A nested attribute estimate; which is the attribute estimate of an attribute estimate
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "range": {"class_name": "Range", "is_contained": False},
        
        
        "attributeEstimate": {"class_name": "AttributeEstimate", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  type:  'CodeableConcept'  = None,  quantity:  'Quantity'  = None,  level:  'float'  = None,  range:  'Range'  = None,  attributeEstimate:  list['AttributeEstimate']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.note = note or []
        self.type = type 
        self.quantity = quantity 
        self.level = level 
        self.range = range 
        self.attributeEstimate = attributeEstimate or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Variable(BaseModel):
    """ A variable adjusted for in the adjusted analysis.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference variableDefinition: Description of the variable
    :param str handling: continuous | dichotomous | ordinal | polychotomous
    :param CodeableConcept valueCategory: Description for grouping of ordinal or polychotomous variables
    :param Quantity valueQuantity: Discrete value for grouping of ordinal or polychotomous variables
    :param Range valueRange: Range of values for grouping of ordinal or polychotomous variables
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "variableDefinition": {"class_name": "Reference", "is_contained": False},
        
        
        
        "valueCategory": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  variableDefinition:  'Reference'  = None,  handling:  'str'  = None,  valueCategory:  list['CodeableConcept']  = None,  valueQuantity:  list['Quantity']  = None,  valueRange:  list['Range']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.variableDefinition = variableDefinition 
        self.handling = handling 
        self.valueCategory = valueCategory or []
        self.valueQuantity = valueQuantity or []
        self.valueRange = valueRange or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class ModelCharacteristic(BaseModel):
    """ A component of the method to generate the statistic.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Model specification
    :param Quantity value: Numerical value to complete model specification
    :param Variable variable: A variable adjusted for in the adjusted analysis
    :param AttributeEstimate attributeEstimate: An attribute of the statistic used as a model characteristic
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "value": {"class_name": "Quantity", "is_contained": False},
        
        
        "variable": {"class_name": "Variable", "is_contained": True},
        
        
        "attributeEstimate": {"class_name": "AttributeEstimate", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  value:  'Quantity'  = None,  variable:  list['Variable']  = None,  attributeEstimate:  list['AttributeEstimate']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.value = value 
        self.variable = variable or []
        self.attributeEstimate = attributeEstimate or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Statistic(BaseModel):
    """ Values and parameters for a single statistic.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Description of content
    :param Annotation note: Footnotes and/or explanatory notes
    :param CodeableConcept statisticType: Type of statistic, e.g., relative risk
    :param CodeableConcept category: Associated category for categorical variable
    :param Quantity quantity: Statistic value
    :param int numberOfEvents: The number of events associated with the statistic
    :param int numberAffected: The number of participants affected
    :param SampleSize sampleSize: Number of samples in the statistic
    :param AttributeEstimate attributeEstimate: An attribute of the Statistic
    :param ModelCharacteristic modelCharacteristic: An aspect of the statistical model
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "statisticType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        "sampleSize": {"class_name": "SampleSize", "is_contained": True},
        
        
        "attributeEstimate": {"class_name": "AttributeEstimate", "is_contained": True},
        
        
        "modelCharacteristic": {"class_name": "ModelCharacteristic", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  statisticType:  'CodeableConcept'  = None,  category:  'CodeableConcept'  = None,  quantity:  'Quantity'  = None,  numberOfEvents:  'int'  = None,  numberAffected:  'int'  = None,  sampleSize:  'SampleSize'  = None,  attributeEstimate:  list['AttributeEstimate']  = None,  modelCharacteristic:  list['ModelCharacteristic']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.note = note or []
        self.statisticType = statisticType 
        self.category = category 
        self.quantity = quantity 
        self.numberOfEvents = numberOfEvents 
        self.numberAffected = numberAffected 
        self.sampleSize = sampleSize 
        self.attributeEstimate = attributeEstimate or []
        self.modelCharacteristic = modelCharacteristic or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Certainty(BaseModel):
    """ Assessment of certainty, confidence in the estimates, or quality of the evidence.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of certainty
    :param Annotation note: Footnotes and/or explanatory notes
    :param CodeableConcept type: Aspect of certainty being rated
    :param CodeableConcept rating: Assessment or judgement of the aspect
    :param str rater: Individual or group who did the rating
    :param Subcomponent subcomponent: A domain or subdomain of certainty
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "rating": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "subcomponent": {"class_name": "Subcomponent", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  note:  list['Annotation']  = None,  type:  'CodeableConcept'  = None,  rating:  'CodeableConcept'  = None,  rater:  'str'  = None,  subcomponent:  list['Subcomponent']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.note = note or []
        self.type = type 
        self.rating = rating 
        self.rater = rater 
        self.subcomponent = subcomponent or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Evidence(DomainResource):
    """ The Evidence Resource provides a machine-interpretable expression of an evidence concept including the evidence variables (e.g., population, exposures/interventions, comparators, outcomes, measured variables, confounding variables), the statistics, and the certainty of this evidence.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this evidence, represented as a globally unique URI
    :param Identifier identifier: Additional identifier for the summary
    :param str version: Business version of this summary
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this summary (machine friendly)
    :param str title: Name for this summary (human friendly)
    :param Reference citeAsReference: Citation for this evidence
    :param str citeAsMarkdown: Citation for this evidence
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str approvalDate: When the summary was approved by publisher
    :param str lastReviewDate: When the summary was last reviewed by the publisher
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param UsageContext useContext: The context that the content is intended to support
    :param str purpose: Why this Evidence is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param RelatedArtifact relatedArtifact: Link or citation to artifact associated with the summary
    :param str description: Description of the particular summary
    :param str assertion: Declarative description of the Evidence
    :param Annotation note: Footnotes and/or explanatory notes
    :param VariableDefinition variableDefinition: Evidence variable such as population, exposure, or outcome
    :param CodeableConcept synthesisType: The method to combine studies
    :param CodeableConcept studyDesign: The design of the study that produced this evidence
    :param Statistic statistic: Values and parameters for a single statistic
    :param Certainty certainty: Certainty or quality of the evidence
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
        
        
        
        
        "citeAsReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "variableDefinition": {"class_name": "VariableDefinition", "is_contained": True},
        
        
        "synthesisType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "studyDesign": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "statistic": {"class_name": "Statistic", "is_contained": True},
        
        
        "certainty": {"class_name": "Certainty", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  citeAsReference:  'Reference'  = None,  citeAsMarkdown:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  useContext:  list['UsageContext']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  description:  'str'  = None,  assertion:  'str'  = None,  note:  list['Annotation']  = None,  variableDefinition:  list['VariableDefinition']  = None,  synthesisType:  'CodeableConcept'  = None,  studyDesign:  list['CodeableConcept']  = None,  statistic:  list['Statistic']  = None,  certainty:  list['Certainty']  = None, ):
        self.resourceType = resourceType or "Evidence"
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
        self.citeAsReference = citeAsReference 
        self.citeAsMarkdown = citeAsMarkdown 
        self.status = status 
        self.experimental = experimental 
        self.date = date 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.publisher = publisher 
        self.contact = contact or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.useContext = useContext or []
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.relatedArtifact = relatedArtifact or []
        self.description = description 
        self.assertion = assertion 
        self.note = note or []
        self.variableDefinition = variableDefinition or []
        self.synthesisType = synthesisType 
        self.studyDesign = studyDesign or []
        self.statistic = statistic or []
        self.certainty = certainty or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Evidence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Evidence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()