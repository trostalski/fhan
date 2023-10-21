"""
Generated class for ExampleScenario. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


class Actor(BaseModel):
    """Actor participating in the resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str actorId: ID or acronym of the actor
    :param str type: person | entity
    :param str name: The name of the actor as shown in the page
    :param str description: The description of the actor
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        actorId: "str" = None,
        type: "str" = None,
        name: "str" = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.actorId = actorId
        self.type = type
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Version(BaseModel):
    """A specific version of the resource.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str versionId: The identifier of a specific version of a resource
    :param str description: The description of the resource version
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        versionId: "str" = None,
        description: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.versionId = versionId
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ContainedInstance(BaseModel):
    """Resources contained in the instance (e.g. the observations contained in a bundle).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: Each resource contained in the instance
    :param str versionId: A specific version of a resource contained in the instance
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        resourceId: "str" = None,
        versionId: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.resourceId = resourceId
        self.versionId = versionId

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Instance(BaseModel):
    """Each resource and each version that is present in the workflow.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str resourceId: The id of the resource for referencing
    :param str resourceType: The type of the resource
    :param str name: A short name for the resource instance
    :param str description: Human-friendly description of the resource instance
    :param Version version: A specific version of the resource
    :param ContainedInstance containedInstance: Resources contained in the instance
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "version": {"class_name": "Version", "is_contained": True},
        "containedInstance": {"class_name": "ContainedInstance", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        resourceId: "str" = None,
        resourceType: "str" = None,
        name: "str" = None,
        description: "str" = None,
        version: list["Version"] = None,
        containedInstance: list["ContainedInstance"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.resourceId = resourceId
        self.resourceType = resourceType
        self.name = name
        self.description = description
        self.version = version or []
        self.containedInstance = containedInstance or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Operation(BaseModel):
    """Each interaction or action.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str number: The sequential number of the interaction
    :param str type: The type of operation - CRUD
    :param str name: The human-friendly name of the interaction
    :param str initiator: Who starts the transaction
    :param str receiver: Who receives the transaction
    :param str description: A comment to be inserted in the diagram
    :param bool initiatorActive: Whether the initiator is deactivated right after the transaction
    :param bool receiverActive: Whether the receiver is deactivated right after the transaction
    :param Request request: Each resource instance used by the initiator
    :param Response response: Each resource instance used by the responder
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "request": {"class_name": "Request", "is_contained": True},
        "response": {"class_name": "Response", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        number: "str" = None,
        type: "str" = None,
        name: "str" = None,
        initiator: "str" = None,
        receiver: "str" = None,
        description: "str" = None,
        initiatorActive: "bool" = None,
        receiverActive: "bool" = None,
        request: "Request" = None,
        response: "Response" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.number = number
        self.type = type
        self.name = name
        self.initiator = initiator
        self.receiver = receiver
        self.description = description
        self.initiatorActive = initiatorActive
        self.receiverActive = receiverActive
        self.request = request
        self.response = response

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Alternative(BaseModel):
    """Indicates an alternative step that can be taken instead of the operations on the base step in exceptional/atypical circumstances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: Label for alternative
    :param str description: A human-readable description of each option
    :param Step step: What happens in each alternative option
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "step": {"class_name": "Step", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        title: "str" = None,
        description: "str" = None,
        step: list["Step"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title
        self.description = description
        self.step = step or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Step(BaseModel):
    """Each step of the process.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Process process: Nested process
    :param bool pause: If there is a pause in the flow
    :param Operation operation: Each interaction or action
    :param Alternative alternative: Alternate non-typical step action
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "process": {"class_name": "Process", "is_contained": True},
        "operation": {"class_name": "Operation", "is_contained": True},
        "alternative": {"class_name": "Alternative", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        process: list["Process"] = None,
        pause: "bool" = None,
        operation: "Operation" = None,
        alternative: list["Alternative"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.process = process or []
        self.pause = pause
        self.operation = operation
        self.alternative = alternative or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Process(BaseModel):
    """Each major process - a group of operations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str title: The diagram title of the group of operations
    :param str description: A longer description of the group of operations
    :param str preConditions: Description of initial status before the process starts
    :param str postConditions: Description of final status after the process ends
    :param Step step: Each step of the process
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "step": {"class_name": "Step", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        title: "str" = None,
        description: "str" = None,
        preConditions: "str" = None,
        postConditions: "str" = None,
        step: list["Step"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.title = title
        self.description = description
        self.preConditions = preConditions
        self.postConditions = postConditions
        self.step = step or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class ExampleScenario(DomainResource):
    """Example of workflow instance.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this example scenario, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the example scenario
    :param str version: Business version of the example scenario
    :param str name: Name for this example scenario (computer friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for example scenario (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str purpose: The purpose of the example, e.g. to illustrate a scenario
    :param Actor actor: Actor participating in the resource
    :param Instance instance: Each resource and each version that is present in the workflow
    :param Process process: Each major process - a group of operations
    :param str workflow: Another nested workflow
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "actor": {"class_name": "Actor", "is_contained": True},
        "instance": {"class_name": "Instance", "is_contained": True},
        "process": {"class_name": "Process", "is_contained": True},
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
        url: "str" = None,
        identifier: list["Identifier"] = None,
        version: "str" = None,
        name: "str" = None,
        status: "str" = None,
        experimental: "bool" = None,
        date: "str" = None,
        publisher: "str" = None,
        contact: list["ContactDetail"] = None,
        useContext: list["UsageContext"] = None,
        jurisdiction: list["CodeableConcept"] = None,
        copyright: "str" = None,
        purpose: "str" = None,
        actor: list["Actor"] = None,
        instance: list["Instance"] = None,
        process: list["Process"] = None,
        workflow: list["str"] = None,
    ):
        self.resourceType = resourceType or "ExampleScenario"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url
        self.identifier = identifier or []
        self.version = version
        self.name = name
        self.status = status
        self.experimental = experimental
        self.date = date
        self.publisher = publisher
        self.contact = contact or []
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.copyright = copyright
        self.purpose = purpose
        self.actor = actor or []
        self.instance = instance or []
        self.process = process or []
        self.workflow = workflow or []

    @classmethod
    def from_dict(cls, data: dict) -> "ExampleScenario":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ExampleScenario":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
