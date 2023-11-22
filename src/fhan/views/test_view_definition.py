import pytest
from fhan.views.view_definition import (
    Constant,
    Tag,
    Column,
    Select,
    Where,
    ViewDefinition,
)

# Assuming 'your_module' is the module where the classes are defined.


def test_constant_creation():
    constant = Constant(name="test", value=42)
    assert constant.name == "test"
    assert constant.value == 42


def test_tag_creation():
    tag = Tag(name="test", value="value")
    assert tag.name == "test"
    assert tag.value == "value"


def test_column_creation_and_validation():
    column = Column(path="Patient.name", name="patientName")
    assert column.is_valid()
    column.validate()

    # Testing missing name
    path = "Patient.name"
    column = Column(path=path, name="")
    assert column.name == path


def test_definition_with_duplicate_column_names():
    view_def = {
        "resource": "Patient",
        "select": [
            {"column": [{"path": "Patient.name", "name": "patientName"}]},
            {"column": [{"path": "Patient.name", "name": "patientName"}]},
        ],
    }
    view_def = ViewDefinition(
        **view_def,
    )
    assert not view_def.is_valid()
    with pytest.raises(Exception):
        view_def.validate()


def test_view_definition_creation_validation_and_dict_conversion():
    constant = Constant(name="test", value=42)
    column = Column(path="Patient.name", name="patientName")
    select = Select(column=[column])
    where = Where(path="Patient.active = true")

    view_def = ViewDefinition(
        resource="Patient", select=[select], where=[where], constant=[constant]
    )
    assert view_def.is_valid()
    view_def.validate()
    view_def_dict = view_def.as_dict()
    assert view_def_dict["resource"] == "Patient"
    assert view_def_dict["select"][0]["column"][0]["path"] == "Patient.name"
    assert view_def_dict["where"][0]["path"] == "Patient.active = true"
    assert view_def_dict["constant"][0]["name"] == "test"

    # Testing invalid ViewDefinition
    view_def_invalid = ViewDefinition()
    assert not view_def_invalid.is_valid()
    with pytest.raises(Exception):
        view_def_invalid.validate()
