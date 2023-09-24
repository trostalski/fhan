"""
Generated class for DataRequirement. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Element import *
from fhan.models.R4.Duration import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Element import *


@dataclass
class DataRequirement(Element):
    """ Base StructureDefinition for DataRequirement Type: Describes a required data item for evaluation in terms of the type of data, and optional code or date-based filters of the data.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: The type of the required data
    :param str profile: The profile of the required data
    :param CodeableConcept subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
    :param str mustSupport: Indicates specific structure elements that are referenced by the knowledge module
    :param Element codeFilter: What codes are expected
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: A code-valued attribute to filter on
    :param str searchParam: A coded (token) parameter to search on
    :param str valueSet: Valueset for the filter
    :param Coding code: What code is expected
    :param Element dateFilter: What dates/date ranges are expected
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: A date-valued attribute to filter on
    :param str searchParam: A date valued parameter to search on
    :param str valueDateTime: The value of the filter, as a Period, DateTime, or Duration value
    :param int limit: Number of results
    :param Element sort: Order of the results
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: The name of the attribute to perform the sort
    :param str direction: ascending | descending
    """

    resourceType: str = "DataRequirement"
    id: str = None
    
    extension: list["Extension"] = None
    
    type: str = None
    
    profile: str = None
    
    subjectCodeableConcept: "CodeableConcept" = None
    
    mustSupport: str = None
    
    codeFilter: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    path: str = None
    
    searchParam: str = None
    
    valueSet: str = None
    
    code: list["Coding"] = None
    
    dateFilter: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    path: str = None
    
    searchParam: str = None
    
    valueDateTime: str = None
    
    limit: int = None
    
    sort: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    path: str = None
    
    direction: str = None
    