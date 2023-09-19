"""
Generated class for Parameters. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Money import *
from fhan.models.R5.Address import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Distance import *
from fhan.models.R5.Extension import *
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
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.DataRequirement import *
from fhan.models.R5.SampledData import *
from fhan.models.R5.ExtendedContactDetail import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.TriggerDefinition import *
from fhan.models.R5.RatioRange import *
from fhan.models.R5.ParameterDefinition import *
from fhan.models.R5.Age import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *


@dataclass
class Parameters:
    """ This resource is used to pass information into and back from an operation (whether invoked directly from REST or within a messaging environment).  It is not persisted or allowed to be referenced by other resources except as described in the definition of the Parameters resource.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param BackboneElement parameter: Operation Parameter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name from the definition
    :param str valuebase64Binary: If parameter is a data type
    :param bool valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param float valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param int valuebase64Binary: If parameter is a data type
    :param int valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param int valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param int valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param str valuebase64Binary: If parameter is a data type
    :param Address valuebase64Binary: If parameter is a data type
    :param Age valuebase64Binary: If parameter is a data type
    :param Annotation valuebase64Binary: If parameter is a data type
    :param Attachment valuebase64Binary: If parameter is a data type
    :param CodeableConcept valuebase64Binary: If parameter is a data type
    :param CodeableReference valuebase64Binary: If parameter is a data type
    :param Coding valuebase64Binary: If parameter is a data type
    :param ContactPoint valuebase64Binary: If parameter is a data type
    :param Count valuebase64Binary: If parameter is a data type
    :param Distance valuebase64Binary: If parameter is a data type
    :param Duration valuebase64Binary: If parameter is a data type
    :param HumanName valuebase64Binary: If parameter is a data type
    :param Identifier valuebase64Binary: If parameter is a data type
    :param Money valuebase64Binary: If parameter is a data type
    :param Period valuebase64Binary: If parameter is a data type
    :param Quantity valuebase64Binary: If parameter is a data type
    :param Range valuebase64Binary: If parameter is a data type
    :param Ratio valuebase64Binary: If parameter is a data type
    :param RatioRange valuebase64Binary: If parameter is a data type
    :param Reference valuebase64Binary: If parameter is a data type
    :param SampledData valuebase64Binary: If parameter is a data type
    :param Signature valuebase64Binary: If parameter is a data type
    :param Timing valuebase64Binary: If parameter is a data type
    :param ContactDetail valuebase64Binary: If parameter is a data type
    :param DataRequirement valuebase64Binary: If parameter is a data type
    :param Expression valuebase64Binary: If parameter is a data type
    :param ParameterDefinition valuebase64Binary: If parameter is a data type
    :param RelatedArtifact valuebase64Binary: If parameter is a data type
    :param TriggerDefinition valuebase64Binary: If parameter is a data type
    :param UsageContext valuebase64Binary: If parameter is a data type
    :param Availability valuebase64Binary: If parameter is a data type
    :param ExtendedContactDetail valuebase64Binary: If parameter is a data type
    :param Dosage valuebase64Binary: If parameter is a data type
    :param Meta valuebase64Binary: If parameter is a data type
    :param Resource resource: If parameter is a whole resource
    :param BackboneElement part: Operation Parameter
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
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
    
    resource: "Resource" = None
    
    part: "BackboneElement" = None
    