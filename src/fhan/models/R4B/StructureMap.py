"""
Generated class for StructureMap. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Signature import *
from fhan.models.R4B.Contributor import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Dosage import *
from fhan.models.R4B.SampledData import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Extension import *
from fhan.models.R4B.HumanName import *
from fhan.models.R4B.Duration import *
from fhan.models.R4B.ContactPoint import *
from fhan.models.R4B.RelatedArtifact import *
from fhan.models.R4B.TriggerDefinition import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.Count import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.DataRequirement import *
from fhan.models.R4B.Quantity import *
from fhan.models.R4B.Range import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Money import *
from fhan.models.R4B.ParameterDefinition import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.Distance import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Address import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Ratio import *
from fhan.models.R4B.Expression import *
from fhan.models.R4B.Reference import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Coding import *
from fhan.models.R4B.Timing import *
from fhan.models.R4B.Age import *
from fhan.models.R4B.Resource import *


@dataclass
class StructureMap:
    """
    A Map of relationships between 2 structures that can be used to transform data.
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
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    structure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    mode: str = None
    
    alias: str = None
    
    documentation: str = None
    
    import: str = None
    
    group: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    extends: str = None
    
    typeMode: str = None
    
    documentation: str = None
    
    input: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: str = None
    
    mode: str = None
    
    documentation: str = None
    
    rule: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    source: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
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
    
    target: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    context: str = None
    
    contextType: str = None
    
    element: str = None
    
    variable: str = None
    
    listMode: str = None
    
    listRuleId: str = None
    
    transform: str = None
    
    parameter: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    valueid: str = None
    
    valueid: str = None
    
    valueid: bool = None
    
    valueid: int = None
    
    valueid: float = None
    
    rule: "BackboneElement" = None
    
    dependent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    variable: str = None
    
    documentation: str = None
    