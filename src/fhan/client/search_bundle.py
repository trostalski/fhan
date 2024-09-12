from typing import Any, Dict, List

from fhan.client import utils
from fhan.client.resource_type import _ResourceType


class SearchBundle:
    def __init__(self, bundle: Dict[str, Any], search_string: str = None):
        if not utils.is_bundle(bundle):
            raise ValueError("Invalid bundle provided to SearchBundle.")
        self.bundle = bundle
        if not utils.is_empty_bundle(bundle):
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

    def get_resources_by_type(self, resource_type: _ResourceType) -> List[dict]:
        return [r for r in self.resources if r["resourceType"] == resource_type]

    def get_paths(self, paths: List[str]) -> List[Any]:
        if isinstance(paths, str):
            paths = [paths]
        return [self.get_path(path) for path in paths]

    def get_path(self, path: str) -> Any:
        def traverse(obj: Any, keys: List[str]) -> Any:
            if not keys:
                return obj
            key = keys[0]
            if isinstance(obj, dict):
                return traverse(obj.get(key), keys[1:])
            elif isinstance(obj, list):
                try:
                    index = int(key)
                    return traverse(obj[index], keys[1:])
                except (ValueError, IndexError):
                    return None
            else:
                return None

        keys = path.split(".")
        return traverse(self.bundle, keys)
