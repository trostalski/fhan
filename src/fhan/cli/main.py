from typing import Literal
import click
import logging

from fhan.models.generate import ModelGenerator

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
    generator = ModelGenerator(version=version)
    generator.generate_model_classes()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    cli()
