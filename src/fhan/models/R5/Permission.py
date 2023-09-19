"""
Generated class for Permission. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.Expression import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Reference import *


@dataclass
class Permission:
    """ Permission resource holds access rules for a given data and context.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str status: active | entered-in-error | draft | rejected
    :param Reference asserter: The person or entity that asserts the permission
    :param str date: The date that permission was asserted
    :param Period validity: The period in which the permission is active
    :param BackboneElement justification: The asserted justification for using the data
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept basis: The regulatory grounds upon which this Permission builds
    :param Reference evidence: Justifing rational
    :param str combining: deny-overrides | permit-overrides | ordered-deny-overrides | ordered-permit-overrides | deny-unless-permit | permit-unless-deny
    :param BackboneElement rule: Constraints to the Permission
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: deny | permit
    :param BackboneElement data: The selection criteria to identify data that is within scope of this provision
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param BackboneElement resource: Explicit FHIR Resource references
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str meaning: instance | related | dependents | authoredby
    :param Reference reference: The actual data reference
    :param Coding security: Security tag code on .meta.security
    :param Period period: Timeframe encompasing data create/update
    :param Expression expression: Expression identifying the data
    :param BackboneElement activity: A description or definition of which activities are allowed to be done on the data
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference actor: Authorized actor(s)
    :param CodeableConcept action: Actions controlled by this rule
    :param CodeableConcept purpose: The purpose for which the permission is given
    :param CodeableConcept limit: What limits apply to the use of the data
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    status: str = None
    
    asserter: "Reference" = None
    
    date: str = None
    
    validity: "Period" = None
    
    justification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    basis: "CodeableConcept" = None
    
    evidence: "Reference" = None
    
    combining: str = None
    
    rule: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    data: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    resource: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    meaning: str = None
    
    reference: "Reference" = None
    
    security: "Coding" = None
    
    period: "Period" = None
    
    expression: "Expression" = None
    
    activity: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    actor: "Reference" = None
    
    action: "CodeableConcept" = None
    
    purpose: "CodeableConcept" = None
    
    limit: "CodeableConcept" = None
    