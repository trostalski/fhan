from fhan.models.R4 import CapabilityStatement


class ServerMetadata:
    """
    Parses the metadata from a FHIR server.
    """

    def __init__(self, cap_statement: CapabilityStatement):
        self._cap_statement = cap_statement
        self._set_available_functionality()

    def _set_available_functionality(
        self,
    ) -> None:
        available_resource_types = []
        available_search_params = {}
        available_includes = {}
        available_revincludes = {}
        rests = self._cap_statement.rest
        for rest in rests:
            for resource in rest.resource:
                available_resource_types.append(resource.type)
                available_search_params[resource.type] = [
                    sp.name for sp in resource.searchParam
                ]
                available_includes[resource.type] = [
                    inc.replace(".", ":") for inc in resource.searchInclude
                ]
                available_revincludes[resource.type] = [
                    revinc.replace(".", ":") for revinc in resource.searchRevInclude
                ]
        available_resource_types = list(set(available_resource_types))

        self.available_resource_types = available_resource_types
        self.available_search_params = available_search_params
        self.available_includes = available_includes
        self.available_revincludes = available_revincludes
