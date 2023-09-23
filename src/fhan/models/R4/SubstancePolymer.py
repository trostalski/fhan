"""
Generated class for SubstancePolymer. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.SubstanceAmount import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    material: "CodeableConcept" = CodeableConcept()
    type: "CodeableConcept" = CodeableConcept()
    
    isDefining: bool = None
    amount: "SubstanceAmount" = SubstanceAmount()
    

  
    
    
@dataclass
class MonomerSet(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept ratioType: Todo
    :param StartingMaterial startingMaterial: Todo
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    ratioType: "CodeableConcept" = CodeableConcept()
    startingMaterial: list[StartingMaterial] = StartingMaterial() 
    

    
        
    
        
    
    
@dataclass
class DegreeOfPolymerisation(Element):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept degree: Todo
    :param SubstanceAmount amount: Todo
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    degree: "CodeableConcept" = CodeableConcept()
    amount: "SubstanceAmount" = SubstanceAmount()
    

    
    
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    type: "CodeableConcept" = CodeableConcept()
    
    representation: str = None
    attachment: "Attachment" = Attachment()
    

  
    
    
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
    """repeatUnitAmountType: "CodeableConcept" = CodeableConcept()
    
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    orientationOfPolymerisation: "CodeableConcept" = CodeableConcept()
    
    repeatUnit: str = None
    amount: "SubstanceAmount" = SubstanceAmount()
    degreeOfPolymerisation: list[DegreeOfPolymerisation] = DegreeOfPolymerisation() 
    structuralRepresentation: list[StructuralRepresentation] = StructuralRepresentation() 
    

  
    
    
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
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    numberOfUnits: int = None
    
    averageMolecularFormula: str = None
    repeatUnitAmountType: "CodeableConcept" = CodeableConcept()
    repeatUnit: list[RepeatUnit] = RepeatUnit() 
    

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
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    _class: "CodeableConcept" = CodeableConcept()
    
    geometry: "CodeableConcept" = CodeableConcept()
    
    copolymerConnectivity: list[CodeableConcept] = CodeableConcept() 
    
    modification: str = None
    
    monomerSet: list[MonomerSet] = MonomerSet() 
    
    repeat: list[Repeat] = Repeat() 
    