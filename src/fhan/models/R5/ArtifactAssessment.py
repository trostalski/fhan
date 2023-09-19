"""
Generated class for ArtifactAssessment. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Quantity import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class ArtifactAssessment:
    """ Represents justification for a recommendation
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Additional identifier for the artifact assessment
    :param str title: A short title for the assessment for use in displaying and selecting
    :param Reference citeAsReference: How to cite the recommendation
    :param str citeAsReference: How to cite the recommendation
    :param str date: Date last changed
    :param str copyright: Use and/or publishing restrictions
    :param str approvalDate: When the artifact assessment was approved by publisher
    :param str lastReviewDate: When the artifact assessment was last reviewed by the publisher
    :param Reference artifactReference: The artifact assessed, commented upon or rated
    :param str artifactReference: The artifact assessed, commented upon or rated
    :param str artifactReference: The artifact assessed, commented upon or rated
    :param BackboneElement content: Comment, classifier, or rating content
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str informationType: comment | classifier | rating | container | response | change-request
    :param str summary: Brief summary of the content
    :param CodeableConcept type: What type of content
    :param CodeableConcept classifier: Rating, classifier, or assessment
    :param Quantity quantity: Quantitative rating
    :param Reference author: Who authored the content
    :param str path: What the comment is directed to
    :param RelatedArtifact relatedArtifact: Additional information
    :param bool freeToShare: Acceptable to publicly share the resource content
    :param BackboneElement component: Comment, classifier, or rating content
    :param str workflowStatus: submitted | triaged | waiting-for-input | resolved-no-change | resolved-change-required | deferred | duplicate | applied | published | entered-in-error
    :param str disposition: unresolved | not-persuasive | persuasive | persuasive-with-modification | not-persuasive-with-modification
    
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
    
    title: str = None
    
    citeAsReference: "Reference" = None
    
    citeAsReference: str = None
    
    date: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    artifactReference: "Reference" = None
    
    artifactReference: str = None
    
    artifactReference: str = None
    
    content: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    informationType: str = None
    
    summary: str = None
    
    type: "CodeableConcept" = None
    
    classifier: "CodeableConcept" = None
    
    quantity: "Quantity" = None
    
    author: "Reference" = None
    
    path: str = None
    
    relatedArtifact: "RelatedArtifact" = None
    
    freeToShare: bool = None
    
    component: "BackboneElement" = None
    
    workflowStatus: str = None
    
    disposition: str = None
    