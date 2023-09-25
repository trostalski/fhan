"""
Generated class for List. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Annotation import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.DomainResource import *


    
    

class Entry(ModelBase):
    """ Entries in this list.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'CodeableConcept' flag: Status/Workflow information about this item
    :param bool deleted: If this item is actually marked as deleted
    :param str date: When item added to list
    :param 'Reference' item: Actual entry
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  flag: 'CodeableConcept' = None,  deleted: bool = None,  date: str = None,  item: 'Reference' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.flag: 'CodeableConcept' = flag 
        self.deleted: bool = deleted 
        self.date: str = date 
        self.item: 'Reference' = item 
        

class List(DomainResource):
    """ A list is a curated collection of resources.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business identifier
    :param str status: current | retired | entered-in-error
    :param str mode: working | snapshot | changes
    :param str title: Descriptive name for the list
    :param 'CodeableConcept' code: What the purpose of this list is
    :param 'Reference' subject: If all resources have the same subject
    :param 'Reference' encounter: Context in which list created
    :param str date: When the list was prepared
    :param 'Reference' source: Who and/or what defined the list contents (aka Author)
    :param 'CodeableConcept' orderedBy: What order the list has
    :param list['Annotation'] note: Comments about the list
    :param list['Entry'] entry: Entries in the list
    :param 'CodeableConcept' emptyReason: Why list is empty
    """
    def __init__(self, resourceType: str = "List",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  mode: str = None,  title: str = None,  code: 'CodeableConcept' = None,  subject: 'Reference' = None,  encounter: 'Reference' = None,  date: str = None,  source: 'Reference' = None,  orderedBy: 'CodeableConcept' = None,  note: list['Annotation'] = None,  entry: list['Entry'] = None,  emptyReason: 'CodeableConcept' = None, ):
        self.resourceType: str = resourceType or "List"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.mode: str = mode 
        self.title: str = title 
        self.code: 'CodeableConcept' = code 
        self.subject: 'Reference' = subject 
        self.encounter: 'Reference' = encounter 
        self.date: str = date 
        self.source: 'Reference' = source 
        self.orderedBy: 'CodeableConcept' = orderedBy 
        self.note: list['Annotation'] = note or []
        self.entry: list['Entry'] = entry or []
        self.emptyReason: 'CodeableConcept' = emptyReason 
        