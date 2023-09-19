"""
Generated class for Parameters. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Signature import *
from fhan.models.R4B.Contributor import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Dosage import *
from fhan.models.R4B.SampledData import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Extension import *
from fhan.models.R4B.HumanName import *
from fhan.models.R4B.Duration import *
from fhan.models.R4B.ContactPoint import *
from fhan.models.R4B.RelatedArtifact import *
from fhan.models.R4B.TriggerDefinition import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Count import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.DataRequirement import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Money import *
from fhan.models.R4B.ParameterDefinition import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.Distance import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Address import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Ratio import *
from fhan.models.R4B.Expression import *
from fhan.models.R4B.Reference import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Timing import *
from fhan.models.R4B.Age import *
from fhan.models.R4B.Resource import *


@dataclass
class Parameters:
    """
    This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
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
    