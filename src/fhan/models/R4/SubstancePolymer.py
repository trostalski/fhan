"""
Generated class for SubstancePolymer. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.SubstanceAmount import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
        
    
    

class StartingMaterial(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' material: Todo
    :param 'CodeableConcept' type: Todo
    :param bool isDefining: Todo
    :param 'SubstanceAmount' amount: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  material: 'CodeableConcept' = None,  type: 'CodeableConcept' = None,  isDefining: bool = None,  amount: 'SubstanceAmount' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.material: 'CodeableConcept' = material 
        self.type: 'CodeableConcept' = type 
        self.isDefining: bool = isDefining 
        self.amount: 'SubstanceAmount' = amount 
        

  
    
    

class MonomerSet(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' ratioType: Todo
    :param list['StartingMaterial'] startingMaterial: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  ratioType: 'CodeableConcept' = None,  startingMaterial: list['StartingMaterial'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.ratioType: 'CodeableConcept' = ratioType 
        self.startingMaterial: list['StartingMaterial'] = startingMaterial or []
        

    
        
    
        
    
    

class DegreeOfPolymerisation(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' degree: Todo
    :param 'SubstanceAmount' amount: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  degree: 'CodeableConcept' = None,  amount: 'SubstanceAmount' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.degree: 'CodeableConcept' = degree 
        self.amount: 'SubstanceAmount' = amount 
        

    
    

class StructuralRepresentation(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' type: Todo
    :param str representation: Todo
    :param 'Attachment' attachment: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: 'CodeableConcept' = None,  representation: str = None,  attachment: 'Attachment' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: 'CodeableConcept' = type 
        self.representation: str = representation 
        self.attachment: 'Attachment' = attachment 
        

  
    
    

class RepeatUnit(ModelBase):
    """ Todo.:param 'CodeableConcept' repeatUnitAmountType: Todo
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' orientationOfPolymerisation: Todo
    :param str repeatUnit: Todo
    :param 'SubstanceAmount' amount: Todo
    :param list['DegreeOfPolymerisation'] degreeOfPolymerisation: Todo
    :param list['StructuralRepresentation'] structuralRepresentation: Todo
    """
    def __init__(self,  repeatUnitAmountType: 'CodeableConcept' = None,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  orientationOfPolymerisation: 'CodeableConcept' = None,  repeatUnit: str = None,  amount: 'SubstanceAmount' = None,  degreeOfPolymerisation: list['DegreeOfPolymerisation'] = None,  structuralRepresentation: list['StructuralRepresentation'] = None, ):
        self.repeatUnitAmountType: 'CodeableConcept' = repeatUnitAmountType 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.orientationOfPolymerisation: 'CodeableConcept' = orientationOfPolymerisation 
        self.repeatUnit: str = repeatUnit 
        self.amount: 'SubstanceAmount' = amount 
        self.degreeOfPolymerisation: list['DegreeOfPolymerisation'] = degreeOfPolymerisation or []
        self.structuralRepresentation: list['StructuralRepresentation'] = structuralRepresentation or []
        

  
    
    

class Repeat(ModelBase):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int numberOfUnits: Todo
    :param str averageMolecularFormula: Todo
    :param 'CodeableConcept' repeatUnitAmountType: Todo
    :param list['RepeatUnit'] repeatUnit: Todo
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  numberOfUnits: int = None,  averageMolecularFormula: str = None,  repeatUnitAmountType: 'CodeableConcept' = None,  repeatUnit: list['RepeatUnit'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.numberOfUnits: int = numberOfUnits 
        self.averageMolecularFormula: str = averageMolecularFormula 
        self.repeatUnitAmountType: 'CodeableConcept' = repeatUnitAmountType 
        self.repeatUnit: list['RepeatUnit'] = repeatUnit or []
        

class SubstancePolymer(DomainResource):
    """ Todo.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'CodeableConcept' _class: Todo
    :param 'CodeableConcept' geometry: Todo
    :param list['CodeableConcept'] copolymerConnectivity: Todo
    :param str modification: Todo
    :param list['MonomerSet'] monomerSet: Todo
    :param list['Repeat'] repeat: Todo
    """
    def __init__(self, resourceType: str = "SubstancePolymer",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  _class: 'CodeableConcept' = None,  geometry: 'CodeableConcept' = None,  copolymerConnectivity: list['CodeableConcept'] = None,  modification: str = None,  monomerSet: list['MonomerSet'] = None,  repeat: list['Repeat'] = None, ):
        self.resourceType: str = resourceType or "SubstancePolymer"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self._class: 'CodeableConcept' = _class 
        self.geometry: 'CodeableConcept' = geometry 
        self.copolymerConnectivity: list['CodeableConcept'] = copolymerConnectivity or []
        self.modification: str = modification or []
        self.monomerSet: list['MonomerSet'] = monomerSet or []
        self.repeat: list['Repeat'] = repeat or []
        