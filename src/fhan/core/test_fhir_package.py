import pytest
import logging
from fhan.core.data_types import (
    get_python_type_for_primitive,
    is_primitive_type,
    FHIR_PRIMITIVES_TO_PYTHON_MAP,
    FHIR_PRIMITIVE_EXPANSION_MAP,
)

# You will have to replace 'your_module' with the actual name of the module where the functions are defined.


@pytest.mark.parametrize(
    "fhir_type, expected", list(FHIR_PRIMITIVES_TO_PYTHON_MAP.items())
)
def test_get_python_type_for_primitive(fhir_type, expected):
    assert get_python_type_for_primitive(fhir_type) is expected


@pytest.mark.parametrize(
    "fhir_type, expected",
    [
        *[(key, True) for key in FHIR_PRIMITIVES_TO_PYTHON_MAP.keys()],
        *[(key, True) for key in FHIR_PRIMITIVE_EXPANSION_MAP.keys()],
        ("nonExistentType", False),
    ],
)
def test_is_primitive_type(fhir_type, expected):
    assert is_primitive_type(fhir_type) is expected


# To include tests for expanded FHIR types
@pytest.mark.parametrize(
    "fhir_type, expected",
    [
        (key, FHIR_PRIMITIVES_TO_PYTHON_MAP[value])
        for key, value in FHIR_PRIMITIVE_EXPANSION_MAP.items()
    ],
)
def test_get_python_type_for_expanded_primitive(fhir_type, expected):
    assert get_python_type_for_primitive(fhir_type) is expected


# Optionally, you can test for logging the warning for unknown types
def test_get_python_type_for_unknown_primitive(caplog):
    unknown_type = "unknown"
    expected_type = str
    with caplog.at_level(logging.WARNING):
        assert get_python_type_for_primitive(unknown_type) is expected_type
        assert f"Unknown FHIR primitive type: {unknown_type}" in caplog.text
