"""
Generated class for Address. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.R4.Element import *

@dataclass
class Address(Element):
    """ Base StructureDefinition for Address Type: An address expressed using postal conventions (as opposed to GPS or other location definition formats).  This data type may be used to convey addresses for use in delivering mail as well as for visiting locations which might not be valid for mail delivery.  There are a variety of postal address formats defined around the world.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str use: home | work | temp | old | billing - purpose of this address
    :param str type: postal | physical | both
    :param str text: Text representation of the address
    :param str line: Street name, number, direction & P.O. Box etc.
    :param str city: Name of city, town etc.
    :param str district: District name (aka county)
    :param str state: Sub-unit of country (abbreviations ok)
    :param str postalCode: Postal code for area
    :param str country: Country (e.g. can be ISO 3166 2 or 3 letter code)
    :param Period period: Time period when address was/is in use
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    use: str = None
    
    type: str = None
    
    text: str = None
    
    line: str = None
    
    city: str = None
    
    district: str = None
    
    state: str = None
    
    postalCode: str = None
    
    country: str = None
    
    period: "Period" = None
    