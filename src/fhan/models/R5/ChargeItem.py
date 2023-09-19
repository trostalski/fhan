"""
Generated class for ChargeItem. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.MonetaryComponent import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Timing import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ChargeItem:
    """ The resource ChargeItem describes the provision of healthcare provider products for a certain patient, therefore referring not only to the product, but containing in addition details of the provision, like date, time, amounts and participating organizations and persons. Main Usage of the ChargeItem is to enable the billing process and internal cost allocation.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business Identifier for item
    :param str definitionUri: Defining information about the code of this charge item
    :param str definitionCanonical: Resource defining the code of this ChargeItem
    :param str status: planned | billable | not-billable | aborted | billed | entered-in-error | unknown
    :param Reference partOf: Part of referenced ChargeItem
    :param CodeableConcept code: A code that identifies the charge, like a billing code
    :param Reference subject: Individual service was done for/to
    :param Reference encounter: Encounter associated with this ChargeItem
    :param str occurrencedateTime: When the charged service was applied
    :param Period occurrencedateTime: When the charged service was applied
    :param Timing occurrencedateTime: When the charged service was applied
    :param BackboneElement performer: Who performed charged service
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: What type of performance was done
    :param Reference actor: Individual who was performing
    :param Reference performingOrganization: Organization providing the charged service
    :param Reference requestingOrganization: Organization requesting the charged service
    :param Reference costCenter: Organization that has ownership of the (potential, future) revenue
    :param Quantity quantity: Quantity of which the charge item has been serviced
    :param CodeableConcept bodysite: Anatomical location, if relevant
    :param MonetaryComponent unitPriceComponent: Unit price overriding the associated rules
    :param MonetaryComponent totalPriceComponent: Total price overriding the associated rules
    :param CodeableConcept overrideReason: Reason for overriding the list price/factor
    :param Reference enterer: Individual who was entering
    :param str enteredDate: Date the charge item was entered
    :param CodeableConcept reason: Why was the charged  service rendered?
    :param CodeableReference service: Which rendered service is being charged?
    :param CodeableReference product: Product charged
    :param Reference account: Account to place this charge
    :param Annotation note: Comments made about the ChargeItem
    :param Reference supportingInformation: Further information supporting this charge
    
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
    
    definitionUri: str = None
    
    definitionCanonical: str = None
    
    status: str = None
    
    partOf: "Reference" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    occurrencedateTime: str = None
    
    occurrencedateTime: "Period" = None
    
    occurrencedateTime: "Timing" = None
    
    performer: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    function: "CodeableConcept" = None
    
    actor: "Reference" = None
    
    performingOrganization: "Reference" = None
    
    requestingOrganization: "Reference" = None
    
    costCenter: "Reference" = None
    
    quantity: "Quantity" = None
    
    bodysite: "CodeableConcept" = None
    
    unitPriceComponent: "MonetaryComponent" = None
    
    totalPriceComponent: "MonetaryComponent" = None
    
    overrideReason: "CodeableConcept" = None
    
    enterer: "Reference" = None
    
    enteredDate: str = None
    
    reason: "CodeableConcept" = None
    
    service: "CodeableReference" = None
    
    product: "CodeableReference" = None
    
    account: "Reference" = None
    
    note: "Annotation" = None
    
    supportingInformation: "Reference" = None
    