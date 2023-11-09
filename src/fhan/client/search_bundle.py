from typing import TypeVar, Generic, List, Dict, Any

from fhirpathpy import evaluate

from fhan.core.utils.fhir_utils import is_bundle, is_empty_bundle


class SearchBundle:
    def __init__(self, bundle: Dict[str, Any], search_string: str = None):
        if not is_bundle(bundle):
            raise ValueError("Invalid bundle provided to SearchBundle.")
        self.bundle = bundle
        if not is_empty_bundle(bundle):
            self.resources: List[dict] = [
                e["resource"] for e in bundle["entry"] if "resource" in e
            ]
        else:
            self.resources = []

    def __repr__(self) -> str:
        return f"SearchBundle({self.bundle})"

    @property
    def id(self) -> str:
        return self.bundle["id"]

    @property
    def size(self) -> int:
        return len(self.resources)

    def get_resources_by_type(self, resource_type: str) -> List[dict]:
        return [r for r in self.resources if r["resourceType"] == resource_type]

    def get_path(self, path: str) -> Any:
        if not path.startswith("entry.resource"):
            path = f"entry.resource.{path}"
        return evaluate(self.bundle, path)

    def get_paths(self, paths: List[str]) -> List[Any]:
        if isinstance(paths, str):
            paths = [paths]
        return [self.get_path(path) for path in paths]
