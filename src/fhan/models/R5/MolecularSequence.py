"""
Generated class for MolecularSequence. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class StartingSequence(BaseModel):
    """ A sequence that is used as a starting sequence to describe variants that are present in a sequence analyzed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept genomeAssembly: The genome assembly used for starting sequence, e.g. GRCh38
    :param CodeableConcept chromosome: Chromosome Identifier
    :param CodeableConcept sequenceCodeableConcept: The reference sequence that represents the starting sequence
    :param str sequenceString: The reference sequence that represents the starting sequence
    :param Reference sequenceReference: The reference sequence that represents the starting sequence
    :param int windowStart: Start position of the window on the starting sequence
    :param int windowEnd: End position of the window on the starting sequence
    :param str orientation: sense | antisense
    :param str strand: watson | crick
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "genomeAssembly": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "chromosome": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "sequenceCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "sequenceReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  genomeAssembly:  'CodeableConcept'  = None,  chromosome:  'CodeableConcept'  = None,  sequenceCodeableConcept:  'CodeableConcept'  = None,  sequenceString:  'str'  = None,  sequenceReference:  'Reference'  = None,  windowStart:  'int'  = None,  windowEnd:  'int'  = None,  orientation:  'str'  = None,  strand:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.genomeAssembly = genomeAssembly 
        self.chromosome = chromosome 
        self.sequenceCodeableConcept = sequenceCodeableConcept 
        self.sequenceString = sequenceString 
        self.sequenceReference = sequenceReference 
        self.windowStart = windowStart 
        self.windowEnd = windowEnd 
        self.orientation = orientation 
        self.strand = strand 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Edit(BaseModel):
    """ Changes in sequence from the starting sequence.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Start position of the edit on the starting sequence
    :param int end: End position of the edit on the starting sequence
    :param str replacementSequence: Allele that was observed
    :param str replacedSequence: Allele in the starting sequence
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  start:  'int'  = None,  end:  'int'  = None,  replacementSequence:  'str'  = None,  replacedSequence:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.start = start 
        self.end = end 
        self.replacementSequence = replacementSequence 
        self.replacedSequence = replacedSequence 
        

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Relative(BaseModel):
    """ A sequence defined relative to another sequence.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept coordinateSystem: Ways of identifying nucleotides or amino acids within a sequence
    :param int ordinalPosition: Indicates the order in which the sequence should be considered when putting multiple 'relative' elements together
    :param Range sequenceRange: Indicates the nucleotide range in the composed sequence when multiple 'relative' elements are used together
    :param StartingSequence startingSequence: A sequence used as starting sequence
    :param Edit edit: Changes in sequence from the starting sequence
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "coordinateSystem": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "sequenceRange": {"class_name": "Range", "is_contained": False},
        
        
        "startingSequence": {"class_name": "StartingSequence", "is_contained": True},
        
        
        "edit": {"class_name": "Edit", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  coordinateSystem:  'CodeableConcept'  = None,  ordinalPosition:  'int'  = None,  sequenceRange:  'Range'  = None,  startingSequence:  'StartingSequence'  = None,  edit:  list['Edit']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.coordinateSystem = coordinateSystem 
        self.ordinalPosition = ordinalPosition 
        self.sequenceRange = sequenceRange 
        self.startingSequence = startingSequence 
        self.edit = edit or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class MolecularSequence(DomainResource):
    """ Representation of a molecular sequence.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Unique ID for this particular sequence
    :param str type: aa | dna | rna
    :param Reference subject: Subject this sequence is associated too
    :param Reference focus: What the molecular sequence is about, when it is not about the subject of record
    :param Reference specimen: Specimen used for sequencing
    :param Reference device: The method for sequencing
    :param Reference performer: Who should be responsible for test result
    :param str literal: Sequence that was observed
    :param Attachment formatted: Embedded file or a link (URL) which contains content to represent the sequence
    :param Relative relative: A sequence defined relative to another sequence
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        "specimen": {"class_name": "Reference", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        "performer": {"class_name": "Reference", "is_contained": False},
        
        
        
        "formatted": {"class_name": "Attachment", "is_contained": False},
        
        
        "relative": {"class_name": "Relative", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  type:  'str'  = None,  subject:  'Reference'  = None,  focus:  list['Reference']  = None,  specimen:  'Reference'  = None,  device:  'Reference'  = None,  performer:  'Reference'  = None,  literal:  'str'  = None,  formatted:  list['Attachment']  = None,  relative:  list['Relative']  = None, ):
        self.resourceType = resourceType or "MolecularSequence"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type 
        self.subject = subject 
        self.focus = focus or []
        self.specimen = specimen 
        self.device = device 
        self.performer = performer 
        self.literal = literal 
        self.formatted = formatted or []
        self.relative = relative or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "MolecularSequence":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()