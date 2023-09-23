"""
Generated class for Specimen. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Collection(Element):
    """ Details concerning the specimen collection.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Who collected the specimen
    :param str collectedDateTime: Collection time
    :param Duration duration: How long it took to collect specimen
    :param Quantity quantity: The quantity of specimen collected
    :param CodeableConcept method: Technique used to perform collection
    :param CodeableConcept bodySite: Anatomical collection site
    :param CodeableConcept fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    collector: "Reference" = Reference()
    
    collectedDateTime: str = None
    duration: "Duration" = Duration()
    quantity: "Quantity" = Quantity()
    method: "CodeableConcept" = CodeableConcept()
    bodySite: "CodeableConcept" = CodeableConcept()
    fastingStatusCodeableConcept: "CodeableConcept" = CodeableConcept()
    

    
    
@dataclass
class Processing(Element):
    """ Details concerning processing and processing steps for the specimen.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of procedure
    :param CodeableConcept procedure: Indicates the treatment step  applied to the specimen
    :param Reference additive: Material used in the processing step
    :param str timeDateTime: Date and time of specimen processing
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    description: str = None
    procedure: "CodeableConcept" = CodeableConcept()
    additive: list[Reference] = Reference() 
    
    timeDateTime: str = None
    

    
    
@dataclass
class Container(Element):
    """ The container holding the specimen.  The recursive nature of containers; i.e. blood in tube in tray in rack is not addressed here.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Id for the container
    :param str description: Textual description of the container
    :param CodeableConcept type: Kind of container directly associated with specimen
    :param Quantity capacity: Container volume or size
    :param Quantity specimenQuantity: Quantity of specimen within container
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    identifier: list[Identifier] = Identifier() 
    
    description: str = None
    type: "CodeableConcept" = CodeableConcept()
    capacity: "Quantity" = Quantity()
    specimenQuantity: "Quantity" = Quantity()
    additiveCodeableConcept: "CodeableConcept" = CodeableConcept()
    

@dataclass
class Specimen(ModelBase):
    """ A sample to be used for analysis.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Identifier
    :param Identifier accessionIdentifier: Identifier assigned by the lab
    :param str status: available | unavailable | unsatisfactory | entered-in-error
    :param CodeableConcept type: Kind of material that forms the specimen
    :param Reference subject: Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance or a device
    :param str receivedTime: The time when specimen was received for processing
    :param Reference parent: Specimen from which this specimen originated
    :param Reference request: Why the specimen was collected
    :param Collection collection: Collection details
    :param Processing processing: Processing and processing step details
    :param Container container: Direct container of specimen (tube/slide, etc.)
    :param CodeableConcept condition: State of the specimen
    :param Annotation note: Comments
    """

    resourceType: str = "Specimen"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    accessionIdentifier: "Identifier" = Identifier()
    
    status: str = None
    
    type: "CodeableConcept" = CodeableConcept()
    
    subject: "Reference" = Reference()
    
    receivedTime: str = None
    
    parent: list[Reference] = Reference() 
    
    request: list[Reference] = Reference() 
    
    collection: "Collection" = Collection()
    
    processing: list[Processing] = Processing() 
    
    container: list[Container] = Container() 
    
    condition: list[CodeableConcept] = CodeableConcept() 
    
    note: list[Annotation] = Annotation() 
    