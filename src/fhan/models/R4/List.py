"""
Generated class for List. 
Time: 2023-09-23 23:45:33
"""
from dataclasses import dataclass
from fhan.models.R4.Annotation import *
from fhan.models.R4.Reference import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Element import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Meta import *
from fhan.models.generator_models import ModelBase

    
    
@dataclass
class Entry(Element):
    """ Entries in this list.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept flag: Status/Workflow information about this item
    :param bool deleted: If this item is actually marked as deleted
    :param str date: When item added to list
    :param Reference item: Actual entry
    """
    id: str = None
    extension: list[Extension] = Extension() 
    modifierExtension: list[Extension] = Extension() 
    flag: "CodeableConcept" = CodeableConcept()
    
    deleted: bool = None
    
    date: str = None
    item: "Reference" = Reference()
    

@dataclass
class List(ModelBase):
    """ A list is a curated collection of resources.
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
    :param Reference subject: If all resources have the same subject
    :param Reference encounter: Context in which list created
    :param str date: When the list was prepared
    :param Reference source: Who and/or what defined the list contents (aka Author)
    :param CodeableConcept orderedBy: What order the list has
    :param Annotation note: Comments about the list
    :param Entry entry: Entries in the list
    :param CodeableConcept emptyReason: Why list is empty
    """

    resourceType: str = "List"
    id: str = None
    
    meta: "Meta" = Meta()
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = Narrative()
    
    contained: list[Resource] = Resource() 
    
    extension: list[Extension] = Extension() 
    
    modifierExtension: list[Extension] = Extension() 
    
    identifier: list[Identifier] = Identifier() 
    
    status: str = None
    
    mode: str = None
    
    title: str = None
    
    code: "CodeableConcept" = CodeableConcept()
    
    subject: "Reference" = Reference()
    
    encounter: "Reference" = Reference()
    
    date: str = None
    
    source: "Reference" = Reference()
    
    orderedBy: "CodeableConcept" = CodeableConcept()
    
    note: list[Annotation] = Annotation() 
    
    entry: list[Entry] = Entry() 
    
    emptyReason: "CodeableConcept" = CodeableConcept()
    