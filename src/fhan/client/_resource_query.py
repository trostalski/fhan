from typing import Literal


class Value:
    """Should contain prefixes and joiners"""

    def __init__(self, query_string: str):
        self.query_string = query_string

    def equals(self, value: str, prefix: Literal["eq", "ne"] = ""):
        query_string = f"{prefix}{value}"
        return BooleanJoin()


class BooleanJoin:
    def __init__(self, query_string: str):
        self.query_string = query_string

    def __call__(self):
        return self.query_string

    def and_(self):
        return PatientQuery()

    def or_(self):
        return PatientQuery()


class PatientQuery:
    """Should include modifiers, and joiners"""

    def __init__(self, query_string: str):
        self.query_string = query_string

    def param(
        self,
        value: Literal[
            "active",
            "address",
            "address-city",
        ],
        modifier="",
    ):
        query_string = +value
        query_string += f":{modifier}"
        return Value()


class ResourceQueryMixin:
    def __init__(self):
        self.query_string = "?"

    @property
    @classmethod
    def Patient(self):
        return PatientQuery(self.query_string)
