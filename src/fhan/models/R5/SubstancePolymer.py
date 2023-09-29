"""
Generated class for SubstancePolymer. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class StartingMaterial(BaseModel):
    """ The starting materials - monomer(s) used in the synthesis of the polymer.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The type of substance for this starting material
    :param CodeableConcept category: Substance high level category, e.g. chemical substance
    :param bool isDefining: Used to specify whether the attribute described is a defining element for the unique identification of the polymer
    :param Quantity amount: A percentage
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  category:  'CodeableConcept'  = None,  isDefining:  'bool'  = None,  amount:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.category = category 
        self.isDefining = isDefining 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class MonomerSet(BaseModel):
    """ Todo.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept ratioType: Captures the type of ratio to the entire polymer, e.g. Monomer/Polymer ratio, SRU/Polymer Ratio
    :param StartingMaterial startingMaterial: The starting materials - monomer(s) used in the synthesis of the polymer
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "ratioType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "startingMaterial": {"class_name": "StartingMaterial", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  ratioType:  'CodeableConcept'  = None,  startingMaterial:  list['StartingMaterial']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.ratioType = ratioType 
        self.startingMaterial = startingMaterial or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class DegreeOfPolymerisation(BaseModel):
    """ Applies to homopolymer and block co-polymers where the degree of polymerisation within a block can be described.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the degree of polymerisation shall be described, e.g. SRU/Polymer Ratio
    :param int average: An average amount of polymerisation
    :param int low: A low expected limit of the amount
    :param int high: A high expected limit of the amount
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  average:  'int'  = None,  low:  'int'  = None,  high:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.average = average 
        self.low = low 
        self.high = high 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class StructuralRepresentation(BaseModel):
    """ A graphical structure for this SRU.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of structure (e.g. Full, Partial, Representative)
    :param str representation: The structural representation as text string in a standard format e.g. InChI, SMILES, MOLFILE, CDX, SDF, PDB, mmCIF
    :param CodeableConcept format: The format of the representation e.g. InChI, SMILES, MOLFILE, CDX, SDF, PDB, mmCIF
    :param Attachment attachment: An attached file with the structural representation
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "format": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "attachment": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  representation:  'str'  = None,  format:  'CodeableConcept'  = None,  attachment:  'Attachment'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.representation = representation 
        self.format = format 
        self.attachment = attachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class RepeatUnit(BaseModel):
    """ An SRU - Structural Repeat Unit.:param CodeableConcept repeatUnitAmountType: How the quantitative amount of Structural Repeat Units is captured (e.g. Exact, Numeric, Average)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str unit: Structural repeat units are essential elements for defining polymers
    :param CodeableConcept orientation: The orientation of the polymerisation, e.g. head-tail, head-head, random
    :param int amount: Number of repeats of this unit
    :param DegreeOfPolymerisation degreeOfPolymerisation: Applies to homopolymer and block co-polymers where the degree of polymerisation within a block can be described
    :param StructuralRepresentation structuralRepresentation: A graphical structure for this SRU
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        "repeatUnitAmountType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "orientation": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "degreeOfPolymerisation": {"class_name": "DegreeOfPolymerisation", "is_contained": True},
        
        
        "structuralRepresentation": {"class_name": "StructuralRepresentation", "is_contained": True},
        
        }
    def __init__(self,  repeatUnitAmountType:  'CodeableConcept'  = None,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  unit:  'str'  = None,  orientation:  'CodeableConcept'  = None,  amount:  'int'  = None,  degreeOfPolymerisation:  list['DegreeOfPolymerisation']  = None,  structuralRepresentation:  list['StructuralRepresentation']  = None, ):
        self.repeatUnitAmountType = repeatUnitAmountType 
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.unit = unit 
        self.orientation = orientation 
        self.amount = amount 
        self.degreeOfPolymerisation = degreeOfPolymerisation or []
        self.structuralRepresentation = structuralRepresentation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Repeat(BaseModel):
    """ Specifies and quantifies the repeated units and their configuration.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str averageMolecularFormula: A representation of an (average) molecular formula from a polymer
    :param CodeableConcept repeatUnitAmountType: How the quantitative amount of Structural Repeat Units is captured (e.g. Exact, Numeric, Average)
    :param RepeatUnit repeatUnit: An SRU - Structural Repeat Unit
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "repeatUnitAmountType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "repeatUnit": {"class_name": "RepeatUnit", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  averageMolecularFormula:  'str'  = None,  repeatUnitAmountType:  'CodeableConcept'  = None,  repeatUnit:  list['RepeatUnit']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.averageMolecularFormula = averageMolecularFormula 
        self.repeatUnitAmountType = repeatUnitAmountType 
        self.repeatUnit = repeatUnit or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstancePolymer(DomainResource):
    """ Properties of a substance specific to it being a polymer.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: A business idenfier for this polymer, but typically this is handled by a SubstanceDefinition identifier
    :param CodeableConcept _class: Overall type of the polymer
    :param CodeableConcept geometry: Polymer geometry, e.g. linear, branched, cross-linked, network or dendritic
    :param CodeableConcept copolymerConnectivity: Descrtibes the copolymer sequence type (polymer connectivity)
    :param str modification: Todo - this is intended to connect to a repeating full modification structure, also used by Protein and Nucleic Acid . String is just a placeholder
    :param MonomerSet monomerSet: Todo
    :param Repeat repeat: Specifies and quantifies the repeated units and their configuration
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "_class": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "geometry": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "copolymerConnectivity": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "monomerSet": {"class_name": "MonomerSet", "is_contained": True},
        
        
        "repeat": {"class_name": "Repeat", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  'Identifier'  = None,  _class:  'CodeableConcept'  = None,  geometry:  'CodeableConcept'  = None,  copolymerConnectivity:  list['CodeableConcept']  = None,  modification:  'str'  = None,  monomerSet:  list['MonomerSet']  = None,  repeat:  list['Repeat']  = None, ):
        self.resourceType = resourceType or "SubstancePolymer"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier 
        self._class = _class 
        self.geometry = geometry 
        self.copolymerConnectivity = copolymerConnectivity or []
        self.modification = modification 
        self.monomerSet = monomerSet or []
        self.repeat = repeat or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstancePolymer":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstancePolymer":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()