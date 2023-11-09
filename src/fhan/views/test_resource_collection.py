import pytest
from fhan.views.resource_collection import (
    ResourceCollection,
)  # Replace 'your_module' with the actual module name where ResourceCollection is located

# Mock data for the tests
mock_bundle = {
    "entry": [
        {"resource": {"resourceType": "Patient", "id": "patient1"}},
        {"resource": {"resourceType": "Observation", "id": "observation1"}},
        {"resource": {"resourceType": "Patient", "id": "patient2"}},
        {"resource": {"resourceType": "Condition", "id": "condition1"}},
        # Add an entry without a resource to test the filtering in from_bundle
    ]
}

mock_resources = [
    {"resourceType": "Patient", "id": "patient1"},
    {"resourceType": "Observation", "id": "observation1"},
    {"resourceType": "Patient", "id": "patient2"},
    {"resourceType": "Condition", "id": "condition1"},
]


# Test __init__ and __iter__ together
def test_resource_collection_init_and_iter():
    resource_collection = ResourceCollection(mock_resources)
    assert list(resource_collection) == mock_resources


# Test from_bundle class method
def test_from_bundle():
    resource_collection = ResourceCollection.from_bundle(mock_bundle)
    assert list(resource_collection) == [
        entry["resource"] for entry in mock_bundle["entry"] if "resource" in entry
    ]


# Test get_resources_by_type method
@pytest.mark.parametrize(
    "resource_type, expected_count",
    [("Patient", 2), ("Observation", 1), ("Condition", 1), ("NonExistentType", 0)],
)
def test_get_resources_by_type(resource_type, expected_count):
    resource_collection = ResourceCollection(mock_resources)
    filtered_resources = resource_collection.get_resources_by_type(resource_type)
    assert len(filtered_resources) == expected_count
    assert all(
        resource["resourceType"] == resource_type for resource in filtered_resources
    )


# Test filter_resources method
def test_filter_resources():
    resource_collection = ResourceCollection(mock_resources)
    # Filter out only Patients
    resource_collection.filter_resources(lambda res: res["resourceType"] == "Patient")
    filtered_resources = list(resource_collection)
    assert all(resource["resourceType"] == "Patient" for resource in filtered_resources)
    assert len(filtered_resources) == 2
