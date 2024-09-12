import fhirmodels
import fhirmodels.R4
import pytest
import requests

from fhan.client.client import Client
from fhan.client.search_bundle import SearchBundle


@pytest.fixture
def client() -> Client:
    return Client(base_url="https://demo.kodjin.com/fhir", auth_method="basic")


def test_client_initialization(client: Client):
    assert client._base_url == "https://demo.kodjin.com/fhir"
    assert client.fhir_version == "R4"


def test_get_patient(client: Client):
    patient = client.get(resource_type="Patient", id="example")
    assert patient["resourceType"] == "Patient"
    assert "id" in patient


def test_search_patients(client: Client):
    search_result = client.get(resource_type="Patient", search_params={"_count": "5"})
    assert search_result["resourceType"] == "Bundle"
    assert len(search_result.get("entry", [])) <= 5


def test_get_with_search_string(client: Client):
    search_result = client.get(
        resource_type="Observation",
        search_string="code=http://loinc.org|8867-4",
    )
    assert search_result["resourceType"] == "Bundle"


def test_get_multiple_pages(client: Client):
    search_result = client.get(
        resource_type="Patient", search_params={"_count": "10"}, pages=2
    )
    assert search_result["resourceType"] == "Bundle"


def test_get_as_object_patient(client: Client):
    patient = client.get(resource_type="Patient", id="example", as_object=True)
    assert isinstance(patient, fhirmodels.R4.Patient)


def test_get_as_object_search(client: Client):
    search_result = client.get(
        resource_type="Patient",
        search_string="code=http://loinc.org|8867-4",
        as_object=True,
    )
    assert isinstance(search_result, SearchBundle)


def test_get_with_custom_headers(client: Client):
    custom_headers = {"X-Custom-Header": "test-value"}
    patient = client.get(resource_type="Patient", id="example", headers=custom_headers)
    assert patient["resourceType"] == "Patient"
    # Note: You can't assert the custom header was sent without mocking the request


def test_get_with_custom_token(client: Client):
    custom_token = "custom_test_token"
    patient = client.get(resource_type="Patient", id="example", token=custom_token)
    assert patient["resourceType"] == "Patient"
    # Note: You can't assert the custom token was used without mocking the request


def test_get_with_raise_for_status(client: Client):
    with pytest.raises(requests.exceptions.HTTPError):
        client.get(resource_type="Patient", id="non_existent_id", raise_for_status=True)


def test_get_specific_url(client: Client):
    specific_url = "/Patient/example"
    patient = client.get(url=specific_url)
    assert patient["resourceType"] == "Patient"
    assert patient["id"] == "example"
