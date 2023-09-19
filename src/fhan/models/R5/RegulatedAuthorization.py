"""
Generated class for RegulatedAuthorization. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.CodeableReference import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class RegulatedAuthorization:
    """ Regulatory approval, clearance or licencing related to a regulated product, treatment, facility or activity that is cited in a guidance, regulation, rule or legislative act. An example is Market Authorization relating to a Medicinal Product.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for the authorization, typically assigned by the authorizing body
    :param Reference subject: The product type, treatment, facility or activity that is being authorized
    :param CodeableConcept type: Overall type of this authorization, for example drug marketing approval, orphan drug designation
    :param str description: General textual supporting information
    :param CodeableConcept region: The territory in which the authorization has been granted
    :param CodeableConcept status: The status that is authorised e.g. approved. Intermediate states can be tracked with cases and applications
    :param str statusDate: The date at which the current status was assigned
    :param Period validityPeriod: The time period in which the regulatory approval etc. is in effect, e.g. a Marketing Authorization includes the date of authorization and/or expiration date
    :param CodeableReference indication: Condition for which the use of the regulated product applies
    :param CodeableConcept intendedUse: The intended use of the product, e.g. prevention, treatment
    :param CodeableConcept basis: The legal/regulatory framework or reasons under which this authorization is granted
    :param Reference holder: The organization that has been granted this authorization, by the regulator
    :param Reference regulator: The regulatory authority or authorizing body granting the authorization
    :param Reference attachedDocument: Additional information or supporting documentation about the authorization
    :param BackboneElement case: The case or regulatory procedure for granting or amending a regulated authorization. Note: This area is subject to ongoing review and the workgroup is seeking implementer feedback on its use (see link at bottom of page)
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Identifier by which this case can be referenced
    :param CodeableConcept type: The defining type of case
    :param CodeableConcept status: The status associated with the case
    :param Period datePeriod: Relevant date for this case
    :param str datePeriod: Relevant date for this case
    :param BackboneElement application: The case or regulatory procedure for granting or amending a regulated authorization. Note: This area is subject to ongoing review and the workgroup is seeking implementer feedback on its use (see link at bottom of page)
    
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
    
    type: "CodeableConcept" = None
    
    description: str = None
    
    region: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    statusDate: str = None
    
    validityPeriod: "Period" = None
    
    indication: "CodeableReference" = None
    
    intendedUse: "CodeableConcept" = None
    
    basis: "CodeableConcept" = None
    
    holder: "Reference" = None
    
    regulator: "Reference" = None
    
    attachedDocument: "Reference" = None
    
    case: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    type: "CodeableConcept" = None
    
    status: "CodeableConcept" = None
    
    datePeriod: "Period" = None
    
    datePeriod: str = None
    
    application: "BackboneElement" = None
    