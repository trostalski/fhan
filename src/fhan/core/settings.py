from dataclasses import dataclass
from typing import Literal
import json
import logging
import os
import configparser

logger = logging.getLogger(__name__)

CONFIG_FILE_NAME = "fhan.ini"


@dataclass
class BaseSettings:
    package_name = "fhan"
    default_fhir_version = "R4"
    supported_fhir_versions = ["R4", "R4B", "R5"]
    fhir_version_package_urls = {
        "R4": "https://hl7.org/fhir/R4/hl7.fhir.r4.core.tgz",
        "R4B": "https://hl7.org/fhir/R4B/hl7.fhir.r4b.core.tgz",
        "R5": "https://hl7.org/fhir/hl7.fhir.r5.core.tgz",
    }


@dataclass
class ClientSettings(BaseSettings):
    server_base_url = None
    available_resources = None
    available_search_params = None


@dataclass
class GeneratorSettings(BaseSettings):
    template_dir = "./templates"
    output_dir = "./"
    template_names = ["structure_definition_model.j2"]
