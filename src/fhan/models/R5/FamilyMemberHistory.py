"""
Generated class for FamilyMemberHistory. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Age import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class FamilyMemberHistory:
    """ Significant health conditions for a person related to the patient relevant in the context of care for the patient.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External Id(s) for this record
    :param str instantiatesCanonical: Instantiates FHIR protocol or definition
    :param str instantiatesUri: Instantiates external protocol or definition
    :param str status: partial | completed | entered-in-error | health-unknown
    :param CodeableConcept dataAbsentReason: subject-unknown | withheld | unable-to-obtain | deferred
    :param Reference patient: Patient history is about
    :param str date: When history was recorded or last updated
    :param BackboneElement participant: Who or what participated in the activities related to the family member history and how they were involved
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: Type of involvement
    :param Reference actor: Who or what participated in the activities related to the family member history
    :param str name: The family member described
    :param CodeableConcept relationship: Relationship to the subject
    :param CodeableConcept sex: male | female | other | unknown
    :param Period bornPeriod: (approximate) date of birth
    :param str bornPeriod: (approximate) date of birth
    :param str bornPeriod: (approximate) date of birth
    :param Age ageAge: (approximate) age
    :param Range ageAge: (approximate) age
    :param str ageAge: (approximate) age
    :param bool estimatedAge: Age is estimated?
    :param bool deceasedboolean: Dead? How old/when?
    :param Age deceasedboolean: Dead? How old/when?
    :param Range deceasedboolean: Dead? How old/when?
    :param str deceasedboolean: Dead? How old/when?
    :param str deceasedboolean: Dead? How old/when?
    :param CodeableReference reason: Why was family member history performed?
    :param Annotation note: General note about related person
    :param BackboneElement condition: Condition that the related person had
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Condition suffered by relation
    :param CodeableConcept outcome: deceased | permanent disability | etc
    :param bool contributedToDeath: Whether the condition contributed to the cause of death
    :param Age onsetAge: When condition first manifested
    :param Range onsetAge: When condition first manifested
    :param Period onsetAge: When condition first manifested
    :param str onsetAge: When condition first manifested
    :param Annotation note: Extra information about condition
    :param BackboneElement procedure: Procedures that the related person had
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Procedures performed on the related person
    :param CodeableConcept outcome: What happened following the procedure
    :param bool contributedToDeath: Whether the procedure contributed to the cause of death
    :param Age performedAge: When the procedure was performed
    :param Range performedAge: When the procedure was performed
    :param Period performedAge: When the procedure was performed
    :param str performedAge: When the procedure was performed
    :param str performedAge: When the procedure was performed
    :param Annotation note: Extra information about the procedure
    
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
    
    instantiatesCanonical: str = None
    
    instantiatesUri: str = None
    
    status: str = None
    
    dataAbsentReason: "CodeableConcept" = None
    
    patient: "Reference" = None
    
    date: str = None
    
    participant: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    name: str = None
    
    relationship: "CodeableConcept" = None
    
    sex: "CodeableConcept" = None
    
    bornPeriod: "Period" = None
    
    bornPeriod: str = None
    
    bornPeriod: str = None
    
    ageAge: "Age" = None
    
    ageAge: "Range" = None
    
    ageAge: str = None
    
    estimatedAge: bool = None
    
    deceasedboolean: bool = None
    
    deceasedboolean: "Age" = None
    
    deceasedboolean: "Range" = None
    
    deceasedboolean: str = None
    
    deceasedboolean: str = None
    
    reason: "CodeableReference" = None
    
    note: "Annotation" = None
    
    condition: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    contributedToDeath: bool = None
    
    onsetAge: "Age" = None
    
    onsetAge: "Range" = None
    
    onsetAge: "Period" = None
    
    onsetAge: str = None
    
    note: "Annotation" = None
    
    procedure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    outcome: "CodeableConcept" = None
    
    contributedToDeath: bool = None
    
    performedAge: "Age" = None
    
    performedAge: "Range" = None
    
    performedAge: "Period" = None
    
    performedAge: str = None
    
    performedAge: str = None
    
    note: "Annotation" = None
    