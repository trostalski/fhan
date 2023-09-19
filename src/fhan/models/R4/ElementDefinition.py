"""
Generated class for ElementDefinition. 
Time: 2023-09-19 20:21:26
"""
from dataclasses import dataclass
from fhan.models.R4.UsageContext import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Expression import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Money import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Period import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Range import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Count import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Extension import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Element import *
from fhan.models.R4.Age import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Distance import *
from fhan.models.R4.Address import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Meta import *


@dataclass
class ElementDefinition:
    """
    Base StructureDefinition for ElementDefinition Type: Captures constraints on each element within the resource, profile, or extension.
    """
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    path: str = None
    
    representation: str = None
    
    sliceName: str = None
    
    sliceIsConstraining: bool = None
    
    label: str = None
    
    code: "Coding" = None
    
    slicing: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    discriminator: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    path: str = None
    
    description: str = None
    
    ordered: bool = None
    
    rules: str = None
    
    short: str = None
    
    definition: str = None
    
    comment: str = None
    
    requirements: str = None
    
    alias: str = None
    
    min: int = None
    
    max: str = None
    
    base: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    path: str = None
    
    min: int = None
    
    max: str = None
    
    contentReference: str = None
    
    type: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    code: str = None
    
    profile: str = None
    
    targetProfile: str = None
    
    aggregation: str = None
    
    versioning: str = None
    
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
    
    meaningWhenMissing: str = None
    
    orderMeaning: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: bool = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: float = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: int = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: int = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: int = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: str = None
    
    fixedbase64Binary: "Address" = None
    
    fixedbase64Binary: "Age" = None
    
    fixedbase64Binary: "Annotation" = None
    
    fixedbase64Binary: "Attachment" = None
    
    fixedbase64Binary: "CodeableConcept" = None
    
    fixedbase64Binary: "Coding" = None
    
    fixedbase64Binary: "ContactPoint" = None
    
    fixedbase64Binary: "Count" = None
    
    fixedbase64Binary: "Distance" = None
    
    fixedbase64Binary: "Duration" = None
    
    fixedbase64Binary: "HumanName" = None
    
    fixedbase64Binary: "Identifier" = None
    
    fixedbase64Binary: "Money" = None
    
    fixedbase64Binary: "Period" = None
    
    fixedbase64Binary: "Quantity" = None
    
    fixedbase64Binary: "Range" = None
    
    fixedbase64Binary: "Ratio" = None
    
    fixedbase64Binary: "Reference" = None
    
    fixedbase64Binary: "SampledData" = None
    
    fixedbase64Binary: "Signature" = None
    
    fixedbase64Binary: "Timing" = None
    
    fixedbase64Binary: "ContactDetail" = None
    
    fixedbase64Binary: "Contributor" = None
    
    fixedbase64Binary: "DataRequirement" = None
    
    fixedbase64Binary: "Expression" = None
    
    fixedbase64Binary: "ParameterDefinition" = None
    
    fixedbase64Binary: "RelatedArtifact" = None
    
    fixedbase64Binary: "TriggerDefinition" = None
    
    fixedbase64Binary: "UsageContext" = None
    
    fixedbase64Binary: "Dosage" = None
    
    fixedbase64Binary: "Meta" = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: bool = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: float = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: int = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: int = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: int = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: str = None
    
    patternbase64Binary: "Address" = None
    
    patternbase64Binary: "Age" = None
    
    patternbase64Binary: "Annotation" = None
    
    patternbase64Binary: "Attachment" = None
    
    patternbase64Binary: "CodeableConcept" = None
    
    patternbase64Binary: "Coding" = None
    
    patternbase64Binary: "ContactPoint" = None
    
    patternbase64Binary: "Count" = None
    
    patternbase64Binary: "Distance" = None
    
    patternbase64Binary: "Duration" = None
    
    patternbase64Binary: "HumanName" = None
    
    patternbase64Binary: "Identifier" = None
    
    patternbase64Binary: "Money" = None
    
    patternbase64Binary: "Period" = None
    
    patternbase64Binary: "Quantity" = None
    
    patternbase64Binary: "Range" = None
    
    patternbase64Binary: "Ratio" = None
    
    patternbase64Binary: "Reference" = None
    
    patternbase64Binary: "SampledData" = None
    
    patternbase64Binary: "Signature" = None
    
    patternbase64Binary: "Timing" = None
    
    patternbase64Binary: "ContactDetail" = None
    
    patternbase64Binary: "Contributor" = None
    
    patternbase64Binary: "DataRequirement" = None
    
    patternbase64Binary: "Expression" = None
    
    patternbase64Binary: "ParameterDefinition" = None
    
    patternbase64Binary: "RelatedArtifact" = None
    
    patternbase64Binary: "TriggerDefinition" = None
    
    patternbase64Binary: "UsageContext" = None
    
    patternbase64Binary: "Dosage" = None
    
    patternbase64Binary: "Meta" = None
    
    example: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    label: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: bool = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: float = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: int = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: str = None
    
    valuebase64Binary: "Address" = None
    
    valuebase64Binary: "Age" = None
    
    valuebase64Binary: "Annotation" = None
    
    valuebase64Binary: "Attachment" = None
    
    valuebase64Binary: "CodeableConcept" = None
    
    valuebase64Binary: "Coding" = None
    
    valuebase64Binary: "ContactPoint" = None
    
    valuebase64Binary: "Count" = None
    
    valuebase64Binary: "Distance" = None
    
    valuebase64Binary: "Duration" = None
    
    valuebase64Binary: "HumanName" = None
    
    valuebase64Binary: "Identifier" = None
    
    valuebase64Binary: "Money" = None
    
    valuebase64Binary: "Period" = None
    
    valuebase64Binary: "Quantity" = None
    
    valuebase64Binary: "Range" = None
    
    valuebase64Binary: "Ratio" = None
    
    valuebase64Binary: "Reference" = None
    
    valuebase64Binary: "SampledData" = None
    
    valuebase64Binary: "Signature" = None
    
    valuebase64Binary: "Timing" = None
    
    valuebase64Binary: "ContactDetail" = None
    
    valuebase64Binary: "Contributor" = None
    
    valuebase64Binary: "DataRequirement" = None
    
    valuebase64Binary: "Expression" = None
    
    valuebase64Binary: "ParameterDefinition" = None
    
    valuebase64Binary: "RelatedArtifact" = None
    
    valuebase64Binary: "TriggerDefinition" = None
    
    valuebase64Binary: "UsageContext" = None
    
    valuebase64Binary: "Dosage" = None
    
    valuebase64Binary: "Meta" = None
    
    minValuedate: str = None
    
    minValuedate: str = None
    
    minValuedate: str = None
    
    minValuedate: str = None
    
    minValuedate: float = None
    
    minValuedate: int = None
    
    minValuedate: int = None
    
    minValuedate: int = None
    
    minValuedate: "Quantity" = None
    
    maxValuedate: str = None
    
    maxValuedate: str = None
    
    maxValuedate: str = None
    
    maxValuedate: str = None
    
    maxValuedate: float = None
    
    maxValuedate: int = None
    
    maxValuedate: int = None
    
    maxValuedate: int = None
    
    maxValuedate: "Quantity" = None
    
    maxLength: int = None
    
    condition: str = None
    
    constraint: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    key: str = None
    
    requirements: str = None
    
    severity: str = None
    
    human: str = None
    
    expression: str = None
    
    xpath: str = None
    
    source: str = None
    
    mustSupport: bool = None
    
    isModifier: bool = None
    
    isModifierReason: str = None
    
    isSummary: bool = None
    
    binding: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    strength: str = None
    
    description: str = None
    
    valueSet: str = None
    
    mapping: "Element" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    identity: str = None
    
    language: str = None
    
    map: str = None
    
    comment: str = None
    