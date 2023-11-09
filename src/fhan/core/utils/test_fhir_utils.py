import pytest

from fhan.core.utils.fhir_utils import is_bundle, is_empty_bundle, safe_get


# Tests for is_bundle
@pytest.mark.parametrize(
    "input, expected",
    [
        ({"resourceType": "Bundle"}, True),
        ({"resourceType": "NotABundle"}, False),
        ([], False),
        ("Not a dict", False),
        ({}, False),
        ({"resourceType": "Bundle", "otherKey": "value"}, True),
    ],
)
def test_is_bundle(input, expected):
    assert is_bundle(input) == expected


# Tests for is_empty_bundle
@pytest.mark.parametrize(
    "input, expected",
    [
        ({"resourceType": "Bundle", "entry": []}, True),
        ({"resourceType": "Bundle", "entry": [1, 2, 3]}, False),
        ({"resourceType": "Bundle"}, True),
        ({"resourceType": "NotABundle", "entry": []}, True),
        ({}, True),
        ({"resourceType": "Bundle", "otherKey": "value"}, True),
    ],
)
def test_is_empty_bundle(input, expected):
    assert is_empty_bundle(input) == expected


# Tests for safe_get
@pytest.mark.parametrize(
    "target, attrs, expected",
    [
        ({"a": {"b": {"c": 1}}}, ("a", "b", "c"), 1),
        ({"a": {"b": {"c": 1}}}, ("a", "b"), {"c": 1}),
        ({"a": {"b": {"c": 1}}}, ("a",), {"b": {"c": 1}}),
        ({"a": {"b": {"c": 1}}}, ("a", "b", "c", "d"), None),
        ({"a": {"b": {"c": 1}}}, ("a", "x"), None),
        ([{"a": {"b": {"c": 1}}}], (0, "a", "b", "c"), 1),
        ([], (0,), None),
        ([{"a": {"b": {"c": 1}}}], (1,), None),
        ({"a": [{"b": {"c": 1}}]}, ("a", 0, "b", "c"), 1),
        ({"a": [{"b": {"c": 1}}]}, ("a", 0, "b", "d"), None),
        ({"a": [{"b": {"c": 1}}]}, ("a", 1, "b", "c"), None),
        ([], (0, "a", "b", "c"), None),
    ],
)
def test_safe_get(target, attrs, expected):
    assert safe_get(target, *attrs) == expected
