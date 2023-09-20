"""
Generated class for Specimen. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Duration import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class collection(Element):
    """ Details concerning the specimen collection.
    :param BackboneElement collection: Collection details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Who collected the specimen
    :param str collecteddateTime: Collection time
    :param Period collecteddateTime: Collection time
    :param Duration duration: How long it took to collect specimen
    :param Quantity quantity: The quantity of specimen collected
    :param CodeableConcept method: Technique used to perform collection
    :param CodeableConcept bodySite: Anatomical collection site
    :param CodeableConcept fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param Duration fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    """
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    collector: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    duration: "Duration" = None
    
    quantity: "Quantity" = None
    
    method: "CodeableConcept" = None
    
    bodySite: "CodeableConcept" = None
    
    fastingStatusCodeableConcept: "CodeableConcept" = None
    
    fastingStatusCodeableConcept: "Duration" = None
    
@dataclass
class processing(Element):
    """ Details concerning processing and processing steps for the specimen.
    :param BackboneElement processing: Processing and processing step details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of procedure
    :param CodeableConcept procedure: Indicates the treatment step  applied to the specimen
    :param Reference additive: Material used in the processing step
    :param str timedateTime: Date and time of specimen processing
    :param Period timedateTime: Date and time of specimen processing
    """
    processing: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    procedure: "CodeableConcept" = None
    
    additive: list["Reference"] = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
@dataclass
class container(Element):
    """ The container holding the specimen.  The recursive nature of containers; i.e. blood in tube in tray in rack is not addressed here.
    :param BackboneElement container: Direct container of specimen (tube/slide, etc.)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Id for the container
    :param str description: Textual description of the container
    :param CodeableConcept type: Kind of container directly associated with specimen
    :param Quantity capacity: Container volume or size
    :param Quantity specimenQuantity: Quantity of specimen within container
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveCodeableConcept: Additive associated with container
    """
    container: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    description: str = None
    
    type: "CodeableConcept" = None
    
    capacity: "Quantity" = None
    
    specimenQuantity: "Quantity" = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    


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
    :param BackboneElement collection: Collection details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference collector: Who collected the specimen
    :param str collecteddateTime: Collection time
    :param Period collecteddateTime: Collection time
    :param Duration duration: How long it took to collect specimen
    :param Quantity quantity: The quantity of specimen collected
    :param CodeableConcept method: Technique used to perform collection
    :param CodeableConcept bodySite: Anatomical collection site
    :param CodeableConcept fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param Duration fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param BackboneElement processing: Processing and processing step details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of procedure
    :param CodeableConcept procedure: Indicates the treatment step  applied to the specimen
    :param Reference additive: Material used in the processing step
    :param str timedateTime: Date and time of specimen processing
    :param Period timedateTime: Date and time of specimen processing
    :param BackboneElement container: Direct container of specimen (tube/slide, etc.)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Id for the container
    :param str description: Textual description of the container
    :param CodeableConcept type: Kind of container directly associated with specimen
    :param Quantity capacity: Container volume or size
    :param Quantity specimenQuantity: Quantity of specimen within container
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveCodeableConcept: Additive associated with container
    :param CodeableConcept condition: State of the specimen
    :param Annotation note: Comments
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    accessionIdentifier: "Identifier" = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    receivedTime: str = None
    
    parent: list["Reference"] = None
    
    request: list["Reference"] = None
    
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    collector: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    duration: "Duration" = None
    
    quantity: "Quantity" = None
    
    method: "CodeableConcept" = None
    
    bodySite: "CodeableConcept" = None
    
    fastingStatusCodeableConcept: "CodeableConcept" = None
    
    fastingStatusCodeableConcept: "Duration" = None
    
    processing: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    description: str = None
    
    procedure: "CodeableConcept" = None
    
    additive: list["Reference"] = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    container: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    description: str = None
    
    type: "CodeableConcept" = None
    
    capacity: "Quantity" = None
    
    specimenQuantity: "Quantity" = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
    condition: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    