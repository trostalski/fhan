"""
Generated class for TestReport. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.DomainResource import *


class Participant(BaseModel):
    """A participant in the test execution, either the execution engine, a client, or a server.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: test-engine | client | server
    :param str uri: The uri of the participant. An absolute URL is preferred
    :param str display: The display name of the participant
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
        type: "str" = None,
        uri: "str" = None,
        display: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type
        self.uri = uri
        self.display = display

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Operation(BaseModel):
    """The operation performed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
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
        result: "str" = None,
        message: "str" = None,
        detail: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.result = result
        self.message = message
        self.detail = detail

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class _assert(BaseModel):
    """The results of the assertion performed on the previous operations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str result: pass | skip | fail | warning | error
    :param str message: A message associated with the result
    :param str detail: A link to further details on the result
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
        result: "str" = None,
        message: "str" = None,
        detail: "str" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.result = result
        self.message = message
        self.detail = detail

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Action(BaseModel):
    """Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The operation to perform
    :param _assert _assert: The assertion to perform
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "operation": {"class_name": "Operation", "is_contained": True},
        "_assert": {"class_name": "_assert", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        operation: "Operation" = None,
        _assert: "_assert" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.operation = operation
        self._assert = _assert

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Setup(BaseModel):
    """The results of the series of required setup operations before the tests were executed.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: A setup operation or assert that was executed
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "Action", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        action: list["Action"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.action = action or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Action(BaseModel):
    """Action would contain either an operation or an assertion.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The operation performed
    :param _assert _assert: The assertion performed
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "operation": {"class_name": "Operation", "is_contained": True},
        "_assert": {"class_name": "_assert", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        operation: "Operation" = None,
        _assert: "_assert" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.operation = operation
        self._assert = _assert

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Test(BaseModel):
    """A test executed from the test script.:param Reference testScript: Reference to the  version-specific TestScript that was executed to produce this TestReport
    :param str tester: Name of the tester producing this report (Organization or individual)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: Tracking/logging name of this test
    :param str description: Tracking/reporting short description of the test
    :param Action action: A test operation or assert that was performed
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "testScript": {"class_name": "Reference", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "Action", "is_contained": True},
    }

    def __init__(
        self,
        testScript: "Reference" = None,
        tester: "str" = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        name: "str" = None,
        description: "str" = None,
        action: list["Action"] = None,
    ):
        self.testScript = testScript
        self.tester = tester
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.name = name
        self.description = description
        self.action = action or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Action(BaseModel):
    """The teardown action will only contain an operation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Operation operation: The teardown operation performed
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "operation": {"class_name": "Operation", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        operation: "Operation" = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.operation = operation

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Teardown(BaseModel):
    """The results of the series of operations required to clean up after all the tests were executed (successfully or otherwise).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Action action: One or more teardown operations performed
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "action": {"class_name": "Action", "is_contained": True},
    }

    def __init__(
        self,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        action: list["Action"] = None,
    ):
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.action = action or []

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class TestReport(DomainResource):
    """A summary of information based on the results of executing a TestScript.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: External identifier
    :param str name: Informal name of the executed TestScript
    :param str status: completed | in-progress | waiting | stopped | entered-in-error
    :param Reference testScript: Reference to the  version-specific TestScript that was executed to produce this TestReport
    :param str result: pass | fail | pending
    :param float score: The final score (percentage of tests passed) resulting from the execution of the TestScript
    :param str tester: Name of the tester producing this report (Organization or individual)
    :param str issued: When the TestScript was executed and this TestReport was generated
    :param Participant participant: A participant in the test execution, either the execution engine, a client, or a server
    :param Setup setup: The results of the series of required setup operations before the tests were executed
    :param Test test: A test executed from the test script
    :param Teardown teardown: The results of running the series of required clean up steps
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "meta": {"class_name": "Meta", "is_contained": False},
        "text": {"class_name": "Narrative", "is_contained": False},
        "contained": {"class_name": "Resource", "is_contained": False},
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "identifier": {"class_name": "Identifier", "is_contained": False},
        "testScript": {"class_name": "Reference", "is_contained": False},
        "participant": {"class_name": "Participant", "is_contained": True},
        "setup": {"class_name": "Setup", "is_contained": True},
        "test": {"class_name": "Test", "is_contained": True},
        "teardown": {"class_name": "Teardown", "is_contained": True},
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
        identifier: "Identifier" = None,
        name: "str" = None,
        status: "str" = None,
        testScript: "Reference" = None,
        result: "str" = None,
        score: "float" = None,
        tester: "str" = None,
        issued: "str" = None,
        participant: list["Participant"] = None,
        setup: "Setup" = None,
        test: list["Test"] = None,
        teardown: "Teardown" = None,
    ):
        self.resourceType = resourceType or "TestReport"
        self.id = id
        self.meta = meta
        self.implicitRules = implicitRules
        self.language = language
        self.text = text
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier
        self.name = name
        self.status = status
        self.testScript = testScript
        self.result = result
        self.score = score
        self.tester = tester
        self.issued = issued
        self.participant = participant or []
        self.setup = setup
        self.test = test or []
        self.teardown = teardown

    @classmethod
    def from_dict(cls, data: dict) -> "TestReport":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "TestReport":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
