"""
Generated class for Composition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class Composition:
    """ The Clinical Document profile constrains Composition to specify a clinical document (matching CDA). 

The base Composition is a general resource for compositions or documents about any kind of subject that might be encountered in healthcare including such things as guidelines, medicines, etc. A clinical document is focused on documents related to the provision of care process, where the subject is a patient, a group of patients, or a closely related concept. A clinical document has additional requirements around confidentiality that do not apply in the same way to other kinds of documents.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this Composition, represented as a URI (globally unique)
    :param Identifier identifier: Version-independent identifier for the Composition
    :param str version: An explicitly assigned identifer of a variation of the content in the Composition
    :param str status: registered | partial | preliminary | final | amended | corrected | appended | cancelled | entered-in-error | deprecated | unknown
    :param CodeableConcept type: Kind of composition (LOINC if possible)
    :param CodeableConcept category: Categorization of Composition
    :param Reference subject: Who and/or what the composition is about
    :param Reference encounter: Context of the Composition
    :param str date: Composition editing time
    :param UsageContext useContext: The context that the content is intended to support
    :param Reference author: Who and/or what authored the composition
    :param str name: Name for this Composition (computer friendly)
    :param str title: Human Readable name/title
    :param Annotation note: For any additional notes
    :param BackboneElement attester: Attests to accuracy of composition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept mode: personal | professional | legal | official
    :param str time: When the composition was attested
    :param Reference party: Who attested the composition
    :param Reference custodian: Organization which maintains the composition
    :param RelatedArtifact relatesTo: Relationships to other compositions/documents
    :param BackboneElement event: The clinical service(s) being documented
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Period period: The period covered by the documentation
    :param CodeableReference detail: The event(s) being documented, as code(s), reference(s), or both
    :param BackboneElement section: Composition is broken into sections
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for section (e.g. for ToC)
    :param CodeableConcept code: Classification of section (recommended)
    :param Reference author: Who and/or what authored the section
    :param Reference focus: Who/what the section is about, when it is not about the subject of composition
    :param Narrative text: Text summary of the section, for human interpretation
    :param CodeableConcept orderedBy: Order of section entries
    :param Reference entry: A reference to data that supports this section
    :param CodeableConcept emptyReason: Why the section is empty
    :param BackboneElement section: Composition is broken into sections
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    date: str = None
    
    useContext: "UsageContext" = None
    
    author: "Reference" = None
    
    name: str = None
    
    title: str = None
    
    note: "Annotation" = None
    
    attester: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: "CodeableConcept" = None
    
    time: str = None
    
    party: "Reference" = None
    
    custodian: "Reference" = None
    
    relatesTo: "RelatedArtifact" = None
    
    event: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    period: "Period" = None
    
    detail: "CodeableReference" = None
    
    section: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    code: "CodeableConcept" = None
    
    author: "Reference" = None
    
    focus: "Reference" = None
    
    text: "Narrative" = None
    
    orderedBy: "CodeableConcept" = None
    
    entry: "Reference" = None
    
    emptyReason: "CodeableConcept" = None
    
    section: "BackboneElement" = None
    