"""
Generated class for Extension. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Element import *


@dataclass
class Extension(Element):
    """ Other resources *from the patient record* that may be relevant to the event.  The information from these resources was either used to create the instance or is provided to help with its interpretation.  This extension **should not** be used if more specific  inline elements  or extensions are available.  For example, use `Observation.hasMember`  instead of supportingInformation for  representing the members of an Observation panel.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Extension
    :param str url: identifies the meaning of the extension
    :param Reference valueReference: Value of extension
    """

    resourceType: str = "Extension"
    id: str = None
    
    extension: "Extension" = None
    
    url: str = None
    
    valueReference: "Reference" = None
    