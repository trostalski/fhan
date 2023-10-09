from typing import Literal

from fhan.core.fhir_types import _ResourceType
from fhirpathpy import evaluate


class SearchBundle:
    def __init__(self, bundle: dict):
        self.bundle = bundle
        self.resources = [e["resource"] for e in bundle["entry"]]

    def __repr__(self) -> str:
        return f"SearchBundle({self.bundle})"

    @property
    def resouce_count(self) -> int:
        return len(self.resources)

    def get_resources(self, resource_type: Literal[_ResourceType]):
        return [r for r in self.resources if r["resourceType"] == resource_type]

    def get_path(self, path: str):
        if not path.startswith("entry.resource"):
            path = f"entry.resource.{path}"
        return evaluate(self.bundle, path)

    def get_paths(self, paths: list[str]):
        return [self.get_path(path) for path in paths]
