"""
Generated class for Patient. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.ContactPoint import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Address import *
from fhan.models.R4.HumanName import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class Patient(ModelBase):
    """ Demographics and other administrative information about an individual or animal receiving care or other health-related services.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: An identifier for this patient
    :param bool active: Whether this patient's record is in active use
    :param HumanName name: A name associated with the patient
    :param ContactPoint telecom: A contact detail for the individual
    :param str gender: male | female | other | unknown
    :param str birthDate: The date of birth for the individual
    :param bool deceasedboolean: Indicates if the individual is deceased or not
    :param str deceasedboolean: Indicates if the individual is deceased or not
    :param Address address: An address for the individual
    :param CodeableConcept maritalStatus: Marital (civil) status of a patient
    :param bool multipleBirthboolean: Whether patient is part of a multiple birth
    :param int multipleBirthboolean: Whether patient is part of a multiple birth
    :param Attachment photo: Image of the patient
    :param BackboneElement contact: A contact party (e.g. guardian, partner, friend) for the patient
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept relationship: The kind of relationship
    :param HumanName name: A name associated with the contact person
    :param ContactPoint telecom: A contact detail for the person
    :param Address address: Address for the contact person
    :param str gender: male | female | other | unknown
    :param Reference organization: Organization that is associated with the contact
    :param Period period: The period during which this contact person or organization is valid to be contacted relating to this patient
    :param BackboneElement communication: A language which may be used to communicate with the patient about his or her health
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept language: The language which can be used to communicate with the patient about his or her health
    :param bool preferred: Language preference indicator
    :param Reference generalPractitioner: Patient's nominated primary care provider
    :param Reference managingOrganization: Organization that is the custodian of the patient record
    :param BackboneElement link: Link to another patient resource that concerns the same actual person
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference other: The other patient or related person resource that the link refers to
    :param str type: replaced-by | replaces | refer | seealso
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    active: bool = None
    
    name: "HumanName" = None
    
    telecom: "ContactPoint" = None
    
    gender: str = None
    
    birthDate: str = None
    
    deceasedboolean: bool = None
    
    deceasedboolean: str = None
    
    address: "Address" = None
    
    maritalStatus: "CodeableConcept" = None
    
    multipleBirthboolean: bool = None
    
    multipleBirthboolean: int = None
    
    photo: "Attachment" = None
    
    contact: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationship: "CodeableConcept" = None
    
    name: "HumanName" = None
    
    telecom: "ContactPoint" = None
    
    address: "Address" = None
    
    gender: str = None
    
    organization: "Reference" = None
    
    period: "Period" = None
    
    communication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: "CodeableConcept" = None
    
    preferred: bool = None
    
    generalPractitioner: "Reference" = None
    
    managingOrganization: "Reference" = None
    
    link: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    other: "Reference" = None
    
    type: str = None
    