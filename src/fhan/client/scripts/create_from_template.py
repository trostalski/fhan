import os
import sys
from fhan.core.fhir_package import FhirPackageLoader
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from dataclasses import dataclass

from fhan.core.fhir_package import FhirPackageLoader

MODIFIER_CODE_SYSTEM_URL = "http://hl7.org/fhir/search-modifier-code"
COMPARATOR_CODE_SYSTEM_URL = "http://hl7.org/fhir/search-comparator"

PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR_NAME = "templates"
TEMPLATE_DIR = os.path.join(PACKAGE_PATH, TEMPLATE_DIR_NAME)
OUTPUT_DIR = os.path.join(PACKAGE_PATH, "..", "generated")


def get_template(template_name: str):
    """Get a jinja2 template from the template_dir by name."""
    env = Environment(loader=FileSystemLoader(searchpath=TEMPLATE_DIR))
    template = env.get_template(template_name)
    return template


def get_resource_types_from_struc_defs(version: str):
    loader = FhirPackageLoader()
    package = loader.load_package_from_version(fhir_version=version)
    structure_definition = package.structure_definitions
    resource_types = [
        sd["type"] for sd in structure_definition if sd["kind"] == "resource"
    ]
    resource_types = list(set(resource_types))
    return resource_types


def get_resource_types_from_cap_stat(version: str):
    loader = FhirPackageLoader()
    package = loader.load_package_from_version(fhir_version=version)
    base_cap_stat = [cs for cs in package.capability_statements if cs["id"] == "base"][
        0
    ]
    resource_types = [
        resource["type"] for resource in base_cap_stat["rest"][0]["resource"]
    ]
    resource_types.sort()
    return resource_types


def create_search_builder(
    version: str,
    template_name: str,
    output_file_name: str,
):
    @dataclass
    class ResourceRequest:
        resource_type: str
        params: list[str]
        includes: list[str]
        revincludes: list[str]

    template = get_template(template_name=template_name)
    loader = FhirPackageLoader()
    package = loader.load_package_from_version(fhir_version=version)
    # extract comparators, modifiers and params from package
    base_cap_statement = [
        cs for cs in package.capability_statements if cs["id"] == "base"
    ][0]
    modifier_code_system = package.get_codesystem_by_url(
        MODIFIER_CODE_SYSTEM_URL
    )  # specified here https://build.fhir.org/search.html#modifiers
    comparator_code_system = package.get_codesystem_by_url(
        COMPARATOR_CODE_SYSTEM_URL
    )  # analogous to modifier_code_system

    modifiers = [c["code"] for c in modifier_code_system["concept"]]
    comparators = [c["code"] for c in comparator_code_system["concept"]]
    default_params = [
        param["name"] for param in base_cap_statement["rest"][0]["searchParam"]
    ]
    resource_requests = []
    for resource in base_cap_statement["rest"][0]["resource"]:
        resource_type = resource["type"]
        params = default_params.copy()
        includes = []
        revincludes = []
        for search_param in resource.get("searchParam", []):
            params.append(search_param["name"])
        for search_include in resource.get("searchInclude", []):
            # TODO: hapi.fhir.org/baseR4 expects the format "_include=RT:value", check if this is always the case
            includes.append(search_include.replace(".", ":"))
        for search_revinclude in resource.get("searchRevInclude", []):
            revincludes.append(search_revinclude.replace(".", ":"))
        resource_requests.append(
            ResourceRequest(
                resource_type=resource_type,
                params=params,
                includes=includes or [""],
                revincludes=revincludes or [""],
            )
        )

    res = template.render(
        resource_requests=resource_requests,
        time=datetime.now(),
        source_script=__file__,
        modifiers=modifiers,
        comparators=comparators,
    )
    output_file = os.path.join(OUTPUT_DIR, output_file_name)
    with open(output_file, "w") as f:
        f.write(res)


def create_search_builder_mixin(
    version: str,
    template_name: str,
    output_file_name: str,
    search_builder_import_path: str,
):
    """Creates SearchBuilderMixin class from template."""
    template = get_template(template_name)
    resource_types = get_resource_types_from_cap_stat(version=version)
    resource_types.sort()
    res = template.render(
        resource_types=resource_types,
        time=datetime.now(),
        source_script=__file__,
        search_builder_import_path=search_builder_import_path,
    )
    output_file = os.path.join(OUTPUT_DIR, output_file_name)
    with open(output_file, "w") as f:
        f.write(res)


def create_resource_mixin(
    version: str,
    template_name: str,
    output_file_name: str,
    model_import_path: str,
):
    """Creates the GetResourceMixin or SearchResourceMixin class from template
    based on the template name input."""
    template = get_template(template_name)
    resource_types = get_resource_types_from_cap_stat(version=version)
    resource_types.sort()
    res = template.render(
        resource_types=resource_types,
        time=datetime.now(),
        source_script=__file__,
        model_import_path=model_import_path,
    )
    output_file = os.path.join(OUTPUT_DIR, output_file_name)
    with open(output_file, "w") as f:
        f.write(res)


if __name__ == "__main__":
    template_settings = {
        "GRM": {  # -> Get Resource Mixin
            "creator_func": create_resource_mixin,
            "version": "R4",
            "output_file_name": "get_resource_mixin.py",
            "template_name": "get_resource_mixin.j2",
            "model_import_path": "fhan.models.R4",
        },
        "SRM": {  # -> Search Resource Mixin
            "creator_func": create_resource_mixin,
            "version": "R4",
            "output_file_name": "search_resource_mixin.py",
            "template_name": "search_resource_mixin.j2",
            "model_import_path": "fhan.client.search_bundle",
        },
        "SBM": {  # -> Search Builder Mixin
            "creator_func": create_search_builder_mixin,
            "version": "R5",
            "output_file_name": "search_builder_mixin.py",
            "template_name": "search_builder_mixin.j2",
            "search_builder_import_path": "fhan.client.generated.search_builder",
        },
        "SB": {  # -> Search Builder
            "creator_func": create_search_builder,
            "version": "R5",
            "output_file_name": "search_builder.py",
            "template_name": "search_builder.j2",
        },
    }
    args = sys.argv[1:]
    if args[0] not in template_settings:
        raise ValueError(
            f"Invalid argument. Supported arguments: {list(template_settings.keys())}"
        )
    settings = template_settings[args[0]]
    func = settings.pop("creator_func")
    func(**settings)
