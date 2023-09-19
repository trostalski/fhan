"""
Generated class for DocumentReference. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class DocumentReference:
    """ A reference to a document of any kind for any purpose. While the term “document” implies a more narrow focus, for this resource this “document” encompasses *any* serialized object with a mime-type, it includes formal patient-centric documents (CDA), clinical notes, scanned paper, non-patient specific documents like policy text, as well as a photo, video, or audio recording acquired or used in healthcare.  The DocumentReference resource provides metadata about the document so that the document can be discovered and managed.  The actual content may be inline base64 encoded data or provided by direct reference.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifiers for the document
    :param str version: An explicitly assigned identifer of a variation of the content in the DocumentReference
    :param Reference basedOn: Procedure that caused this media to be created
    :param str status: current | superseded | entered-in-error
    :param str docStatus: registered | partial | preliminary | final | amended | corrected | appended | cancelled | entered-in-error | deprecated | unknown
    :param CodeableConcept modality: Imaging modality used
    :param CodeableConcept type: Kind of document (LOINC if possible)
    :param CodeableConcept category: Categorization of document
    :param Reference subject: Who/what is the subject of the document
    :param Reference context: Context of the document content
    :param CodeableReference event: Main clinical acts documented
    :param CodeableReference bodySite: Body part included
    :param CodeableConcept facilityType: Kind of facility where patient was seen
    :param CodeableConcept practiceSetting: Additional details about where the content was created (e.g. clinical specialty)
    :param Period period: Time of service that is being documented
    :param str date: When this document reference was created
    :param Reference author: Who and/or what authored the document
    :param BackboneElement attester: Attests to accuracy of the document
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept mode: personal | professional | legal | official
    :param str time: When the document was attested
    :param Reference party: Who attested the document
    :param Reference custodian: Organization which maintains the document
    :param BackboneElement relatesTo: Relationships to other documents
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The relationship type with another document
    :param Reference target: Target of the relationship
    :param str description: Human-readable description
    :param CodeableConcept securityLabel: Document security-tags
    :param BackboneElement content: Document referenced
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Attachment attachment: Where to access the document
    :param BackboneElement profile: Content profile rules for the document
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Coding valueCoding: Code|uri|canonical
    :param str valueCoding: Code|uri|canonical
    :param str valueCoding: Code|uri|canonical
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    basedOn: "Reference" = None
    
    status: str = None
    
    docStatus: str = None
    
    modality: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    event: "CodeableReference" = None
    
    bodySite: "CodeableReference" = None
    
    facilityType: "CodeableConcept" = None
    
    practiceSetting: "CodeableConcept" = None
    
    period: "Period" = None
    
    date: str = None
    
    author: "Reference" = None
    
    attester: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: "CodeableConcept" = None
    
    time: str = None
    
    party: "Reference" = None
    
    custodian: "Reference" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    target: "Reference" = None
    
    description: str = None
    
    securityLabel: "CodeableConcept" = None
    
    content: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    attachment: "Attachment" = None
    
    profile: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    valueCoding: "Coding" = None
    
    valueCoding: str = None
    
    valueCoding: str = None
    