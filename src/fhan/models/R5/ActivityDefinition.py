"""
Generated class for ActivityDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.Period import *
from fhan.models.R5.Dosage import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Duration import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Expression import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Range import *
from fhan.models.R5.Age import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Timing import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Coding import *
from fhan.models.R5.DomainResource import *


    
    

class Participant(BaseModel):
    """ Indicates who should participate in performing the action described.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: careteam | device | group | healthcareservice | location | organization | patient | practitioner | practitionerrole | relatedperson
    :param str typeCanonical: Who or what can participate
    :param Reference typeReference: Who or what can participate
    :param CodeableConcept role: E.g. Nurse, Surgeon, Parent, etc
    :param CodeableConcept function: E.g. Author, Reviewer, Witness, etc
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "typeReference": {"class_name": "Reference", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "function": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  typeCanonical:  'str'  = None,  typeReference:  'Reference'  = None,  role:  'CodeableConcept'  = None,  function:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.typeCanonical = typeCanonical 
        self.typeReference = typeReference 
        self.role = role 
        self.function = function 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ActivityDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ActivityDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class DynamicValue(BaseModel):
    """ Dynamic values that will be evaluated to produce values for elements of the resulting resource. For example, if the dosage of a medication must be computed based on the patient's weight, a dynamic value would be used to specify an expression that calculated the weight, and the path on the request resource that would contain the result.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str path: The path to the element to be set dynamically
    :param Expression expression: An expression that provides the dynamic value for the customization
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "expression": {"class_name": "Expression", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  path:  'str'  = None,  expression:  'Expression'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.path = path 
        self.expression = expression 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ActivityDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ActivityDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ActivityDefinition(DomainResource):
    """ This resource allows for the definition of some activity to be performed, independent of a particular patient, practitioner, or other performance context.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this activity definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the activity definition
    :param str version: Business version of the activity definition
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this activity definition (computer friendly)
    :param str title: Name for this activity definition (human friendly)
    :param str subtitle: Subordinate title of the activity definition
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param CodeableConcept subjectCodeableConcept: Type of individual the activity definition is intended for
    :param Reference subjectReference: Type of individual the activity definition is intended for
    :param str subjectCanonical: Type of individual the activity definition is intended for
    :param str date: Date last changed
    :param str publisher: Name of the publisher/steward (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the activity definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for activity definition (if applicable)
    :param str purpose: Why this activity definition is defined
    :param str usage: Describes the clinical usage of the activity definition
    :param str copyright: Use and/or publishing restrictions
    :param str copyrightLabel: Copyright holder and year(s)
    :param str approvalDate: When the activity definition was approved by publisher
    :param str lastReviewDate: When the activity definition was last reviewed by the publisher
    :param Period effectivePeriod: When the activity definition is expected to be used
    :param CodeableConcept topic: E.g. Education, Treatment, Assessment, etc
    :param ContactDetail author: Who authored the content
    :param ContactDetail editor: Who edited the content
    :param ContactDetail reviewer: Who reviewed the content
    :param ContactDetail endorser: Who endorsed the content
    :param RelatedArtifact relatedArtifact: Additional documentation, citations, etc
    :param str library: Logic used by the activity definition
    :param str kind: Kind of resource
    :param str profile: What profile the resource needs to conform to
    :param CodeableConcept code: Detail type of activity
    :param str intent: proposal | plan | directive | order | original-order | reflex-order | filler-order | instance-order | option
    :param str priority: routine | urgent | asap | stat
    :param bool doNotPerform: True if the activity should not be performed
    :param Timing timingTiming: When activity is to occur
    :param Age timingAge: When activity is to occur
    :param Range timingRange: When activity is to occur
    :param Duration timingDuration: When activity is to occur
    :param bool asNeededBoolean: Preconditions for service
    :param CodeableConcept asNeededCodeableConcept: Preconditions for service
    :param CodeableReference location: Where it should happen
    :param Participant participant: Who should participate in the action
    :param Reference productReference: What's administered/supplied
    :param CodeableConcept productCodeableConcept: What's administered/supplied
    :param Quantity quantity: How much is administered/consumed/supplied
    :param Dosage dosage: Detailed dosage instructions
    :param CodeableConcept bodySite: What part of body to perform on
    :param str specimenRequirement: What specimens are required to perform this action
    :param str observationRequirement: What observations are required to perform this action
    :param str observationResultRequirement: What observations must be produced by this action
    :param str transform: Transform to apply the template
    :param DynamicValue dynamicValue: Dynamic aspects of the definition
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        "subjectCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subjectReference": {"class_name": "Reference", "is_contained": False},
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "topic": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "timingTiming": {"class_name": "Timing", "is_contained": False},
        
        
        "timingAge": {"class_name": "Age", "is_contained": False},
        
        
        "timingRange": {"class_name": "Range", "is_contained": False},
        
        
        "timingDuration": {"class_name": "Duration", "is_contained": False},
        
        
        
        "asNeededCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "location": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "participant": {"class_name": "Participant", "is_contained": True},
        
        
        "productReference": {"class_name": "Reference", "is_contained": False},
        
        
        "productCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "quantity": {"class_name": "Quantity", "is_contained": False},
        
        
        "dosage": {"class_name": "Dosage", "is_contained": False},
        
        
        "bodySite": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        "dynamicValue": {"class_name": "DynamicValue", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  subtitle:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  subjectCodeableConcept:  'CodeableConcept'  = None,  subjectReference:  'Reference'  = None,  subjectCanonical:  'str'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  usage:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  topic:  list['CodeableConcept']  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  library:  list['str']  = None,  kind:  'str'  = None,  profile:  'str'  = None,  code:  'CodeableConcept'  = None,  intent:  'str'  = None,  priority:  'str'  = None,  doNotPerform:  'bool'  = None,  timingTiming:  'Timing'  = None,  timingAge:  'Age'  = None,  timingRange:  'Range'  = None,  timingDuration:  'Duration'  = None,  asNeededBoolean:  'bool'  = None,  asNeededCodeableConcept:  'CodeableConcept'  = None,  location:  'CodeableReference'  = None,  participant:  list['Participant']  = None,  productReference:  'Reference'  = None,  productCodeableConcept:  'CodeableConcept'  = None,  quantity:  'Quantity'  = None,  dosage:  list['Dosage']  = None,  bodySite:  list['CodeableConcept']  = None,  specimenRequirement:  list['str']  = None,  observationRequirement:  list['str']  = None,  observationResultRequirement:  list['str']  = None,  transform:  'str'  = None,  dynamicValue:  list['DynamicValue']  = None, ):
        self.resourceType = resourceType or "ActivityDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.subtitle = subtitle 
        self.status = status 
        self.experimental = experimental 
        self.subjectCodeableConcept = subjectCodeableConcept 
        self.subjectReference = subjectReference 
        self.subjectCanonical = subjectCanonical 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.usage = usage 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.topic = topic or []
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.relatedArtifact = relatedArtifact or []
        self.library = library or []
        self.kind = kind 
        self.profile = profile 
        self.code = code 
        self.intent = intent 
        self.priority = priority 
        self.doNotPerform = doNotPerform 
        self.timingTiming = timingTiming 
        self.timingAge = timingAge 
        self.timingRange = timingRange 
        self.timingDuration = timingDuration 
        self.asNeededBoolean = asNeededBoolean 
        self.asNeededCodeableConcept = asNeededCodeableConcept 
        self.location = location 
        self.participant = participant or []
        self.productReference = productReference 
        self.productCodeableConcept = productCodeableConcept 
        self.quantity = quantity 
        self.dosage = dosage or []
        self.bodySite = bodySite or []
        self.specimenRequirement = specimenRequirement or []
        self.observationRequirement = observationRequirement or []
        self.observationResultRequirement = observationResultRequirement or []
        self.transform = transform 
        self.dynamicValue = dynamicValue or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ActivityDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ActivityDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()