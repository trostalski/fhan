import logging
import os
import pathlib
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

from fhan.core.fhir_package import FhirPackage
from fhan.core.fhir_package import FhirPackageLoader
from fhan.core.settings import GeneratorSettings
from fhan.models.generator_models import GeneratorStructureDefinition

logger = logging.getLogger(__name__)

TEMLPATE_DIR = GeneratorSettings.template_dir
OUTPUT_DIR = GeneratorSettings.output_dir
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

        self._structure_def_model_template = (
            GeneratorSettings.structure_definition_template_name
        )
        self._model_init_template = GeneratorSettings.model_init_template_name
        self.generator_struc_defs = [
            GeneratorStructureDefinition(sd)
            for sd in self._package.structure_definitions
        ]

    def generate_model_classes(self):
        """Create the python classes for the FHIR package."""
        logger.info("Generating model classes for %s", self._package.name)
        logger.info("Output dir: %s", self._output_dir)
        self._generate_structure_definition_classes()
        self._generate_model_init()

    def _generate_structure_definition_classes(self):
        """Generate the python classes for the StructureDefinitions in the FHIR package."""
        env = Environment(loader=FileSystemLoader(searchpath=self._template_dir))
        template = env.get_template(self._structure_def_model_template)
        for structure_definition in self.generator_struc_defs:
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
                source_file=__file__,
            )
            output_file = f"{self._output_dir}/{structure_definition.type}.py"
            with open(output_file, "w") as f:
                f.write(model_code)

    def _generate_model_init(self):
        env = Environment(loader=FileSystemLoader(searchpath=self._template_dir))
        template = env.get_template(self._model_init_template)
        klasses = []
        for structure_definition in self.generator_struc_defs:
            if (
                not structure_definition.has_snapshot  # no elemnns present
                or structure_definition.is_primitive
                or not structure_definition.is_base  # TODO: add support for Extensions and non-base classes
            ):
                continue
            klasses.append(structure_definition.type)
        model_init_code = template.render(
            time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            source_file=__file__,
            klasses=klasses,
        )
        output_file = f"{self._output_dir}/__init__.py"
        with open(output_file, "w") as f:
            f.write(model_init_code)


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
