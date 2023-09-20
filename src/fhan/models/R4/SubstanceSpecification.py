"""
Generated class for SubstanceSpecification. 
Time: 2023-09-20 20:29:43
"""
from dataclasses import dataclass
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Attachment import *
from fhan.models.R4.Range import *
from fhan.models.R4.Ratio import *
from fhan.models.R4.Element import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Moiety(Element):
    """ Moiety, for structural modifications.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Role that the moiety is playing
    :param Identifier identifier: Identifier by which this moiety substance is known
    :param str name: Textual name for this moiety substance
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula
    :param Quantity amountQuantity: Quantitative value for this moiety
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    role: "CodeableConcept" = None
    identifier: "Identifier" = None
    
    name: str = None
    stereochemistry: "CodeableConcept" = None
    opticalActivity: "CodeableConcept" = None
    
    molecularFormula: str = None
    amountQuantity: "Quantity" = None
    

    
    
@dataclass
class Property(Element):
    """ General specifications for this substance, including how it is related to other substances.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept category: A category for this property, e.g. Physical, Chemical, Enzymatic
    :param CodeableConcept code: Property type e.g. viscosity, pH, isoelectric point
    :param str parameters: Parameters that were used in the measurement of a property (e.g. for viscosity: measured at 20C with a pH of 7.1)
    :param Reference definingSubstanceReference: A substance upon which a defining property depends (e.g. for solubility: in water, in alcohol)
    :param Quantity amountQuantity: Quantitative value for this property
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    category: "CodeableConcept" = None
    code: "CodeableConcept" = None
    
    parameters: str = None
    definingSubstanceReference: "Reference" = None
    amountQuantity: "Quantity" = None
    

    
        
    
        
    
    
@dataclass
class MolecularWeight(Element):
    """ The molecular weight or weight range (for proteins, polymers or nucleic acids).:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept method: The method by which the molecular weight was determined
    :param CodeableConcept type: Type of molecular weight such as exact, average (also known as. number average), weight average
    :param Quantity amount: Used to capture quantitative values for a variety of elements. If only limits are given, the arithmetic mean would be the average. If only a single definite value for a given element is given, it would be captured in this field
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    method: "CodeableConcept" = None
    type: "CodeableConcept" = None
    amount: "Quantity" = None
    
  
    
    
@dataclass
class Isotope(Element):
    """ Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Substance identifier for each non-natural or radioisotope
    :param CodeableConcept name: Substance name for each non-natural or radioisotope
    :param CodeableConcept substitution: The type of isotopic substitution present in a single substance
    :param Quantity halfLife: Half life - for a non-natural nuclide
    :param MolecularWeight molecularWeight: The molecular weight or weight range (for proteins, polymers or nucleic acids)
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    identifier: "Identifier" = None
    name: "CodeableConcept" = None
    substitution: "CodeableConcept" = None
    halfLife: "Quantity" = None
    molecularWeight: "MolecularWeight" = None
    

    
    
@dataclass
class Representation(Element):
    """ Molecular structural representation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The type of structure (e.g. Full, Partial, Representative)
    :param str representation: The structural representation as text string in a format e.g. InChI, SMILES, MOLFILE, CDX
    :param Attachment attachment: An attached file with the structural representation
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    type: "CodeableConcept" = None
    
    representation: str = None
    attachment: "Attachment" = None
    
  
    
    
@dataclass
class Structure(Element):
    """ Structural information.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula
    :param str molecularFormulaByMoiety: Specified per moiety according to the Hill system, i.e. first C, then H, then alphabetical, each moiety separated by a dot
    :param Isotope isotope: Applicable for single substances that contain a radionuclide or a non-natural isotopic ratio
    :param Reference source: Supporting literature
    :param Representation representation: Molecular structural representation
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    stereochemistry: "CodeableConcept" = None
    opticalActivity: "CodeableConcept" = None
    
    molecularFormula: str = None
    
    molecularFormulaByMoiety: str = None
    isotope: list[Isotope] = None
    source: list[Reference] = None
    representation: list[Representation] = None
    

    
    
