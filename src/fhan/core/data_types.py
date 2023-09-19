import logging

logger = logging.getLogger(__name__)

PYTHON_KEYWORDS = [
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]


FHIR_PRIMITIVES_TO_PYTHON_MAP = {
    "base64Binary": str,
    "boolean": bool,
    "canonical": str,
    "code": str,
    "date": str,
    "dateTime": str,
    "decimal": float,
    "id": str,
    "instant": str,
    "integer": int,
    "integer64": int,
    "markdown": str,
    "oid": str,
    "positiveInt": int,
    "string": str,
    "time": str,
    "unsignedInt": int,
    "uri": str,
    "url": str,
    "uuid": str,
    "xhtml": str,
}

FHIR_PRIMITIVE_EXPANSION_MAP = {
    "http://hl7.org/fhirpath/System.String": "string",
    "http://hl7.org/fhirpath/System.Boolean": "boolean",
    "http://hl7.org/fhirpath/System.Integer": "integer",
    "http://hl7.org/fhirpath/System.Decimal": "decimal",
    "http://hl7.org/fhirpath/System.DateTime": "dateTime",
    "http://hl7.org/fhirpath/System.Date": "date",
    "http://hl7.org/fhirpath/System.Time": "time",
}


def get_python_type_for_primitive(fhir_type: str) -> type:
    """Returns the Python type for a FHIR primitive type."""
    if fhir_type in FHIR_PRIMITIVES_TO_PYTHON_MAP:
        return FHIR_PRIMITIVES_TO_PYTHON_MAP[fhir_type]
    elif fhir_type in FHIR_PRIMITIVE_EXPANSION_MAP:
        return FHIR_PRIMITIVES_TO_PYTHON_MAP[FHIR_PRIMITIVE_EXPANSION_MAP[fhir_type]]
    else:
        logging.warning("Unknown FHIR primitive type: %s", fhir_type)
        return str


def is_primitive_type(fhir_type: str) -> bool:
    """Returns True if the given FHIR type is a primitive type."""
    if fhir_type in FHIR_PRIMITIVES_TO_PYTHON_MAP:
        return True
    elif fhir_type in FHIR_PRIMITIVE_EXPANSION_MAP:
        return True
    else:
        return False
