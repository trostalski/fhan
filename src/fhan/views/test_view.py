from pandas import DataFrame
import pytest
from pandas.testing import assert_frame_equal
from fhan.views.resource_collection import ResourceCollection
from fhan.views.view import View, ViewResult

# Assuming there is a sample ViewDefinition and ResourceCollection to work with
sample_view_definition = {
    "resource": "Patient",
    "select": [
        {"column": [{"path": "Patient.name", "name": "familyName"}]},
        {"column": [{"path": "gender", "name": "gender"}]},
    ],
}

sample_fhir_data = {
    "resourceType": "Patient",
    "name": [{"family": "Doe"}],
}  # Add more fields as needed


# Tests for ViewResult
def test_view_result_initialization():
    table = {"familyName": ["Doe"]}
    view_result = ViewResult(view_definition=sample_view_definition, table=table)
    assert view_result.columns == ["familyName"]
    assert view_result["familyName"] == ["Doe"]


def test_view_result_to_dataframe():
    table = {"familyName": ["Doe"]}
    view_result = ViewResult(view_definition=sample_view_definition, table=table)
    df = view_result.to_dataframe()
    expected_df = DataFrame(table, columns=["familyName"])
    assert_frame_equal(df, expected_df)


def test_view_result_to_row_lists():
    table = {"familyName": ["Doe"]}
    view_result = ViewResult(view_definition=sample_view_definition, table=table)
    row_lists = view_result.to_row_lists()
    expected_row_lists = [{"familyName": "Doe"}]
    assert row_lists == expected_row_lists


def test_view_execute():
    view = View(view_definition=sample_view_definition)
    result = view.execute(fhir_input=sample_fhir_data)
    assert isinstance(result, ViewResult)
    # Test that the results are what you expect, based on the select and where definitions


def test_view_call():
    view = View(view_definition=sample_view_definition)
    result = view(sample_fhir_data)
    assert isinstance(result, ViewResult)
    # Further assertions can be made based on the expected behavior of the __call__ method


def test_view_constraints():
    # Assuming we have certain constraints that should filter the resource collection
    view = View(view_definition=sample_view_definition)
    # Execute the view to apply constraints
    view.execute(fhir_input=sample_fhir_data)
    # Now test that the resource collection within the view object is as expected
