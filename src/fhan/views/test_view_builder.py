import pytest
from fhan.views.view import View
from fhan.views.view_definition import ViewDefinition, Column, Select, Where, Constant
from fhan.core.fhir_types import _ResourceType

# Import your ViewBuilder class here
from fhan.views.view_builder import ViewBuilder

# Make sure you have a valid _ResourceType for testing purposes.
valid_resource_type = "Patient"


def test_view_builder_initialization():
    view_builder = ViewBuilder(valid_resource_type)
    assert view_builder.resource == valid_resource_type
    assert isinstance(view_builder._view_definition, ViewDefinition)
    assert view_builder.select == []
    assert view_builder.where == []
    assert view_builder.constant == []


def test_add_select_column():
    view_builder = ViewBuilder(valid_resource_type)
    view_builder.add_select_column(
        path="Patient.name",
        name="patientName",
        description="Patient's Name",
        type="string",
        tag_name="exampleTag",
        tag_value="exampleValue",
    )
    assert len(view_builder.select) == 1
    column = view_builder.select[0].column[0]
    assert column.path == "Patient.name"
    assert column.name == "patientName"
    assert column.description == "Patient's Name"
    assert column.type == "string"
    assert column.tag.name == "exampleTag"
    assert column.tag.value == "exampleValue"


def test_add_where():
    view_builder = ViewBuilder(valid_resource_type)
    view_builder.add_where(path="Patient.active = true", description="Active Patients")
    assert len(view_builder.where) == 1
    where = view_builder.where[0]
    assert where.path == "Patient.active = true"
    assert where.description == "Active Patients"


def test_add_constant():
    view_builder = ViewBuilder(valid_resource_type)
    view_builder.add_constant(name="constValue", value="42")
    assert len(view_builder.constant) == 1
    constant = view_builder.constant[0]
    assert constant.name == "constValue"
    assert constant.value == "42"


def test_view_builder_build():
    view_builder = ViewBuilder(valid_resource_type)
    view_builder.add_select_column(path="Patient.name", name="patientName")
    view_builder.add_where(path="Patient.active = true")
    view_builder.add_constant(name="constValue", value="42")

    view = view_builder.build()
    assert view._view_definition.as_dict() == {
        "resource": "Patient",
        "uri": None,
        "identifier": None,
        "name": None,
        "version": None,
        "title": None,
        "status": None,
        "experimental": None,
        "publisher": None,
        "description": None,
        "copyright": None,
        "resourceVersion": None,
        "constant": [{"name": "constValue", "value": "42"}],
        "select": [
            {
                "column": [
                    {
                        "path": "Patient.name",
                        "name": "patientName",
                        "description": None,
                        "collection": None,
                        "type": None,
                        "tag": {"name": None, "value": None},
                    }
                ]
            }
        ],
        "where": [{"path": "Patient.active = true", "description": None}],
    }
    assert isinstance(view, View)
