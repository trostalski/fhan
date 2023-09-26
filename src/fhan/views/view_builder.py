from fhan.views.view import View
from fhan.views.view_definition import (
    ViewDefinition,
    ViewDefinitionConstant,
    ViewDefinitionSelect,
    ViewDefinitionWhere,
    validate_view_definition,
)
from fhan.core.types import _ResourceType


class ViewBuilder:
    """View builder to construct ViewDefinition objects. This should
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

    def add_select(self, path: str, alias: str = None):
        select = ViewDefinitionSelect(path=path, alias=alias)
        self._view_definition.select.append(select)
        return self

    def add_where(self, path: str, description: str = None):
        where = ViewDefinitionWhere(path=path, description=description)
        self._view_definition.where.append(where)
        return self

    def add_constant(self, path: str, value: str, description: str = None):
        constant = ViewDefinitionConstant(
            path=path, value=value, description=description
        )
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
