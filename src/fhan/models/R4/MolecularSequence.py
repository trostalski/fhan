"""
Generated class for MolecularSequence. 
Time: 2023-09-25 16:30:45
"""
from importlib import import_module
import inspect

from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Reference import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class ReferenceSeq(ModelBase):
    """ A sequence that is used as a reference to describe variants that are present in a sequence analyzed.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' chromosome: Chromosome containing genetic finding
    :param str genomeBuild: The Genome Build used for reference, following GRCh build versions e.g. 'GRCh 37'
    :param str orientation: sense | antisense
    :param 'CodeableConcept' referenceSeqId: Reference identifier
    :param 'Reference' referenceSeqPointer: A pointer to another MolecularSequence entity as reference sequence
    :param str referenceSeqString: A string to represent reference sequence
    :param str strand: watson | crick
    :param int windowStart: Start position of the window on the  reference sequence
    :param int windowEnd: End position of the window on the reference sequence
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  chromosome: 'CodeableConcept' = None,  genomeBuild: str = None,  orientation: str = None,  referenceSeqId: 'CodeableConcept' = None,  referenceSeqPointer: 'Reference' = None,  referenceSeqString: str = None,  strand: str = None,  windowStart: int = None,  windowEnd: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.chromosome: 'CodeableConcept' = chromosome 
        self.genomeBuild: str = genomeBuild 
        self.orientation: str = orientation 
        self.referenceSeqId: 'CodeableConcept' = referenceSeqId 
        self.referenceSeqPointer: 'Reference' = referenceSeqPointer 
        self.referenceSeqString: str = referenceSeqString 
        self.strand: str = strand 
        self.windowStart: int = windowStart 
        self.windowEnd: int = windowEnd 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ReferenceSeq":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class Variant(ModelBase):
    """ The definition of variant here originates from Sequence ontology ([variant_of](http://www.sequenceontology.org/browser/current_svn/term/variant_of)). This element can represent amino acid or nucleic sequence change(including insertion,deletion,SNP,etc.)  It can represent some complex mutation or segment variation with the assist of CIGAR string.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Start position of the variant on the  reference sequence
    :param int end: End position of the variant on the reference sequence
    :param str observedAllele: Allele that was observed
    :param str referenceAllele: Allele in the reference sequence
    :param str cigar: Extended CIGAR string for aligning the sequence with reference bases
    :param 'Reference' variantPointer: Pointer to observed variant information
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  start: int = None,  end: int = None,  observedAllele: str = None,  referenceAllele: str = None,  cigar: str = None,  variantPointer: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.start: int = start 
        self.end: int = end 
        self.observedAllele: str = observedAllele 
        self.referenceAllele: str = referenceAllele 
        self.cigar: str = cigar 
        self.variantPointer: 'Reference' = variantPointer 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Variant":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
        
    
    

class Roc(ModelBase):
    """ Receiver Operator Characteristic (ROC) Curve  to give sensitivity/specificity tradeoff.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int score: Genotype quality score
    :param int numTP: Roc score true positive numbers
    :param int numFP: Roc score false positive numbers
    :param int numFN: Roc score false negative numbers
    :param float precision: Precision of the GQ score
    :param float sensitivity: Sensitivity of the GQ score
    :param float fMeasure: FScore of the GQ score
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  score: int = None,  numTP: int = None,  numFP: int = None,  numFN: int = None,  precision: float = None,  sensitivity: float = None,  fMeasure: float = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.score: int = score or []
        self.numTP: int = numTP or []
        self.numFP: int = numFP or []
        self.numFN: int = numFN or []
        self.precision: float = precision or []
        self.sensitivity: float = sensitivity or []
        self.fMeasure: float = fMeasure or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Roc":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


  
    
    

class Quality(ModelBase):
    """ An experimental feature attribute that defines the quality of the feature in a quantitative way, such as a phred quality score ([SO:0001686](http://www.sequenceontology.org/browser/current_svn/term/SO:0001686)).:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: indel | snp | unknown
    :param 'CodeableConcept' standardSequence: Standard sequence for comparison
    :param int start: Start position of the sequence
    :param int end: End position of the sequence
    :param 'Quantity' score: Quality score for the comparison
    :param 'CodeableConcept' method: Method to get quality
    :param float truthTP: True positives from the perspective of the truth data
    :param float queryTP: True positives from the perspective of the query data
    :param float truthFN: False negatives
    :param float queryFP: False positives
    :param float gtFP: False positives where the non-REF alleles in the Truth and Query Call Sets match
    :param float precision: Precision of comparison
    :param float recall: Recall of comparison
    :param float fScore: F-score
    :param 'Roc' roc: Receiver Operator Characteristic (ROC) Curve
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  standardSequence: 'CodeableConcept' = None,  start: int = None,  end: int = None,  score: 'Quantity' = None,  method: 'CodeableConcept' = None,  truthTP: float = None,  queryTP: float = None,  truthFN: float = None,  queryFP: float = None,  gtFP: float = None,  precision: float = None,  recall: float = None,  fScore: float = None,  roc: 'Roc' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.standardSequence: 'CodeableConcept' = standardSequence 
        self.start: int = start 
        self.end: int = end 
        self.score: 'Quantity' = score 
        self.method: 'CodeableConcept' = method 
        self.truthTP: float = truthTP 
        self.queryTP: float = queryTP 
        self.truthFN: float = truthFN 
        self.queryFP: float = queryFP 
        self.gtFP: float = gtFP 
        self.precision: float = precision 
        self.recall: float = recall 
        self.fScore: float = fScore 
        self.roc: 'Roc' = roc 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Quality":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class Repository(ModelBase):
    """ Configurations of the external repository. The repository shall store target's observedSeq or records related with target's observedSeq.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: directlink | openapi | login | oauth | other
    :param str url: URI of the repository
    :param str name: Repository's name
    :param str datasetId: Id of the dataset that used to call for dataset in repository
    :param str variantsetId: Id of the variantset that used to call for variantset in repository
    :param str readsetId: Id of the read
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  url: str = None,  name: str = None,  datasetId: str = None,  variantsetId: str = None,  readsetId: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.url: str = url 
        self.name: str = name 
        self.datasetId: str = datasetId 
        self.variantsetId: str = variantsetId 
        self.readsetId: str = readsetId 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Repository":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
        
    
    

class Outer(ModelBase):
    """ Structural variant outer.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant outer start
    :param int end: Structural variant outer end
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  start: int = None,  end: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.start: int = start 
        self.end: int = end 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Outer":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


    
    

class Inner(ModelBase):
    """ Structural variant inner.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int start: Structural variant inner start
    :param int end: Structural variant inner end
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  start: int = None,  end: int = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.start: int = start 
        self.end: int = end 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Inner":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


  
    
    

class StructureVariant(ModelBase):
    """ Information about chromosome structure variation.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' variantType: Structural variant change type
    :param bool exact: Does the structural variant have base pair resolution breakpoints?
    :param int length: Structural variant length
    :param 'Outer' outer: Structural variant outer
    :param 'Inner' inner: Structural variant inner
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  variantType: 'CodeableConcept' = None,  exact: bool = None,  length: int = None,  outer: 'Outer' = None,  inner: 'Inner' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.variantType: 'CodeableConcept' = variantType 
        self.exact: bool = exact 
        self.length: int = length 
        self.outer: 'Outer' = outer 
        self.inner: 'Inner' = inner 
        

    @classmethod
    def from_dict(cls, data: dict) -> "StructureVariant":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance


class MolecularSequence(DomainResource):
    """ Raw data describing a biological sequence.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Unique ID for this particular sequence. This is a FHIR-defined id
    :param str type: aa | dna | rna
    :param int coordinateSystem: Base number of coordinate system (0 for 0-based numbering or coordinates, inclusive start, exclusive end, 1 for 1-based numbering, inclusive start, inclusive end)
    :param 'Reference' patient: Who and/or what this is about
    :param 'Reference' specimen: Specimen used for sequencing
    :param 'Reference' device: The method for sequencing
    :param 'Reference' performer: Who should be responsible for test result
    :param 'Quantity' quantity: The number of copies of the sequence of interest.  (RNASeq)
    :param 'ReferenceSeq' referenceSeq: A sequence used as reference
    :param list['Variant'] variant: Variant in sequence
    :param str observedSeq: Sequence that was observed
    :param list['Quality'] quality: An set of value as quality of sequence
    :param int readCoverage: Average number of reads representing a given nucleotide in the reconstructed sequence
    :param list['Repository'] repository: External repository which contains detailed report related with observedSeq in this resource
    :param list['Reference'] pointer: Pointer to next atomic sequence
    :param list['StructureVariant'] structureVariant: Structural variant
    """
    def __init__(self, resourceType: str = "MolecularSequence",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  type: str = None,  coordinateSystem: int = None,  patient: 'Reference' = None,  specimen: 'Reference' = None,  device: 'Reference' = None,  performer: 'Reference' = None,  quantity: 'Quantity' = None,  referenceSeq: 'ReferenceSeq' = None,  variant: list['Variant'] = None,  observedSeq: str = None,  quality: list['Quality'] = None,  readCoverage: int = None,  repository: list['Repository'] = None,  pointer: list['Reference'] = None,  structureVariant: list['StructureVariant'] = None, ):
        self.resourceType: str = resourceType or "MolecularSequence"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.type: str = type 
        self.coordinateSystem: int = coordinateSystem 
        self.patient: 'Reference' = patient 
        self.specimen: 'Reference' = specimen 
        self.device: 'Reference' = device 
        self.performer: 'Reference' = performer 
        self.quantity: 'Quantity' = quantity 
        self.referenceSeq: 'ReferenceSeq' = referenceSeq 
        self.variant: list['Variant'] = variant or []
        self.observedSeq: str = observedSeq 
        self.quality: list['Quality'] = quality or []
        self.readCoverage: int = readCoverage 
        self.repository: list['Repository'] = repository or []
        self.pointer: list['Reference'] = pointer or []
        self.structureVariant: list['StructureVariant'] = structureVariant or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "MolecularSequence":
        """Create a model instance from a dict. The instance is recursively
        created by importing the classes for complex fhir types."""
        instance = cls()
        for key, value in data.items():
            # if value is dict try to create complex type
            if isinstance(value, dict):
                class_name = key[0].upper() + key[1:]
                models_path = ".".join(cls.__module__.split(".")[:-1])
                import_path = f"{models_path}.{class_name}"
                try:
                    module = import_module(import_path)
                    model_class = getattr(module, class_name)
                except ModuleNotFoundError:
                    continue
                # Check if the class is a subclass of ModelBase
                if inspect.isclass(model_class) and issubclass(model_class, ModelBase):
                    # Recursively create an instance of the nested class
                    nested_instance = model_class.from_dict(value)
                    setattr(instance, key, nested_instance)
            # if value is list recursively create instances of the list items
            elif isinstance(value, list):
                setattr(
                    instance,
                    key,
                    [
                        cls.from_dict(item) if isinstance(item, dict) else item
                        for item in value
                    ],
                )
            # else set the value
            else:
                setattr(instance, key, value)

        return instance