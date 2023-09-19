"""
Generated class for Observation. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Range import *
from fhan.models.generator_models import ModelBase


@dataclass
class Observation(ModelBase):
    """ FHIR Vital Signs Panel Profile
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for observation
    :param Reference basedOn: Fulfills plan, proposal or order
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
    :param CodeableConcept code: Vital Signs Panel
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Coding coding: Code defined by a terminology system
    :param Coding coding:VitalsPanelCode: Code defined by a terminology system
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
    :param CodeableConcept dataAbsentReason: Why the result is missing
    :param CodeableConcept interpretation: High, low, normal, etc.
    :param Annotation note: Comments about the observation
    :param CodeableConcept bodySite: Observed body part
    :param CodeableConcept method: How it was done
    :param Reference specimen: Specimen used for this observation
    :param Reference device: (Measurement) Device
    :param BackboneElement referenceRange: Provides guide for interpretation
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity low: Low Range, if relevant
    :param Quantity high: High Range, if relevant
    :param CodeableConcept type: Reference range qualifier
    :param CodeableConcept appliesTo: Reference range population
    :param Range age: Applicable age range, if relevant
    :param str text: Text based reference range in an observation
    :param Reference hasMember: Used when reporting vital signs panel components
    :param Reference derivedFrom: Related measurements the observation is made from
    :param BackboneElement component: Used when reporting systolic and diastolic blood pressure.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of component observation (code / type)
    :param Quantity valueQuantity: Vital Sign Value recorded with UCUM
    :param CodeableConcept valueQuantity: Vital Sign Value recorded with UCUM
    :param str valueQuantity: Vital Sign Value recorded with UCUM
    :param bool valueQuantity: Vital Sign Value recorded with UCUM
    :param int valueQuantity: Vital Sign Value recorded with UCUM
    :param Range valueQuantity: Vital Sign Value recorded with UCUM
    :param Ratio valueQuantity: Vital Sign Value recorded with UCUM
    :param SampledData valueQuantity: Vital Sign Value recorded with UCUM
    :param str valueQuantity: Vital Sign Value recorded with UCUM
    :param str valueQuantity: Vital Sign Value recorded with UCUM
    :param Period valueQuantity: Vital Sign Value recorded with UCUM
    :param CodeableConcept dataAbsentReason: Why the component result is missing
    :param CodeableConcept interpretation: High, low, normal, etc.
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
    
    basedOn: "Reference" = None
    
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
    
    coding:VitalsPanelCode: "Coding" = None
    
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
    
    dataAbsentReason: "CodeableConcept" = None
    
    interpretation: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    bodySite: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    referenceRange: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    low: "Quantity" = None
    
    high: "Quantity" = None
    
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
    
    dataAbsentReason: "CodeableConcept" = None
    
    interpretation: "CodeableConcept" = None
    
    referenceRange: "BackboneElement" = None
    