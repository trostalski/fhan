"""
Generated class for ElementDefinition. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Element import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.ParameterDefinition import *
from fhan.models.R4.Contributor import *
from fhan.models.R4.TriggerDefinition import *
from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.RelatedArtifact import *
from fhan.models.R4.Range import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Duration import *
from fhan.models.R4.Address import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Distance import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Money import *
from fhan.models.R4.Age import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Coding import *
from fhan.models.R4.Dosage import *
from fhan.models.R4.Extension import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Signature import *
from fhan.models.R4.Count import *
from fhan.models.R4.SampledData import *
from fhan.models.R4.Period import *
from fhan.models.R4.Expression import *
from fhan.models.generator_models import ModelBase

class ElementDefinition(ModelBase):
    """ Base StructureDefinition for ElementDefinition Type: Captures constraints on each element within the resource, profile, or extension.
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: Path of the element in the hierarchy of elements
    :param str representation: xmlAttr | xmlText | typeAttr | cdaText | xhtml
    :param str sliceName: Name for this particular element (in a set of slices)
    :param bool sliceIsConstraining: If this slice definition constrains an inherited slice definition (or not)
    :param str label: Name for element to display with or prompt for element
    :param list['Coding'] code: Corresponding codes in terminologies
    :param 'Element' slicing: This element is sliced - slices follow
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Element'] discriminator: Element values that are used to distinguish the slices
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
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
    :param 'Element' base: Base definition information for tools
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str path: Path that identifies the base element
    :param int min: Min cardinality of the base element
    :param str max: Max cardinality of the base element
    :param str contentReference: Reference to definition of content for the element
    :param list['Element'] type: Data type and Profile for this element
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str code: Data type or Resource (reference to definition)
    :param str profile: Profiles (StructureDefinition or IG) - one must apply
    :param str targetProfile: Profile (StructureDefinition or IG) on the Reference/canonical target - one must apply
    :param str aggregation: contained | referenced | bundled - how aggregated
    :param str versioning: either | independent | specific
    :param str defaultValueBase64Binary: Specified value if missing from instance
    :param str meaningWhenMissing: Implicit meaning when this element is missing
    :param str orderMeaning: What the order of the elements means
    :param str fixedBase64Binary: Value must be exactly this
    :param str patternBase64Binary: Value must have at least these property values
    :param list['Element'] example: Example value (as defined for type)
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str label: Describes the purpose of this example
    :param str valueBase64Binary: Value of Example (one of allowed types)
    :param str minValueDate: Minimum Allowed Value (for some types)
    :param str maxValueDate: Maximum Allowed Value (for some types)
    :param int maxLength: Max length for strings
    :param str condition: Reference to invariant about presence
    :param list['Element'] constraint: Condition that must evaluate to true
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
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
    :param 'Element' binding: ValueSet details if this is coded
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str strength: required | extensible | preferred | example
    :param str description: Human explanation of the value set
    :param str valueSet: Source of value set
    :param list['Element'] mapping: Map element to another set of definitions
    :param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param str identity: Reference to mapping declaration
    :param str language: Computable language of mapping
    :param str map: Details of the mapping
    :param str comment: Comments about the mapping or its use
    """
    def __init__(self, resourceType: str = "ElementDefinition",  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  path: str = None,  representation: str = None,  sliceName: str = None,  sliceIsConstraining: bool = None,  label: str = None,  code: list['Coding'] = None,  slicing: 'Element' = None,  id: str = None,  extension: list['Extension'] = None,  discriminator: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  type: str = None,  path: str = None,  description: str = None,  ordered: bool = None,  rules: str = None,  short: str = None,  definition: str = None,  comment: str = None,  requirements: str = None,  alias: str = None,  min: int = None,  max: str = None,  base: 'Element' = None,  id: str = None,  extension: list['Extension'] = None,  path: str = None,  min: int = None,  max: str = None,  contentReference: str = None,  type: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  code: str = None,  profile: str = None,  targetProfile: str = None,  aggregation: str = None,  versioning: str = None,  defaultValueBase64Binary: str = None,  meaningWhenMissing: str = None,  orderMeaning: str = None,  fixedBase64Binary: str = None,  patternBase64Binary: str = None,  example: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  label: str = None,  valueBase64Binary: str = None,  minValueDate: str = None,  maxValueDate: str = None,  maxLength: int = None,  condition: str = None,  constraint: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  key: str = None,  requirements: str = None,  severity: str = None,  human: str = None,  expression: str = None,  xpath: str = None,  source: str = None,  mustSupport: bool = None,  isModifier: bool = None,  isModifierReason: str = None,  isSummary: bool = None,  binding: 'Element' = None,  id: str = None,  extension: list['Extension'] = None,  strength: str = None,  description: str = None,  valueSet: str = None,  mapping: list['Element'] = None,  id: str = None,  extension: list['Extension'] = None,  identity: str = None,  language: str = None,  map: str = None,  comment: str = None, ):
        self.resourceType: str = resourceType or "ElementDefinition"
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.path: str = path 
        self.representation: str = representation or []
        self.sliceName: str = sliceName 
        self.sliceIsConstraining: bool = sliceIsConstraining 
        self.label: str = label 
        self.code: list['Coding'] = code or []
        self.slicing: 'Element' = slicing 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.discriminator: list['Element'] = discriminator or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.type: str = type 
        self.path: str = path 
        self.description: str = description 
        self.ordered: bool = ordered 
        self.rules: str = rules 
        self.short: str = short 
        self.definition: str = definition 
        self.comment: str = comment 
        self.requirements: str = requirements 
        self.alias: str = alias or []
        self.min: int = min 
        self.max: str = max 
        self.base: 'Element' = base 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.path: str = path 
        self.min: int = min 
        self.max: str = max 
        self.contentReference: str = contentReference 
        self.type: list['Element'] = type or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.code: str = code 
        self.profile: str = profile or []
        self.targetProfile: str = targetProfile or []
        self.aggregation: str = aggregation or []
        self.versioning: str = versioning 
        self.defaultValueBase64Binary: str = defaultValueBase64Binary 
        self.meaningWhenMissing: str = meaningWhenMissing 
        self.orderMeaning: str = orderMeaning 
        self.fixedBase64Binary: str = fixedBase64Binary 
        self.patternBase64Binary: str = patternBase64Binary 
        self.example: list['Element'] = example or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.label: str = label 
        self.valueBase64Binary: str = valueBase64Binary 
        self.minValueDate: str = minValueDate 
        self.maxValueDate: str = maxValueDate 
        self.maxLength: int = maxLength 
        self.condition: str = condition or []
        self.constraint: list['Element'] = constraint or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.key: str = key 
        self.requirements: str = requirements 
        self.severity: str = severity 
        self.human: str = human 
        self.expression: str = expression 
        self.xpath: str = xpath 
        self.source: str = source 
        self.mustSupport: bool = mustSupport 
        self.isModifier: bool = isModifier 
        self.isModifierReason: str = isModifierReason 
        self.isSummary: bool = isSummary 
        self.binding: 'Element' = binding 
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.strength: str = strength 
        self.description: str = description 
        self.valueSet: str = valueSet 
        self.mapping: list['Element'] = mapping or []
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.identity: str = identity 
        self.language: str = language 
        self.map: str = map 
        self.comment: str = comment 
        