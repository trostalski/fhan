"""
Generated class for ChargeItem. 
Time: 2023-09-24 20:01:56
"""
from dataclasses import dataclass
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Money import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Quantity import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Period import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Element import *
from fhan.models.R4.Timing import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Performer(Element):
    """ Indicates who or what performed or participated in the charged service.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept function: What type of performance was done
    :param Reference actor: Individual who was performing
    """
    id: str = None
    
    extension:  list["Extension"] = [Extension()]
    
    modifierExtension:  list["Extension"] = [Extension()]
    
    function:  "CodeableConcept" = CodeableConcept()
    
    actor:  "Reference" = Reference()
    

@dataclass
class ChargeItem(ModelBase):
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
    :param Reference context: Encounter / Episode associated with event
    :param str occurrenceDateTime: When the charged service was applied
    :param Performer performer: Who performed charged service
    :param Reference performingOrganization: Organization providing the charged service
    :param Reference requestingOrganization: Organization requesting the charged service
    :param Reference costCenter: Organization that has ownership of the (potential, future) revenue
    :param Quantity quantity: Quantity of which the charge item has been serviced
    :param CodeableConcept bodysite: Anatomical location, if relevant
    :param float factorOverride: Factor overriding the associated rules
    :param Money priceOverride: Price overriding the associated rules
    :param str overrideReason: Reason for overriding the list price/factor
    :param Reference enterer: Individual who was entering
    :param str enteredDate: Date the charge item was entered
    :param CodeableConcept reason: Why was the charged  service rendered?
    :param Reference service: Which rendered service is being charged?
    :param Reference productReference: Product charged
    :param Reference account: Account to place this charge
    :param Annotation note: Comments made about the ChargeItem
    :param Reference supportingInformation: Further information supporting this charge
    """

    resourceType: str = "ChargeItem"
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: list["Resource"] = None
    
    extension: list["Extension"] = None
    
    modifierExtension: list["Extension"] = None
    
    identifier: list["Identifier"] = None
    
    definitionUri: str = None
    
    definitionCanonical: str = None
    
    status: str = None
    
    partOf: list["Reference"] = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    context: "Reference" = None
    
    occurrenceDateTime: str = None
    
    performer: list["Performer"] = None
    
    performingOrganization: "Reference" = None
    
    requestingOrganization: "Reference" = None
    
    costCenter: "Reference" = None
    
    quantity: "Quantity" = None
    
    bodysite: list["CodeableConcept"] = None
    
    factorOverride: float = None
    
    priceOverride: "Money" = None
    
    overrideReason: str = None
    
    enterer: "Reference" = None
    
    enteredDate: str = None
    
    reason: list["CodeableConcept"] = None
    
    service: list["Reference"] = None
    
    productReference: "Reference" = None
    
    account: list["Reference"] = None
    
    note: list["Annotation"] = None
    
    supportingInformation: list["Reference"] = None
    