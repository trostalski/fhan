"""
Generated class for MedicinalProductContraindication. 
Time: 2023-09-24 21:52:32
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Population import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DomainResource import *


    
    

class OtherTherapy(ModelBase):
    """ Information about the use of the medicinal product in relation to other therapies described as part of the indication.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' therapyRelationshipType: The type of relationship between the medicinal product indication or contraindication and another therapy
    :param 'CodeableConcept' medicationCodeableConcept: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  therapyRelationshipType: 'CodeableConcept' = None,  medicationCodeableConcept: 'CodeableConcept' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.therapyRelationshipType: 'CodeableConcept' = therapyRelationshipType 
        self.medicationCodeableConcept: 'CodeableConcept' = medicationCodeableConcept 
        

class MedicinalProductContraindication(DomainResource):
    """ The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory purposes.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Reference'] subject: The medication for which this is an indication
    :param 'CodeableConcept' disease: The disease, symptom or procedure for the contraindication
    :param 'CodeableConcept' diseaseStatus: The status of the disease or symptom for the contraindication
    :param list['CodeableConcept'] comorbidity: A comorbidity (concurrent condition) or coinfection
    :param list['Reference'] therapeuticIndication: Information about the use of the medicinal product in relation to other therapies as part of the indication
    :param list['OtherTherapy'] otherTherapy: Information about the use of the medicinal product in relation to other therapies described as part of the indication
    :param list['Population'] population: The population group to which this applies
    """
    def __init__(self, resourceType: str = "MedicinalProductContraindication",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  subject: list['Reference'] = None,  disease: 'CodeableConcept' = None,  diseaseStatus: 'CodeableConcept' = None,  comorbidity: list['CodeableConcept'] = None,  therapeuticIndication: list['Reference'] = None,  otherTherapy: list['OtherTherapy'] = None,  population: list['Population'] = None, ):
        self.resourceType: str = resourceType or "MedicinalProductContraindication"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.subject: list['Reference'] = subject or []
        self.disease: 'CodeableConcept' = disease 
        self.diseaseStatus: 'CodeableConcept' = diseaseStatus 
        self.comorbidity: list['CodeableConcept'] = comorbidity or []
        self.therapeuticIndication: list['Reference'] = therapeuticIndication or []
        self.otherTherapy: list['OtherTherapy'] = otherTherapy or []
        self.population: list['Population'] = population or []
        