"""
Generated class for SpecimenDefinition. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Range import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Element import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class typeTested(Element):
    """ Specimen conditioned in a container as expected by the testing laboratory.
    :param BackboneElement typeTested: Specimen in container intended for testing by lab
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool isDerived: Primary or secondary specimen
    :param CodeableConcept type: Type of intended specimen
    :param str preference: preferred | alternate
    :param BackboneElement container: The specimen's container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Container material
    :param CodeableConcept type: Kind of container associated with the kind of specimen
    :param CodeableConcept cap: Color of container cap
    :param str description: Container description
    :param Quantity capacity: Container capacity
    :param Quantity minimumVolumeQuantity: Minimum volume
    :param str minimumVolumeQuantity: Minimum volume
    :param BackboneElement additive: Additive associated with container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveCodeableConcept: Additive associated with container
    :param str preparation: Specimen container preparation
    :param str requirement: Specimen requirements
    :param Duration retentionTime: Specimen retention time
    :param CodeableConcept rejectionCriterion: Rejection criterion
    :param BackboneElement handling: Specimen handling before testing
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept temperatureQualifier: Temperature qualifier
    :param Range temperatureRange: Temperature range
    :param Duration maxDuration: Maximum preservation time
    :param str instruction: Preservation instruction
    """
    typeTested: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    isDerived: bool = None
    
    type: "CodeableConcept" = None
    
    preference: str = None
    
    container: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    cap: "CodeableConcept" = None
    
    description: str = None
    
    capacity: "Quantity" = None
    
    minimumVolumeQuantity: "Quantity" = None
    
    minimumVolumeQuantity: str = None
    
    additive: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
    preparation: str = None
    
    requirement: str = None
    
    retentionTime: "Duration" = None
    
    rejectionCriterion: list["CodeableConcept"] = None
    
    handling: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    temperatureQualifier: "CodeableConcept" = None
    
    temperatureRange: "Range" = None
    
    maxDuration: "Duration" = None
    
    instruction: str = None
    
@dataclass
class container(Element):
    """ The specimen's container.
    :param BackboneElement container: The specimen's container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Container material
    :param CodeableConcept type: Kind of container associated with the kind of specimen
    :param CodeableConcept cap: Color of container cap
    :param str description: Container description
    :param Quantity capacity: Container capacity
    :param Quantity minimumVolumeQuantity: Minimum volume
    :param str minimumVolumeQuantity: Minimum volume
    :param BackboneElement additive: Additive associated with container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveCodeableConcept: Additive associated with container
    :param str preparation: Specimen container preparation
    """
    container: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    cap: "CodeableConcept" = None
    
    description: str = None
    
    capacity: "Quantity" = None
    
    minimumVolumeQuantity: "Quantity" = None
    
    minimumVolumeQuantity: str = None
    
    additive: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
    preparation: str = None
    
@dataclass
class additive(Element):
    """ Substance introduced in the kind of container to preserve, maintain or enhance the specimen. Examples: Formalin, Citrate, EDTA.
    :param BackboneElement additive: Additive associated with container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveCodeableConcept: Additive associated with container
    """
    additive: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
@dataclass
class handling(Element):
    """ Set of instructions for preservation/transport of the specimen at a defined temperature interval, prior the testing process.
    :param BackboneElement handling: Specimen handling before testing
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept temperatureQualifier: Temperature qualifier
    :param Range temperatureRange: Temperature range
    :param Duration maxDuration: Maximum preservation time
    :param str instruction: Preservation instruction
    """
    handling: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    temperatureQualifier: "CodeableConcept" = None
    
    temperatureRange: "Range" = None
    
    maxDuration: "Duration" = None
    
    instruction: str = None
    


@dataclass
class SpecimenDefinition(ModelBase):
    """ A kind of specimen with associated set of requirements.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier of a kind of specimen
    :param CodeableConcept typeCollected: Kind of material to collect
    :param CodeableConcept patientPreparation: Patient preparation for collection
    :param str timeAspect: Time aspect for collection
    :param CodeableConcept collection: Specimen collection procedure
    :param BackboneElement typeTested: Specimen in container intended for testing by lab
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool isDerived: Primary or secondary specimen
    :param CodeableConcept type: Type of intended specimen
    :param str preference: preferred | alternate
    :param BackboneElement container: The specimen's container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Container material
    :param CodeableConcept type: Kind of container associated with the kind of specimen
    :param CodeableConcept cap: Color of container cap
    :param str description: Container description
    :param Quantity capacity: Container capacity
    :param Quantity minimumVolumeQuantity: Minimum volume
    :param str minimumVolumeQuantity: Minimum volume
    :param BackboneElement additive: Additive associated with container
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept additiveCodeableConcept: Additive associated with container
    :param Reference additiveCodeableConcept: Additive associated with container
    :param str preparation: Specimen container preparation
    :param str requirement: Specimen requirements
    :param Duration retentionTime: Specimen retention time
    :param CodeableConcept rejectionCriterion: Rejection criterion
    :param BackboneElement handling: Specimen handling before testing
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept temperatureQualifier: Temperature qualifier
    :param Range temperatureRange: Temperature range
    :param Duration maxDuration: Maximum preservation time
    :param str instruction: Preservation instruction
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: "Identifier" = None
    
    typeCollected: "CodeableConcept" = None
    
    patientPreparation: list["CodeableConcept"] = None
    
    timeAspect: str = None
    
    collection: list["CodeableConcept"] = None
    
    typeTested: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    isDerived: bool = None
    
    type: "CodeableConcept" = None
    
    preference: str = None
    
    container: "BackboneElement" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    cap: "CodeableConcept" = None
    
    description: str = None
    
    capacity: "Quantity" = None
    
    minimumVolumeQuantity: "Quantity" = None
    
    minimumVolumeQuantity: str = None
    
    additive: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    additiveCodeableConcept: "CodeableConcept" = None
    
    additiveCodeableConcept: "Reference" = None
    
    preparation: str = None
    
    requirement: str = None
    
    retentionTime: "Duration" = None
    
    rejectionCriterion: list["CodeableConcept"] = None
    
    handling: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    temperatureQualifier: "CodeableConcept" = None
    
    temperatureRange: "Range" = None
    
    maxDuration: "Duration" = None
    
    instruction: str = None
    