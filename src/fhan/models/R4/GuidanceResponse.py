"""
Generated class for GuidanceResponse. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
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
    :param str moduleUri: What guidance was requested
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

    resourceType: str = "GuidanceResponse"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    requestIdentifier: "Identifier" = Identifier()
    
    identifier: list[Identifier] = Identifier() 
    
    moduleUri: str = None
    
    status: str = None
    
    subject: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    occurrenceDateTime: str = None
    
    performer: "Reference" = Reference()
    
    reasonCode: list[CodeableConcept] = CodeableConcept() 
    
    reasonReference: list[Reference] = Reference() 
    
    note: list[Annotation] = Annotation() 
    
    evaluationMessage: list[Reference] = Reference() 
    
    outputParameters: "Reference" = Reference()
    
    result: "Reference" = Reference()
    
    dataRequirement: list[DataRequirement] = DataRequirement() 
    