"""
Generated class for ChargeItemDefinition. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.Money import *
from fhan.models.R4.Period import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.UsageContext import *
from fhan.models.R4.ContactDetail import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.generator_models import ModelBase


@dataclass
class ChargeItemDefinition(ModelBase):
    """ The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices. The properties may differ largely depending on type and realm, therefore this resource gives only a rough structure and requires profiling for each type of billing code system.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this charge item definition, represented as a URI (globally unique)
    :param Identifier identifier: Additional identifier for the charge item definition
    :param str version: Business version of the charge item definition
    :param str title: Name for this charge item definition (human friendly)
    :param str derivedFromUri: Underlying externally-defined charge item definition
    :param str partOf: A larger definition of which this particular definition is a component or step
    :param str replaces: Completed or terminated request(s) whose function is taken by this new request
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: Name of the publisher (organization or individual)
    :param ContactDetail contact: Contact details for the publisher
    :param str description: Natural language description of the charge item definition
    :param UsageContext useContext: The context that the content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for charge item definition (if applicable)
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the charge item definition was approved by publisher
    :param str lastReviewDate: When the charge item definition was last reviewed
    :param Period effectivePeriod: When the charge item definition is expected to be used
    :param CodeableConcept code: Billing codes or product types this definition applies to
    :param Reference instance: Instances this definition applies to
    :param BackboneElement applicability: Whether or not the billing code is applicable
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str description: Natural language description of the condition
    :param str language: Language of the expression
    :param str expression: Boolean-valued expression
    :param BackboneElement propertyGroup: Group of properties which are applicable under the same conditions
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement applicability: Whether or not the billing code is applicable
    :param BackboneElement priceComponent: Components of total line item price
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: base | surcharge | deduction | discount | tax | informational
    :param CodeableConcept code: Code identifying the specific component
    :param float factor: Factor used for calculating this component
    :param Money amount: Monetary amount associated with this component
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    title: str = None
    
    derivedFromUri: str = None
    
    partOf: str = None
    
    replaces: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    code: "CodeableConcept" = None
    
    instance: "Reference" = None
    
    applicability: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    description: str = None
    
    language: str = None
    
    expression: str = None
    
    propertyGroup: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    applicability: "BackboneElement" = None
    
    priceComponent: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    code: "CodeableConcept" = None
    
    factor: float = None
    
    amount: "Money" = None
    