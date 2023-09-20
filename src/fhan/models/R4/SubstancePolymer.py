"""
Generated class for SubstancePolymer. 
Time: 2023-09-20 20:39:03
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.SubstanceAmount import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.generator_models import ModelBase

    
        
    
    
@dataclass
class StartingMaterial(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept material: Todo
    :param CodeableConcept type: Todo
    :param bool isDefining: Todo
    :param SubstanceAmount amount: Todo
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    material: "CodeableConcept" = None
    type: "CodeableConcept" = None
    
    isDefining: bool = None
    amount: "SubstanceAmount" = None
    

  
    
    
@dataclass
class MonomerSet(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept ratioType: Todo
    :param StartingMaterial startingMaterial: Todo
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    ratioType: "CodeableConcept" = None
    startingMaterial: list[StartingMaterial] = None
    

    
        
    
        
    
    
@dataclass
class DegreeOfPolymerisation(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept degree: Todo
    :param SubstanceAmount amount: Todo
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    degree: "CodeableConcept" = None
    amount: "SubstanceAmount" = None
    

    
    
@dataclass
class StructuralRepresentation(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Todo
    :param str representation: Todo
    :param Attachment attachment: Todo
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    
    representation: str = None
    attachment: "Attachment" = None
    

  
    
    
@dataclass
class RepeatUnit(Element):
    """ Todo.:param CodeableConcept repeatUnitAmountType: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept orientationOfPolymerisation: Todo
    :param str repeatUnit: Todo
    :param SubstanceAmount amount: Todo
    :param DegreeOfPolymerisation degreeOfPolymerisation: Todo
    :param StructuralRepresentation structuralRepresentation: Todo
    """repeatUnitAmountType: "CodeableConcept" = None
    
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    orientationOfPolymerisation: "CodeableConcept" = None
    
    repeatUnit: str = None
    amount: "SubstanceAmount" = None
    degreeOfPolymerisation: list[DegreeOfPolymerisation] = None
    structuralRepresentation: list[StructuralRepresentation] = None
    

  
    
    
@dataclass
class Repeat(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int numberOfUnits: Todo
    :param str averageMolecularFormula: Todo
    :param CodeableConcept repeatUnitAmountType: Todo
    :param RepeatUnit repeatUnit: Todo
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    numberOfUnits: int = None
    
    averageMolecularFormula: str = None
    repeatUnitAmountType: "CodeableConcept" = None
    repeatUnit: list[RepeatUnit] = None
    

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
    :param MonomerSet monomerSet: Todo
    :param Repeat repeat: Todo
    """

    resourceType: str = "SubstancePolymer"
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
    
    monomerSet: list["MonomerSet"] = None
    
    repeat: list["Repeat"] = None
    