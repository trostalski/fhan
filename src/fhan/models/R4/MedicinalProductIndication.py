"""
Generated class for MedicinalProductIndication. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Population import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class OtherTherapy(ModelBase):
    """ Information about the use of the medicinal product in relation to other therapies described as part of the indication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' therapyRelationshipType: The type of relationship between the medicinal product indication or contraindication and another therapy
    :param 'CodeableConcept' medicationCodeableConcept: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    :param 'Reference' medicationReference: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  therapyRelationshipType: 'CodeableConcept' = None,  medicationCodeableConcept: 'CodeableConcept' = None,  medicationReference: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.therapyRelationshipType: 'CodeableConcept' = therapyRelationshipType 
        self.medicationCodeableConcept: 'CodeableConcept' = medicationCodeableConcept 
        self.medicationReference: 'Reference' = medicationReference 
        

class MedicinalProductIndication(DomainResource):
    """ Indication for the Medicinal Product.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Reference'] subject: The medication for which this is an indication
    :param 'CodeableConcept' diseaseSymptomProcedure: The disease, symptom or procedure that is the indication for treatment
    :param 'CodeableConcept' diseaseStatus: The status of the disease or symptom for which the indication applies
    :param list['CodeableConcept'] comorbidity: Comorbidity (concurrent condition) or co-infection as part of the indication
    :param 'CodeableConcept' intendedEffect: The intended effect, aim or strategy to be achieved by the indication
    :param 'Quantity' duration: Timing or duration information as part of the indication
    :param list['OtherTherapy'] otherTherapy: Information about the use of the medicinal product in relation to other therapies described as part of the indication
    :param list['Reference'] undesirableEffect: Describe the undesirable effects of the medicinal product
    :param list['Population'] population: The population group to which this applies
    """
    def __init__(self, resourceType: str = "MedicinalProductIndication",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  subject: list['Reference'] = None,  diseaseSymptomProcedure: 'CodeableConcept' = None,  diseaseStatus: 'CodeableConcept' = None,  comorbidity: list['CodeableConcept'] = None,  intendedEffect: 'CodeableConcept' = None,  duration: 'Quantity' = None,  otherTherapy: list['OtherTherapy'] = None,  undesirableEffect: list['Reference'] = None,  population: list['Population'] = None, ):
        self.resourceType: str = resourceType or "MedicinalProductIndication"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.subject: list['Reference'] = subject or []
        self.diseaseSymptomProcedure: 'CodeableConcept' = diseaseSymptomProcedure 
        self.diseaseStatus: 'CodeableConcept' = diseaseStatus 
        self.comorbidity: list['CodeableConcept'] = comorbidity or []
        self.intendedEffect: 'CodeableConcept' = intendedEffect 
        self.duration: 'Quantity' = duration 
        self.otherTherapy: list['OtherTherapy'] = otherTherapy or []
        self.undesirableEffect: list['Reference'] = undesirableEffect or []
        self.population: list['Population'] = population or []
        