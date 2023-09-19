"""
Generated class for Shareable. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Coding import *


@dataclass
class Shareable:
    """ Logical Model: A pattern to be followed by [canonical resources](canonicalresource.html) that meet minimal requirements for sharing via registries or similar mechanisms.
    :param str url: Canonical identifier for this {{title}}, represented as a URI (globally unique)
    :param str version: Business version of the {{title}}
    :param str versionAlgorithmstring: How to compare versions
    :param Coding versionAlgorithmstring: How to compare versions
    :param str name: Name for this {{title}} (computer friendly)
    :param str title: Name for this {{title}} (human-friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str publisher: Name of the publisher (or steward) (organization or individual)
    :param str description: Natural language description of the {{title}}
    :param CodeableConcept knowledgeRepresentationLevel: narrative | semi-structured | structured | executable
    
    """
    url: str = None
    
    version: str = None
    
    versionAlgorithmstring: str = None
    
    versionAlgorithmstring: "Coding" = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    publisher: str = None
    
    description: str = None
    
    knowledgeRepresentationLevel: "CodeableConcept" = None
    