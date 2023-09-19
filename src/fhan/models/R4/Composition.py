"""
Generated class for Composition. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Composition(ModelBase):
    """ A set of healthcare-related information that is assembled together into a single logical package that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. A Composition defines the structure and narrative content necessary for a document. However, a Composition alone does not constitute a document. Rather, the Composition must be the first entry in a Bundle where Bundle.type=document, and any other resources referenced from Composition must be included as subsequent entries in the Bundle (for example Patient, Practitioner, Encounter, etc.).
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Version-independent identifier for the Composition
    :param str status: preliminary | final | amended | entered-in-error
    :param CodeableConcept type: Kind of composition (LOINC if possible)
    :param CodeableConcept category: Categorization of Composition
    :param Reference subject: Who and/or what the composition is about
    :param Reference encounter: Context of the Composition
    :param str date: Composition editing time
    :param Reference author: Who and/or what authored the composition
    :param str title: Human Readable name/title
    :param str confidentiality: As defined by affinity domain
    :param BackboneElement attester: Attests to accuracy of composition
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str mode: personal | professional | legal | official
    :param str time: When the composition was attested
    :param Reference party: Who attested the composition
    :param Reference custodian: Organization which maintains the composition
    :param BackboneElement relatesTo: Relationships to other compositions/documents
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str code: replaces | transforms | signs | appends
    :param Identifier targetIdentifier: Target of the relationship
    :param Reference targetIdentifier: Target of the relationship
    :param BackboneElement event: The clinical service(s) being documented
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Code(s) that apply to the event being documented
    :param Period period: The period covered by the documentation
    :param Reference detail: The event(s) being documented
    :param BackboneElement section: Composition is broken into sections
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for section (e.g. for ToC)
    :param CodeableConcept code: Classification of section (recommended)
    :param Reference author: Who and/or what authored the section
    :param Reference focus: Who/what the section is about, when it is not about the subject of composition
    :param Narrative text: Text summary of the section, for human interpretation
    :param str mode: working | snapshot | changes
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
    
    identifier: "Identifier" = None
    
    status: str = None
    
    type: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    date: str = None
    
    author: "Reference" = None
    
    title: str = None
    
    confidentiality: str = None
    
    attester: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    mode: str = None
    
    time: str = None
    
    party: "Reference" = None
    
    custodian: "Reference" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: str = None
    
    targetIdentifier: "Identifier" = None
    
    targetIdentifier: "Reference" = None
    
    event: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    period: "Period" = None
    
    detail: "Reference" = None
    
    section: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    title: str = None
    
    code: "CodeableConcept" = None
    
    author: "Reference" = None
    
    focus: "Reference" = None
    
    text: "Narrative" = None
    
    mode: str = None
    
    orderedBy: "CodeableConcept" = None
    
    entry: "Reference" = None
    
    emptyReason: "CodeableConcept" = None
    
    section: "BackboneElement" = None
    