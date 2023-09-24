"""
Generated class for DocumentReference. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Period import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Coding import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class RelatesTo(ModelBase):
    """ Relationships that this document has with other document references that already exist.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | transforms | signs | appends
    :param 'Reference' target: Target of the relationship
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  code: str = None,  target: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.code: str = code 
        self.target: 'Reference' = target 
        

    
    

class Content(ModelBase):
    """ The document and format referenced. There may be multiple content element repetitions, each with a different format.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Attachment' attachment: Where to access the document
    :param 'Coding' format: Format/content rules for the document
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  attachment: 'Attachment' = None,  format: 'Coding' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.attachment: 'Attachment' = attachment 
        self.format: 'Coding' = format 
        

    
    

class Context(ModelBase):
    """ The clinical context in which the document was prepared.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param list['Reference'] encounter: Context of the document  content
    :param list['CodeableConcept'] event: Main clinical acts documented
    :param 'Period' period: Time of service that is being documented
    :param 'CodeableConcept' facilityType: Kind of facility where patient was seen
    :param 'CodeableConcept' practiceSetting: Additional details about where the content was created (e.g. clinical specialty)
    :param 'Reference' sourcePatientInfo: Patient demographics from source
    :param list['Reference'] related: Related identifiers or resources
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  encounter: list['Reference'] = None,  event: list['CodeableConcept'] = None,  period: 'Period' = None,  facilityType: 'CodeableConcept' = None,  practiceSetting: 'CodeableConcept' = None,  sourcePatientInfo: 'Reference' = None,  related: list['Reference'] = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.encounter: list['Reference'] = encounter or []
        self.event: list['CodeableConcept'] = event or []
        self.period: 'Period' = period 
        self.facilityType: 'CodeableConcept' = facilityType 
        self.practiceSetting: 'CodeableConcept' = practiceSetting 
        self.sourcePatientInfo: 'Reference' = sourcePatientInfo 
        self.related: list['Reference'] = related or []
        

class DocumentReference(DomainResource):
    """ A reference to a document of any kind for any purpose. Provides metadata about the document so that the document can be discovered and managed. The scope of a document is any seralized object with a mime-type, so includes formal patient centric documents (CDA), cliical notes, scanned paper, and non-patient specific documents like policy text.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param 'Identifier' masterIdentifier: Master Version Specific Identifier
    :param list['Identifier'] identifier: Other identifiers for the document
    :param str status: current | superseded | entered-in-error
    :param str docStatus: preliminary | final | amended | entered-in-error
    :param 'CodeableConcept' type: Kind of document (LOINC if possible)
    :param list['CodeableConcept'] category: Categorization of document
    :param 'Reference' subject: Who/what is the subject of the document
    :param str date: When this document reference was created
    :param list['Reference'] author: Who and/or what authored the document
    :param 'Reference' authenticator: Who/what authenticated the document
    :param 'Reference' custodian: Organization which maintains the document
    :param list['RelatesTo'] relatesTo: Relationships to other documents
    :param str description: Human-readable description
    :param list['CodeableConcept'] securityLabel: Document security-tags
    :param list['Content'] content: Document referenced
    :param 'Context' context: Clinical context of document
    """
    def __init__(self, resourceType: str = "DocumentReference",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  masterIdentifier: 'Identifier' = None,  identifier: list['Identifier'] = None,  status: str = None,  docStatus: str = None,  type: 'CodeableConcept' = None,  category: list['CodeableConcept'] = None,  subject: 'Reference' = None,  date: str = None,  author: list['Reference'] = None,  authenticator: 'Reference' = None,  custodian: 'Reference' = None,  relatesTo: list['RelatesTo'] = None,  description: str = None,  securityLabel: list['CodeableConcept'] = None,  content: list['Content'] = None,  context: 'Context' = None, ):
        self.resourceType: str = resourceType or "DocumentReference"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.masterIdentifier: 'Identifier' = masterIdentifier 
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.docStatus: str = docStatus 
        self.type: 'CodeableConcept' = type 
        self.category: list['CodeableConcept'] = category or []
        self.subject: 'Reference' = subject 
        self.date: str = date 
        self.author: list['Reference'] = author or []
        self.authenticator: 'Reference' = authenticator 
        self.custodian: 'Reference' = custodian 
        self.relatesTo: list['RelatesTo'] = relatesTo or []
        self.description: str = description 
        self.securityLabel: list['CodeableConcept'] = securityLabel or []
        self.content: list['Content'] = content or []
        self.context: 'Context' = context 
        