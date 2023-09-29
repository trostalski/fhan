"""
Generated class for ResearchStudy. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Label(BaseModel):
    """ Additional names for the study.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: primary | official | scientific | plain-language | subtitle | short-title | acronym | earlier-title | language | auto-translated | human-use | machine-use | duplicate-uid
    :param str value: The name
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class AssociatedParty(BaseModel):
    """ Sponsors, collaborators, and other parties.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Name of associated party
    :param CodeableConcept role: sponsor | lead-sponsor | sponsor-investigator | primary-investigator | collaborator | funding-source | general-contact | recruitment-contact | sub-investigator | study-director | study-chair
    :param Period period: When active in the role
    :param CodeableConcept classifier: nih | fda | government | nonprofit | academic | industry
    :param Reference party: Individual or organization associated with study (use practitionerRole to specify their organisation)
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "party": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  role:  'CodeableConcept'  = None,  period:  list['Period']  = None,  classifier:  list['CodeableConcept']  = None,  party:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.role = role 
        self.period = period or []
        self.classifier = classifier or []
        self.party = party 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ProgressStatus(BaseModel):
    """ Status of study with time for that status.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept state: Label for status or state (e.g. recruitment status)
    :param bool actual: Actual if true else anticipated
    :param Period period: Date range
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "state": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  state:  'CodeableConcept'  = None,  actual:  'bool'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.state = state 
        self.actual = actual 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Recruitment(BaseModel):
    """ Target or actual group of participants enrolled in study.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param int targetNumber: Estimated total number of participants to be enrolled
    :param int actualNumber: Actual total number of participants enrolled in study
    :param Reference eligibility: Inclusion and exclusion criteria
    :param Reference actualGroup: Group of participants who were enrolled in study
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "eligibility": {"class_name": "Reference", "is_contained": False},
        
        
        "actualGroup": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  targetNumber:  'int'  = None,  actualNumber:  'int'  = None,  eligibility:  'Reference'  = None,  actualGroup:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.targetNumber = targetNumber 
        self.actualNumber = actualNumber 
        self.eligibility = eligibility 
        self.actualGroup = actualGroup 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class ComparisonGroup(BaseModel):
    """ Describes an expected event or sequence of events for one of the subjects of a study. E.g. for a living subject: exposure to drug A, wash-out, exposure to drug B, wash-out, follow-up. E.g. for a stability study: {store sample from lot A at 25 degrees for 1 month}, {store sample from lot A at 40 degrees for 1 month}.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str linkId: Allows the comparisonGroup for the study and the comparisonGroup for the subject to be linked easily
    :param str name: Label for study comparisonGroup
    :param CodeableConcept type: Categorization of study comparisonGroup
    :param str description: Short explanation of study path
    :param Reference intendedExposure: Interventions or exposures in this comparisonGroup or cohort
    :param Reference observedGroup: Group of participants who were enrolled in study comparisonGroup
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "intendedExposure": {"class_name": "Reference", "is_contained": False},
        
        
        "observedGroup": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  linkId:  'str'  = None,  name:  'str'  = None,  type:  'CodeableConcept'  = None,  description:  'str'  = None,  intendedExposure:  list['Reference']  = None,  observedGroup:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.linkId = linkId 
        self.name = name 
        self.type = type 
        self.description = description 
        self.intendedExposure = intendedExposure or []
        self.observedGroup = observedGroup 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Objective(BaseModel):
    """ A goal that the study is aiming to achieve in terms of a scientific question to be answered by the analysis of data collected during the study.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the objective
    :param CodeableConcept type: primary | secondary | exploratory
    :param str description: Description of the objective
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  type:  'CodeableConcept'  = None,  description:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.type = type 
        self.description = description 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class OutcomeMeasure(BaseModel):
    """ An "outcome measure", "endpoint", "effect measure" or "measure of effect" is a specific measurement or observation used to quantify the effect of experimental variables on the participants in a study, or for observational studies, to describe patterns of diseases or traits or associations with exposures, risk factors or treatment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Label for the outcome
    :param CodeableConcept type: primary | secondary | exploratory
    :param str description: Description of the outcome
    :param Reference reference: Structured outcome definition
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "reference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  name:  'str'  = None,  type:  list['CodeableConcept']  = None,  description:  'str'  = None,  reference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name 
        self.type = type or []
        self.description = description 
        self.reference = reference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ResearchStudy(DomainResource):
    """ A scientific study of nature that sometimes includes processes involved in health and disease. For example, clinical trials are research studies that involve people. These studies may be related to new ways to screen, prevent, diagnose, and treat disease. They may also study certain outcomes and certain groups of people by looking at data collected in the past or future.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this study resource
    :param Identifier identifier: Business Identifier for study
    :param str version: The business version for the study record
    :param str name: Name for this study (computer friendly)
    :param str title: Human readable name of the study
    :param Label label: Additional names for the study
    :param Reference protocol: Steps followed in executing study
    :param Reference partOf: Part of larger study
    :param RelatedArtifact relatedArtifact: References, URLs, and attachments
    :param str date: Date the resource last changed
    :param str status: draft | active | retired | unknown
    :param CodeableConcept primaryPurposeType: treatment | prevention | diagnostic | supportive-care | screening | health-services-research | basic-science | device-feasibility
    :param CodeableConcept phase: n-a | early-phase-1 | phase-1 | phase-1-phase-2 | phase-2 | phase-2-phase-3 | phase-3 | phase-4
    :param CodeableConcept studyDesign: Classifications of the study design characteristics
    :param CodeableReference focus: Drugs, devices, etc. under study
    :param CodeableConcept condition: Condition being studied
    :param CodeableConcept keyword: Used to search for the study
    :param CodeableConcept region: Geographic area for the study
    :param str descriptionSummary: Brief text explaining the study
    :param str description: Detailed narrative of the study
    :param Period period: When the study began and ended
    :param Reference site: Facility where study activities are conducted
    :param Annotation note: Comments made about the study
    :param CodeableConcept classifier: Classification for the study
    :param AssociatedParty associatedParty: Sponsors, collaborators, and other parties
    :param ProgressStatus progressStatus: Status of study with time for that status
    :param CodeableConcept whyStopped: accrual-goal-met | closed-due-to-toxicity | closed-due-to-lack-of-study-progress | temporarily-closed-per-study-design
    :param Recruitment recruitment: Target or actual group of participants enrolled in study
    :param ComparisonGroup comparisonGroup: Defined path through the study for a subject
    :param Objective objective: A goal for the study
    :param OutcomeMeasure outcomeMeasure: A variable measured during the study
    :param Reference result: Link to results generated during the study
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        
        "label": {"class_name": "Label", "is_contained": True},
        
        
        "protocol": {"class_name": "Reference", "is_contained": False},
        
        
        "partOf": {"class_name": "Reference", "is_contained": False},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        
        
        "primaryPurposeType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "phase": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "studyDesign": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "focus": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "condition": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "keyword": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "region": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        
        "site": {"class_name": "Reference", "is_contained": False},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "associatedParty": {"class_name": "AssociatedParty", "is_contained": True},
        
        
        "progressStatus": {"class_name": "ProgressStatus", "is_contained": True},
        
        
        "whyStopped": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "recruitment": {"class_name": "Recruitment", "is_contained": True},
        
        
        "comparisonGroup": {"class_name": "ComparisonGroup", "is_contained": True},
        
        
        "objective": {"class_name": "Objective", "is_contained": True},
        
        
        "outcomeMeasure": {"class_name": "OutcomeMeasure", "is_contained": True},
        
        
        "result": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  name:  'str'  = None,  title:  'str'  = None,  label:  list['Label']  = None,  protocol:  list['Reference']  = None,  partOf:  list['Reference']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  date:  'str'  = None,  status:  'str'  = None,  primaryPurposeType:  'CodeableConcept'  = None,  phase:  'CodeableConcept'  = None,  studyDesign:  list['CodeableConcept']  = None,  focus:  list['CodeableReference']  = None,  condition:  list['CodeableConcept']  = None,  keyword:  list['CodeableConcept']  = None,  region:  list['CodeableConcept']  = None,  descriptionSummary:  'str'  = None,  description:  'str'  = None,  period:  'Period'  = None,  site:  list['Reference']  = None,  note:  list['Annotation']  = None,  classifier:  list['CodeableConcept']  = None,  associatedParty:  list['AssociatedParty']  = None,  progressStatus:  list['ProgressStatus']  = None,  whyStopped:  'CodeableConcept'  = None,  recruitment:  'Recruitment'  = None,  comparisonGroup:  list['ComparisonGroup']  = None,  objective:  list['Objective']  = None,  outcomeMeasure:  list['OutcomeMeasure']  = None,  result:  list['Reference']  = None, ):
        self.resourceType = resourceType or "ResearchStudy"
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
        self.name = name 
        self.title = title 
        self.label = label or []
        self.protocol = protocol or []
        self.partOf = partOf or []
        self.relatedArtifact = relatedArtifact or []
        self.date = date 
        self.status = status 
        self.primaryPurposeType = primaryPurposeType 
        self.phase = phase 
        self.studyDesign = studyDesign or []
        self.focus = focus or []
        self.condition = condition or []
        self.keyword = keyword or []
        self.region = region or []
        self.descriptionSummary = descriptionSummary 
        self.description = description 
        self.period = period 
        self.site = site or []
        self.note = note or []
        self.classifier = classifier or []
        self.associatedParty = associatedParty or []
        self.progressStatus = progressStatus or []
        self.whyStopped = whyStopped 
        self.recruitment = recruitment 
        self.comparisonGroup = comparisonGroup or []
        self.objective = objective or []
        self.outcomeMeasure = outcomeMeasure or []
        self.result = result or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ResearchStudy":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ResearchStudy":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()