"""
Generated class for StructureMap. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.UsageContext import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Count import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Signature import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Address import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Money import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.Range import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Reference import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Expression import *
from fhan.models.R4.Distance import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Age import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase

@dataclass
class structure(Element):
    """ A structure definition used by this map. The structure definition may describe instances that are converted, or the instances that are produced.
    :param BackboneElement structure: Structure Definition used by this map
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: Canonical reference to structure definition
    :param str mode: source | queried | target | produced
    :param str alias: Name for type in this map
    :param str documentation: Documentation on use of structure
    """
    structure: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    mode: str = None
    
    alias: str = None
    
    documentation: str = None
    
@dataclass
class group(Element):
    """ Organizes the mapping into manageable chunks for human review/ease of maintenance.
    :param BackboneElement group: Named sections for reader convenience
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Human-readable label
    :param str extends: Another group that this group adds rules to
    :param str typeMode: none | types | type-and-types
    :param str documentation: Additional description/explanation for group
    :param BackboneElement input: Named instance provided when invoking the map
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name for this instance of data
    :param str type: Type for this instance of data
    :param str mode: source | target
    :param str documentation: Documentation for this instance of data
    :param BackboneElement rule: Transform Rule from source to target
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of the rule for internal references
    :param BackboneElement source: Source inputs to the mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValuebase64Binary: Default value if no value exists
    :param bool defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param float defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param Address defaultValuebase64Binary: Default value if no value exists
    :param Age defaultValuebase64Binary: Default value if no value exists
    :param Annotation defaultValuebase64Binary: Default value if no value exists
    :param Attachment defaultValuebase64Binary: Default value if no value exists
    :param CodeableConcept defaultValuebase64Binary: Default value if no value exists
    :param Coding defaultValuebase64Binary: Default value if no value exists
    :param ContactPoint defaultValuebase64Binary: Default value if no value exists
    :param Count defaultValuebase64Binary: Default value if no value exists
    :param Distance defaultValuebase64Binary: Default value if no value exists
    :param Duration defaultValuebase64Binary: Default value if no value exists
    :param HumanName defaultValuebase64Binary: Default value if no value exists
    :param Identifier defaultValuebase64Binary: Default value if no value exists
    :param Money defaultValuebase64Binary: Default value if no value exists
    :param Period defaultValuebase64Binary: Default value if no value exists
    :param Quantity defaultValuebase64Binary: Default value if no value exists
    :param Range defaultValuebase64Binary: Default value if no value exists
    :param Ratio defaultValuebase64Binary: Default value if no value exists
    :param Reference defaultValuebase64Binary: Default value if no value exists
    :param SampledData defaultValuebase64Binary: Default value if no value exists
    :param Signature defaultValuebase64Binary: Default value if no value exists
    :param Timing defaultValuebase64Binary: Default value if no value exists
    :param ContactDetail defaultValuebase64Binary: Default value if no value exists
    :param Contributor defaultValuebase64Binary: Default value if no value exists
    :param DataRequirement defaultValuebase64Binary: Default value if no value exists
    :param Expression defaultValuebase64Binary: Default value if no value exists
    :param ParameterDefinition defaultValuebase64Binary: Default value if no value exists
    :param RelatedArtifact defaultValuebase64Binary: Default value if no value exists
    :param TriggerDefinition defaultValuebase64Binary: Default value if no value exists
    :param UsageContext defaultValuebase64Binary: Default value if no value exists
    :param Dosage defaultValuebase64Binary: Default value if no value exists
    :param Meta defaultValuebase64Binary: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    :param BackboneElement target: Content to create because of this mapping rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param str contextType: type | variable
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | collate
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param BackboneElement parameter: Parameters to the transform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueid: Parameter value - variable or literal
    :param str valueid: Parameter value - variable or literal
    :param bool valueid: Parameter value - variable or literal
    :param int valueid: Parameter value - variable or literal
    :param float valueid: Parameter value - variable or literal
    :param BackboneElement rule: Transform Rule from source to target
    :param BackboneElement dependent: Which other rules to apply in the context of this rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param str variable: Variable to pass to the rule or group
    :param str documentation: Documentation for this instance of data
    """
    group: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    extends: str = None
    
    typeMode: str = None
    
    documentation: str = None
    
    input: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    type: str = None
    
    mode: str = None
    
    documentation: str = None
    
    rule: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    source: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    min: int = None
    
    max: str = None
    
    type: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: bool = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: float = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: "Address" = None
    
    defaultValuebase64Binary: "Age" = None
    
    defaultValuebase64Binary: "Annotation" = None
    
    defaultValuebase64Binary: "Attachment" = None
    
    defaultValuebase64Binary: "CodeableConcept" = None
    
    defaultValuebase64Binary: "Coding" = None
    
    defaultValuebase64Binary: "ContactPoint" = None
    
    defaultValuebase64Binary: "Count" = None
    
    defaultValuebase64Binary: "Distance" = None
    
    defaultValuebase64Binary: "Duration" = None
    
    defaultValuebase64Binary: "HumanName" = None
    
    defaultValuebase64Binary: "Identifier" = None
    
    defaultValuebase64Binary: "Money" = None
    
    defaultValuebase64Binary: "Period" = None
    
    defaultValuebase64Binary: "Quantity" = None
    
    defaultValuebase64Binary: "Range" = None
    
    defaultValuebase64Binary: "Ratio" = None
    
    defaultValuebase64Binary: "Reference" = None
    
    defaultValuebase64Binary: "SampledData" = None
    
    defaultValuebase64Binary: "Signature" = None
    
    defaultValuebase64Binary: "Timing" = None
    
    defaultValuebase64Binary: "ContactDetail" = None
    
    defaultValuebase64Binary: "Contributor" = None
    
    defaultValuebase64Binary: "DataRequirement" = None
    
    defaultValuebase64Binary: "Expression" = None
    
    defaultValuebase64Binary: "ParameterDefinition" = None
    
    defaultValuebase64Binary: "RelatedArtifact" = None
    
    defaultValuebase64Binary: "TriggerDefinition" = None
    
    defaultValuebase64Binary: "UsageContext" = None
    
    defaultValuebase64Binary: "Dosage" = None
    
    defaultValuebase64Binary: "Meta" = None
    
    element: str = None
    
    listMode: str = None
    
    variable: str = None
    
    condition: str = None
    
    check: str = None
    
    logMessage: str = None
    
    target: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    contextType: str = None
    
    element: str = None
    
    variable: str = None
    
    listMode: str = None
    
    listRuleId: str = None
    
    transform: str = None
    
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    valueid: str = None
    
    valueid: str = None
    
    valueid: bool = None
    
    valueid: int = None
    
    valueid: float = None
    
    rule: list["BackboneElement"] = None
    
    dependent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    variable: str = None
    
    documentation: str = None
    
@dataclass
class input(Element):
    """ A name assigned to an instance of data. The instance must be provided when the mapping is invoked.
    :param BackboneElement input: Named instance provided when invoking the map
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name for this instance of data
    :param str type: Type for this instance of data
    :param str mode: source | target
    :param str documentation: Documentation for this instance of data
    """
    input: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    type: str = None
    
    mode: str = None
    
    documentation: str = None
    
@dataclass
class rule(Element):
    """ Transform Rule from source to target.
    :param BackboneElement rule: Transform Rule from source to target
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of the rule for internal references
    :param BackboneElement source: Source inputs to the mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValuebase64Binary: Default value if no value exists
    :param bool defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param float defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param Address defaultValuebase64Binary: Default value if no value exists
    :param Age defaultValuebase64Binary: Default value if no value exists
    :param Annotation defaultValuebase64Binary: Default value if no value exists
    :param Attachment defaultValuebase64Binary: Default value if no value exists
    :param CodeableConcept defaultValuebase64Binary: Default value if no value exists
    :param Coding defaultValuebase64Binary: Default value if no value exists
    :param ContactPoint defaultValuebase64Binary: Default value if no value exists
    :param Count defaultValuebase64Binary: Default value if no value exists
    :param Distance defaultValuebase64Binary: Default value if no value exists
    :param Duration defaultValuebase64Binary: Default value if no value exists
    :param HumanName defaultValuebase64Binary: Default value if no value exists
    :param Identifier defaultValuebase64Binary: Default value if no value exists
    :param Money defaultValuebase64Binary: Default value if no value exists
    :param Period defaultValuebase64Binary: Default value if no value exists
    :param Quantity defaultValuebase64Binary: Default value if no value exists
    :param Range defaultValuebase64Binary: Default value if no value exists
    :param Ratio defaultValuebase64Binary: Default value if no value exists
    :param Reference defaultValuebase64Binary: Default value if no value exists
    :param SampledData defaultValuebase64Binary: Default value if no value exists
    :param Signature defaultValuebase64Binary: Default value if no value exists
    :param Timing defaultValuebase64Binary: Default value if no value exists
    :param ContactDetail defaultValuebase64Binary: Default value if no value exists
    :param Contributor defaultValuebase64Binary: Default value if no value exists
    :param DataRequirement defaultValuebase64Binary: Default value if no value exists
    :param Expression defaultValuebase64Binary: Default value if no value exists
    :param ParameterDefinition defaultValuebase64Binary: Default value if no value exists
    :param RelatedArtifact defaultValuebase64Binary: Default value if no value exists
    :param TriggerDefinition defaultValuebase64Binary: Default value if no value exists
    :param UsageContext defaultValuebase64Binary: Default value if no value exists
    :param Dosage defaultValuebase64Binary: Default value if no value exists
    :param Meta defaultValuebase64Binary: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    :param BackboneElement target: Content to create because of this mapping rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param str contextType: type | variable
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | collate
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param BackboneElement parameter: Parameters to the transform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueid: Parameter value - variable or literal
    :param str valueid: Parameter value - variable or literal
    :param bool valueid: Parameter value - variable or literal
    :param int valueid: Parameter value - variable or literal
    :param float valueid: Parameter value - variable or literal
    :param BackboneElement rule: Transform Rule from source to target
    :param BackboneElement dependent: Which other rules to apply in the context of this rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param str variable: Variable to pass to the rule or group
    :param str documentation: Documentation for this instance of data
    """
    rule: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    source: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    min: int = None
    
    max: str = None
    
    type: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: bool = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: float = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: "Address" = None
    
    defaultValuebase64Binary: "Age" = None
    
    defaultValuebase64Binary: "Annotation" = None
    
    defaultValuebase64Binary: "Attachment" = None
    
    defaultValuebase64Binary: "CodeableConcept" = None
    
    defaultValuebase64Binary: "Coding" = None
    
    defaultValuebase64Binary: "ContactPoint" = None
    
    defaultValuebase64Binary: "Count" = None
    
    defaultValuebase64Binary: "Distance" = None
    
    defaultValuebase64Binary: "Duration" = None
    
    defaultValuebase64Binary: "HumanName" = None
    
    defaultValuebase64Binary: "Identifier" = None
    
    defaultValuebase64Binary: "Money" = None
    
    defaultValuebase64Binary: "Period" = None
    
    defaultValuebase64Binary: "Quantity" = None
    
    defaultValuebase64Binary: "Range" = None
    
    defaultValuebase64Binary: "Ratio" = None
    
    defaultValuebase64Binary: "Reference" = None
    
    defaultValuebase64Binary: "SampledData" = None
    
    defaultValuebase64Binary: "Signature" = None
    
    defaultValuebase64Binary: "Timing" = None
    
    defaultValuebase64Binary: "ContactDetail" = None
    
    defaultValuebase64Binary: "Contributor" = None
    
    defaultValuebase64Binary: "DataRequirement" = None
    
    defaultValuebase64Binary: "Expression" = None
    
    defaultValuebase64Binary: "ParameterDefinition" = None
    
    defaultValuebase64Binary: "RelatedArtifact" = None
    
    defaultValuebase64Binary: "TriggerDefinition" = None
    
    defaultValuebase64Binary: "UsageContext" = None
    
    defaultValuebase64Binary: "Dosage" = None
    
    defaultValuebase64Binary: "Meta" = None
    
    element: str = None
    
    listMode: str = None
    
    variable: str = None
    
    condition: str = None
    
    check: str = None
    
    logMessage: str = None
    
    target: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    contextType: str = None
    
    element: str = None
    
    variable: str = None
    
    listMode: str = None
    
    listRuleId: str = None
    
    transform: str = None
    
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    valueid: str = None
    
    valueid: str = None
    
    valueid: bool = None
    
    valueid: int = None
    
    valueid: float = None
    
    rule: list["BackboneElement"] = None
    
    dependent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    variable: str = None
    
    documentation: str = None
    
@dataclass
class source(Element):
    """ Source inputs to the mapping.
    :param BackboneElement source: Source inputs to the mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValuebase64Binary: Default value if no value exists
    :param bool defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param float defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param Address defaultValuebase64Binary: Default value if no value exists
    :param Age defaultValuebase64Binary: Default value if no value exists
    :param Annotation defaultValuebase64Binary: Default value if no value exists
    :param Attachment defaultValuebase64Binary: Default value if no value exists
    :param CodeableConcept defaultValuebase64Binary: Default value if no value exists
    :param Coding defaultValuebase64Binary: Default value if no value exists
    :param ContactPoint defaultValuebase64Binary: Default value if no value exists
    :param Count defaultValuebase64Binary: Default value if no value exists
    :param Distance defaultValuebase64Binary: Default value if no value exists
    :param Duration defaultValuebase64Binary: Default value if no value exists
    :param HumanName defaultValuebase64Binary: Default value if no value exists
    :param Identifier defaultValuebase64Binary: Default value if no value exists
    :param Money defaultValuebase64Binary: Default value if no value exists
    :param Period defaultValuebase64Binary: Default value if no value exists
    :param Quantity defaultValuebase64Binary: Default value if no value exists
    :param Range defaultValuebase64Binary: Default value if no value exists
    :param Ratio defaultValuebase64Binary: Default value if no value exists
    :param Reference defaultValuebase64Binary: Default value if no value exists
    :param SampledData defaultValuebase64Binary: Default value if no value exists
    :param Signature defaultValuebase64Binary: Default value if no value exists
    :param Timing defaultValuebase64Binary: Default value if no value exists
    :param ContactDetail defaultValuebase64Binary: Default value if no value exists
    :param Contributor defaultValuebase64Binary: Default value if no value exists
    :param DataRequirement defaultValuebase64Binary: Default value if no value exists
    :param Expression defaultValuebase64Binary: Default value if no value exists
    :param ParameterDefinition defaultValuebase64Binary: Default value if no value exists
    :param RelatedArtifact defaultValuebase64Binary: Default value if no value exists
    :param TriggerDefinition defaultValuebase64Binary: Default value if no value exists
    :param UsageContext defaultValuebase64Binary: Default value if no value exists
    :param Dosage defaultValuebase64Binary: Default value if no value exists
    :param Meta defaultValuebase64Binary: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    """
    source: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    min: int = None
    
    max: str = None
    
    type: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: bool = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: float = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: "Address" = None
    
    defaultValuebase64Binary: "Age" = None
    
    defaultValuebase64Binary: "Annotation" = None
    
    defaultValuebase64Binary: "Attachment" = None
    
    defaultValuebase64Binary: "CodeableConcept" = None
    
    defaultValuebase64Binary: "Coding" = None
    
    defaultValuebase64Binary: "ContactPoint" = None
    
    defaultValuebase64Binary: "Count" = None
    
    defaultValuebase64Binary: "Distance" = None
    
    defaultValuebase64Binary: "Duration" = None
    
    defaultValuebase64Binary: "HumanName" = None
    
    defaultValuebase64Binary: "Identifier" = None
    
    defaultValuebase64Binary: "Money" = None
    
    defaultValuebase64Binary: "Period" = None
    
    defaultValuebase64Binary: "Quantity" = None
    
    defaultValuebase64Binary: "Range" = None
    
    defaultValuebase64Binary: "Ratio" = None
    
    defaultValuebase64Binary: "Reference" = None
    
    defaultValuebase64Binary: "SampledData" = None
    
    defaultValuebase64Binary: "Signature" = None
    
    defaultValuebase64Binary: "Timing" = None
    
    defaultValuebase64Binary: "ContactDetail" = None
    
    defaultValuebase64Binary: "Contributor" = None
    
    defaultValuebase64Binary: "DataRequirement" = None
    
    defaultValuebase64Binary: "Expression" = None
    
    defaultValuebase64Binary: "ParameterDefinition" = None
    
    defaultValuebase64Binary: "RelatedArtifact" = None
    
    defaultValuebase64Binary: "TriggerDefinition" = None
    
    defaultValuebase64Binary: "UsageContext" = None
    
    defaultValuebase64Binary: "Dosage" = None
    
    defaultValuebase64Binary: "Meta" = None
    
    element: str = None
    
    listMode: str = None
    
    variable: str = None
    
    condition: str = None
    
    check: str = None
    
    logMessage: str = None
    
@dataclass
class target(Element):
    """ Content to create because of this mapping rule.
    :param BackboneElement target: Content to create because of this mapping rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param str contextType: type | variable
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | collate
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param BackboneElement parameter: Parameters to the transform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueid: Parameter value - variable or literal
    :param str valueid: Parameter value - variable or literal
    :param bool valueid: Parameter value - variable or literal
    :param int valueid: Parameter value - variable or literal
    :param float valueid: Parameter value - variable or literal
    """
    target: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    contextType: str = None
    
    element: str = None
    
    variable: str = None
    
    listMode: str = None
    
    listRuleId: str = None
    
    transform: str = None
    
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    valueid: str = None
    
    valueid: str = None
    
    valueid: bool = None
    
    valueid: int = None
    
    valueid: float = None
    
@dataclass
class parameter(Element):
    """ Parameters to the transform.
    :param BackboneElement parameter: Parameters to the transform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueid: Parameter value - variable or literal
    :param str valueid: Parameter value - variable or literal
    :param bool valueid: Parameter value - variable or literal
    :param int valueid: Parameter value - variable or literal
    :param float valueid: Parameter value - variable or literal
    """
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    valueid: str = None
    
    valueid: str = None
    
    valueid: bool = None
    
    valueid: int = None
    
    valueid: float = None
    
@dataclass
class rule(Element):
    """ Transform Rule from source to target.
    :param BackboneElement rule: Transform Rule from source to target
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of the rule for internal references
    :param BackboneElement source: Source inputs to the mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValuebase64Binary: Default value if no value exists
    :param bool defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param float defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param Address defaultValuebase64Binary: Default value if no value exists
    :param Age defaultValuebase64Binary: Default value if no value exists
    :param Annotation defaultValuebase64Binary: Default value if no value exists
    :param Attachment defaultValuebase64Binary: Default value if no value exists
    :param CodeableConcept defaultValuebase64Binary: Default value if no value exists
    :param Coding defaultValuebase64Binary: Default value if no value exists
    :param ContactPoint defaultValuebase64Binary: Default value if no value exists
    :param Count defaultValuebase64Binary: Default value if no value exists
    :param Distance defaultValuebase64Binary: Default value if no value exists
    :param Duration defaultValuebase64Binary: Default value if no value exists
    :param HumanName defaultValuebase64Binary: Default value if no value exists
    :param Identifier defaultValuebase64Binary: Default value if no value exists
    :param Money defaultValuebase64Binary: Default value if no value exists
    :param Period defaultValuebase64Binary: Default value if no value exists
    :param Quantity defaultValuebase64Binary: Default value if no value exists
    :param Range defaultValuebase64Binary: Default value if no value exists
    :param Ratio defaultValuebase64Binary: Default value if no value exists
    :param Reference defaultValuebase64Binary: Default value if no value exists
    :param SampledData defaultValuebase64Binary: Default value if no value exists
    :param Signature defaultValuebase64Binary: Default value if no value exists
    :param Timing defaultValuebase64Binary: Default value if no value exists
    :param ContactDetail defaultValuebase64Binary: Default value if no value exists
    :param Contributor defaultValuebase64Binary: Default value if no value exists
    :param DataRequirement defaultValuebase64Binary: Default value if no value exists
    :param Expression defaultValuebase64Binary: Default value if no value exists
    :param ParameterDefinition defaultValuebase64Binary: Default value if no value exists
    :param RelatedArtifact defaultValuebase64Binary: Default value if no value exists
    :param TriggerDefinition defaultValuebase64Binary: Default value if no value exists
    :param UsageContext defaultValuebase64Binary: Default value if no value exists
    :param Dosage defaultValuebase64Binary: Default value if no value exists
    :param Meta defaultValuebase64Binary: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    :param BackboneElement target: Content to create because of this mapping rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param str contextType: type | variable
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | collate
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param BackboneElement parameter: Parameters to the transform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueid: Parameter value - variable or literal
    :param str valueid: Parameter value - variable or literal
    :param bool valueid: Parameter value - variable or literal
    :param int valueid: Parameter value - variable or literal
    :param float valueid: Parameter value - variable or literal
    :param BackboneElement rule: Transform Rule from source to target
    :param BackboneElement dependent: Which other rules to apply in the context of this rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param str variable: Variable to pass to the rule or group
    :param str documentation: Documentation for this instance of data
    """
    rule: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    source: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    min: int = None
    
    max: str = None
    
    type: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: bool = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: float = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: "Address" = None
    
    defaultValuebase64Binary: "Age" = None
    
    defaultValuebase64Binary: "Annotation" = None
    
    defaultValuebase64Binary: "Attachment" = None
    
    defaultValuebase64Binary: "CodeableConcept" = None
    
    defaultValuebase64Binary: "Coding" = None
    
    defaultValuebase64Binary: "ContactPoint" = None
    
    defaultValuebase64Binary: "Count" = None
    
    defaultValuebase64Binary: "Distance" = None
    
    defaultValuebase64Binary: "Duration" = None
    
    defaultValuebase64Binary: "HumanName" = None
    
    defaultValuebase64Binary: "Identifier" = None
    
    defaultValuebase64Binary: "Money" = None
    
    defaultValuebase64Binary: "Period" = None
    
    defaultValuebase64Binary: "Quantity" = None
    
    defaultValuebase64Binary: "Range" = None
    
    defaultValuebase64Binary: "Ratio" = None
    
    defaultValuebase64Binary: "Reference" = None
    
    defaultValuebase64Binary: "SampledData" = None
    
    defaultValuebase64Binary: "Signature" = None
    
    defaultValuebase64Binary: "Timing" = None
    
    defaultValuebase64Binary: "ContactDetail" = None
    
    defaultValuebase64Binary: "Contributor" = None
    
    defaultValuebase64Binary: "DataRequirement" = None
    
    defaultValuebase64Binary: "Expression" = None
    
    defaultValuebase64Binary: "ParameterDefinition" = None
    
    defaultValuebase64Binary: "RelatedArtifact" = None
    
    defaultValuebase64Binary: "TriggerDefinition" = None
    
    defaultValuebase64Binary: "UsageContext" = None
    
    defaultValuebase64Binary: "Dosage" = None
    
    defaultValuebase64Binary: "Meta" = None
    
    element: str = None
    
    listMode: str = None
    
    variable: str = None
    
    condition: str = None
    
    check: str = None
    
    logMessage: str = None
    
    target: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    contextType: str = None
    
    element: str = None
    
    variable: str = None
    
    listMode: str = None
    
    listRuleId: str = None
    
    transform: str = None
    
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    valueid: str = None
    
    valueid: str = None
    
    valueid: bool = None
    
    valueid: int = None
    
    valueid: float = None
    
    rule: list["BackboneElement"] = None
    
    dependent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    variable: str = None
    
    documentation: str = None
    
@dataclass
class dependent(Element):
    """ Which other rules to apply in the context of this rule.
    :param BackboneElement dependent: Which other rules to apply in the context of this rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param str variable: Variable to pass to the rule or group
    """
    dependent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    variable: str = None
    


@dataclass
class StructureMap(ModelBase):
    """ A Map of relationships between 2 structures that can be used to transform data.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this structure map, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the structure map
    :param str version: Business version of the structure map
    :param str name: Name for this structure map (computer friendly)
    :param str title: Name for this structure map (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the structure map
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for structure map (if applicable)
    :param str purpose: Why this structure map is defined
    :param str copyright: Use and/or publishing restrictions
    :param BackboneElement structure: Structure Definition used by this map
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str url: Canonical reference to structure definition
    :param str mode: source | queried | target | produced
    :param str alias: Name for type in this map
    :param str documentation: Documentation on use of structure
    :param str _import: Other maps used by this map (canonical URLs)
    :param BackboneElement group: Named sections for reader convenience
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Human-readable label
    :param str extends: Another group that this group adds rules to
    :param str typeMode: none | types | type-and-types
    :param str documentation: Additional description/explanation for group
    :param BackboneElement input: Named instance provided when invoking the map
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name for this instance of data
    :param str type: Type for this instance of data
    :param str mode: source | target
    :param str documentation: Documentation for this instance of data
    :param BackboneElement rule: Transform Rule from source to target
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of the rule for internal references
    :param BackboneElement source: Source inputs to the mapping
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param int min: Specified minimum cardinality
    :param str max: Specified maximum cardinality (number or *)
    :param str type: Rule only applies if source has this type
    :param str defaultValuebase64Binary: Default value if no value exists
    :param bool defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param float defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param int defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param str defaultValuebase64Binary: Default value if no value exists
    :param Address defaultValuebase64Binary: Default value if no value exists
    :param Age defaultValuebase64Binary: Default value if no value exists
    :param Annotation defaultValuebase64Binary: Default value if no value exists
    :param Attachment defaultValuebase64Binary: Default value if no value exists
    :param CodeableConcept defaultValuebase64Binary: Default value if no value exists
    :param Coding defaultValuebase64Binary: Default value if no value exists
    :param ContactPoint defaultValuebase64Binary: Default value if no value exists
    :param Count defaultValuebase64Binary: Default value if no value exists
    :param Distance defaultValuebase64Binary: Default value if no value exists
    :param Duration defaultValuebase64Binary: Default value if no value exists
    :param HumanName defaultValuebase64Binary: Default value if no value exists
    :param Identifier defaultValuebase64Binary: Default value if no value exists
    :param Money defaultValuebase64Binary: Default value if no value exists
    :param Period defaultValuebase64Binary: Default value if no value exists
    :param Quantity defaultValuebase64Binary: Default value if no value exists
    :param Range defaultValuebase64Binary: Default value if no value exists
    :param Ratio defaultValuebase64Binary: Default value if no value exists
    :param Reference defaultValuebase64Binary: Default value if no value exists
    :param SampledData defaultValuebase64Binary: Default value if no value exists
    :param Signature defaultValuebase64Binary: Default value if no value exists
    :param Timing defaultValuebase64Binary: Default value if no value exists
    :param ContactDetail defaultValuebase64Binary: Default value if no value exists
    :param Contributor defaultValuebase64Binary: Default value if no value exists
    :param DataRequirement defaultValuebase64Binary: Default value if no value exists
    :param Expression defaultValuebase64Binary: Default value if no value exists
    :param ParameterDefinition defaultValuebase64Binary: Default value if no value exists
    :param RelatedArtifact defaultValuebase64Binary: Default value if no value exists
    :param TriggerDefinition defaultValuebase64Binary: Default value if no value exists
    :param UsageContext defaultValuebase64Binary: Default value if no value exists
    :param Dosage defaultValuebase64Binary: Default value if no value exists
    :param Meta defaultValuebase64Binary: Default value if no value exists
    :param str element: Optional field for this source
    :param str listMode: first | not_first | last | not_last | only_one
    :param str variable: Named context for field, if a field is specified
    :param str condition: FHIRPath expression  - must be true or the rule does not apply
    :param str check: FHIRPath expression  - must be true or the mapping engine throws an error instead of completing
    :param str logMessage: Message to put in log if source exists (FHIRPath)
    :param BackboneElement target: Content to create because of this mapping rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str context: Type or variable this rule applies to
    :param str contextType: type | variable
    :param str element: Field to create in the context
    :param str variable: Named context for field, if desired, and a field is specified
    :param str listMode: first | share | last | collate
    :param str listRuleId: Internal rule reference for shared list items
    :param str transform: create | copy +
    :param BackboneElement parameter: Parameters to the transform
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str valueid: Parameter value - variable or literal
    :param str valueid: Parameter value - variable or literal
    :param bool valueid: Parameter value - variable or literal
    :param int valueid: Parameter value - variable or literal
    :param float valueid: Parameter value - variable or literal
    :param BackboneElement rule: Transform Rule from source to target
    :param BackboneElement dependent: Which other rules to apply in the context of this rule
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of a rule or group to apply
    :param str variable: Variable to pass to the rule or group
    :param str documentation: Documentation for this instance of data
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    identifier: list["Identifier"] = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: list["ContactDetail"] = None
    
    description: str = None
    
    useContext: list["UsageContext"] = None
    
    jurisdiction: list["CodeableConcept"] = None
    
    purpose: str = None
    
    copyright: str = None
    
    structure: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    url: str = None
    
    mode: str = None
    
    alias: str = None
    
    documentation: str = None
    
    _import: str = None
    
    group: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    extends: str = None
    
    typeMode: str = None
    
    documentation: str = None
    
    input: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    type: str = None
    
    mode: str = None
    
    documentation: str = None
    
    rule: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    source: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    min: int = None
    
    max: str = None
    
    type: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: bool = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: float = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: int = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: str = None
    
    defaultValuebase64Binary: "Address" = None
    
    defaultValuebase64Binary: "Age" = None
    
    defaultValuebase64Binary: "Annotation" = None
    
    defaultValuebase64Binary: "Attachment" = None
    
    defaultValuebase64Binary: "CodeableConcept" = None
    
    defaultValuebase64Binary: "Coding" = None
    
    defaultValuebase64Binary: "ContactPoint" = None
    
    defaultValuebase64Binary: "Count" = None
    
    defaultValuebase64Binary: "Distance" = None
    
    defaultValuebase64Binary: "Duration" = None
    
    defaultValuebase64Binary: "HumanName" = None
    
    defaultValuebase64Binary: "Identifier" = None
    
    defaultValuebase64Binary: "Money" = None
    
    defaultValuebase64Binary: "Period" = None
    
    defaultValuebase64Binary: "Quantity" = None
    
    defaultValuebase64Binary: "Range" = None
    
    defaultValuebase64Binary: "Ratio" = None
    
    defaultValuebase64Binary: "Reference" = None
    
    defaultValuebase64Binary: "SampledData" = None
    
    defaultValuebase64Binary: "Signature" = None
    
    defaultValuebase64Binary: "Timing" = None
    
    defaultValuebase64Binary: "ContactDetail" = None
    
    defaultValuebase64Binary: "Contributor" = None
    
    defaultValuebase64Binary: "DataRequirement" = None
    
    defaultValuebase64Binary: "Expression" = None
    
    defaultValuebase64Binary: "ParameterDefinition" = None
    
    defaultValuebase64Binary: "RelatedArtifact" = None
    
    defaultValuebase64Binary: "TriggerDefinition" = None
    
    defaultValuebase64Binary: "UsageContext" = None
    
    defaultValuebase64Binary: "Dosage" = None
    
    defaultValuebase64Binary: "Meta" = None
    
    element: str = None
    
    listMode: str = None
    
    variable: str = None
    
    condition: str = None
    
    check: str = None
    
    logMessage: str = None
    
    target: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    context: str = None
    
    contextType: str = None
    
    element: str = None
    
    variable: str = None
    
    listMode: str = None
    
    listRuleId: str = None
    
    transform: str = None
    
    parameter: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    valueid: str = None
    
    valueid: str = None
    
    valueid: bool = None
    
    valueid: int = None
    
    valueid: float = None
    
    rule: list["BackboneElement"] = None
    
    dependent: list["BackboneElement"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    name: str = None
    
    variable: str = None
    
    documentation: str = None
    