"""
Generated class for ParameterDefinition. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.Extension import *
from fhan.models.generator_models import BaseModel


class ParameterDefinition(BaseModel):
    """Base StructureDefinition for ParameterDefinition Type: The parameters to the module. This collection specifies both the input and output parameters. Input parameters are provided by the caller as part of the $evaluate operation. Output parameters are included in the GuidanceResponse.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str name: Name used to access the parameter value
    :param str use: in | out
    :param int min: Minimum cardinality
    :param str max: Maximum cardinality (a number of *)
    :param str documentation: A brief description of the parameter
    :param str type: What type of value
    :param str profile: What profile the value is expected to be
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        name: "str" = None,
        use: "str" = None,
        min: "int" = None,
        max: "str" = None,
        documentation: "str" = None,
        type: "str" = None,
        profile: "str" = None,
    ):
        self.resourceType = resourceType or "ParameterDefinition"
        self.id = id
        self.extension = extension or []
        self.name = name
        self.use = use
        self.min = min
        self.max = max
        self.documentation = documentation
        self.type = type
        self.profile = profile

    @classmethod
    def from_dict(cls, data: dict) -> "ParameterDefinition":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "ParameterDefinition":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