@dataclass
class Code(Element):
    """ Codes associated with the substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The specific code
    :param CodeableConcept status: Status of the code assignment
    :param str statusDate: The date at which the code status is changed as part of the terminology maintenance
    :param str comment: Any comment can be provided in this field, if necessary
    :param Reference source: Supporting literature
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    code: "CodeableConcept" = None
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    comment: str = None
    source: list[Reference] = None
    

    
        
    
    
@dataclass
class Official(Element):
    """ Details of the official nature of this name.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept authority: Which authority uses this official name
    :param CodeableConcept status: The status of the official name
    :param str date: Date of official name change
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    authority: "CodeableConcept" = None
    status: "CodeableConcept" = None
    
    date: str = None
    
  
    
    
@dataclass
class Name(Element):
    """ Names applicable to this substance.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The actual name
    :param CodeableConcept type: Name type
    :param CodeableConcept status: The status of the name
    :param bool preferred: If this is the preferred name for this substance
    :param CodeableConcept language: Language of the name
    :param CodeableConcept domain: The use context of this name for example if there is a different name a drug active ingredient as opposed to a food colour additive
    :param CodeableConcept jurisdiction: The jurisdiction where this name applies
    :param Official official: Details of the official nature of this name
    :param Reference source: Supporting literature
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    
    name: str = None
    type: "CodeableConcept" = None
    status: "CodeableConcept" = None
    
    preferred: bool = None
    language: list[CodeableConcept] = None
    domain: list[CodeableConcept] = None
    jurisdiction: list[CodeableConcept] = None
    official: list[Official] = None
    source: list[Reference] = None
    

    
    
@dataclass
class Relationship(Element):
    """ A link between this substance and another, with details of the relationship.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference substanceReference: A pointer to another substance, as a resource or just a representational code
    :param CodeableConcept relationship: For example "salt to parent", "active moiety", "starting material"
    :param bool isDefining: For example where an enzyme strongly bonds with a particular substance, this is a defining relationship for that enzyme, out of several possible substance relationships
    :param Quantity amountQuantity: A numeric factor for the relationship, for instance to express that the salt of a substance has some percentage of the active substance in relation to some other
    :param Ratio amountRatioLowLimit: For use when the numeric
    :param CodeableConcept amountType: An operator for the amount, for example "average", "approximately", "less than"
    :param Reference source: Supporting literature
    """
    id: str = None
    extension: list[Extension] = None
    modifierExtension: list[Extension] = None
    substanceReference: "Reference" = None
    relationship: "CodeableConcept" = None
    
    isDefining: bool = None
    amountQuantity: "Quantity" = None
    amountRatioLowLimit: "Ratio" = None
    amountType: "CodeableConcept" = None
    source: list[Reference] = None
    
@dataclass
class SubstanceSpecification(ModelBase):
    """ The detailed description of a substance, typically at a level beyond what is used for prescribing.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Identifier by which this substance is known
    :param CodeableConcept type: High level categorization, e.g. polymer or nucleic acid
    :param CodeableConcept status: Status of substance within the catalogue e.g. approved
    :param CodeableConcept domain: If the substance applies to only human or veterinary use
    :param str description: Textual description of the substance
    :param Reference source: Supporting literature
    :param str comment: Textual comment about this record of a substance
    :param Moiety moiety: Moiety, for structural modifications
    :param Property property: General specifications for this substance, including how it is related to other substances
    :param Reference referenceInformation: General information detailing this substance
    :param Structure structure: Structural information
    :param Code code: Codes associated with the substance
    :param Name name: Names applicable to this substance
    :param Relationship relationship: A link between this substance and another, with details of the relationship
    :param Reference nucleicAcid: Data items specific to nucleic acids
    :param Reference polymer: Data items specific to polymers
    :param Reference protein: Data items specific to proteins
    :param Reference sourceMaterial: Material or taxonomic/anatomical source for the substance
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    domain: "CodeableConcept" = None
    
    description: str = None
    
    source: list["Reference"] = None
    
    comment: str = None
    
    moiety: list["Moiety"] = None
    
    property: list["Property"] = None
    
    referenceInformation: "Reference" = None
    
    structure: "Structure" = None
    
    code: list["Code"] = None
    
    name: list["Name"] = None
    
    relationship: list["Relationship"] = None
    
    nucleicAcid: "Reference" = None
    
    polymer: "Reference" = None
    
    protein: "Reference" = None
    
    sourceMaterial: "Reference" = None
    