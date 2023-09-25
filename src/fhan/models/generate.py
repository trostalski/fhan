from typing import Literal
import logging
import io
import os
import pathlib
from datetime import datetime

import requests
from jinja2 import Environment, FileSystemLoader

from fhan.core.fhir_package import FhirPackage
from fhan.core.fhir_package import FhirPackageLoader
from fhan.core.settings import GeneratorSettings
from fhan.models.generator_models import GeneratorStructureDefinition

logger = logging.getLogger(__name__)

TEMLPATE_DIR = GeneratorSettings.template_dir
OUTPUT_DIR = GeneratorSettings.output_dir
TEMPLATE_NAMES = GeneratorSettings.template_names
SUPPORTED_FHIR_VERSIONS = GeneratorSettings.supported_fhir_versions


class ModelGenerator:
    """Generates model classes from FHIR Packages."""

    def __init__(
        self,
        package: FhirPackage,
        template_dir: str = None,
        output_dir: str = None,
        template_names: list[str] = None,
    ):
        self._package = package

        # specify output dir for generated model classes
        self._output_dir = output_dir or OUTPUT_DIR
        self._output_dir = get_full_path_to_dir(
            os.path.join(self._output_dir, self._package.name)
        )
        open(os.path.join(self._output_dir, "__init__.py"), "a").close()

        # specify template dir for jinja2 templates
        self._template_dir = template_dir or TEMLPATE_DIR
        self._template_dir = get_full_path_to_dir(self._template_dir)

        self._template_names = template_names or TEMPLATE_NAMES

    def generate_model_classes(self):
        """Create the python classes for the FHIR package."""
        logger.info("Generating model classes for %s", self._package.name)
        logger.info("Output dir: %s", self._output_dir)
        self._generate_structure_definition_classes()

    def _generate_structure_definition_classes(self):
        """Generate the python classes for the StructureDefinitions in the FHIR package."""
        generator_struc_defs = [
            GeneratorStructureDefinition(sd)
            for sd in self._package.structure_definitions
        ]
        env = Environment(loader=FileSystemLoader(searchpath=self._template_dir))
        for template_name in self._template_names:
            template = env.get_template(template_name)
            for structure_definition in generator_struc_defs:
                if (
                    not structure_definition.has_snapshot  # no elemnns present
                    or structure_definition.is_primitive
                    or not structure_definition.is_base  # TODO: add support for Extensions and non-base classes
                ):
                    continue
                model_code = template.render(
                    structure_definition=structure_definition,
                    base_class="",
                    dir_name=self._package.name,
                    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                )
                output_file = f"{self._output_dir}/{structure_definition.type}.py"
                with open(output_file, "w") as f:
                    f.write(model_code)


def get_full_path_to_dir(dir: str):
    full_path = pathlib.Path(os.path.dirname(os.path.realpath(__file__))) / dir
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    package_loader = FhirPackageLoader()
    package = package_loader.load_package(version="R4")
    generator = ModelGenerator(package=package)
    generator.generate_model_classes()
