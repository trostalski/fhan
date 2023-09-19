"""
Generated class for Practitioner. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.ContactPoint import *
from fhan.models.R5.Address import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.HumanName import *
from fhan.models.R5.Reference import *


@dataclass
class Practitioner:
    """ A person who is directly or indirectly involved in the provisioning of healthcare or related services.
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
    :param str gender: male | female | other | unknown
    :param str birthDate: The date  on which the practitioner was born
    :param bool deceasedboolean: Indicates if the practitioner is deceased or not
    :param str deceasedboolean: Indicates if the practitioner is deceased or not
    :param Address address: Address(es) of the practitioner that are not role specific (typically home address)
    :param Attachment photo: Image of the person
    :param BackboneElement qualification: Qualifications, certifications, accreditations, licenses, training, etc. pertaining to the provision of care
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: An identifier for this qualification for the practitioner
    :param CodeableConcept code: Coded representation of the qualification
    :param Period period: Period during which the qualification is valid
    :param Reference issuer: Organization that regulates and issues the qualification
    :param BackboneElement communication: A language which may be used to communicate with the practitioner
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept language: The language code used to communicate with the practitioner
    :param bool preferred: Language preference indicator
    
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
    
    photo: "Attachment" = None
    
    qualification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    code: "CodeableConcept" = None
    
    period: "Period" = None
    
    issuer: "Reference" = None
    
    communication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    language: "CodeableConcept" = None
    
    preferred: bool = None
    