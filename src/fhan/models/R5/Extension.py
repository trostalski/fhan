"""
Generated class for Extension. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.Address import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Distance import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.Range import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Signature import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.Availability import *
from fhan.models.R5.Count import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Period import *
from fhan.models.R5.Timing import *
from fhan.models.R5.HumanName import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Expression import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.SampledData import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.TriggerDefinition import *
from fhan.models.R5.RatioRange import *
from fhan.models.R5.ParameterDefinition import *
from fhan.models.R5.Age import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *


@dataclass
class Extension:
    """ Extension Type: Optional Extension Element - found in all resources.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str url: identifies the meaning of the extension
    :param str valuebase64Binary: Value of extension
    :param bool valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param float valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param int valuebase64Binary: Value of extension
    :param int valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param int valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param int valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param str valuebase64Binary: Value of extension
    :param Address valuebase64Binary: Value of extension
    :param Age valuebase64Binary: Value of extension
    :param Annotation valuebase64Binary: Value of extension
    :param Attachment valuebase64Binary: Value of extension
    :param CodeableConcept valuebase64Binary: Value of extension
    :param CodeableReference valuebase64Binary: Value of extension
    :param Coding valuebase64Binary: Value of extension
    :param ContactPoint valuebase64Binary: Value of extension
    :param Count valuebase64Binary: Value of extension
    :param Distance valuebase64Binary: Value of extension
    :param Duration valuebase64Binary: Value of extension
    :param HumanName valuebase64Binary: Value of extension
    :param Identifier valuebase64Binary: Value of extension
    :param Money valuebase64Binary: Value of extension
    :param Period valuebase64Binary: Value of extension
    :param Quantity valuebase64Binary: Value of extension
    :param Range valuebase64Binary: Value of extension
    :param Ratio valuebase64Binary: Value of extension
    :param RatioRange valuebase64Binary: Value of extension
    :param Reference valuebase64Binary: Value of extension
    :param SampledData valuebase64Binary: Value of extension
    :param Signature valuebase64Binary: Value of extension
    :param Timing valuebase64Binary: Value of extension
    :param ContactDetail valuebase64Binary: Value of extension
    :param DataRequirement valuebase64Binary: Value of extension
    :param Expression valuebase64Binary: Value of extension
    :param ParameterDefinition valuebase64Binary: Value of extension
    :param RelatedArtifact valuebase64Binary: Value of extension
    :param TriggerDefinition valuebase64Binary: Value of extension
    :param UsageContext valuebase64Binary: Value of extension
    :param Availability valuebase64Binary: Value of extension
    :param ExtendedContactDetail valuebase64Binary: Value of extension
    :param Dosage valuebase64Binary: Value of extension
    :param Meta valuebase64Binary: Value of extension
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    url: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: bool = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: float = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: "Address" = None
    
    valuebase64Binary: "Age" = None
    
    valuebase64Binary: "Annotation" = None
    
    valuebase64Binary: "Attachment" = None
    
    valuebase64Binary: "CodeableConcept" = None
    
    valuebase64Binary: "CodeableReference" = None
    
    valuebase64Binary: "Coding" = None
    
    valuebase64Binary: "ContactPoint" = None
    
    valuebase64Binary: "Count" = None
    
    valuebase64Binary: "Distance" = None
    
    valuebase64Binary: "Duration" = None
    
    valuebase64Binary: "HumanName" = None
    
    valuebase64Binary: "Identifier" = None
    
    valuebase64Binary: "Money" = None
    
    valuebase64Binary: "Period" = None
    
    valuebase64Binary: "Quantity" = None
    
    valuebase64Binary: "Range" = None
    
    valuebase64Binary: "Ratio" = None
    
    valuebase64Binary: "RatioRange" = None
    
    valuebase64Binary: "Reference" = None
    
    valuebase64Binary: "SampledData" = None
    
    valuebase64Binary: "Signature" = None
    
    valuebase64Binary: "Timing" = None
    
    valuebase64Binary: "ContactDetail" = None
    
    valuebase64Binary: "DataRequirement" = None
    
    valuebase64Binary: "Expression" = None
    
    valuebase64Binary: "ParameterDefinition" = None
    
    valuebase64Binary: "RelatedArtifact" = None
    
    valuebase64Binary: "TriggerDefinition" = None
    
    valuebase64Binary: "UsageContext" = None
    
    valuebase64Binary: "Availability" = None
    
    valuebase64Binary: "ExtendedContactDetail" = None
    
    valuebase64Binary: "Dosage" = None
    
    valuebase64Binary: "Meta" = None
    