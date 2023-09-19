"""
Generated class for SubstancePolymer. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *


@dataclass
class SubstancePolymer:
    """ Properties of a substance specific to it being a polymer.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: A business idenfier for this polymer, but typically this is handled by a SubstanceDefinition identifier
    :param CodeableConcept class: Overall type of the polymer
    :param CodeableConcept geometry: Polymer geometry, e.g. linear, branched, cross-linked, network or dendritic
    :param CodeableConcept copolymerConnectivity: Descrtibes the copolymer sequence type (polymer connectivity)
    :param str modification: Todo - this is intended to connect to a repeating full modification structure, also used by Protein and Nucleic Acid . String is just a placeholder
    :param BackboneElement monomerSet: Todo
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept ratioType: Captures the type of ratio to the entire polymer, e.g. Monomer/Polymer ratio, SRU/Polymer Ratio
    :param BackboneElement startingMaterial: The starting materials - monomer(s) used in the synthesis of the polymer
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The type of substance for this starting material
    :param CodeableConcept category: Substance high level category, e.g. chemical substance
    :param bool isDefining: Used to specify whether the attribute described is a defining element for the unique identification of the polymer
    :param Quantity amount: A percentage
    :param BackboneElement repeat: Specifies and quantifies the repeated units and their configuration
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str averageMolecularFormula: A representation of an (average) molecular formula from a polymer
    :param CodeableConcept repeatUnitAmountType: How the quantitative amount of Structural Repeat Units is captured (e.g. Exact, Numeric, Average)
    :param BackboneElement repeatUnit: An SRU - Structural Repeat Unit
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str unit: Structural repeat units are essential elements for defining polymers
    :param CodeableConcept orientation: The orientation of the polymerisation, e.g. head-tail, head-head, random
    :param int amount: Number of repeats of this unit
    :param BackboneElement degreeOfPolymerisation: Applies to homopolymer and block co-polymers where the degree of polymerisation within a block can be described
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of the degree of polymerisation shall be described, e.g. SRU/Polymer Ratio
    :param int average: An average amount of polymerisation
    :param int low: A low expected limit of the amount
    :param int high: A high expected limit of the amount
    :param BackboneElement structuralRepresentation: A graphical structure for this SRU
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of structure (e.g. Full, Partial, Representative)
    :param str representation: The structural representation as text string in a standard format e.g. InChI, SMILES, MOLFILE, CDX, SDF, PDB, mmCIF
    :param CodeableConcept format: The format of the representation e.g. InChI, SMILES, MOLFILE, CDX, SDF, PDB, mmCIF
    :param Attachment attachment: An attached file with the structural representation
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    class: "CodeableConcept" = None
    
    geometry: "CodeableConcept" = None
    
    copolymerConnectivity: "CodeableConcept" = None
    
    modification: str = None
    
    monomerSet: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    ratioType: "CodeableConcept" = None
    
    startingMaterial: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    category: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amount: "Quantity" = None
    
    repeat: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    averageMolecularFormula: str = None
    
    repeatUnitAmountType: "CodeableConcept" = None
    
    repeatUnit: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    unit: str = None
    
    orientation: "CodeableConcept" = None
    
    amount: int = None
    
    degreeOfPolymerisation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    average: int = None
    
    low: int = None
    
    high: int = None
    
    structuralRepresentation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    format: "CodeableConcept" = None
    
    attachment: "Attachment" = None
    