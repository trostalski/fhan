"""
Generated class for ClinicalUseDefinition. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Range import *
from fhan.models.R5.Expression import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
        
    
    

class OtherTherapy(BaseModel):
    """ Information about the use of the medicinal product in relation to other therapies described as part of the contraindication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationshipType: The type of relationship between the product indication/contraindication and another therapy
    :param CodeableReference treatment: Reference to a specific medication, substance etc. as part of an indication or contraindication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "relationshipType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "treatment": {"class_name": "CodeableReference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  relationshipType:  'CodeableConcept'  = None,  treatment:  'CodeableReference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.relationshipType = relationshipType 
        self.treatment = treatment 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Contraindication(BaseModel):
    """ Specifics for when this is a contraindication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference diseaseSymptomProcedure: The situation that is being documented as contraindicating against this item
    :param CodeableReference diseaseStatus: The status of the disease or symptom for the contraindication
    :param CodeableReference comorbidity: A comorbidity (concurrent condition) or coinfection
    :param Reference indication: The indication which this is a contraidication for
    :param Expression applicability: An expression that returns true or false, indicating whether the indication is applicable or not, after having applied its other elements
    :param OtherTherapy otherTherapy: Information about use of the product in relation to other therapies described as part of the contraindication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "diseaseSymptomProcedure": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "diseaseStatus": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "comorbidity": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "indication": {"class_name": "Reference", "is_contained": False},
        
        
        "applicability": {"class_name": "Expression", "is_contained": False},
        
        
        "otherTherapy": {"class_name": "OtherTherapy", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  diseaseSymptomProcedure:  'CodeableReference'  = None,  diseaseStatus:  'CodeableReference'  = None,  comorbidity:  list['CodeableReference']  = None,  indication:  list['Reference']  = None,  applicability:  'Expression'  = None,  otherTherapy:  list['OtherTherapy']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.diseaseSymptomProcedure = diseaseSymptomProcedure 
        self.diseaseStatus = diseaseStatus 
        self.comorbidity = comorbidity or []
        self.indication = indication or []
        self.applicability = applicability 
        self.otherTherapy = otherTherapy or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Indication(BaseModel):
    """ Specifics for when this is an indication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference diseaseSymptomProcedure: The situation that is being documented as an indicaton for this item
    :param CodeableReference diseaseStatus: The status of the disease or symptom for the indication
    :param CodeableReference comorbidity: A comorbidity or coinfection as part of the indication
    :param CodeableReference intendedEffect: The intended effect, aim or strategy to be achieved
    :param Range durationRange: Timing or duration information
    :param str durationString: Timing or duration information
    :param Reference undesirableEffect: An unwanted side effect or negative outcome of the subject of this resource when being used for this indication
    :param Expression applicability: An expression that returns true or false, indicating whether the indication is applicable or not, after having applied its other elements
    :param OtherTherapy otherTherapy: The use of the medicinal product in relation to other therapies described as part of the indication
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "diseaseSymptomProcedure": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "diseaseStatus": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "comorbidity": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "intendedEffect": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "durationRange": {"class_name": "Range", "is_contained": False},
        
        
        
        "undesirableEffect": {"class_name": "Reference", "is_contained": False},
        
        
        "applicability": {"class_name": "Expression", "is_contained": False},
        
        
        "otherTherapy": {"class_name": "OtherTherapy", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  diseaseSymptomProcedure:  'CodeableReference'  = None,  diseaseStatus:  'CodeableReference'  = None,  comorbidity:  list['CodeableReference']  = None,  intendedEffect:  'CodeableReference'  = None,  durationRange:  'Range'  = None,  durationString:  'str'  = None,  undesirableEffect:  list['Reference']  = None,  applicability:  'Expression'  = None,  otherTherapy:  list['OtherTherapy']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.diseaseSymptomProcedure = diseaseSymptomProcedure 
        self.diseaseStatus = diseaseStatus 
        self.comorbidity = comorbidity or []
        self.intendedEffect = intendedEffect 
        self.durationRange = durationRange 
        self.durationString = durationString 
        self.undesirableEffect = undesirableEffect or []
        self.applicability = applicability 
        self.otherTherapy = otherTherapy or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Interactant(BaseModel):
    """ The specific medication, product, food, substance etc. or laboratory test that interacts.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference itemReference: The specific medication, product, food etc. or laboratory test that interacts
    :param CodeableConcept itemCodeableConcept: The specific medication, product, food etc. or laboratory test that interacts
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "itemReference": {"class_name": "Reference", "is_contained": False},
        
        
        "itemCodeableConcept": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  itemReference:  'Reference'  = None,  itemCodeableConcept:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.itemReference = itemReference 
        self.itemCodeableConcept = itemCodeableConcept 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Interaction(BaseModel):
    """ Specifics for when this is an interaction.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Interactant interactant: The specific medication, product, food etc. or laboratory test that interacts
    :param CodeableConcept type: The type of the interaction e.g. drug-drug interaction, drug-lab test interaction
    :param CodeableReference effect: The effect of the interaction, for example "reduced gastric absorption of primary medication"
    :param CodeableConcept incidence: The incidence of the interaction, e.g. theoretical, observed
    :param CodeableConcept management: Actions for managing the interaction
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "interactant": {"class_name": "Interactant", "is_contained": True},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "effect": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "incidence": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "management": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  interactant:  list['Interactant']  = None,  type:  'CodeableConcept'  = None,  effect:  'CodeableReference'  = None,  incidence:  'CodeableConcept'  = None,  management:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.interactant = interactant or []
        self.type = type 
        self.effect = effect 
        self.incidence = incidence 
        self.management = management or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class UndesirableEffect(BaseModel):
    """ Describe the possible undesirable effects (negative outcomes) from the use of the medicinal product as treatment.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableReference symptomConditionEffect: The situation in which the undesirable effect may manifest
    :param CodeableConcept classification: High level classification of the effect
    :param CodeableConcept frequencyOfOccurrence: How often the effect is seen
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "symptomConditionEffect": {"class_name": "CodeableReference", "is_contained": False},
        
        
        "classification": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "frequencyOfOccurrence": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  symptomConditionEffect:  'CodeableReference'  = None,  classification:  'CodeableConcept'  = None,  frequencyOfOccurrence:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.symptomConditionEffect = symptomConditionEffect 
        self.classification = classification 
        self.frequencyOfOccurrence = frequencyOfOccurrence 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Warning(BaseModel):
    """ A critical piece of information about environmental, health or physical risks or hazards that serve as caution to the user. For example 'Do not operate heavy machinery', 'May cause drowsiness', or 'Get medical advice/attention if you feel unwell'.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: A textual definition of this warning, with formatting
    :param CodeableConcept code: A coded or unformatted textual definition of this warning
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "code": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  description:  'str'  = None,  code:  'CodeableConcept'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.description = description 
        self.code = code 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ClinicalUseDefinition(DomainResource):
    """ A single issue - either an indication, contraindication, interaction or an undesirable effect for a medicinal product, medication, device or procedure.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for this issue
    :param str type: indication | contraindication | interaction | undesirable-effect | warning
    :param CodeableConcept category: A categorisation of the issue, primarily for dividing warnings into subject heading areas such as "Pregnancy", "Overdose"
    :param Reference subject: The medication, product, substance, device, procedure etc. for which this is an indication
    :param CodeableConcept status: Whether this is a current issue or one that has been retired etc
    :param Contraindication contraindication: Specifics for when this is a contraindication
    :param Indication indication: Specifics for when this is an indication
    :param Interaction interaction: Specifics for when this is an interaction
    :param Reference population: The population group to which this applies
    :param str library: Logic used by the clinical use definition
    :param UndesirableEffect undesirableEffect: A possible negative outcome from the use of this treatment
    :param Warning warning: Critical environmental, health or physical risks or hazards. For example 'Do not operate heavy machinery', 'May cause drowsiness'
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "category": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "subject": {"class_name": "Reference", "is_contained": False},
        
        
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "contraindication": {"class_name": "Contraindication", "is_contained": True},
        
        
        "indication": {"class_name": "Indication", "is_contained": True},
        
        
        "interaction": {"class_name": "Interaction", "is_contained": True},
        
        
        "population": {"class_name": "Reference", "is_contained": False},
        
        
        
        "undesirableEffect": {"class_name": "UndesirableEffect", "is_contained": True},
        
        
        "warning": {"class_name": "Warning", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  type:  'str'  = None,  category:  list['CodeableConcept']  = None,  subject:  list['Reference']  = None,  status:  'CodeableConcept'  = None,  contraindication:  'Contraindication'  = None,  indication:  'Indication'  = None,  interaction:  'Interaction'  = None,  population:  list['Reference']  = None,  library:  list['str']  = None,  undesirableEffect:  'UndesirableEffect'  = None,  warning:  'Warning'  = None, ):
        self.resourceType = resourceType or "ClinicalUseDefinition"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.type = type 
        self.category = category or []
        self.subject = subject or []
        self.status = status 
        self.contraindication = contraindication 
        self.indication = indication 
        self.interaction = interaction 
        self.population = population or []
        self.library = library or []
        self.undesirableEffect = undesirableEffect 
        self.warning = warning 
        

    @classmethod
    def from_dict(cls, data: dict) -> "ClinicalUseDefinition":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "ClinicalUseDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()