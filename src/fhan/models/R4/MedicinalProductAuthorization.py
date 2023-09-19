"""
Generated class for MedicinalProductAuthorization. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class MedicinalProductAuthorization(ModelBase):
    """ The regulatory authorization of a medicinal product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the marketing authorization, as assigned by a regulator
    :param Reference subject: The medicinal product that is being authorized
    :param CodeableConcept country: The country in which the marketing authorization has been granted
    :param CodeableConcept jurisdiction: Jurisdiction within a country
    :param CodeableConcept status: The status of the marketing authorization
    :param str statusDate: The date at which the given status has become applicable
    :param str restoreDate: The date when a suspended the marketing or the marketing authorization of the product is anticipated to be restored
    :param Period validityPeriod: The beginning of the time period in which the marketing authorization is in the specific status shall be specified A complete date consisting of day, month and year shall be specified using the ISO 8601 date format
    :param Period dataExclusivityPeriod: A period of time after authorization before generic product applicatiosn can be submitted
    :param str dateOfFirstAuthorization: The date when the first authorization was granted by a Medicines Regulatory Agency
    :param str internationalBirthDate: Date of first marketing authorization for a company's new medicinal product in any country in the World
    :param CodeableConcept legalBasis: The legal framework against which this authorization is granted
    :param BackboneElement jurisdictionalAuthorization: Authorization in areas within a country
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: The assigned number for the marketing authorization
    :param CodeableConcept country: Country of authorization
    :param CodeableConcept jurisdiction: Jurisdiction within a country
    :param CodeableConcept legalStatusOfSupply: The legal status of supply in a jurisdiction or region
    :param Period validityPeriod: The start and expected end date of the authorization
    :param Reference holder: Marketing Authorization Holder
    :param Reference regulator: Medicines Regulatory Agency
    :param BackboneElement procedure: The regulatory procedure for granting or amending a marketing authorization
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier for this procedure
    :param CodeableConcept type: Type of procedure
    :param Period datePeriod: Date of procedure
    :param str datePeriod: Date of procedure
    :param BackboneElement application: The regulatory procedure for granting or amending a marketing authorization
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
    
    subject: "Reference" = None
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    restoreDate: str = None
    
    validityPeriod: "Period" = None
    
    dataExclusivityPeriod: "Period" = None
    
    dateOfFirstAuthorization: str = None
    
    internationalBirthDate: str = None
    
    legalBasis: "CodeableConcept" = None
    
    jurisdictionalAuthorization: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    country: "CodeableConcept" = None
    
    jurisdiction: "CodeableConcept" = None
    
    legalStatusOfSupply: "CodeableConcept" = None
    
    validityPeriod: "Period" = None
    
    holder: "Reference" = None
    
    regulator: "Reference" = None
    
    procedure: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    datePeriod: "Period" = None
    
    datePeriod: str = None
    
    application: "BackboneElement" = None
    