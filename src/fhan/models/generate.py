from typing import Literal
import logging
import io
import os
import pathlib
from datetime import datetime

import requests
from jinja2 import Environment, FileSystemLoader

from fhan.core.fhir_package import FhirPackage
from fhan.models.generator_models import GeneratorStructureDefinition

logger = logging.getLogger(__name__)

# TODO move to config
TEMLPATE_DIR = "./templates"
OUTPUT_DIR = "./"
TEMPLATE_NAMES = ["structure_definition.j2"]


class ModelGenerator:
    """Generates model classes from FHIR Packages."""

    version_urls = {
        "R4": "https://hl7.org/fhir/R4/hl7.fhir.r4.core.tgz",
        "R4B": "https://hl7.org/fhir/R4B/hl7.fhir.r4b.core.tgz",
        "R5": "https://hl7.org/fhir/hl7.fhir.r5.core.tgz",
    }

    def __init__(
        self,
        version: Literal["R4", "R4B", "R5"],
        template_dir: str = None,
        output_dir: str = None,
        template_names: list[str] = None,
    ):
        self._version = version
        if version not in self.version_urls:
            raise ValueError(
                f"Unsupported version: {version}. Supported versions: {self.version_urls.keys()}"
            )

        self._output_dir = output_dir or OUTPUT_DIR
        self._output_dir = get_full_path_to_dir(os.path.join(self._output_dir, version))
        open(os.path.join(self._output_dir, "__init__.py"), "a").close()

        self._template_dir = template_dir or TEMLPATE_DIR
        self._template_dir = get_full_path_to_dir(self._template_dir)

        self._template_names = template_names or TEMPLATE_NAMES

        self._package = self._load_package()

    def _load_package(self):
        """Load the FHIR package from the given URL and store in
        FhirPackage instance."""
        url = ModelGenerator.version_urls[self._version]
        package = _load_npm_package(url)
        return package

    def generate_model_classes(self):
        """Create the python classes for the FHIR package."""
        self._generate_structure_definition_classes()

    def _generate_structure_definition_classes(self):
        """Generate the python classes for the StructureDefinitions in the FHIR package."""
        generator_struc_defs = [
            GeneratorStructureDefinition(sd)
            for sd in self._package._structure_definitions
        ]
        env = Environment(loader=FileSystemLoader(searchpath=self._template_dir))
        for template_name in self._template_names:
            template = env.get_template(template_name)
            for structure_definition in generator_struc_defs:
                if (
                    not structure_definition.has_snapshot
                    or structure_definition.is_primitive
                ):
                    continue
                model_code = template.render(
                    structure_definition=structure_definition,
                    base_class="",
                    dir_name=self._version,
                    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                )
                output_file = f"{self._output_dir}/{structure_definition.type}.py"
                with open(output_file, "w") as f:
                    f.write(model_code)


def _load_npm_package(url: str) -> FhirPackage:
    """Loads a FHIR npm package from an URL."""
    res = requests.get(url, stream=True)
    res.raise_for_status()
    package_bytes = res.content
    package_buffer = io.BytesIO(package_bytes)
    return FhirPackage.from_npm(npm_file=package_buffer)


def get_full_path_to_dir(dir: str):
    full_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__))) / dir
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def main():
    generator = ModelGenerator(version="R4")
    generator._generate_structure_definition_classes()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
