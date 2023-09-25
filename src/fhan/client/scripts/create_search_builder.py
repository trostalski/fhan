import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

from fhan.core.fhir_package import FhirPackageLoader

VERSION_USED = "R5"
TEMPLATE_DIR_NAME = "templates"
TEMLPATE_NAME = "resource_getter.j2"
OUTPUT_FILE = "_resource_getter.py"
MODIFIER_CODE_SYSTEM_URL = "http://hl7.org/fhir/search-modifier-code"
COMPARATOR_CODE_SYSTEM_URL = "http://hl7.org/fhir/search-comparator"


def get_resource_types():
    loader = FhirPackageLoader()
    package = loader.load_package(version=VERSION_USED)

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
    resource_params = {}
    for resource in base_cap_statement["rest"][0]["resource"]:
        resource_type = resource["type"]
        params = []
        for search_param in resource["searchParam"]:
            params.append(search_param["name"])
        resource_params[resource_type] = params


def main():
    scripts_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(scripts_dir, TEMPLATE_DIR_NAME)
    env = Environment(loader=FileSystemLoader(searchpath=template_dir))
    template = env.get_template(TEMLPATE_NAME)
    resource_types = get_resource_types()
    # resource_types.sort()
    # res = template.render(
    #     resource_types=resource_types, time=datetime.now(), source_script=__file__
    # )
    # output_file = os.path.join(scripts_dir, "..", OUTPUT_FILE)
    # with open(output_file, "w") as f:
    #     f.write(res)


if __name__ == "__main__":
    main()
