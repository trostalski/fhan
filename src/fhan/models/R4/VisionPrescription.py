"""
Generated class for VisionPrescription. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class Prism(Element):
    """ Allows for adjustment on two axis.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param float amount: Amount of adjustment
    :param str base: up | down | in | out
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    amount: float = None
    
    base: str = None
    

  
    
    
@dataclass
class LensSpecification(Element):
    """ Contain the details of  the individual lens specifications and serves as the authorization for the fullfillment by certified professionals.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept product: Product to be supplied
    :param str eye: right | left
    :param float sphere: Power of the lens
    :param float cylinder: Lens power for astigmatism
    :param int axis: Lens meridian which contain no power for astigmatism
    :param Prism prism: Eye alignment compensation
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    product: "CodeableConcept" = CodeableConcept()
    
    eye: str = None
    
    sphere: float = None
    
    cylinder: float = None
    
    axis: int = None
    prism: list[Prism] = Prism() 
    
    add: float = None
    
    power: float = None
    
    backCurve: float = None
    
    diameter: float = None
    duration: "Quantity" = Quantity()
    
    color: str = None
    
    brand: str = None
    note: list[Annotation] = Annotation() 
    

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
    :param LensSpecification lensSpecification: Vision lens authorization
    """

    resourceType: str = "VisionPrescription"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    created: str = None
    
    patient: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    dateWritten: str = None
    
    prescriber: "Reference" = Reference()
    
    lensSpecification: list[LensSpecification] = LensSpecification() 
    