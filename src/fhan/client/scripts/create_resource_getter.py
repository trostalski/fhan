import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

from fhan.core.fhir_package import FhirPackageLoader

VERSION_USED = "R5"
TEMPLATE_DIR_NAME = "templates"
TEMLPATE_NAME = "resource_getter.j2"
OUTPUT_FILE = "_resource_getter.py"


def get_resource_types():
    loader = FhirPackageLoader()
    package = loader.load_package(version=VERSION_USED)
    structure_definition = package.structure_definitions
    resource_types = [
        sd["type"] for sd in structure_definition if sd["kind"] == "resource"
    ]
    resource_types = list(set(resource_types))
    return resource_types


def main():
    scripts_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(scripts_dir, TEMPLATE_DIR_NAME)
    env = Environment(loader=FileSystemLoader(searchpath=template_dir))
    template = env.get_template(TEMLPATE_NAME)
    resource_types = get_resource_types()
    resource_types.sort()
    res = template.render(
        resource_types=resource_types, time=datetime.now(), source_script=__file__
    )
    output_file = os.path.join(scripts_dir, "..", OUTPUT_FILE)
    with open(output_file, "w") as f:
        f.write(res)


if __name__ == "__main__":
    main()
