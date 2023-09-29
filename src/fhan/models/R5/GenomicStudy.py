"""
Generated class for GenomicStudy. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class Input(BaseModel):
    """ Inputs for the analysis event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference file: File containing input data
    :param CodeableConcept type: Type of input data (e.g., BAM, CRAM, or FASTA)
    :param Identifier generatedByIdentifier: The analysis event or other GenomicStudy that generated this input file
    :param Reference generatedByReference: The analysis event or other GenomicStudy that generated this input file
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "file": {"class_name": "Reference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "generatedByIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "generatedByReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  file:  'Reference'  = None,  type:  'CodeableConcept'  = None,  generatedByIdentifier:  'Identifier'  = None,  generatedByReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.file = file 
        self.type = type 
        self.generatedByIdentifier = generatedByIdentifier 
        self.generatedByReference = generatedByReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "GenomicStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GenomicStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Output(BaseModel):
    """ Outputs for the analysis event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference file: File containing output data
    :param CodeableConcept type: Type of output data (e.g., VCF, MAF, or BAM)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "file": {"class_name": "Reference", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  file:  'Reference'  = None,  type:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.file = file 
        self.type = type 
        

    @classmethod
    def from_dict(cls, data: dict) -> "GenomicStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GenomicStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Performer(BaseModel):
    """ Performer for the analysis event.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference actor: The organization, healthcare professional, or others who participated in performing this analysis
    :param CodeableConcept role: Role of the actor for this analysis
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "actor": {"class_name": "Reference", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  actor:  'Reference'  = None,  role:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.actor = actor 
        self.role = role 
        

    @classmethod
    def from_dict(cls, data: dict) -> "GenomicStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GenomicStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Device(BaseModel):
    """ Devices used for the analysis (e.g., instruments, software), with settings and parameters.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference device: Device used for the analysis
    :param CodeableConcept function: Specific function for the device used for the analysis
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "device": {"class_name": "Reference", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  device:  'Reference'  = None,  function:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.device = device 
        self.function = function 
        

    @classmethod
    def from_dict(cls, data: dict) -> "GenomicStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GenomicStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Analysis(BaseModel):
    """ The details about a specific analysis that was performed in this GenomicStudy.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifiers for the analysis event
    :param CodeableConcept methodType: Type of the methods used in the analysis (e.g., FISH, Karyotyping, MSI)
    :param CodeableConcept changeType: Type of the genomic changes studied in the analysis (e.g., DNA, RNA, or AA change)
    :param CodeableConcept genomeBuild: Genome build that is used in this analysis
    :param str instantiatesCanonical: The defined protocol that describes the analysis
    :param str instantiatesUri: The URL pointing to an externally maintained protocol that describes the analysis
    :param str title: Name of the analysis event (human friendly)
    :param Reference focus: What the genomic analysis is about, when it is not about the subject of record
    :param Reference specimen: The specimen used in the analysis event
    :param str date: The date of the analysis event
    :param Annotation note: Any notes capture with the analysis event
    :param Reference protocolPerformed: The protocol that was performed for the analysis event
    :param Reference regionsStudied: The genomic regions to be studied in the analysis (BED file)
    :param Reference regionsCalled: Genomic regions actually called in the analysis event (BED file)
    :param Input input: Inputs for the analysis event
    :param Output output: Outputs for the analysis event
    :param Performer performer: Performer for the analysis event
    :param Device device: Devices used for the analysis (e.g., instruments, software), with settings and parameters
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "methodType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "changeType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "genomeBuild": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "focus": {"class_name": "Reference", "is_contained": False},
        
        
        "specimen": {"class_name": "Reference", "is_contained": False},
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "protocolPerformed": {"class_name": "Reference", "is_contained": False},
        
        
        "regionsStudied": {"class_name": "Reference", "is_contained": False},
        
        
        "regionsCalled": {"class_name": "Reference", "is_contained": False},
        
        
        "input": {"class_name": "Input", "is_contained": True},
        
        
        "output": {"class_name": "Output", "is_contained": True},
        
        
        "performer": {"class_name": "Performer", "is_contained": True},
        
        
        "device": {"class_name": "Device", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  methodType:  list['CodeableConcept']  = None,  changeType:  list['CodeableConcept']  = None,  genomeBuild:  'CodeableConcept'  = None,  instantiatesCanonical:  'str'  = None,  instantiatesUri:  'str'  = None,  title:  'str'  = None,  focus:  list['Reference']  = None,  specimen:  list['Reference']  = None,  date:  'str'  = None,  note:  list['Annotation']  = None,  protocolPerformed:  'Reference'  = None,  regionsStudied:  list['Reference']  = None,  regionsCalled:  list['Reference']  = None,  input:  list['Input']  = None,  output:  list['Output']  = None,  performer:  list['Performer']  = None,  device:  list['Device']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.methodType = methodType or []
        self.changeType = changeType or []
        self.genomeBuild = genomeBuild 
        self.instantiatesCanonical = instantiatesCanonical 
        self.instantiatesUri = instantiatesUri 
        self.title = title 
        self.focus = focus or []
        self.specimen = specimen or []
        self.date = date 
        self.note = note or []
        self.protocolPerformed = protocolPerformed 
        self.regionsStudied = regionsStudied or []
        self.regionsCalled = regionsCalled or []
        self.input = input or []
        self.output = output or []
        self.performer = performer or []
        self.device = device or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "GenomicStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GenomicStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class GenomicStudy(DomainResource):
    """ A set of analyses performed to analyze and generate genomic data.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifiers for this genomic study
    :param str status: registered | available | cancelled | entered-in-error | unknown
    :param CodeableConcept type: The type of the study (e.g., Familial variant segregation, Functional variation detection, or Gene expression profiling)
    :param Reference subject: The primary subject of the genomic study
    :param Reference encounter: The healthcare event with which this genomics study is associated
    :param str startDate: When the genomic study was started
    :param Reference basedOn: Event resources that the genomic study is based on
    :param Reference referrer: Healthcare professional who requested or referred the genomic study
    :param Reference interpreter: Healthcare professionals who interpreted the genomic study
    :param CodeableReference reason: Why the genomic study was performed
    :param str instantiatesCanonical: The defined protocol that describes the study
    :param str instantiatesUri: The URL pointing to an externally maintained protocol that describes the study
    :param Annotation note: Comments related to the genomic study
    :param str description: Description of the genomic study
    :param Analysis analysis: Genomic Analysis Event
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "encounter": {"class_name": "Reference", "is_contained": False},
        
        
        
        "basedOn": {"class_name": "Reference", "is_contained": False},
        
        
        "referrer": {"class_name": "Reference", "is_contained": False},
        
        
        "interpreter": {"class_name": "Reference", "is_contained": False},
        
        
        "reason": {"class_name": "CodeableReference", "is_contained": False},
        
        
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        
        "analysis": {"class_name": "Analysis", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  status:  'str'  = None,  type:  list['CodeableConcept']  = None,  subject:  'Reference'  = None,  encounter:  'Reference'  = None,  startDate:  'str'  = None,  basedOn:  list['Reference']  = None,  referrer:  'Reference'  = None,  interpreter:  list['Reference']  = None,  reason:  list['CodeableReference']  = None,  instantiatesCanonical:  'str'  = None,  instantiatesUri:  'str'  = None,  note:  list['Annotation']  = None,  description:  'str'  = None,  analysis:  list['Analysis']  = None, ):
        self.resourceType = resourceType or "GenomicStudy"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.status = status 
        self.type = type or []
        self.subject = subject 
        self.encounter = encounter 
        self.startDate = startDate 
        self.basedOn = basedOn or []
        self.referrer = referrer 
        self.interpreter = interpreter or []
        self.reason = reason or []
        self.instantiatesCanonical = instantiatesCanonical 
        self.instantiatesUri = instantiatesUri 
        self.note = note or []
        self.description = description 
        self.analysis = analysis or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "GenomicStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "GenomicStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()