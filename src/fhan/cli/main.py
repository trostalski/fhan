from typing import Literal
import click
import logging

from fhan.models.generate import ModelGenerator
from fhan.core.fhir_package import FhirPackageLoader
from fhan.core.settings import BaseSettings

logger = logging.getLogger(__name__)


@click.group()
def cli():
    """CLI entrypoint for fhan."""
    pass


@cli.command()
@click.option(
    "--version",
    "-v",
    default="R4",
    help="FHIR version to generate models for. Defaults to R4.",
)
def generate(
    version: Literal["R4", "R4B", "R5"],
):
    """Generate models from FHIR packages."""
    package_loader = FhirPackageLoader()
    package = package_loader.load_package_from_version(fhir_version=version)
    generator = ModelGenerator(package=package)
    generator.generate_model_classes()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    cli()
