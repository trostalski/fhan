"""
Generated class for Parameters. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Coding import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.Period import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Range import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Element import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Age import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Duration import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Count import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Money import *
from fhan.models.R4.Signature import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Address import *
from fhan.models.R4.Distance import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Extension import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Reference import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Parameter(Element):
    """ A parameter passed to or received from the operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name from the definition
    :param str valueBase64Binary: If parameter is a data type
    :param Resource resource: If parameter is a whole resource
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    
    valueBase64Binary: str = None
    resource: "Resource" = None
    
@dataclass
class Parameters(ModelBase):
    """ This resource is a non-persisted resource used to pass information into and back from an [operation](operations.html). It has no other use, and there is no RESTful endpoint associated with it.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Parameter parameter: Operation Parameter
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    parameter: list["Parameter"] = None
    