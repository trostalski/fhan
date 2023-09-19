"""
Generated class for RelatedArtifact. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Attachment import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Extension import *
from fhan.models.R5.CodeableConcept import *


@dataclass
class RelatedArtifact:
    """ RelatedArtifact Type: Related artifacts such as additional documentation, justification, or bibliographic references.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of | part-of | amends | amended-with | appends | appended-with | cites | cited-by | comments-on | comment-in | contains | contained-in | corrects | correction-in | replaces | replaced-with | retracts | retracted-by | signs | similar-to | supports | supported-with | transforms | transformed-into | transformed-with | documents | specification-of | created-with | cite-as
    :param CodeableConcept classifier: Additional classifiers
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param Attachment document: What document is being referenced
    :param str resource: What artifact is being referenced
    :param Reference resourceReference: What artifact, if not a conformance resource
    :param str publicationStatus: draft | active | retired | unknown
    :param str publicationDate: Date of publication of the artifact being referred to
    
    """
    id: str = None
    
    extension: "Extension" = None
    
    type: str = None
    
    classifier: "CodeableConcept" = None
    
    label: str = None
    
    display: str = None
    
    citation: str = None
    
    document: "Attachment" = None
    
    resource: str = None
    
    resourceReference: "Reference" = None
    
    publicationStatus: str = None
    
    publicationDate: str = None
    