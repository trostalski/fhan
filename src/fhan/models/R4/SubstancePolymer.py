"""
Generated class for SubstancePolymer. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.SubstanceAmount import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

@dataclass
class monomerSet(Element):
    """ Todo.
    :param BackboneElement monomerSet: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept ratioType: Todo
    :param BackboneElement startingMaterial: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Todo
    :param CodeableConcept type: Todo
    :param bool isDefining: Todo
    :param SubstanceAmount amount: Todo
    """
    monomerSet: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    ratioType: "CodeableConcept" = None
    
    startingMaterial: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amount: "SubstanceAmount" = None
    
@dataclass
class startingMaterial(Element):
    """ Todo.
    :param BackboneElement startingMaterial: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Todo
    :param CodeableConcept type: Todo
    :param bool isDefining: Todo
    :param SubstanceAmount amount: Todo
    """
    startingMaterial: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amount: "SubstanceAmount" = None
    
@dataclass
class repeat(Element):
    """ Todo.
    :param BackboneElement repeat: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int numberOfUnits: Todo
    :param str averageMolecularFormula: Todo
    :param CodeableConcept repeatUnitAmountType: Todo
    :param BackboneElement repeatUnit: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept orientationOfPolymerisation: Todo
    :param str repeatUnit: Todo
    :param SubstanceAmount amount: Todo
    :param BackboneElement degreeOfPolymerisation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept degree: Todo
    :param SubstanceAmount amount: Todo
    :param BackboneElement structuralRepresentation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param str representation: Todo
    :param Attachment attachment: Todo
    """
    repeat: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    numberOfUnits: int = None
    
    averageMolecularFormula: str = None
    
    repeatUnitAmountType: "CodeableConcept" = None
    
    repeatUnit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    orientationOfPolymerisation: "CodeableConcept" = None
    
    repeatUnit: str = None
    
    amount: "SubstanceAmount" = None
    
    degreeOfPolymerisation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    degree: "CodeableConcept" = None
    
    amount: "SubstanceAmount" = None
    
    structuralRepresentation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    attachment: "Attachment" = None
    
@dataclass
class repeatUnit(Element):
    """ Todo.
    :param CodeableConcept repeatUnitAmountType: Todo
    :param BackboneElement repeatUnit: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept orientationOfPolymerisation: Todo
    :param str repeatUnit: Todo
    :param SubstanceAmount amount: Todo
    :param BackboneElement degreeOfPolymerisation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept degree: Todo
    :param SubstanceAmount amount: Todo
    :param BackboneElement structuralRepresentation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param str representation: Todo
    :param Attachment attachment: Todo
    """
    repeatUnitAmountType: "CodeableConcept" = None
    
    repeatUnit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    orientationOfPolymerisation: "CodeableConcept" = None
    
    repeatUnit: str = None
    
    amount: "SubstanceAmount" = None
    
    degreeOfPolymerisation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    degree: "CodeableConcept" = None
    
    amount: "SubstanceAmount" = None
    
    structuralRepresentation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    attachment: "Attachment" = None
    
@dataclass
class degreeOfPolymerisation(Element):
    """ Todo.
    :param BackboneElement degreeOfPolymerisation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept degree: Todo
    :param SubstanceAmount amount: Todo
    """
    degreeOfPolymerisation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    degree: "CodeableConcept" = None
    
    amount: "SubstanceAmount" = None
    
@dataclass
class structuralRepresentation(Element):
    """ Todo.
    :param BackboneElement structuralRepresentation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param str representation: Todo
    :param Attachment attachment: Todo
    """
    structuralRepresentation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    attachment: "Attachment" = None
    


@dataclass
class SubstancePolymer(ModelBase):
    """ Todo.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param CodeableConcept _class: Todo
    :param CodeableConcept geometry: Todo
    :param CodeableConcept copolymerConnectivity: Todo
    :param str modification: Todo
    :param BackboneElement monomerSet: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept ratioType: Todo
    :param BackboneElement startingMaterial: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Todo
    :param CodeableConcept type: Todo
    :param bool isDefining: Todo
    :param SubstanceAmount amount: Todo
    :param BackboneElement repeat: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int numberOfUnits: Todo
    :param str averageMolecularFormula: Todo
    :param CodeableConcept repeatUnitAmountType: Todo
    :param BackboneElement repeatUnit: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept orientationOfPolymerisation: Todo
    :param str repeatUnit: Todo
    :param SubstanceAmount amount: Todo
    :param BackboneElement degreeOfPolymerisation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept degree: Todo
    :param SubstanceAmount amount: Todo
    :param BackboneElement structuralRepresentation: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param str representation: Todo
    :param Attachment attachment: Todo
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    _class: "CodeableConcept" = None
    
    geometry: "CodeableConcept" = None
    
    copolymerConnectivity: list["CodeableConcept"] = None
    
    modification: str = None
    
    monomerSet: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    ratioType: "CodeableConcept" = None
    
    startingMaterial: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    material: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amount: "SubstanceAmount" = None
    
    repeat: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    numberOfUnits: int = None
    
    averageMolecularFormula: str = None
    
    repeatUnitAmountType: "CodeableConcept" = None
    
    repeatUnit: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    orientationOfPolymerisation: "CodeableConcept" = None
    
    repeatUnit: str = None
    
    amount: "SubstanceAmount" = None
    
    degreeOfPolymerisation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    degree: "CodeableConcept" = None
    
    amount: "SubstanceAmount" = None
    
    structuralRepresentation: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    attachment: "Attachment" = None
    