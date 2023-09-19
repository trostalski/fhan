"""
Generated class for Specimen. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Duration import *


@dataclass
class Specimen:
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
    :param Reference subject: Where the specimen came from. This may be from patient(s), from a location (e.g., the source of an environmental sample), or a sampling of a substance, a biologically-derived product, or a device
    :param str receivedTime: The time when specimen is received by the testing laboratory
    :param Reference parent: Specimen from which this specimen originated
    :param Reference request: Why the specimen was collected
    :param str combined: grouped | pooled
    :param CodeableConcept role: The role the specimen serves
    :param BackboneElement feature: The physical feature of a specimen
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Highlighted feature
    :param str description: Information about the feature
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
    :param CodeableReference device: Device used to perform collection
    :param Reference procedure: The procedure that collects the specimen
    :param CodeableReference bodySite: Anatomical collection site
    :param CodeableConcept fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param Duration fastingStatusCodeableConcept: Whether or how long patient abstained from food and/or drink
    :param BackboneElement processing: Processing and processing step details
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Textual description of procedure
    :param CodeableConcept method: Indicates the treatment step  applied to the specimen
    :param Reference additive: Material used in the processing step
    :param str timedateTime: Date and time of specimen processing
    :param Period timedateTime: Date and time of specimen processing
    :param BackboneElement container: Direct container of specimen (tube/slide, etc.)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference device: Device resource for the container
    :param Reference location: Where the container is
    :param Quantity specimenQuantity: Quantity of specimen within container
    :param CodeableConcept condition: State of the specimen
    :param Annotation note: Comments
    
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
    
    accessionIdentifier: "Identifier" = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    receivedTime: str = None
    
    parent: "Reference" = None
    
    request: "Reference" = None
    
    combined: str = None
    
    role: "CodeableConcept" = None
    
    feature: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    collection: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    collector: "Reference" = None
    
    collecteddateTime: str = None
    
    collecteddateTime: "Period" = None
    
    duration: "Duration" = None
    
    quantity: "Quantity" = None
    
    method: "CodeableConcept" = None
    
    device: "CodeableReference" = None
    
    procedure: "Reference" = None
    
    bodySite: "CodeableReference" = None
    
    fastingStatusCodeableConcept: "CodeableConcept" = None
    
    fastingStatusCodeableConcept: "Duration" = None
    
    processing: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    method: "CodeableConcept" = None
    
    additive: "Reference" = None
    
    timedateTime: str = None
    
    timedateTime: "Period" = None
    
    container: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    device: "Reference" = None
    
    location: "Reference" = None
    
    specimenQuantity: "Quantity" = None
    
    condition: "CodeableConcept" = None
    
    note: "Annotation" = None
    