"""
Generated class for Practitioner. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Address import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Element import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Qualification(Element):
    """ The official certifications, training, and licenses that authorize or otherwise pertain to the provision of care by the practitioner.  For example, a medical license issued by a medical board authorizing the practitioner to practice medicine within a certian locality.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: An identifier for this qualification for the practitioner
    :param CodeableConcept code: Coded representation of the qualification
    :param Period period: Period during which the qualification is valid
    :param Reference issuer: Organization that regulates and issues the qualification
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    identifier:  list["Identifier"] = [Identifier()]
    
    code:  "CodeableConcept" = CodeableConcept()
    
    period:  "Period" = Period()
    
    issuer:  "Reference" = Reference()
    

@dataclass
class Practitioner(ModelBase):
    """ A person who is directly or indirectly involved in the provisioning of healthcare.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier for the person as this agent
    :param bool active: Whether this practitioner's record is in active use
    :param HumanName name: The name(s) associated with the practitioner
    :param ContactPoint telecom: A contact detail for the practitioner (that apply to all roles)
    :param Address address: Address(es) of the practitioner that are not role specific (typically home address)
    :param str gender: male | female | other | unknown
    :param str birthDate: The date  on which the practitioner was born
    :param Attachment photo: Image of the person
    :param Qualification qualification: Certification, licenses, or training pertaining to the provision of care
    :param CodeableConcept communication: A language the practitioner can use in patient communication
    """

    resourceType: str = "Practitioner"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    active: bool = None
    
    name: list["HumanName"] = None
    
    telecom: list["ContactPoint"] = None
    
    address: list["Address"] = None
    
    gender: str = None
    
    birthDate: str = None
    
    photo: list["Attachment"] = None
    
    qualification: list["Qualification"] = None
    
    communication: list["CodeableConcept"] = None
    