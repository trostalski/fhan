import pytest

from fhan.client import Client
from fhan.models.R4 import Patient
from fhan.client import SearchBundle

TEST_SERVER_URL = "https://hapi.fhir.org/baseR4"


@pytest.fixture
def client():
    client = Client(base_url=TEST_SERVER_URL, authenticate=False)
    return client


def test_get_patient_by_id(client: Client):
    patient = client.get(resource_type="Patient", id="592817")
    assert patient is not None
    assert patient["resourceType"] == "Patient"
    assert patient["id"] == "592817"


def test_get_patient_by_id_as_object(client: Client):
    patient = client.get(resource_type="Patient", id="592817", as_object=True)
    assert patient is not None
    assert isinstance(patient, Patient)
    assert patient.id == "592817"


def test_search_patients_by_multiple_ids(client: Client):
    patient_bundle = client.get(resource_type="Patient", id=["592817", "592825"])
    assert patient_bundle is not None
    assert patient_bundle["resourceType"] == "Bundle"
    assert patient_bundle["type"] == "searchset"


def test_search_as_object(client: Client):
    patient_bundle = client.get(
        resource_type="Patient", id=["592817", "592825"], as_object=True
    )
    assert patient_bundle is not None
    assert isinstance(patient_bundle, SearchBundle)
    assert patient_bundle.size == 2


def test_search_with_search_params(client: Client):
    bundle = client.get(
        resource_type="Condition",
        search_params={
            "_count": 4,
            "code": "8310-5",
            "_revinclude": "Condition:subject",
        },
    )
    assert bundle is not None
    assert bundle["resourceType"] == "Bundle"
    assert bundle["type"] == "searchset"


def test_search_multiple_pages(client: Client):
    bundle = client.get(
        resource_type="Condition",
        pages=2,
    )
    assert bundle is not None
    assert bundle["resourceType"] == "Bundle"
