"""
Generated class for BodyStructure. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class BodyStructure(DomainResource):
    """ Record details about an anatomical structure.  This resource may be used when a coded concept does not provide the necessary detail needed for the use case.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Bodystructure identifier
    :param bool active: Whether this record is in active use
    :param 'CodeableConcept' morphology: Kind of Structure
    :param 'CodeableConcept' location: Body site
    :param list['CodeableConcept'] locationQualifier: Body site modifier
    :param str description: Text description
    :param list['Attachment'] image: Attached images
    :param 'Reference' patient: Who this is about
    """
    def __init__(self, resourceType: str = "BodyStructure",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  active: bool = None,  morphology: 'CodeableConcept' = None,  location: 'CodeableConcept' = None,  locationQualifier: list['CodeableConcept'] = None,  description: str = None,  image: list['Attachment'] = None,  patient: 'Reference' = None, ):
        self.resourceType: str = resourceType or "BodyStructure"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.active: bool = active 
        self.morphology: 'CodeableConcept' = morphology 
        self.location: 'CodeableConcept' = location 
        self.locationQualifier: list['CodeableConcept'] = locationQualifier or []
        self.description: str = description 
        self.image: list['Attachment'] = image or []
        self.patient: 'Reference' = patient 
        