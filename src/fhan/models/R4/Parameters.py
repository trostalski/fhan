"""
Generated class for Parameters. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Address import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Range import *
from fhan.models.R4.Money import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Distance import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Count import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Age import *
from fhan.models.R4.Coding import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Meta import *
from fhan.models.R4.HumanName import *
from fhan.models.generator_models import ModelBase


@dataclass
class Parameters(ModelBase):
    """ This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
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
    :param Reference valuebase64Binary: If parameter is a data type
    :param SampledData valuebase64Binary: If parameter is a data type
    :param Signature valuebase64Binary: If parameter is a data type
    :param Timing valuebase64Binary: If parameter is a data type
    :param ContactDetail valuebase64Binary: If parameter is a data type
    :param Contributor valuebase64Binary: If parameter is a data type
    :param DataRequirement valuebase64Binary: If parameter is a data type
    :param Expression valuebase64Binary: If parameter is a data type
    :param ParameterDefinition valuebase64Binary: If parameter is a data type
    :param RelatedArtifact valuebase64Binary: If parameter is a data type
    :param TriggerDefinition valuebase64Binary: If parameter is a data type
    :param UsageContext valuebase64Binary: If parameter is a data type
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
    
    valuebase64Binary: "Reference" = None
    
    valuebase64Binary: "SampledData" = None
    
    valuebase64Binary: "Signature" = None
    
    valuebase64Binary: "Timing" = None
    
    valuebase64Binary: "ContactDetail" = None
    
    valuebase64Binary: "Contributor" = None
    
    valuebase64Binary: "DataRequirement" = None
    
    valuebase64Binary: "Expression" = None
    
    valuebase64Binary: "ParameterDefinition" = None
    
    valuebase64Binary: "RelatedArtifact" = None
    
    valuebase64Binary: "TriggerDefinition" = None
    
    valuebase64Binary: "UsageContext" = None
    
    valuebase64Binary: "Dosage" = None
    
    valuebase64Binary: "Meta" = None
    
    resource: "Resource" = None
    
    part: "BackboneElement" = None
    