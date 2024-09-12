import pytest
import requests
from unittest.mock import Mock, patch
from fhirmodels.R4 import OperationOutcome, DetectedIssue
from fhan.client.utils import (
    join_urls,
    make_get_request,
    handle_operation_outcome,
    is_bundle,
    is_empty_bundle,
    safe_get,
    get_next_link,
    get_params_from_kwargs,
    incorporate_ids_in_search,
    convert_params_to_string,
)
from fhan.client.exceptions import OperationOutcomeException, RequestException

def test_join_urls():
    assert join_urls("http://example.com", "api", "v1") == "http://example.com/api/v1"
    assert join_urls("http://example.com/", "/api/", "/v1/") == "http://example.com/api/v1"
    assert join_urls("http://example.com", None, "v1") == "http://example.com/v1"

def test_make_get_request_json_decode_error():
    mock_response = Mock()
    mock_response.json.side_effect = requests.exceptions.JSONDecodeError("", "", 0)

    with patch("requests.get", return_value=mock_response):
        with pytest.raises(RequestException):
            make_get_request("http://example.com")

def test_is_bundle():
    assert is_bundle({"resourceType": "Bundle"}) == True
    assert is_bundle({"resourceType": "Patient"}) == False
    assert is_bundle("Not a dict") == False

def test_is_empty_bundle():
    assert is_empty_bundle({"entry": []}) == True
    assert is_empty_bundle({"entry": [{"resource": {}}]}) == False
    assert is_empty_bundle({}) == True

def test_safe_get():
    test_dict = {"a": {"b": {"c": 1}}}
    assert safe_get(test_dict, "a", "b", "c") == 1
    assert safe_get(test_dict, "a", "b", "d") == None
    assert safe_get(test_dict, "x", "y", "z") == None

    test_list = [1, [2, 3]]
    assert safe_get(test_list, 1, 0) == 2
    assert safe_get(test_list, 2, 0) == None

def test_get_next_link():
    bundle = {
        "link": [
            {"relation": "self", "url": "http://example.com/fhir/Patient?_count=50"},
            {"relation": "next", "url": "http://example.com/fhir/Patient?_count=50&_offset=50"}
        ]
    }
    assert get_next_link(bundle, "http://example.com") == "http://example.com/fhir/Patient?_count=50&_offset=50"
    assert get_next_link({}, "http://example.com") == None

def test_get_params_from_kwargs():
    kwargs = {"param1": "value1", "param2": "", "param3": None, "param4": "value4"}
    expected = {"_param1": "value1", "_param4": "value4"}
    assert get_params_from_kwargs(**kwargs) == expected

@pytest.mark.parametrize("id_input,search_string,expected", [
    ("123", "", "_id=123"),
    (["123", "456"], "name=John", "name=John_id=123,456"),
    (None, "name=John", "name=John"),
])
def test_incorporate_ids_in_search(id_input, search_string, expected):
    assert incorporate_ids_in_search(id_input, search_string) == expected

def test_convert_params_to_string():
    params = {"param1": "value1", "param2": "value2"}
    expected = "param1=value1&param2=value2"
    assert convert_params_to_string(params) == expected
