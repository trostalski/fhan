"""
Generated class for ElementDefinition. 
Time: 2023-09-20 10:09:03
"""
from dataclasses import dataclass

from fhan.models.R4.UsageContext import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Count import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Signature import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Address import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Money import *
from fhan.models.R4.Coding import *
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
from fhan.models.R4.Age import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Element import *




@dataclass
class ElementDefinition(Element):
    """ Base StructureDefinition for ElementDefinition Type: Captures constraints on each element within the resource, profile, or extension.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: Path of the element in the hierarchy of elements
    :param str representation: xmlAttr | xmlText | typeAttr | cdaText | xhtml
    :param str sliceName: Name for this particular element (in a set of slices)
    :param bool sliceIsConstraining: If this slice definition constrains an inherited slice definition (or not)
    :param str label: Name for element to display with or prompt for element
    :param Coding code: Corresponding codes in terminologies
    :param Element slicing: This element is sliced - slices follow
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Element discriminator: Element values that are used to distinguish the slices
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: value | exists | pattern | type | profile
    :param str path: Path to element value
    :param str description: Text description of how slicing works (or not)
    :param bool ordered: If elements must be in same order as slices
    :param str rules: closed | open | openAtEnd
    :param str short: Concise definition for space-constrained presentation
    :param str definition: Full formal definition as narrative text
    :param str comment: Comments about the use of this element
    :param str requirements: Why this resource has been created
    :param str alias: Other names
    :param int min: Minimum Cardinality
    :param str max: Maximum Cardinality (a number or *)
    :param Element base: Base definition information for tools
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str path: Path that identifies the base element
    :param int min: Min cardinality of the base element
    :param str max: Max cardinality of the base element
    :param str contentReference: Reference to definition of content for the element
    :param Element type: Data type and Profile for this element
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str code: Data type or Resource (reference to definition)
    :param str profile: Profiles (StructureDefinition or IG) - one must apply
    :param str targetProfile: Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    :param str aggregation: contained | referenced | bundled - how aggregated
    :param str versioning: either | independent | specific
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param bool defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param float defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param int defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param int defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param int defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param str defaultValuebase64Binary: Specified value if missing from instance
    :param Address defaultValuebase64Binary: Specified value if missing from instance
    :param Age defaultValuebase64Binary: Specified value if missing from instance
    :param Annotation defaultValuebase64Binary: Specified value if missing from instance
    :param Attachment defaultValuebase64Binary: Specified value if missing from instance
    :param CodeableConcept defaultValuebase64Binary: Specified value if missing from instance
    :param Coding defaultValuebase64Binary: Specified value if missing from instance
    :param ContactPoint defaultValuebase64Binary: Specified value if missing from instance
    :param Count defaultValuebase64Binary: Specified value if missing from instance
    :param Distance defaultValuebase64Binary: Specified value if missing from instance
    :param Duration defaultValuebase64Binary: Specified value if missing from instance
    :param HumanName defaultValuebase64Binary: Specified value if missing from instance
    :param Identifier defaultValuebase64Binary: Specified value if missing from instance
    :param Money defaultValuebase64Binary: Specified value if missing from instance
    :param Period defaultValuebase64Binary: Specified value if missing from instance
    :param Quantity defaultValuebase64Binary: Specified value if missing from instance
    :param Range defaultValuebase64Binary: Specified value if missing from instance
    :param Ratio defaultValuebase64Binary: Specified value if missing from instance
    :param Reference defaultValuebase64Binary: Specified value if missing from instance
    :param SampledData defaultValuebase64Binary: Specified value if missing from instance
    :param Signature defaultValuebase64Binary: Specified value if missing from instance
    :param Timing defaultValuebase64Binary: Specified value if missing from instance
    :param ContactDetail defaultValuebase64Binary: Specified value if missing from instance
    :param Contributor defaultValuebase64Binary: Specified value if missing from instance
    :param DataRequirement defaultValuebase64Binary: Specified value if missing from instance
    :param Expression defaultValuebase64Binary: Specified value if missing from instance
    :param ParameterDefinition defaultValuebase64Binary: Specified value if missing from instance
    :param RelatedArtifact defaultValuebase64Binary: Specified value if missing from instance
    :param TriggerDefinition defaultValuebase64Binary: Specified value if missing from instance
    :param UsageContext defaultValuebase64Binary: Specified value if missing from instance
    :param Dosage defaultValuebase64Binary: Specified value if missing from instance
    :param Meta defaultValuebase64Binary: Specified value if missing from instance
    :param str meaningWhenMissing: Implicit meaning when this element is missing
    :param str orderMeaning: What the order of the elements means
    :param str fixedbase64Binary: Value must be exactly this
    :param bool fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param float fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param int fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param int fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param int fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param str fixedbase64Binary: Value must be exactly this
    :param Address fixedbase64Binary: Value must be exactly this
    :param Age fixedbase64Binary: Value must be exactly this
    :param Annotation fixedbase64Binary: Value must be exactly this
    :param Attachment fixedbase64Binary: Value must be exactly this
    :param CodeableConcept fixedbase64Binary: Value must be exactly this
    :param Coding fixedbase64Binary: Value must be exactly this
    :param ContactPoint fixedbase64Binary: Value must be exactly this
    :param Count fixedbase64Binary: Value must be exactly this
    :param Distance fixedbase64Binary: Value must be exactly this
    :param Duration fixedbase64Binary: Value must be exactly this
    :param HumanName fixedbase64Binary: Value must be exactly this
    :param Identifier fixedbase64Binary: Value must be exactly this
    :param Money fixedbase64Binary: Value must be exactly this
    :param Period fixedbase64Binary: Value must be exactly this
    :param Quantity fixedbase64Binary: Value must be exactly this
    :param Range fixedbase64Binary: Value must be exactly this
    :param Ratio fixedbase64Binary: Value must be exactly this
    :param Reference fixedbase64Binary: Value must be exactly this
    :param SampledData fixedbase64Binary: Value must be exactly this
    :param Signature fixedbase64Binary: Value must be exactly this
    :param Timing fixedbase64Binary: Value must be exactly this
    :param ContactDetail fixedbase64Binary: Value must be exactly this
    :param Contributor fixedbase64Binary: Value must be exactly this
    :param DataRequirement fixedbase64Binary: Value must be exactly this
    :param Expression fixedbase64Binary: Value must be exactly this
    :param ParameterDefinition fixedbase64Binary: Value must be exactly this
    :param RelatedArtifact fixedbase64Binary: Value must be exactly this
    :param TriggerDefinition fixedbase64Binary: Value must be exactly this
    :param UsageContext fixedbase64Binary: Value must be exactly this
    :param Dosage fixedbase64Binary: Value must be exactly this
    :param Meta fixedbase64Binary: Value must be exactly this
    :param str patternbase64Binary: Value must have at least these property values
    :param bool patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param float patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param int patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param int patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param int patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param str patternbase64Binary: Value must have at least these property values
    :param Address patternbase64Binary: Value must have at least these property values
    :param Age patternbase64Binary: Value must have at least these property values
    :param Annotation patternbase64Binary: Value must have at least these property values
    :param Attachment patternbase64Binary: Value must have at least these property values
    :param CodeableConcept patternbase64Binary: Value must have at least these property values
    :param Coding patternbase64Binary: Value must have at least these property values
    :param ContactPoint patternbase64Binary: Value must have at least these property values
    :param Count patternbase64Binary: Value must have at least these property values
    :param Distance patternbase64Binary: Value must have at least these property values
    :param Duration patternbase64Binary: Value must have at least these property values
    :param HumanName patternbase64Binary: Value must have at least these property values
    :param Identifier patternbase64Binary: Value must have at least these property values
    :param Money patternbase64Binary: Value must have at least these property values
    :param Period patternbase64Binary: Value must have at least these property values
    :param Quantity patternbase64Binary: Value must have at least these property values
    :param Range patternbase64Binary: Value must have at least these property values
    :param Ratio patternbase64Binary: Value must have at least these property values
    :param Reference patternbase64Binary: Value must have at least these property values
    :param SampledData patternbase64Binary: Value must have at least these property values
    :param Signature patternbase64Binary: Value must have at least these property values
    :param Timing patternbase64Binary: Value must have at least these property values
    :param ContactDetail patternbase64Binary: Value must have at least these property values
    :param Contributor patternbase64Binary: Value must have at least these property values
    :param DataRequirement patternbase64Binary: Value must have at least these property values
    :param Expression patternbase64Binary: Value must have at least these property values
    :param ParameterDefinition patternbase64Binary: Value must have at least these property values
    :param RelatedArtifact patternbase64Binary: Value must have at least these property values
    :param TriggerDefinition patternbase64Binary: Value must have at least these property values
    :param UsageContext patternbase64Binary: Value must have at least these property values
    :param Dosage patternbase64Binary: Value must have at least these property values
    :param Meta patternbase64Binary: Value must have at least these property values
    :param Element example: Example value (as defined for type)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str label: Describes the purpose of this example
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param bool valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param float valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param int valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param int valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param int valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param str valuebase64Binary: Value of Example (one of allowed types)
    :param Address valuebase64Binary: Value of Example (one of allowed types)
    :param Age valuebase64Binary: Value of Example (one of allowed types)
    :param Annotation valuebase64Binary: Value of Example (one of allowed types)
    :param Attachment valuebase64Binary: Value of Example (one of allowed types)
    :param CodeableConcept valuebase64Binary: Value of Example (one of allowed types)
    :param Coding valuebase64Binary: Value of Example (one of allowed types)
    :param ContactPoint valuebase64Binary: Value of Example (one of allowed types)
    :param Count valuebase64Binary: Value of Example (one of allowed types)
    :param Distance valuebase64Binary: Value of Example (one of allowed types)
    :param Duration valuebase64Binary: Value of Example (one of allowed types)
    :param HumanName valuebase64Binary: Value of Example (one of allowed types)
    :param Identifier valuebase64Binary: Value of Example (one of allowed types)
    :param Money valuebase64Binary: Value of Example (one of allowed types)
    :param Period valuebase64Binary: Value of Example (one of allowed types)
    :param Quantity valuebase64Binary: Value of Example (one of allowed types)
    :param Range valuebase64Binary: Value of Example (one of allowed types)
    :param Ratio valuebase64Binary: Value of Example (one of allowed types)
    :param Reference valuebase64Binary: Value of Example (one of allowed types)
    :param SampledData valuebase64Binary: Value of Example (one of allowed types)
    :param Signature valuebase64Binary: Value of Example (one of allowed types)
    :param Timing valuebase64Binary: Value of Example (one of allowed types)
    :param ContactDetail valuebase64Binary: Value of Example (one of allowed types)
    :param Contributor valuebase64Binary: Value of Example (one of allowed types)
    :param DataRequirement valuebase64Binary: Value of Example (one of allowed types)
    :param Expression valuebase64Binary: Value of Example (one of allowed types)
    :param ParameterDefinition valuebase64Binary: Value of Example (one of allowed types)
    :param RelatedArtifact valuebase64Binary: Value of Example (one of allowed types)
    :param TriggerDefinition valuebase64Binary: Value of Example (one of allowed types)
    :param UsageContext valuebase64Binary: Value of Example (one of allowed types)
    :param Dosage valuebase64Binary: Value of Example (one of allowed types)
    :param Meta valuebase64Binary: Value of Example (one of allowed types)
    :param str minValuedate: Minimum Allowed Value (for some types)
    :param str minValuedate: Minimum Allowed Value (for some types)
    :param str minValuedate: Minimum Allowed Value (for some types)
    :param str minValuedate: Minimum Allowed Value (for some types)
    :param float minValuedate: Minimum Allowed Value (for some types)
    :param int minValuedate: Minimum Allowed Value (for some types)
    :param int minValuedate: Minimum Allowed Value (for some types)
    :param int minValuedate: Minimum Allowed Value (for some types)
    :param Quantity minValuedate: Minimum Allowed Value (for some types)
    :param str maxValuedate: Maximum Allowed Value (for some types)
    :param str maxValuedate: Maximum Allowed Value (for some types)
    :param str maxValuedate: Maximum Allowed Value (for some types)
    :param str maxValuedate: Maximum Allowed Value (for some types)
    :param float maxValuedate: Maximum Allowed Value (for some types)
    :param int maxValuedate: Maximum Allowed Value (for some types)
    :param int maxValuedate: Maximum Allowed Value (for some types)
    :param int maxValuedate: Maximum Allowed Value (for some types)
    :param Quantity maxValuedate: Maximum Allowed Value (for some types)
    :param int maxLength: Max length for strings
    :param str condition: Reference to invariant about presence
    :param Element constraint: Condition that must evaluate to true
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str key: Target of 'condition' reference above
    :param str requirements: Why this constraint is necessary or appropriate
    :param str severity: error | warning
    :param str human: Human description of constraint
    :param str expression: FHIRPath expression of constraint
    :param str xpath: XPath expression of constraint
    :param str source: Reference to original source of constraint
    :param bool mustSupport: If the element must be supported
    :param bool isModifier: If this modifies the meaning of other elements
    :param str isModifierReason: Reason that this element is marked as a modifier
    :param bool isSummary: Include when _summary = true?
    :param Element binding: ValueSet details if this is coded
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str strength: required | extensible | preferred | example
    :param str description: Human explanation of the value set
    :param str valueSet: Source of value set
    :param Element mapping: Map element to another set of definitions
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str identity: Reference to mapping declaration
    :param str language: Computable language of mapping
    :param str map: Details of the mapping
    :param str comment: Comments about the mapping or its use
    """
    id: str = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    path: str = None
    
    representation: str = None
    
    sliceName: str = None
    
    sliceIsConstraining: bool = None
    
    label: str = None
    
    code: list["Coding"] = None
    
    slicing: "Element" = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    discriminator: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
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
    
    extension: list["Extension"] = None
    
    path: str = None
    
    min: int = None
    
    max: str = None
    
    contentReference: str = None
    
    type: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
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
    
    example: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
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
    
    constraint: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
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
    
    extension: list["Extension"] = None
    
    strength: str = None
    
    description: str = None
    
    valueSet: str = None
    
    mapping: list["Element"] = None
    
    id: str = None
    
    extension: list["Extension"] = None
    
    identity: str = None
    
    language: str = None
    
    map: str = None
    
    comment: str = None
    