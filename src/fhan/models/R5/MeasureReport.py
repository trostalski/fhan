"""
Generated class for MeasureReport. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Population(BaseModel):
    """ The populations that make up the population group, one for each type of population appropriate for the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific population from Measure
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    :param Reference subjectReport: For subject-list reports, a subject result in this population
    :param Reference subjects: What individual(s) in the population
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "subjectResults": {"class_name": "Reference", "is_contained": False},
        
        
        "subjectReport": {"class_name": "Reference", "is_contained": False},
        
        
        "subjects": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  count:  'int'  = None,  subjectResults:  'Reference'  = None,  subjectReport:  list['Reference']  = None,  subjects:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.count = count 
        self.subjectResults = subjectResults 
        self.subjectReport = subjectReport or []
        self.subjects = subjects 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MeasureReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MeasureReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class Component(BaseModel):
    """ A stratifier component value.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific stratifier component from Measure
    :param CodeableConcept code: What stratifier component of the group
    :param CodeableConcept valueCodeableConcept: The stratum component value, e.g. male
    :param bool valueBoolean: The stratum component value, e.g. male
    :param Quantity valueQuantity: The stratum component value, e.g. male
    :param Range valueRange: The stratum component value, e.g. male
    :param Reference valueReference: The stratum component value, e.g. male
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueBoolean:  'bool'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueBoolean = valueBoolean 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueReference = valueReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MeasureReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MeasureReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Population(BaseModel):
    """ The populations that make up the stratum, one for each type of population appropriate to the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific population from Measure
    :param CodeableConcept code: initial-population | numerator | numerator-exclusion | denominator | denominator-exclusion | denominator-exception | measure-population | measure-population-exclusion | measure-observation
    :param int count: Size of the population
    :param Reference subjectResults: For subject-list reports, the subject results in this population
    :param Reference subjectReport: For subject-list reports, a subject result in this population
    :param Reference subjects: What individual(s) in the population
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "subjectResults": {"class_name": "Reference", "is_contained": False},
        
        
        "subjectReport": {"class_name": "Reference", "is_contained": False},
        
        
        "subjects": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  count:  'int'  = None,  subjectResults:  'Reference'  = None,  subjectReport:  list['Reference']  = None,  subjects:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.count = count 
        self.subjectResults = subjectResults 
        self.subjectReport = subjectReport or []
        self.subjects = subjects 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MeasureReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MeasureReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Stratum(BaseModel):
    """ This element contains the results for a single stratum within the stratifier. For example, when stratifying on administrative gender, there will be four strata, one for each possible gender value.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept valueCodeableConcept: The stratum value, e.g. male
    :param bool valueBoolean: The stratum value, e.g. male
    :param Quantity valueQuantity: The stratum value, e.g. male
    :param Range valueRange: The stratum value, e.g. male
    :param Reference valueReference: The stratum value, e.g. male
    :param Component component: Stratifier component values
    :param Population population: Population results in this stratum
    :param Quantity measureScoreQuantity: What score this stratum achieved
    :param str measureScoreDateTime: What score this stratum achieved
    :param CodeableConcept measureScoreCodeableConcept: What score this stratum achieved
    :param Period measureScorePeriod: What score this stratum achieved
    :param Range measureScoreRange: What score this stratum achieved
    :param Duration measureScoreDuration: What score this stratum achieved
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "valueRange": {"class_name": "Range", "is_contained": False},
        
        
        "valueReference": {"class_name": "Reference", "is_contained": False},
        
        
        "component": {"class_name": "Component", "is_contained": True},
        
        
        "population": {"class_name": "Population", "is_contained": True},
        
        
        "measureScoreQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "measureScoreCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "measureScorePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "measureScoreRange": {"class_name": "Range", "is_contained": False},
        
        
        "measureScoreDuration": {"class_name": "Duration", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueBoolean:  'bool'  = None,  valueQuantity:  'Quantity'  = None,  valueRange:  'Range'  = None,  valueReference:  'Reference'  = None,  component:  list['Component']  = None,  population:  list['Population']  = None,  measureScoreQuantity:  'Quantity'  = None,  measureScoreDateTime:  'str'  = None,  measureScoreCodeableConcept:  'CodeableConcept'  = None,  measureScorePeriod:  'Period'  = None,  measureScoreRange:  'Range'  = None,  measureScoreDuration:  'Duration'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueBoolean = valueBoolean 
        self.valueQuantity = valueQuantity 
        self.valueRange = valueRange 
        self.valueReference = valueReference 
        self.component = component or []
        self.population = population or []
        self.measureScoreQuantity = measureScoreQuantity 
        self.measureScoreDateTime = measureScoreDateTime 
        self.measureScoreCodeableConcept = measureScoreCodeableConcept 
        self.measureScorePeriod = measureScorePeriod 
        self.measureScoreRange = measureScoreRange 
        self.measureScoreDuration = measureScoreDuration 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MeasureReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MeasureReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Stratifier(BaseModel):
    """ When a measure includes multiple stratifiers, there will be a stratifier group for each stratifier defined by the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific stratifier from Measure
    :param CodeableConcept code: What stratifier of the group
    :param Stratum stratum: Stratum results, one for each unique value, or set of values, in the stratifier, or stratifier components
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "stratum": {"class_name": "Stratum", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  stratum:  list['Stratum']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.stratum = stratum or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MeasureReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MeasureReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Group(BaseModel):
    """ The results of the calculation, one for each population group in the measure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Pointer to specific group from Measure
    :param CodeableConcept code: Meaning of the group
    :param Reference subject: What individual(s) the report is for
    :param Population population: The populations in the group
    :param Quantity measureScoreQuantity: What score this group achieved
    :param str measureScoreDateTime: What score this group achieved
    :param CodeableConcept measureScoreCodeableConcept: What score this group achieved
    :param Period measureScorePeriod: What score this group achieved
    :param Range measureScoreRange: What score this group achieved
    :param Duration measureScoreDuration: What score this group achieved
    :param Stratifier stratifier: Stratification results
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "population": {"class_name": "Population", "is_contained": True},
        
        
        "measureScoreQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "measureScoreCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "measureScorePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "measureScoreRange": {"class_name": "Range", "is_contained": False},
        
        
        "measureScoreDuration": {"class_name": "Duration", "is_contained": False},
        
        
        "stratifier": {"class_name": "Stratifier", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  code:  'CodeableConcept'  = None,  subject:  'Reference'  = None,  population:  list['Population']  = None,  measureScoreQuantity:  'Quantity'  = None,  measureScoreDateTime:  'str'  = None,  measureScoreCodeableConcept:  'CodeableConcept'  = None,  measureScorePeriod:  'Period'  = None,  measureScoreRange:  'Range'  = None,  measureScoreDuration:  'Duration'  = None,  stratifier:  list['Stratifier']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.code = code 
        self.subject = subject 
        self.population = population or []
        self.measureScoreQuantity = measureScoreQuantity 
        self.measureScoreDateTime = measureScoreDateTime 
        self.measureScoreCodeableConcept = measureScoreCodeableConcept 
        self.measureScorePeriod = measureScorePeriod 
        self.measureScoreRange = measureScoreRange 
        self.measureScoreDuration = measureScoreDuration 
        self.stratifier = stratifier or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MeasureReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MeasureReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MeasureReport(DomainResource):
    """ The MeasureReport resource contains the results of the calculation of a measure; and optionally a reference to the resources involved in that calculation.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Additional identifier for the MeasureReport
    :param str status: complete | pending | error
    :param str type: individual | subject-list | summary | data-exchange
    :param str dataUpdateType: incremental | snapshot
    :param str measure: What measure was calculated
    :param Reference subject: What individual(s) the report is for
    :param str date: When the measure was calculated
    :param Reference reporter: Who is reporting the data
    :param Reference reportingVendor: What vendor prepared the data
    :param Reference location: Where the reported data is from
    :param Period period: What period the report covers
    :param Reference inputParameters: What parameters were provided to the report
    :param CodeableConcept scoring: What scoring method (e.g. proportion, ratio, continuous-variable)
    :param CodeableConcept improvementNotation: increase | decrease
    :param Group group: Measure results for each group
    :param Reference supplementalData: Additional information collected for the report
    :param Reference evaluatedResource: What data was used to calculate the measure score
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        
        "reporter": {"class_name": "Reference", "is_contained": False},
        
        
        "reportingVendor": {"class_name": "Reference", "is_contained": False},
        
        
        "location": {"class_name": "Reference", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "inputParameters": {"class_name": "Reference", "is_contained": False},
        
        
        "scoring": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "improvementNotation": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "group": {"class_name": "Group", "is_contained": True},
        
        
        "supplementalData": {"class_name": "Reference", "is_contained": False},
        
        
        "evaluatedResource": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  type:  'str'  = None,  dataUpdateType:  'str'  = None,  measure:  'str'  = None,  subject:  'Reference'  = None,  date:  'str'  = None,  reporter:  'Reference'  = None,  reportingVendor:  'Reference'  = None,  location:  'Reference'  = None,  period:  'Period'  = None,  inputParameters:  'Reference'  = None,  scoring:  'CodeableConcept'  = None,  improvementNotation:  'CodeableConcept'  = None,  group:  list['Group']  = None,  supplementalData:  list['Reference']  = None,  evaluatedResource:  list['Reference']  = None, ):
        self.resourceType = resourceType or "MeasureReport"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.type = type 
        self.dataUpdateType = dataUpdateType 
        self.measure = measure 
        self.subject = subject 
        self.date = date 
        self.reporter = reporter 
        self.reportingVendor = reportingVendor 
        self.location = location 
        self.period = period 
        self.inputParameters = inputParameters 
        self.scoring = scoring 
        self.improvementNotation = improvementNotation 
        self.group = group or []
        self.supplementalData = supplementalData or []
        self.evaluatedResource = evaluatedResource or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MeasureReport":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MeasureReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()