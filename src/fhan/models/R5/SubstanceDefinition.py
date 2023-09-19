"""
Generated class for SubstanceDefinition. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Ratio import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class SubstanceDefinition:
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
    :param str version: A business level version identifier of the substance
    :param CodeableConcept status: Status of substance within the catalogue e.g. active, retired
    :param CodeableConcept classification: A categorization, high level e.g. polymer or nucleic acid, or food, chemical, biological, or lower e.g. polymer linear or branch chain, or type of impurity
    :param CodeableConcept domain: If the substance applies to human or veterinary use
    :param CodeableConcept grade: The quality standard, established benchmark, to which substance complies (e.g. USP/NF, BP)
    :param str description: Textual description of the substance
    :param Reference informationSource: Supporting literature
    :param Annotation note: Textual comment about the substance's catalogue or registry record
    :param Reference manufacturer: The entity that creates, makes, produces or fabricates the substance
    :param Reference supplier: An entity that is the source for the substance. It may be different from the manufacturer
    :param BackboneElement moiety: Moiety, for structural modifications
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept role: Role that the moiety is playing
    :param Identifier identifier: Identifier by which this moiety substance is known
    :param str name: Textual name for this moiety substance
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: Molecular formula for this moiety (e.g. with the Hill system)
    :param Quantity amountQuantity: Quantitative value for this moiety
    :param str amountQuantity: Quantitative value for this moiety
    :param CodeableConcept measurementType: The measurement type of the quantitative value
    :param BackboneElement characterization: General specifications for this substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept technique: The method used to find the characterization e.g. HPLC
    :param CodeableConcept form: Describes the nature of the chemical entity and explains, for instance, whether this is a base or a salt form
    :param str description: The description or justification in support of the interpretation of the data file
    :param Attachment file: The data produced by the analytical instrument or a pictorial representation of that data. Examples: a JCAMP, JDX, or ADX file, or a chromatogram or spectrum analysis
    :param BackboneElement property: General specifications for this substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: A code expressing the type of property
    :param CodeableConcept valueCodeableConcept: A value for the property
    :param Quantity valueCodeableConcept: A value for the property
    :param str valueCodeableConcept: A value for the property
    :param bool valueCodeableConcept: A value for the property
    :param Attachment valueCodeableConcept: A value for the property
    :param Reference referenceInformation: General information detailing this substance
    :param BackboneElement molecularWeight: The average mass of a molecule of a compound
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept method: The method by which the weight was determined
    :param CodeableConcept type: Type of molecular weight e.g. exact, average, weight average
    :param Quantity amount: Used to capture quantitative values for a variety of elements
    :param BackboneElement structure: Structural information
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept stereochemistry: Stereochemistry type
    :param CodeableConcept opticalActivity: Optical activity type
    :param str molecularFormula: An expression which states the number and type of atoms present in a molecule of a substance
    :param str molecularFormulaByMoiety: Specified per moiety according to the Hill system
    :param BackboneElement molecularWeight: The average mass of a molecule of a compound
    :param CodeableConcept technique: The method used to find the structure e.g. X-ray, NMR
    :param Reference sourceDocument: Source of information for the structure
    :param BackboneElement representation: A depiction of the structure of the substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of structural representation (e.g. full, partial)
    :param str representation: The structural representation as a text string in a standard format
    :param CodeableConcept format: The format of the representation e.g. InChI, SMILES, MOLFILE (note: not the physical file format)
    :param Reference document: An attachment with the structural representation e.g. a structure graphic or AnIML file
    :param BackboneElement code: Codes associated with the substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept code: The specific code
    :param CodeableConcept status: Status of the code assignment, for example 'provisional', 'approved'
    :param str statusDate: The date at which the code status was changed
    :param Annotation note: Any comment can be provided in this field
    :param Reference source: Supporting literature
    :param BackboneElement name: Names applicable to this substance
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str name: The actual name
    :param CodeableConcept type: Name type e.g. 'systematic',  'scientific, 'brand'
    :param CodeableConcept status: The status of the name e.g. 'current', 'proposed'
    :param bool preferred: If this is the preferred name for this substance
    :param CodeableConcept language: Human language that the name is written in
    :param CodeableConcept domain: The use context of this name e.g. as an active ingredient or as a food colour additive
    :param CodeableConcept jurisdiction: The jurisdiction where this name applies
    :param BackboneElement synonym: Names applicable to this substance
    :param BackboneElement translation: Names applicable to this substance
    :param BackboneElement official: Details of the official nature of this name
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept authority: Which authority uses this official name
    :param CodeableConcept status: The status of the official name, for example 'draft', 'active'
    :param str date: Date of official name change
    :param Reference source: Supporting literature
    :param BackboneElement relationship: A link between this substance and another
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference substanceDefinitionReference: A pointer to another substance, as a resource or a representational code
    :param CodeableConcept substanceDefinitionReference: A pointer to another substance, as a resource or a representational code
    :param CodeableConcept type: For example "salt to parent", "active moiety"
    :param bool isDefining: For example where an enzyme strongly bonds with a particular substance, this is a defining relationship for that enzyme, out of several possible relationships
    :param Quantity amountQuantity: A numeric factor for the relationship, e.g. that a substance salt has some percentage of active substance in relation to some other
    :param Ratio amountQuantity: A numeric factor for the relationship, e.g. that a substance salt has some percentage of active substance in relation to some other
    :param str amountQuantity: A numeric factor for the relationship, e.g. that a substance salt has some percentage of active substance in relation to some other
    :param Ratio ratioHighLimitAmount: For use when the numeric has an uncertain range
    :param CodeableConcept comparator: An operator for the amount, for example "average", "approximately", "less than"
    :param Reference source: Supporting literature
    :param Reference nucleicAcid: Data items specific to nucleic acids
    :param Reference polymer: Data items specific to polymers
    :param Reference protein: Data items specific to proteins
    :param BackboneElement sourceMaterial: Material or taxonomic/anatomical source
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Classification of the origin of the raw material. e.g. cat hair is an Animal source type
    :param CodeableConcept genus: The genus of an organism e.g. the Latin epithet of the plant/animal scientific name
    :param CodeableConcept species: The species of an organism e.g. the Latin epithet of the species of the plant/animal
    :param CodeableConcept part: An anatomical origin of the source material within an organism
    :param CodeableConcept countryOfOrigin: The country or countries where the material is harvested
    
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
    
    version: str = None
    
    status: "CodeableConcept" = None
    
    classification: "CodeableConcept" = None
    
    domain: "CodeableConcept" = None
    
    grade: "CodeableConcept" = None
    
    description: str = None
    
    informationSource: "Reference" = None
    
    note: "Annotation" = None
    
    manufacturer: "Reference" = None
    
    supplier: "Reference" = None
    
    moiety: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    role: "CodeableConcept" = None
    
    identifier: "Identifier" = None
    
    name: str = None
    
    stereochemistry: "CodeableConcept" = None
    
    opticalActivity: "CodeableConcept" = None
    
    molecularFormula: str = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: str = None
    
    measurementType: "CodeableConcept" = None
    
    characterization: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    technique: "CodeableConcept" = None
    
    form: "CodeableConcept" = None
    
    description: str = None
    
    file: "Attachment" = None
    
    property: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    valueCodeableConcept: "CodeableConcept" = None
    
    valueCodeableConcept: "Quantity" = None
    
    valueCodeableConcept: str = None
    
    valueCodeableConcept: bool = None
    
    valueCodeableConcept: "Attachment" = None
    
    referenceInformation: "Reference" = None
    
    molecularWeight: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    method: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    amount: "Quantity" = None
    
    structure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    stereochemistry: "CodeableConcept" = None
    
    opticalActivity: "CodeableConcept" = None
    
    molecularFormula: str = None
    
    molecularFormulaByMoiety: str = None
    
    molecularWeight: "BackboneElement" = None
    
    technique: "CodeableConcept" = None
    
    sourceDocument: "Reference" = None
    
    representation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    representation: str = None
    
    format: "CodeableConcept" = None
    
    document: "Reference" = None
    
    code: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    code: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    note: "Annotation" = None
    
    source: "Reference" = None
    
    name: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: str = None
    
    type: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    preferred: bool = None
    
    language: "CodeableConcept" = None
    
    domain: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    synonym: "BackboneElement" = None
    
    translation: "BackboneElement" = None
    
    official: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    authority: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    date: str = None
    
    source: "Reference" = None
    
    relationship: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    substanceDefinitionReference: "Reference" = None
    
    substanceDefinitionReference: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    isDefining: bool = None
    
    amountQuantity: "Quantity" = None
    
    amountQuantity: "Ratio" = None
    
    amountQuantity: str = None
    
    ratioHighLimitAmount: "Ratio" = None
    
    comparator: "CodeableConcept" = None
    
    source: "Reference" = None
    
    nucleicAcid: "Reference" = None
    
    polymer: "Reference" = None
    
    protein: "Reference" = None
    
    sourceMaterial: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    genus: "CodeableConcept" = None
    
    species: "CodeableConcept" = None
    
    part: "CodeableConcept" = None
    
    countryOfOrigin: "CodeableConcept" = None
    