"""
Generated class for List. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class List:
    """ A List is a curated collection of resources, for things such as problem lists, allergy lists, facility list, organization list, etc.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier
    :param str status: current | retired | entered-in-error
    :param str mode: working | snapshot | changes
    :param str title: Descriptive name for the list
    :param CodeableConcept code: What the purpose of this list is
    :param Reference subject: If all resources have the same subject(s)
    :param Reference encounter: Context in which list created
    :param str date: When the list was prepared
    :param Reference source: Who and/or what defined the list contents (aka Author)
    :param CodeableConcept orderedBy: What order the list has
    :param Annotation note: Comments about the list
    :param BackboneElement entry: Entries in the list
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept flag: Status/Workflow information about this item
    :param bool deleted: If this item is actually marked as deleted
    :param str date: When item added to list
    :param Reference item: Actual entry
    :param CodeableConcept emptyReason: Why list is empty
    
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
    
    status: str = None
    
    mode: str = None
    
    title: str = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    date: str = None
    
    source: "Reference" = None
    
    orderedBy: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    entry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    flag: "CodeableConcept" = None
    
    deleted: bool = None
    
    date: str = None
    
    item: "Reference" = None
    
    emptyReason: "CodeableConcept" = None
    