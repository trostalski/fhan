class ResourceCollection:
    """
    Container for FHIR resources that abstracts resource collections from
    different sources, e.g. bundles, lists of resources.
    """

    def __init__(self, resources):
        self.resources = resources

    @classmethod
    def from_bundle(cls, bundle: dict):
        resources = []
        if bundle.get("entry"):
            resources = [
                entry["resource"] for entry in bundle["entry"] if "resource" in entry
            ]
        return cls(resources)

    def get_resources_by_type(self, resource_type: str):
        return [
            resource
            for resource in self.resources
            if resource["resourceType"] == resource_type
        ]

    def filter_resources(self, fn):
        self.resources = list(filter(fn, self.resources))

    def __iter__(self):
        return iter(self.resources)
