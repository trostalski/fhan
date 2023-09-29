"""
Generated class for SubstanceDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Moiety(BaseModel):
    """ Moiety, for structural modifications.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Role that the moiety is playing
    :param Identifier identifier: Identifier by which this moiety substance is known
    :param str name: Textual name for this moiety substance
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula for this moiety (e.g. with the Hill system)
    :param Quantity amountQuantity: Quantitative value for this moiety
    :param str amountString: Quantitative value for this moiety
    :param CodeableConcept measurementType: The measurement type of the quantitative value
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "stereochemistry": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "opticalActivity": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "amountQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        "measurementType": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  role:  'CodeableConcept'  = None,  identifier:  'Identifier'  = None,  name:  'str'  = None,  stereochemistry:  'CodeableConcept'  = None,  opticalActivity:  'CodeableConcept'  = None,  molecularFormula:  'str'  = None,  amountQuantity:  'Quantity'  = None,  amountString:  'str'  = None,  measurementType:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.role = role 
        self.identifier = identifier 
        self.name = name 
        self.stereochemistry = stereochemistry 
        self.opticalActivity = opticalActivity 
        self.molecularFormula = molecularFormula 
        self.amountQuantity = amountQuantity 
        self.amountString = amountString 
        self.measurementType = measurementType 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Characterization(BaseModel):
    """ General specifications for this substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept technique: The method used to find the characterization e.g. HPLC
    :param CodeableConcept form: Describes the nature of the chemical entity and explains, for instance, whether this is a base or a salt form
    :param str description: The description or justification in support of the interpretation of the data file
    :param Attachment file: The data produced by the analytical instrument or a pictorial representation of that data. Examples: a JCAMP, JDX, or ADX file, or a chromatogram or spectrum analysis
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "technique": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "form": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "file": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  technique:  'CodeableConcept'  = None,  form:  'CodeableConcept'  = None,  description:  'str'  = None,  file:  list['Attachment']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.technique = technique 
        self.form = form 
        self.description = description 
        self.file = file or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Property(BaseModel):
    """ General specifications for this substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of property
    :param CodeableConcept valueCodeableConcept: A value for the property
    :param Quantity valueQuantity: A value for the property
    :param str valueDate: A value for the property
    :param bool valueBoolean: A value for the property
    :param Attachment valueAttachment: A value for the property
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "valueQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        
        
        "valueAttachment": {"class_name": "Attachment", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  valueCodeableConcept:  'CodeableConcept'  = None,  valueQuantity:  'Quantity'  = None,  valueDate:  'str'  = None,  valueBoolean:  'bool'  = None,  valueAttachment:  'Attachment'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.valueCodeableConcept = valueCodeableConcept 
        self.valueQuantity = valueQuantity 
        self.valueDate = valueDate 
        self.valueBoolean = valueBoolean 
        self.valueAttachment = valueAttachment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class MolecularWeight(BaseModel):
    """ The average mass of a molecule of a compound compared to 1/12 the mass of carbon 12 and calculated as the sum of the atomic weights of the constituent atoms.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept method: The method by which the weight was determined
    :param CodeableConcept type: Type of molecular weight e.g. exact, average, weight average
    :param Quantity amount: Used to capture quantitative values for a variety of elements
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "method": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "amount": {"class_name": "Quantity", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  method:  'CodeableConcept'  = None,  type:  'CodeableConcept'  = None,  amount:  'Quantity'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.method = method 
        self.type = type 
        self.amount = amount 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Representation(BaseModel):
    """ A depiction of the structure of the substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of structural representation (e.g. full, partial)
    :param str representation: The structural representation as a text string in a standard format
    :param CodeableConcept format: The format of the representation e.g. InChI, SMILES, MOLFILE (note: not the physical file format)
    :param Reference document: An attachment with the structural representation e.g. a structure graphic or AnIML file
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "format": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "document": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  representation:  'str'  = None,  format:  'CodeableConcept'  = None,  document:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.representation = representation 
        self.format = format 
        self.document = document 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Structure(BaseModel):
    """ Structural information.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: An expression which states the number and type of atoms present in a molecule of a substance
    :param str molecularFormulaByMoiety: Specified per moiety according to the Hill system
    :param MolecularWeight molecularWeight: The molecular weight or weight range
    :param CodeableConcept technique: The method used to find the structure e.g. X-ray, NMR
    :param Reference sourceDocument: Source of information for the structure
    :param Representation representation: A depiction of the structure of the substance
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "stereochemistry": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "opticalActivity": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "molecularWeight": {"class_name": "MolecularWeight", "is_contained": True},
        
        
        "technique": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "sourceDocument": {"class_name": "Reference", "is_contained": False},
        
        
        "representation": {"class_name": "Representation", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  stereochemistry:  'CodeableConcept'  = None,  opticalActivity:  'CodeableConcept'  = None,  molecularFormula:  'str'  = None,  molecularFormulaByMoiety:  'str'  = None,  molecularWeight:  'MolecularWeight'  = None,  technique:  list['CodeableConcept']  = None,  sourceDocument:  list['Reference']  = None,  representation:  list['Representation']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.stereochemistry = stereochemistry 
        self.opticalActivity = opticalActivity 
        self.molecularFormula = molecularFormula 
        self.molecularFormulaByMoiety = molecularFormulaByMoiety 
        self.molecularWeight = molecularWeight 
        self.technique = technique or []
        self.sourceDocument = sourceDocument or []
        self.representation = representation or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Code(BaseModel):
    """ Codes associated with the substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The specific code
    :param CodeableConcept status: Status of the code assignment, for example 'provisional', 'approved'
    :param str statusDate: The date at which the code status was changed
    :param Annotation note: Any comment can be provided in this field
    :param Reference source: Supporting literature
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "source": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  code:  'CodeableConcept'  = None,  status:  'CodeableConcept'  = None,  statusDate:  'str'  = None,  note:  list['Annotation']  = None,  source:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.code = code 
        self.status = status 
        self.statusDate = statusDate 
        self.note = note or []
        self.source = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Official(BaseModel):
    """ Details of the official nature of this name.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept authority: Which authority uses this official name
    :param CodeableConcept status: The status of the official name, for example 'draft', 'active'
    :param str date: Date of official name change
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "authority": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  authority:  'CodeableConcept'  = None,  status:  'CodeableConcept'  = None,  date:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.authority = authority 
        self.status = status 
        self.date = date 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Name(BaseModel):
    """ Names applicable to this substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The actual name
    :param CodeableConcept type: Name type e.g. 'systematic',  'scientific, 'brand'
    :param CodeableConcept status: The status of the name e.g. 'current', 'proposed'
    :param bool preferred: If this is the preferred name for this substance
    :param CodeableConcept language: Human language that the name is written in
    :param CodeableConcept domain: The use context of this name e.g. as an active ingredient or as a food colour additive
    :param CodeableConcept jurisdiction: The jurisdiction where this name applies
    :param Synonym synonym: A synonym of this particular name, by which the substance is also known
    :param Translation translation: A translation for this name into another human language
    :param Official official: Details of the official nature of this name
    :param Reference source: Supporting literature
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "domain": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "synonym": {"class_name": "Synonym", "is_contained": True},
        
        
        "translation": {"class_name": "Translation", "is_contained": True},
        
        
        "official": {"class_name": "Official", "is_contained": True},
        
        
        "source": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  type:  'CodeableConcept'  = None,  status:  'CodeableConcept'  = None,  preferred:  'bool'  = None,  language:  list['CodeableConcept']  = None,  domain:  list['CodeableConcept']  = None,  jurisdiction:  list['CodeableConcept']  = None,  synonym:  list['Synonym']  = None,  translation:  list['Translation']  = None,  official:  list['Official']  = None,  source:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.type = type 
        self.status = status 
        self.preferred = preferred 
        self.language = language or []
        self.domain = domain or []
        self.jurisdiction = jurisdiction or []
        self.synonym = synonym or []
        self.translation = translation or []
        self.official = official or []
        self.source = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Relationship(BaseModel):
    """ A link between this substance and another, with details of the relationship.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference substanceDefinitionReference: A pointer to another substance, as a resource or a representational code
    :param CodeableConcept substanceDefinitionCodeableConcept: A pointer to another substance, as a resource or a representational code
    :param CodeableConcept type: For example "salt to parent", "active moiety"
    :param bool isDefining: For example where an enzyme strongly bonds with a particular substance, this is a defining relationship for that enzyme, out of several possible relationships
    :param Quantity amountQuantity: A numeric factor for the relationship, e.g. that a substance salt has some percentage of active substance in relation to some other
    :param Ratio amountRatio: A numeric factor for the relationship, e.g. that a substance salt has some percentage of active substance in relation to some other
    :param str amountString: A numeric factor for the relationship, e.g. that a substance salt has some percentage of active substance in relation to some other
    :param Ratio ratioHighLimitAmount: For use when the numeric has an uncertain range
    :param CodeableConcept comparator: An operator for the amount, for example "average", "approximately", "less than"
    :param Reference source: Supporting literature
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "substanceDefinitionReference": {"class_name": "Reference", "is_contained": False},
        
        
        "substanceDefinitionCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "amountQuantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "amountRatio": {"class_name": "Ratio", "is_contained": False},
        
        
        
        "ratioHighLimitAmount": {"class_name": "Ratio", "is_contained": False},
        
        
        "comparator": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "source": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  substanceDefinitionReference:  'Reference'  = None,  substanceDefinitionCodeableConcept:  'CodeableConcept'  = None,  type:  'CodeableConcept'  = None,  isDefining:  'bool'  = None,  amountQuantity:  'Quantity'  = None,  amountRatio:  'Ratio'  = None,  amountString:  'str'  = None,  ratioHighLimitAmount:  'Ratio'  = None,  comparator:  'CodeableConcept'  = None,  source:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.substanceDefinitionReference = substanceDefinitionReference 
        self.substanceDefinitionCodeableConcept = substanceDefinitionCodeableConcept 
        self.type = type 
        self.isDefining = isDefining 
        self.amountQuantity = amountQuantity 
        self.amountRatio = amountRatio 
        self.amountString = amountString 
        self.ratioHighLimitAmount = ratioHighLimitAmount 
        self.comparator = comparator 
        self.source = source or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class SourceMaterial(BaseModel):
    """ Material or taxonomic/anatomical source for the substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Classification of the origin of the raw material. e.g. cat hair is an Animal source type
    :param CodeableConcept genus: The genus of an organism e.g. the Latin epithet of the plant/animal scientific name
    :param CodeableConcept species: The species of an organism e.g. the Latin epithet of the species of the plant/animal
    :param CodeableConcept part: An anatomical origin of the source material within an organism
    :param CodeableConcept countryOfOrigin: The country or countries where the material is harvested
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "genus": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "species": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "part": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "countryOfOrigin": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  genus:  'CodeableConcept'  = None,  species:  'CodeableConcept'  = None,  part:  'CodeableConcept'  = None,  countryOfOrigin:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.genus = genus 
        self.species = species 
        self.part = part 
        self.countryOfOrigin = countryOfOrigin or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class SubstanceDefinition(DomainResource):
    """ The detailed description of a substance, typically at a level beyond what is used for prescribing.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier by which this substance is known
    :param str version: A business level version identifier of the substance
    :param CodeableConcept status: Status of substance within the catalogue e.g. active, retired
    :param CodeableConcept classification: A categorization, high level e.g. polymer or nucleic acid, or food, chemical, biological, or lower e.g. polymer linear or branch chain, or type of impurity
    :param CodeableConcept domain: If the substance applies to human or veterinary use
    :param CodeableConcept grade: The quality standard, established benchmark, to which substance complies (e.g. USP/NF, BP)
    :param str description: Textual description of the substance
    :param Reference informationSource: Supporting literature
    :param Annotation note: Textual comment about the substance's catalogue or registry record
    :param Reference manufacturer: The entity that creates, makes, produces or fabricates the substance
    :param Reference supplier: An entity that is the source for the substance. It may be different from the manufacturer
    :param Moiety moiety: Moiety, for structural modifications
    :param Characterization characterization: General specifications for this substance
    :param Property property: General specifications for this substance
    :param Reference referenceInformation: General information detailing this substance
    :param MolecularWeight molecularWeight: The average mass of a molecule of a compound
    :param Structure structure: Structural information
    :param Code code: Codes associated with the substance
    :param Name name: Names applicable to this substance
    :param Relationship relationship: A link between this substance and another
    :param Reference nucleicAcid: Data items specific to nucleic acids
    :param Reference polymer: Data items specific to polymers
    :param Reference protein: Data items specific to proteins
    :param SourceMaterial sourceMaterial: Material or taxonomic/anatomical source
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "domain": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "grade": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "informationSource": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "manufacturer": {"class_name": "Reference", "is_contained": False},
        
        
        "supplier": {"class_name": "Reference", "is_contained": False},
        
        
        "moiety": {"class_name": "Moiety", "is_contained": True},
        
        
        "characterization": {"class_name": "Characterization", "is_contained": True},
        
        
        "property": {"class_name": "Property", "is_contained": True},
        
        
        "referenceInformation": {"class_name": "Reference", "is_contained": False},
        
        
        "molecularWeight": {"class_name": "MolecularWeight", "is_contained": True},
        
        
        "structure": {"class_name": "Structure", "is_contained": True},
        
        
        "code": {"class_name": "Code", "is_contained": True},
        
        
        "name": {"class_name": "Name", "is_contained": True},
        
        
        "relationship": {"class_name": "Relationship", "is_contained": True},
        
        
        "nucleicAcid": {"class_name": "Reference", "is_contained": False},
        
        
        "polymer": {"class_name": "Reference", "is_contained": False},
        
        
        "protein": {"class_name": "Reference", "is_contained": False},
        
        
        "sourceMaterial": {"class_name": "SourceMaterial", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  status:  'CodeableConcept'  = None,  classification:  list['CodeableConcept']  = None,  domain:  'CodeableConcept'  = None,  grade:  list['CodeableConcept']  = None,  description:  'str'  = None,  informationSource:  list['Reference']  = None,  note:  list['Annotation']  = None,  manufacturer:  list['Reference']  = None,  supplier:  list['Reference']  = None,  moiety:  list['Moiety']  = None,  characterization:  list['Characterization']  = None,  property:  list['Property']  = None,  referenceInformation:  'Reference'  = None,  molecularWeight:  list['MolecularWeight']  = None,  structure:  'Structure'  = None,  code:  list['Code']  = None,  name:  list['Name']  = None,  relationship:  list['Relationship']  = None,  nucleicAcid:  'Reference'  = None,  polymer:  'Reference'  = None,  protein:  'Reference'  = None,  sourceMaterial:  'SourceMaterial'  = None, ):
        self.resourceType = resourceType or "SubstanceDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.version = version 
        self.status = status 
        self.classification = classification or []
        self.domain = domain 
        self.grade = grade or []
        self.description = description 
        self.informationSource = informationSource or []
        self.note = note or []
        self.manufacturer = manufacturer or []
        self.supplier = supplier or []
        self.moiety = moiety or []
        self.characterization = characterization or []
        self.property = property or []
        self.referenceInformation = referenceInformation 
        self.molecularWeight = molecularWeight or []
        self.structure = structure 
        self.code = code or []
        self.name = name or []
        self.relationship = relationship or []
        self.nucleicAcid = nucleicAcid 
        self.polymer = polymer 
        self.protein = protein 
        self.sourceMaterial = sourceMaterial 
        

    @classmethod
    def from_dict(cls, data: dict) -> "SubstanceDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "SubstanceDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()