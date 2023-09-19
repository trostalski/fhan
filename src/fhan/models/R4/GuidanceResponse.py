"""
Generated class for GuidanceResponse. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DataRequirement import *
from fhan.models.generator_models import ModelBase


@dataclass
class GuidanceResponse(ModelBase):
    """ A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier requestIdentifier: The identifier of the request associated with this response, if any
    :param Identifier identifier: Business identifier
    :param str moduleuri: What guidance was requested
    :param str moduleuri: What guidance was requested
    :param CodeableConcept moduleuri: What guidance was requested
    :param str status: success | data-requested | data-required | in-progress | failure | entered-in-error
    :param Reference subject: Patient the request was performed for
    :param Reference encounter: Encounter during which the response was returned
    :param str occurrenceDateTime: When the guidance response was processed
    :param Reference performer: Device returning the guidance
    :param CodeableConcept reasonCode: Why guidance is needed
    :param Reference reasonReference: Why guidance is needed
    :param Annotation note: Additional notes about the response
    :param Reference evaluationMessage: Messages resulting from the evaluation of the artifact or artifacts
    :param Reference outputParameters: The output parameters of the evaluation, if any
    :param Reference result: Proposed actions, if any
    :param DataRequirement dataRequirement: Additional required data
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    requestIdentifier: "Identifier" = None
    
    identifier: "Identifier" = None
    
    moduleuri: str = None
    
    moduleuri: str = None
    
    moduleuri: "CodeableConcept" = None
    
    status: str = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrenceDateTime: str = None
    
    performer: "Reference" = None
    
    reasonCode: "CodeableConcept" = None
    
    reasonReference: "Reference" = None
    
    note: "Annotation" = None
    
    evaluationMessage: "Reference" = None
    
    outputParameters: "Reference" = None
    
    result: "Reference" = None
    
    dataRequirement: "DataRequirement" = None
    