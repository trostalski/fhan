"""
Generated class for DocumentReference. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


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
    :param BackboneElement relatesTo: Relationships to other documents
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | transforms | signs | appends
    :param Reference target: Target of the relationship
    :param str description: Human-readable description
    :param CodeableConcept securityLabel: Document security-tags
    :param BackboneElement content: Document referenced
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment attachment: Where to access the document
    :param Coding format: Format/content rules for the document
    :param BackboneElement context: Clinical context of document
    :param str id: Unique id for inter-element referencing
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
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    masterIdentifier: "Identifier" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    docStatus: str = None
    
    type: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    date: str = None
    
    author: "Reference" = None
    
    authenticator: "Reference" = None
    
    custodian: "Reference" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    target: "Reference" = None
    
    description: str = None
    
    securityLabel: "CodeableConcept" = None
    
    content: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    attachment: "Attachment" = None
    
    format: "Coding" = None
    
    context: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    encounter: "Reference" = None
    
    event: "CodeableConcept" = None
    
    period: "Period" = None
    
    facilityType: "CodeableConcept" = None
    
    practiceSetting: "CodeableConcept" = None
    
    sourcePatientInfo: "Reference" = None
    
    related: "Reference" = None
    