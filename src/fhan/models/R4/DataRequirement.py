"""
Generated class for DataRequirement. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Element import *
from fhan.models.R4.Coding import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

class DataRequirement(ModelBase):
    """ Base StructureDefinition for DataRequirement Type: Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str type: The type of the required data
    :param str profile: The profile of the required data
    :param 'CodeableConcept' subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str mustSupport: Indicates specific structure elements that are referenced by the knowledge module
    :param list['Element'] codeFilter: What codes are expected
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: A code-valued attribute to filter on
    :param str searchParam: A coded (token) parameter to search on
    :param str valueSet: Valueset for the filter
    :param list['Coding'] code: What code is expected
    :param list['Element'] dateFilter: What dates/date ranges are expected
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: A date-valued attribute to filter on
    :param str searchParam: A date valued parameter to search on
    :param str valueDateTime: The value of the filter, as a Period, DateTime, or Duration value
    :param int limit: Number of results
    :param list['Element'] sort: Order of the results
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: The name of the attribute to perform the sort
    :param str direction: ascending | descending
    """
    def __init__(self, resourceType: str = "DataRequirement",  id: str = None,  extension: list['Extension'] = None,  type: str = None,  profile: str = None,  subjectCodeableConcept: 'CodeableConcept' = None,  mustSupport: str = None,  codeFilter: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  searchParam: str = None,  valueSet: str = None,  code: list['Coding'] = None,  dateFilter: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  searchParam: str = None,  valueDateTime: str = None,  limit: int = None,  sort: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  direction: str = None, ):
        self.resourceType: str = resourceType or "DataRequirement"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.profile: str = profile or []
        self.subjectCodeableConcept: 'CodeableConcept' = subjectCodeableConcept 
        self.mustSupport: str = mustSupport or []
        self.codeFilter: list['Element'] = codeFilter or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.searchParam: str = searchParam 
        self.valueSet: str = valueSet 
        self.code: list['Coding'] = code or []
        self.dateFilter: list['Element'] = dateFilter or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.searchParam: str = searchParam 
        self.valueDateTime: str = valueDateTime 
        self.limit: int = limit 
        self.sort: list['Element'] = sort or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.direction: str = direction 
        