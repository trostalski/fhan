"""
Generated class for Observation. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.SampledData import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Range import *
from fhan.models.R5.Reference import *


@dataclass
class Observation:
    """ FHIR Oxygen Saturation Profile
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for observation
    :param str instantiatescanonical: Instantiates FHIR ObservationDefinition
    :param Reference instantiatescanonical: Instantiates FHIR ObservationDefinition
    :param Reference basedOn: Fulfills plan, proposal or order
    :param BackboneElement triggeredBy: Triggering observation(s)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference observation: Triggering observation
    :param str type: reflex | repeat | re-run
    :param str reason: Reason that the observation was triggered
    :param Reference partOf: Part of referenced event
    :param str status: registered | preliminary | final | amended +
    :param CodeableConcept category: Classification of  type of observation
    :param CodeableConcept category:VSCat: Classification of  type of observation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding coding: Code defined by a terminology system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str system: Identity of the terminology system
    :param str version: Version of the system - if relevant
    :param str code: Symbol in syntax defined by the system
    :param str display: Representation defined by the system
    :param bool userSelected: If this coding was chosen directly by the user
    :param str text: Plain text representation of the concept
    :param CodeableConcept code: Oxygen Saturation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding coding: Code defined by a terminology system
    :param Coding coding:OxygenSatCode: Code defined by a terminology system
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str system: Identity of the terminology system
    :param str version: Version of the system - if relevant
    :param str code: Symbol in syntax defined by the system
    :param str display: Representation defined by the system
    :param bool userSelected: If this coding was chosen directly by the user
    :param str text: Plain text representation of the concept
    :param Reference subject: Who and/or what the observation is about
    :param Reference focus: What the observation is about, when it is not about the subject of record
    :param Reference encounter: Healthcare event during which this observation is made
    :param str effectivedateTime: Often just a dateTime for Vital Signs
    :param Period effectivedateTime: Often just a dateTime for Vital Signs
    :param str issued: Date/Time this version was made available
    :param Reference performer: Who is responsible for the observation
    :param Quantity valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param CodeableConcept valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param str valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param bool valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param int valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param Range valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param Ratio valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param SampledData valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param str valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param str valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param Period valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param Attachment valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param Reference valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param Quantity valueQuantity:valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param float value: Numerical value (with implicit precision)
    :param str comparator: < | <= | >= | > | ad - how to understand the value
    :param str unit: Unit representation
    :param str system: System that defines coded unit form
    :param str code: Coded responses from the common UCUM units for vital signs value set.
    :param CodeableConcept dataAbsentReason: Why the result is missing
    :param CodeableConcept interpretation: High, low, normal, etc
    :param Annotation note: Comments about the observation
    :param CodeableConcept bodySite: Observed body part
    :param Reference bodyStructure: Observed body structure
    :param CodeableConcept method: How it was done
    :param Reference specimen: Specimen used for this observation
    :param Reference device: A reference to the device that generates the measurements or the device settings for the device
    :param BackboneElement referenceRange: Provides guide for interpretation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity low: Low Range, if relevant
    :param Quantity high: High Range, if relevant
    :param CodeableConcept normalValue: Normal value, if relevant
    :param CodeableConcept type: Reference range qualifier
    :param CodeableConcept appliesTo: Reference range population
    :param Range age: Applicable age range, if relevant
    :param str text: Text based reference range in an observation
    :param Reference hasMember: Used when reporting vital signs panel components
    :param Reference derivedFrom: Related resource from which the observation is made
    :param BackboneElement component: Used when reporting systolic and diastolic blood pressure.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of component observation (code / type)
    :param Quantity valueQuantity: Vital Sign Value
    :param CodeableConcept valueQuantity: Vital Sign Value
    :param str valueQuantity: Vital Sign Value
    :param bool valueQuantity: Vital Sign Value
    :param int valueQuantity: Vital Sign Value
    :param Range valueQuantity: Vital Sign Value
    :param Ratio valueQuantity: Vital Sign Value
    :param SampledData valueQuantity: Vital Sign Value
    :param str valueQuantity: Vital Sign Value
    :param str valueQuantity: Vital Sign Value
    :param Period valueQuantity: Vital Sign Value
    :param Attachment valueQuantity: Vital Sign Value
    :param Reference valueQuantity: Vital Sign Value
    :param Quantity valueQuantity:valueQuantity: Vital Sign Value recorded with UCUM
    :param CodeableConcept dataAbsentReason: Why the component result is missing
    :param CodeableConcept interpretation: High, low, normal, etc
    :param BackboneElement referenceRange: Provides guide for interpretation
    
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
    
    instantiatescanonical: str = None
    
    instantiatescanonical: "Reference" = None
    
    basedOn: "Reference" = None
    
    triggeredBy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    observation: "Reference" = None
    
    type: str = None
    
    reason: str = None
    
    partOf: "Reference" = None
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    category:VSCat: "CodeableConcept" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    coding: "Coding" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    system: str = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    userSelected: bool = None
    
    text: str = None
    
    code: "CodeableConcept" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    coding: "Coding" = None
    
    coding:OxygenSatCode: "Coding" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    system: str = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    userSelected: bool = None
    
    text: str = None
    
    subject: "Reference" = None
    
    focus: "Reference" = None
    
    encounter: "Reference" = None
    
    effectivedateTime: str = None
    
    effectivedateTime: "Period" = None
    
    issued: str = None
    
    performer: "Reference" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "CodeableConcept" = None
    
    valueQuantity: str = None
    
    valueQuantity: bool = None
    
    valueQuantity: int = None
    
    valueQuantity: "Range" = None
    
    valueQuantity: "Ratio" = None
    
    valueQuantity: "SampledData" = None
    
    valueQuantity: str = None
    
    valueQuantity: str = None
    
    valueQuantity: "Period" = None
    
    valueQuantity: "Attachment" = None
    
    valueQuantity: "Reference" = None
    
    valueQuantity:valueQuantity: "Quantity" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    value: float = None
    
    comparator: str = None
    
    unit: str = None
    
    system: str = None
    
    code: str = None
    
    dataAbsentReason: "CodeableConcept" = None
    
    interpretation: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    bodySite: "CodeableConcept" = None
    
    bodyStructure: "Reference" = None
    
    method: "CodeableConcept" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    referenceRange: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    low: "Quantity" = None
    
    high: "Quantity" = None
    
    normalValue: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    appliesTo: "CodeableConcept" = None
    
    age: "Range" = None
    
    text: str = None
    
    hasMember: "Reference" = None
    
    derivedFrom: "Reference" = None
    
    component: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    valueQuantity: "Quantity" = None
    
    valueQuantity: "CodeableConcept" = None
    
    valueQuantity: str = None
    
    valueQuantity: bool = None
    
    valueQuantity: int = None
    
    valueQuantity: "Range" = None
    
    valueQuantity: "Ratio" = None
    
    valueQuantity: "SampledData" = None
    
    valueQuantity: str = None
    
    valueQuantity: str = None
    
    valueQuantity: "Period" = None
    
    valueQuantity: "Attachment" = None
    
    valueQuantity: "Reference" = None
    
    valueQuantity:valueQuantity: "Quantity" = None
    
    dataAbsentReason: "CodeableConcept" = None
    
    interpretation: "CodeableConcept" = None
    
    referenceRange: "BackboneElement" = None
    