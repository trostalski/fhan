from fhan.views.view import View
from fhan.views.view_definition import (
    Column,
    Tag,
    ViewDefinition,
    Constant,
    Select,
    Where,
    validate_view_definition,
)
from fhan.core.fhir_types import _ResourceType


class ViewBuilder:
    """View builder to construct View objects. This should
    enable incremental view construction and validation.
    """

    def __init__(self, resource: _ResourceType):
        self._view_definition = ViewDefinition()
        self._view_definition.resource = resource
        self._view_definition.select = []
        self._view_definition.where = []
        self._view_definition.constant = []

    @property
    def resource(self):
        return self._view_definition.resource

    @property
    def select(self):
        return self._view_definition.select

    @property
    def where(self):
        return self._view_definition.where

    @property
    def constant(self):
        return self._view_definition.constant

    def add_select_column(
        self,
        path: str,
        name: str = None,
        description: str = None,
        type: str = None,
        tag_name: str = None,
        tag_value: str = None,
    ):
        tag = Tag(name=tag_name, value=tag_value)
        column = Column(
            path=path,
            name=name,
            description=description,
            type=type,
            tag=tag,
        )
        tag = Tag(name=tag_name, value=tag_value)
        select = Select(column=[column])
        self._view_definition.select.append(select)
        return self

    def add_where(self, path: str, description: str = None):
        where = Where(path=path, description=description)
        self._view_definition.where.append(where)
        return self

    def add_constant(self, name: str, value: str):
        constant = Constant(name=name, value=value)
        self._view_definition.constant.append(constant)
        return self

    def build(self, validate=True) -> View:
        if validate:
            self.validate()
        return View(view_definition=self._view_definition)

    def validate(self):
        [s.validate() for s in self._view_definition.select]
        [w.validate() for w in self._view_definition.where]
        validate_view_definition(self._view_definition)
