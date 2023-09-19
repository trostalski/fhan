"""
Generated class for MedicinalProductIndication. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Population import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class MedicinalProductIndication(ModelBase):
    """ Indication for the Medicinal Product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference subject: The medication for which this is an indication
    :param CodeableConcept diseaseSymptomProcedure: The disease, symptom or procedure that is the indication for treatment
    :param CodeableConcept diseaseStatus: The status of the disease or symptom for which the indication applies
    :param CodeableConcept comorbidity: Comorbidity (concurrent condition) or co-infection as part of the indication
    :param CodeableConcept intendedEffect: The intended effect, aim or strategy to be achieved by the indication
    :param Quantity duration: Timing or duration information as part of the indication
    :param BackboneElement otherTherapy: Information about the use of the medicinal product in relation to other therapies described as part of the indication
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept therapyRelationshipType: The type of relationship between the medicinal product indication or contraindication and another therapy
    :param CodeableConcept medicationCodeableConcept: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    :param Reference medicationCodeableConcept: Reference to a specific medication (active substance, medicinal product or class of products) as part of an indication or contraindication
    :param Reference undesirableEffect: Describe the undesirable effects of the medicinal product
    :param Population population: The population group to which this applies
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    subject: "Reference" = None
    
    diseaseSymptomProcedure: "CodeableConcept" = None
    
    diseaseStatus: "CodeableConcept" = None
    
    comorbidity: "CodeableConcept" = None
    
    intendedEffect: "CodeableConcept" = None
    
    duration: "Quantity" = None
    
    otherTherapy: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    therapyRelationshipType: "CodeableConcept" = None
    
    medicationCodeableConcept: "CodeableConcept" = None
    
    medicationCodeableConcept: "Reference" = None
    
    undesirableEffect: "Reference" = None
    
    population: "Population" = None
    