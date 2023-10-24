from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class BaseSettings:
    package_name = "fhan"
    fhir_version = "R4"
    supported_fhir_versions = ["R4", "R4B", "R5"]
    fhir_version_package_urls = {
        "R4": "https://hl7.org/fhir/R4/hl7.fhir.r4.core.tgz",
        "R4B": "https://hl7.org/fhir/R4B/hl7.fhir.r4b.core.tgz",
        "R5": "https://hl7.org/fhir/hl7.fhir.r5.core.tgz",
    }


@dataclass
class ClientSettings(BaseSettings):
    pass


@dataclass
class GeneratorSettings(BaseSettings):
    template_dir = "./templates"
    output_dir = "./"
    structure_definition_template_name = "structure_definition_model.j2"
    model_init_template_name = "model_init.j2"
