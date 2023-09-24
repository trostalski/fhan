"""
Generated class for Observation. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Coding import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Range import *
from fhan.models.R4.Element import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class ReferenceRange(Element):
    """ Guidance on how to interpret the value by comparison to a normal or recommended range.  Multiple reference ranges are interpreted as an "OR".   In other words, to represent two distinct target populations, two `referenceRange` elements would be used.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Quantity low: Low Range, if relevant
    :param Quantity high: High Range, if relevant
    :param CodeableConcept type: Reference range qualifier
    :param CodeableConcept appliesTo: Reference range population
    :param Range age: Applicable age range, if relevant
    :param str text: Text based reference range in an observation
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    low:  "Quantity" = Quantity()
    
    high:  "Quantity" = Quantity()
    
    type:  "CodeableConcept" = CodeableConcept()
    
    appliesTo:  list["CodeableConcept"] = [CodeableConcept()]
    
    age:  "Range" = Range()
    
    text: str = None
    

    
    
@dataclass
class Component(Element):
    """ Used when reporting systolic and diastolic blood pressure.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: Type of component observation (code / type)
    :param Quantity valueQuantity: Vital Sign Value recorded with UCUM
    :param CodeableConcept dataAbsentReason: Why the component result is missing
    :param CodeableConcept interpretation: High, low, normal, etc.
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    code:  "CodeableConcept" = CodeableConcept()
    
    valueQuantity:  "Quantity" = Quantity()
    
    dataAbsentReason:  "CodeableConcept" = CodeableConcept()
    
    interpretation:  list["CodeableConcept"] = [CodeableConcept()]
    

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
    :param str effectiveDateTime: Often just a dateTime for Vital Signs
    :param str issued: Date/Time this version was made available
    :param Reference performer: Who is responsible for the observation
    :param Quantity valueQuantity: Vital Signs value are recorded using the Quantity data type. For supporting observations such as Cuff size could use other datatypes such as CodeableConcept.
    :param CodeableConcept dataAbsentReason: Why the result is missing
    :param CodeableConcept interpretation: High, low, normal, etc.
    :param Annotation note: Comments about the observation
    :param CodeableConcept bodySite: Observed body part
    :param CodeableConcept method: How it was done
    :param Reference specimen: Specimen used for this observation
    :param Reference device: (Measurement) Device
    :param ReferenceRange referenceRange: Provides guide for interpretation
    :param Reference hasMember: Used when reporting vital signs panel components
    :param Reference derivedFrom: Related measurements the observation is made from
    :param Component component: Used when reporting systolic and diastolic blood pressure.
    """

    resourceType: str = "Observation"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    basedOn: list["Reference"] = None
    
    partOf: list["Reference"] = None
    
    status: str = None
    
    category: list["CodeableConcept"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    coding: list["Coding"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    system: str = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    userSelected: bool = None
    
    text: str = None
    
    code: "CodeableConcept" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    coding: list["Coding"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    system: str = None
    
    version: str = None
    
    code: str = None
    
    display: str = None
    
    userSelected: bool = None
    
    text: str = None
    
    subject: "Reference" = None
    
    focus: list["Reference"] = None
    
    encounter: "Reference" = None
    
    effectiveDateTime: str = None
    
    issued: str = None
    
    performer: list["Reference"] = None
    
    valueQuantity: "Quantity" = None
    
    dataAbsentReason: "CodeableConcept" = None
    
    interpretation: list["CodeableConcept"] = None
    
    note: list["Annotation"] = None
    
    bodySite: "CodeableConcept" = None
    
    method: "CodeableConcept" = None
    
    specimen: "Reference" = None
    
    device: "Reference" = None
    
    referenceRange: list["ReferenceRange"] = None
    
    hasMember: list["Reference"] = None
    
    derivedFrom: list["Reference"] = None
    
    component: list["Component"] = None
    