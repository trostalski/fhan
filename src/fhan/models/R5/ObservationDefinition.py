"""
Generated class for ObservationDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class QualifiedValue(BaseModel):
    """ A set of qualified values associated with a context and a set of conditions -  provides a range for quantitative and ordinal observations and a collection of value sets for qualitative observations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept context: Context qualifier for the set of qualified values
    :param CodeableConcept appliesTo: Targetted population for the set of qualified values
    :param str gender: male | female | other | unknown
    :param Range age: Applicable age range for the set of qualified values
    :param Range gestationalAge: Applicable gestational age range for the set of qualified values
    :param str condition: Condition associated with the set of qualified values
    :param str rangeCategory: reference | critical | absolute
    :param Range range: The range for continuous or ordinal observations
    :param str validCodedValueSet: Value set of valid coded values as part of this set of qualified values
    :param str normalCodedValueSet: Value set of normal coded values as part of this set of qualified values
    :param str abnormalCodedValueSet: Value set of abnormal coded values as part of this set of qualified values
    :param str criticalCodedValueSet: Value set of critical coded values as part of this set of qualified values
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "context": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "appliesTo": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "age": {"class_name": "Range", "is_contained": False},
        
        
        "gestationalAge": {"class_name": "Range", "is_contained": False},
        
        
        
        
        "range": {"class_name": "Range", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  context:  'CodeableConcept'  = None,  appliesTo:  list['CodeableConcept']  = None,  gender:  'str'  = None,  age:  'Range'  = None,  gestationalAge:  'Range'  = None,  condition:  'str'  = None,  rangeCategory:  'str'  = None,  range:  'Range'  = None,  validCodedValueSet:  'str'  = None,  normalCodedValueSet:  'str'  = None,  abnormalCodedValueSet:  'str'  = None,  criticalCodedValueSet:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.context = context 
        self.appliesTo = appliesTo or []
        self.gender = gender 
        self.age = age 
        self.gestationalAge = gestationalAge 
        self.condition = condition 
        self.rangeCategory = rangeCategory 
        self.range = range 
        self.validCodedValueSet = validCodedValueSet 
        self.normalCodedValueSet = normalCodedValueSet 
        self.abnormalCodedValueSet = abnormalCodedValueSet 
        self.criticalCodedValueSet = criticalCodedValueSet 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ObservationDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ObservationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Component(BaseModel):
    """ Some observations have multiple component observations, expressed as separate code value pairs.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of observation
    :param str permittedDataType: Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period
    :param Coding permittedUnit: Unit for quantitative results
    :param QualifiedValue qualifiedValue: Set of qualified values for observation results
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "permittedUnit": {"class_name": "Coding", "is_contained": False},
        
        
        "qualifiedValue": {"class_name": "QualifiedValue", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  permittedDataType:  list['str']  = None,  permittedUnit:  list['Coding']  = None,  qualifiedValue:  list['QualifiedValue']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.permittedDataType = permittedDataType or []
        self.permittedUnit = permittedUnit or []
        self.qualifiedValue = qualifiedValue or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ObservationDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ObservationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ObservationDefinition(DomainResource):
    """ Set of definitional characteristics for a kind of observation or measurement produced or consumed by an orderable health care service.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Logical canonical URL to reference this ObservationDefinition (globally unique)
    :param Identifier identifier: Business identifier of the ObservationDefinition
    :param str version: Business version of the ObservationDefinition
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this ObservationDefinition (computer friendly)
    :param str title: Name for this ObservationDefinition (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: If for testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: The name of the individual or organization that published the ObservationDefinition
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the ObservationDefinition
    :param UsageContext useContext: Content intends to support these contexts
    :param CodeableConcept jurisdiction: Intended jurisdiction for this ObservationDefinition (if applicable)
    :param str purpose: Why this ObservationDefinition is defined
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When ObservationDefinition was approved by publisher
    :param str lastReviewDate: Date on which the asset content was last reviewed by the publisher
    :param Period effectivePeriod: The effective date range for the ObservationDefinition
    :param str derivedFromCanonical: Based on FHIR definition of another observation
    :param str derivedFromUri: Based on external definition
    :param CodeableConcept subject: Type of subject for the defined observation
    :param CodeableConcept performerType: Desired kind of performer for such kind of observation
    :param CodeableConcept category: General type of observation
    :param CodeableConcept code: Type of observation
    :param str permittedDataType: Quantity | CodeableConcept | string | boolean | integer | Range | Ratio | SampledData | time | dateTime | Period
    :param bool multipleResultsAllowed: Multiple results allowed for conforming observations
    :param CodeableConcept bodySite: Body part to be observed
    :param CodeableConcept method: Method used to produce the observation
    :param Reference specimen: Kind of specimen used by this type of observation
    :param Reference device: Measurement device or model of device
    :param str preferredReportName: The preferred name to be used when reporting the observation results
    :param Coding permittedUnit: Unit for quantitative results
    :param QualifiedValue qualifiedValue: Set of qualified values for observation results
    :param Reference hasMember: Definitions of related resources belonging to this kind of observation group
    :param Component component: Component results
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
        
        
        
        
        "subject": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "performerType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "specimen": {"class_name": "Reference", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        
        "permittedUnit": {"class_name": "Coding", "is_contained": False},
        
        
        "qualifiedValue": {"class_name": "QualifiedValue", "is_contained": True},
        
        
        "hasMember": {"class_name": "Reference", "is_contained": False},
        
        
        "component": {"class_name": "Component", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  'Identifier'  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  derivedFromCanonical:  list['str']  = None,  derivedFromUri:  list['str']  = None,  subject:  list['CodeableConcept']  = None,  performerType:  'CodeableConcept'  = None,  category:  list['CodeableConcept']  = None,  code:  'CodeableConcept'  = None,  permittedDataType:  list['str']  = None,  multipleResultsAllowed:  'bool'  = None,  bodySite:  'CodeableConcept'  = None,  method:  'CodeableConcept'  = None,  specimen:  list['Reference']  = None,  device:  list['Reference']  = None,  preferredReportName:  'str'  = None,  permittedUnit:  list['Coding']  = None,  qualifiedValue:  list['QualifiedValue']  = None,  hasMember:  list['Reference']  = None,  component:  list['Component']  = None, ):
        self.resourceType = resourceType or "ObservationDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier 
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
        self.derivedFromCanonical = derivedFromCanonical or []
        self.derivedFromUri = derivedFromUri or []
        self.subject = subject or []
        self.performerType = performerType 
        self.category = category or []
        self.code = code 
        self.permittedDataType = permittedDataType or []
        self.multipleResultsAllowed = multipleResultsAllowed 
        self.bodySite = bodySite 
        self.method = method 
        self.specimen = specimen or []
        self.device = device or []
        self.preferredReportName = preferredReportName 
        self.permittedUnit = permittedUnit or []
        self.qualifiedValue = qualifiedValue or []
        self.hasMember = hasMember or []
        self.component = component or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ObservationDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ObservationDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()