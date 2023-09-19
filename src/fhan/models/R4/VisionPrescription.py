"""
Generated class for VisionPrescription. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class VisionPrescription(ModelBase):
    """ An authorization for the provision of glasses and/or contact lenses to a patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for vision prescription
    :param str status: active | cancelled | draft | entered-in-error
    :param str created: Response creation date
    :param Reference patient: Who prescription is for
    :param Reference encounter: Created during encounter / admission / stay
    :param str dateWritten: When prescription was authorized
    :param Reference prescriber: Who authorized the vision prescription
    :param BackboneElement lensSpecification: Vision lens authorization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept product: Product to be supplied
    :param str eye: right | left
    :param float sphere: Power of the lens
    :param float cylinder: Lens power for astigmatism
    :param int axis: Lens meridian which contain no power for astigmatism
    :param BackboneElement prism: Eye alignment compensation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float amount: Amount of adjustment
    :param str base: up | down | in | out
    :param float add: Added power for multifocal levels
    :param float power: Contact lens power
    :param float backCurve: Contact lens back curvature
    :param float diameter: Contact lens diameter
    :param Quantity duration: Lens wear duration
    :param str color: Color required
    :param str brand: Brand required
    :param Annotation note: Notes for coatings
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    created: str = None
    
    patient: "Reference" = None
    
    encounter: "Reference" = None
    
    dateWritten: str = None
    
    prescriber: "Reference" = None
    
    lensSpecification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    product: "CodeableConcept" = None
    
    eye: str = None
    
    sphere: float = None
    
    cylinder: float = None
    
    axis: int = None
    
    prism: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    amount: float = None
    
    base: str = None
    
    add: float = None
    
    power: float = None
    
    backCurve: float = None
    
    diameter: float = None
    
    duration: "Quantity" = None
    
    color: str = None
    
    brand: str = None
    
    note: "Annotation" = None
    