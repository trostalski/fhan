"""
Generated class for DocumentReference. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Period import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class RelatesTo(Element):
    """ Relationships that this document has with other document references that already exist.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | transforms | signs | appends
    :param Reference target: Target of the relationship
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    
    code: str = None
    target: "Reference" = Reference()
    

    
    
@dataclass
class Content(Element):
    """ The document and format referenced. There may be multiple content element repetitions, each with a different format.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment attachment: Where to access the document
    :param Coding format: Format/content rules for the document
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    attachment: "Attachment" = Attachment()
    format: "Coding" = Coding()
    

    
    
@dataclass
class Context(Element):
    """ The clinical context in which the document was prepared.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference encounter: Context of the document  content
    :param CodeableConcept event: Main clinical acts documented
    :param Period period: Time of service that is being documented
    :param CodeableConcept facilityType: Kind of facility where patient was seen
    :param CodeableConcept practiceSetting: Additional details about where the content was created (e.g. clinical specialty)
    :param Reference sourcePatientInfo: Patient demographics from source
    :param Reference related: Related identifiers or resources
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    encounter: list[Reference] = Reference() 
    event: list[CodeableConcept] = CodeableConcept() 
    period: "Period" = Period()
    facilityType: "CodeableConcept" = CodeableConcept()
    practiceSetting: "CodeableConcept" = CodeableConcept()
    sourcePatientInfo: "Reference" = Reference()
    related: list[Reference] = Reference() 
    

@dataclass
class DocumentReference(ModelBase):
    """ A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier masterIdentifier: Master Version Specific Identifier
    :param Identifier identifier: Other identifiers for the document
    :param str status: current | superseded | entered-in-error
    :param str docStatus: preliminary | final | amended | entered-in-error
    :param CodeableConcept type: Kind of document (LOINC if possible)
    :param CodeableConcept category: Categorization of document
    :param Reference subject: Who/what is the subject of the document
    :param str date: When this document reference was created
    :param Reference author: Who and/or what authored the document
    :param Reference authenticator: Who/what authenticated the document
    :param Reference custodian: Organization which maintains the document
    :param RelatesTo relatesTo: Relationships to other documents
    :param str description: Human-readable description
    :param CodeableConcept securityLabel: Document security-tags
    :param Content content: Document referenced
    :param Context context: Clinical context of document
    """

    resourceType: str = "DocumentReference"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    masterIdentifier: "Identifier" = Identifier()
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    docStatus: str = None
    
    type: "CodeableConcept" = CodeableConcept()
    
    category: list[CodeableConcept] = CodeableConcept() 
    
    subject: "Reference" = Reference()
    
    date: str = None
    
    author: list[Reference] = Reference() 
    
    authenticator: "Reference" = Reference()
    
    custodian: "Reference" = Reference()
    
    relatesTo: list[RelatesTo] = RelatesTo() 
    
    description: str = None
    
    securityLabel: list[CodeableConcept] = CodeableConcept() 
    
    content: list[Content] = Content() 
    
    context: "Context" = Context()
    