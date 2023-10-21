"""
Generated class for GuidanceResponse. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.DataRequirement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class GuidanceResponse(DomainResource):
    """A guidance response is the formal response to a guidance request, including any output parameters returned by the evaluation, as well as the description of any proposed actions to be taken.
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
    :param str moduleCanonical: What guidance was requested
    :param CodeableConcept moduleCodeableConcept: What guidance was requested
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

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "requestIdentifier": {"class_name": "Identifier", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "moduleCodeableConcept": {
            "class_name": "CodeableConcept",
            "is_contained": False,
        },
        "subject": {"class_name": "Reference", "is_contained": False},
        "encounter": {"class_name": "Reference", "is_contained": False},
        "performer": {"class_name": "Reference", "is_contained": False},
        "reasonCode": {"class_name": "CodeableConcept", "is_contained": False},
        "reasonReference": {"class_name": "Reference", "is_contained": False},
        "note": {"class_name": "Annotation", "is_contained": False},
        "evaluationMessage": {"class_name": "Reference", "is_contained": False},
        "outputParameters": {"class_name": "Reference", "is_contained": False},
        "result": {"class_name": "Reference", "is_contained": False},
        "dataRequirement": {"class_name": "DataRequirement", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        meta: "Meta" = None,
        implicitRules: "str" = None,
        language: "str" = None,
        text: "Narrative" = None,
        contained: list["Resource"] = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        requestIdentifier: "Identifier" = None,
        identifier: list["Identifier"] = None,
        moduleUri: "str" = None,
        moduleCanonical: "str" = None,
        moduleCodeableConcept: "CodeableConcept" = None,
        status: "str" = None,
        subject: "Reference" = None,
        encounter: "Reference" = None,
        occurrenceDateTime: "str" = None,
        performer: "Reference" = None,
        reasonCode: list["CodeableConcept"] = None,
        reasonReference: list["Reference"] = None,
        note: list["Annotation"] = None,
        evaluationMessage: list["Reference"] = None,
        outputParameters: "Reference" = None,
        result: "Reference" = None,
        dataRequirement: list["DataRequirement"] = None,
    ):
        self.resourceType = resourceType or "GuidanceResponse"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.requestIdentifier = requestIdentifier
        self.identifier = identifier or []
        self.moduleUri = moduleUri
        self.moduleCanonical = moduleCanonical
        self.moduleCodeableConcept = moduleCodeableConcept
        self.status = status
        self.subject = subject
        self.encounter = encounter
        self.occurrenceDateTime = occurrenceDateTime
        self.performer = performer
        self.reasonCode = reasonCode or []
        self.reasonReference = reasonReference or []
        self.note = note or []
        self.evaluationMessage = evaluationMessage or []
        self.outputParameters = outputParameters
        self.result = result
        self.dataRequirement = dataRequirement or []

    @classmethod
    def from_dict(cls, data: dict) -> "GuidanceResponse":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "GuidanceResponse":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
