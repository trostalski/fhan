"""
Generated class for MedicinalProductContraindication. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Reference import *
from fhan.models.R4.Population import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class OtherTherapy(Element):
    """ Information about the use of the medicinal product in relation to other therapies described as part of the indication.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept therapyRelationshipType: The type of relationship between the medicinal product indication or contraindication and another therapy
    :param CodeableConcept medicationCodeableConcept: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    therapyRelationshipType: "CodeableConcept" = CodeableConcept()
    medicationCodeableConcept: "CodeableConcept" = CodeableConcept()
    

@dataclass
class MedicinalProductContraindication(ModelBase):
    """ The clinical particulars - indications, contraindications etc. of a medicinal product, including for regulatory purposes.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference subject: The medication for which this is an indication
    :param CodeableConcept disease: The disease, symptom or procedure for the contraindication
    :param CodeableConcept diseaseStatus: The status of the disease or symptom for the contraindication
    :param CodeableConcept comorbidity: A comorbidity (concurrent condition) or coinfection
    :param Reference therapeuticIndication: Information about the use of the medicinal product in relation to other therapies as part of the indication
    :param OtherTherapy otherTherapy: Information about the use of the medicinal product in relation to other therapies described as part of the indication
    :param Population population: The population group to which this applies
    """

    resourceType: str = "MedicinalProductContraindication"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    subject: list[Reference] = Reference() 
    
    disease: "CodeableConcept" = CodeableConcept()
    
    diseaseStatus: "CodeableConcept" = CodeableConcept()
    
    comorbidity: list[CodeableConcept] = CodeableConcept() 
    
    therapeuticIndication: list[Reference] = Reference() 
    
    otherTherapy: list[OtherTherapy] = OtherTherapy() 
    
    population: list[Population] = Population() 
    