"""
Generated class for Citation. 
Time: 2023-09-29 13:03:58
"""
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.RelatedArtifact import *
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Coding import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Reference import *
from fhan.models.R5.Period import *
from fhan.models.R5.ContactDetail import *
from fhan.models.R5.UsageContext import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Extension import *
from fhan.models.R5.DomainResource import *


    
    

class Summary(BaseModel):
    """ A human-readable display of key concepts to represent the citation.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept style: Format for display of the citation summary
    :param str text: The human-readable display of the citation summary
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "style": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  style:  'CodeableConcept'  = None,  text:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.style = style 
        self.text = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Classification(BaseModel):
    """ The assignment to an organizing scheme.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of classifier (e.g. publication type, keyword)
    :param CodeableConcept classifier: The specific classification value
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  classifier:  list['CodeableConcept']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.classifier = classifier or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class StatusDate(BaseModel):
    """ The state or status of the citation record paired with an effective date or period for that state.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept activity: Classification of the status
    :param bool actual: Either occurred or expected
    :param Period period: When the status started and/or ended
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "activity": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  activity:  'CodeableConcept'  = None,  actual:  'bool'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.activity = activity 
        self.actual = actual 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class Version(BaseModel):
    """ The defined version of the cited artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str value: The version number or other version identifier
    :param Reference baseCitation: Citation for the main version of the cited artifact
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "baseCitation": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  value:  'str'  = None,  baseCitation:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.value = value 
        self.baseCitation = baseCitation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class StatusDate(BaseModel):
    """ An effective date or period, historical or future, actual or expected, for a status of the cited artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept activity: Classification of the status
    :param bool actual: Either occurred or expected
    :param Period period: When the status started and/or ended
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "activity": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "period": {"class_name": "Period", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  activity:  'CodeableConcept'  = None,  actual:  'bool'  = None,  period:  'Period'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.activity = activity 
        self.actual = actual 
        self.period = period 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Title(BaseModel):
    """ The title details of the article or artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of title
    :param CodeableConcept language: Used to express the specific language
    :param str text: The title of the article or artifact
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  list['CodeableConcept']  = None,  language:  'CodeableConcept'  = None,  text:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type or []
        self.language = language 
        self.text = text 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Abstract(BaseModel):
    """ The abstract may be used to convey article-contained abstracts, externally-created abstracts, or other descriptive summaries.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of abstract
    :param CodeableConcept language: Used to express the specific language
    :param str text: Abstract content
    :param str copyright: Copyright notice for the abstract
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  language:  'CodeableConcept'  = None,  text:  'str'  = None,  copyright:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.language = language 
        self.text = text 
        self.copyright = copyright 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Part(BaseModel):
    """ The component of the article or artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of component
    :param str value: The specification of the component
    :param Reference baseCitation: The citation for the full article or artifact
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        "baseCitation": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  value:  'str'  = None,  baseCitation:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.value = value 
        self.baseCitation = baseCitation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class RelatesTo(BaseModel):
    """ The artifact related to the cited artifact.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: documentation | justification | citation | predecessor | successor | derived-from | depends-on | composed-of | part-of | amends | amended-with | appends | appended-with | cites | cited-by | comments-on | comment-in | contains | contained-in | corrects | correction-in | replaces | replaced-with | retracts | retracted-by | signs | similar-to | supports | supported-with | transforms | transformed-into | transformed-with | documents | specification-of | created-with | cite-as | reprint | reprint-of
    :param CodeableConcept classifier: Additional classifiers
    :param str label: Short label
    :param str display: Brief description of the related artifact
    :param str citation: Bibliographic citation for the artifact
    :param Attachment document: What document is being referenced
    :param str resource: What artifact is being referenced
    :param Reference resourceReference: What artifact, if not a conformance resource
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        "document": {"class_name": "Attachment", "is_contained": False},
        
        
        
        "resourceReference": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'str'  = None,  classifier:  list['CodeableConcept']  = None,  label:  'str'  = None,  display:  'str'  = None,  citation:  'str'  = None,  document:  'Attachment'  = None,  resource:  'str'  = None,  resourceReference:  'Reference'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.classifier = classifier or []
        self.label = label 
        self.display = display 
        self.citation = citation 
        self.document = document 
        self.resource = resource 
        self.resourceReference = resourceReference 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
    

class PublishedIn(BaseModel):
    """ The collection the cited article or artifact is published in.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Kind of container (e.g. Periodical, database, or book)
    :param Identifier identifier: Journal identifiers include ISSN, ISO Abbreviation and NLMuniqueID; Book identifiers include ISBN
    :param str title: Name of the database or title of the book or journal
    :param Reference publisher: Name of or resource describing the publisher
    :param str publisherLocation: Geographic location of the publisher
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "publisher": {"class_name": "Reference", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  identifier:  list['Identifier']  = None,  title:  'str'  = None,  publisher:  'Reference'  = None,  publisherLocation:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.identifier = identifier or []
        self.title = title 
        self.publisher = publisher 
        self.publisherLocation = publisherLocation 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class PublicationForm(BaseModel):
    """ If multiple, used to represent alternative forms of the article that are not separate citations.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param PublishedIn publishedIn: The collection the cited article or artifact is published in
    :param CodeableConcept citedMedium: Internet or Print
    :param str volume: Volume number of journal or other collection in which the article is published
    :param str issue: Issue, part or supplement of journal or other collection in which the article is published
    :param str articleDate: The date the article was added to the database, or the date the article was released
    :param str publicationDateText: Text representation of the date on which the issue of the cited artifact was published
    :param str publicationDateSeason: Season in which the cited artifact was published
    :param str lastRevisionDate: The date the article was last revised or updated in the database
    :param CodeableConcept language: Language(s) in which this form of the article is published
    :param str accessionNumber: Entry number or identifier for inclusion in a database
    :param str pageString: Used for full display of pagination
    :param str firstPage: Used for isolated representation of first page
    :param str lastPage: Used for isolated representation of last page
    :param str pageCount: Number of pages or screens
    :param str copyright: Copyright notice for the full article or artifact
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "publishedIn": {"class_name": "PublishedIn", "is_contained": True},
        
        
        "citedMedium": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        
        "language": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  publishedIn:  'PublishedIn'  = None,  citedMedium:  'CodeableConcept'  = None,  volume:  'str'  = None,  issue:  'str'  = None,  articleDate:  'str'  = None,  publicationDateText:  'str'  = None,  publicationDateSeason:  'str'  = None,  lastRevisionDate:  'str'  = None,  language:  list['CodeableConcept']  = None,  accessionNumber:  'str'  = None,  pageString:  'str'  = None,  firstPage:  'str'  = None,  lastPage:  'str'  = None,  pageCount:  'str'  = None,  copyright:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.publishedIn = publishedIn 
        self.citedMedium = citedMedium 
        self.volume = volume 
        self.issue = issue 
        self.articleDate = articleDate 
        self.publicationDateText = publicationDateText 
        self.publicationDateSeason = publicationDateSeason 
        self.lastRevisionDate = lastRevisionDate 
        self.language = language or []
        self.accessionNumber = accessionNumber 
        self.pageString = pageString 
        self.firstPage = firstPage 
        self.lastPage = lastPage 
        self.pageCount = pageCount 
        self.copyright = copyright 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class WebLocation(BaseModel):
    """ Used for any URL for the article or artifact cited.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept classifier: Code the reason for different URLs, e.g. abstract and full-text
    :param str url: The specific URL
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  classifier:  list['CodeableConcept']  = None,  url:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.classifier = classifier or []
        self.url = url 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Classification(BaseModel):
    """ The assignment to an organizing scheme.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The kind of classifier (e.g. publication type, keyword)
    :param CodeableConcept classifier: The specific classification value
    :param Reference artifactAssessment: Complex or externally created classification
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "classifier": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "artifactAssessment": {"class_name": "Reference", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  classifier:  list['CodeableConcept']  = None,  artifactAssessment:  list['Reference']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.classifier = classifier or []
        self.artifactAssessment = artifactAssessment or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
        
    
        
    
    

class ContributionInstance(BaseModel):
    """ Contributions with accounting for time or number.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: The specific contribution
    :param str time: The time that the contribution was made
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  time:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.time = time 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Entry(BaseModel):
    """ An individual entity named as a contributor, for example in the author list or contributor list.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference contributor: The identity of the individual contributor
    :param str forenameInitials: For citation styles that use initials
    :param Reference affiliation: Organizational affiliation
    :param CodeableConcept contributionType: The specific contribution
    :param CodeableConcept role: The role of the contributor (e.g. author, editor, reviewer, funder)
    :param ContributionInstance contributionInstance: Contributions with accounting for time or number
    :param bool correspondingContact: Whether the contributor is the corresponding contributor for the role
    :param int rankingOrder: Ranked order of contribution
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "contributor": {"class_name": "Reference", "is_contained": False},
        
        
        
        "affiliation": {"class_name": "Reference", "is_contained": False},
        
        
        "contributionType": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "role": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "contributionInstance": {"class_name": "ContributionInstance", "is_contained": True},
        
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  contributor:  'Reference'  = None,  forenameInitials:  'str'  = None,  affiliation:  list['Reference']  = None,  contributionType:  list['CodeableConcept']  = None,  role:  'CodeableConcept'  = None,  contributionInstance:  list['ContributionInstance']  = None,  correspondingContact:  'bool'  = None,  rankingOrder:  'int'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.contributor = contributor 
        self.forenameInitials = forenameInitials 
        self.affiliation = affiliation or []
        self.contributionType = contributionType or []
        self.role = role 
        self.contributionInstance = contributionInstance or []
        self.correspondingContact = correspondingContact 
        self.rankingOrder = rankingOrder 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


    
    

class Summary(BaseModel):
    """ Used to record a display of the author/contributor list without separate data element for each list member.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Such as author list, contributorship statement, funding statement, acknowledgements statement, or conflicts of interest statement
    :param CodeableConcept style: The format for the display string
    :param CodeableConcept source: Used to code the producer or rule for creating the display string
    :param str value: The display string for the author list, contributor list, or contributorship statement
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "type": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "style": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "source": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  type:  'CodeableConcept'  = None,  style:  'CodeableConcept'  = None,  source:  'CodeableConcept'  = None,  value:  'str'  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.type = type 
        self.style = style 
        self.source = source 
        self.value = value 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class Contributorship(BaseModel):
    """ This element is used to list authors and other contributors, their contact information, specific contributions, and summary statements.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param bool complete: Indicates if the list includes all authors and/or contributors
    :param Entry entry: An individual entity named as a contributor
    :param Summary summary: Used to record a display of the author/contributor list without separate data element for each list member
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "entry": {"class_name": "Entry", "is_contained": True},
        
        
        "summary": {"class_name": "Summary", "is_contained": True},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  complete:  'bool'  = None,  entry:  list['Entry']  = None,  summary:  list['Summary']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.complete = complete 
        self.entry = entry or []
        self.summary = summary or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


  
    
    

class CitedArtifact(BaseModel):
    """ The article or artifact being described.:param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Identifier identifier: Unique identifier. May include DOI, PMID, PMCID, etc
    :param Identifier relatedIdentifier: Identifier not unique to the cited artifact. May include trial registry identifiers
    :param str dateAccessed: When the cited artifact was accessed
    :param Version version: The defined version of the cited artifact
    :param CodeableConcept currentState: The status of the cited artifact
    :param StatusDate statusDate: An effective date or period for a status of the cited artifact
    :param Title title: The title details of the article or artifact
    :param Abstract abstract: Summary of the article or artifact
    :param Part part: The component of the article or artifact
    :param RelatesTo relatesTo: The artifact related to the cited artifact
    :param PublicationForm publicationForm: If multiple, used to represent alternative forms of the article that are not separate citations
    :param WebLocation webLocation: Used for any URL for the article or artifact cited
    :param Classification classification: The assignment to an organizing scheme
    :param Contributorship contributorship: Attribution of authors and other contributors
    :param Annotation note: Any additional information or content for the article or artifact
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        "relatedIdentifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        "version": {"class_name": "Version", "is_contained": True},
        
        
        "currentState": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "statusDate": {"class_name": "StatusDate", "is_contained": True},
        
        
        "title": {"class_name": "Title", "is_contained": True},
        
        
        "abstract": {"class_name": "Abstract", "is_contained": True},
        
        
        "part": {"class_name": "Part", "is_contained": True},
        
        
        "relatesTo": {"class_name": "RelatesTo", "is_contained": True},
        
        
        "publicationForm": {"class_name": "PublicationForm", "is_contained": True},
        
        
        "webLocation": {"class_name": "WebLocation", "is_contained": True},
        
        
        "classification": {"class_name": "Classification", "is_contained": True},
        
        
        "contributorship": {"class_name": "Contributorship", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        }
    def __init__(self,  id:  'str'  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  identifier:  list['Identifier']  = None,  relatedIdentifier:  list['Identifier']  = None,  dateAccessed:  'str'  = None,  version:  'Version'  = None,  currentState:  list['CodeableConcept']  = None,  statusDate:  list['StatusDate']  = None,  title:  list['Title']  = None,  abstract:  list['Abstract']  = None,  part:  'Part'  = None,  relatesTo:  list['RelatesTo']  = None,  publicationForm:  list['PublicationForm']  = None,  webLocation:  list['WebLocation']  = None,  classification:  list['Classification']  = None,  contributorship:  'Contributorship'  = None,  note:  list['Annotation']  = None, ):
        self.id = id 
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.identifier = identifier or []
        self.relatedIdentifier = relatedIdentifier or []
        self.dateAccessed = dateAccessed 
        self.version = version 
        self.currentState = currentState or []
        self.statusDate = statusDate or []
        self.title = title or []
        self.abstract = abstract or []
        self.part = part 
        self.relatesTo = relatesTo or []
        self.publicationForm = publicationForm or []
        self.webLocation = webLocation or []
        self.classification = classification or []
        self.contributorship = contributorship 
        self.note = note or []
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()


class Citation(DomainResource):
    """ The Citation Resource enables reference to any knowledge artifact for purposes of identification and attribution. The Citation Resource supports existing reference structures and developing publication practices such as versioning, expressing complex contributorship roles, and referencing computable resources.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param str url: Canonical identifier for this citation record, represented as a globally unique URI
    :param Identifier identifier: Identifier for the citation record itself
    :param str version: Business version of the citation record
    :param str versionAlgorithmString: How to compare versions
    :param Coding versionAlgorithmCoding: How to compare versions
    :param str name: Name for this citation record (computer friendly)
    :param str title: Name for this citation record (human friendly)
    :param str status: draft | active | retired | unknown
    :param bool experimental: For testing purposes, not real usage
    :param str date: Date last changed
    :param str publisher: The publisher of the citation record, not the publisher of the article or artifact being cited
    :param ContactDetail contact: Contact details for the publisher of the citation record
    :param str description: Natural language description of the citation
    :param UsageContext useContext: The context that the citation record content is intended to support
    :param CodeableConcept jurisdiction: Intended jurisdiction for citation record (if applicable)
    :param str purpose: Why this citation is defined
    :param str copyright: Use and/or publishing restrictions for the citation record, not for the cited artifact
    :param str copyrightLabel: Copyright holder and year(s) for the ciation record, not for the cited artifact
    :param str approvalDate: When the citation record was approved by publisher
    :param str lastReviewDate: When the citation record was last reviewed by the publisher
    :param Period effectivePeriod: When the citation record is expected to be used
    :param ContactDetail author: Who authored the citation record
    :param ContactDetail editor: Who edited the citation record
    :param ContactDetail reviewer: Who reviewed the citation record
    :param ContactDetail endorser: Who endorsed the citation record
    :param Summary summary: A human-readable display of key concepts to represent the citation
    :param Classification classification: The assignment to an organizing scheme
    :param Annotation note: Used for general notes and annotations not coded elsewhere
    :param CodeableConcept currentState: The status of the citation record
    :param StatusDate statusDate: An effective date or period for a status of the citation record
    :param RelatedArtifact relatedArtifact: Artifact related to the citation record
    :param CitedArtifact citedArtifact: The article or artifact being described
    """
    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        
        
        "meta": {"class_name": "Meta", "is_contained": False},
        
        
        
        
        "text": {"class_name": "Narrative", "is_contained": False},
        
        
        "contained": {"class_name": "Resource", "is_contained": False},
        
        
        "extension": {"class_name": "Extension", "is_contained": False},
        
        
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        
        
        
        "identifier": {"class_name": "Identifier", "is_contained": False},
        
        
        
        
        "versionAlgorithmCoding": {"class_name": "Coding", "is_contained": False},
        
        
        
        
        
        
        
        
        "contact": {"class_name": "ContactDetail", "is_contained": False},
        
        
        
        "useContext": {"class_name": "UsageContext", "is_contained": False},
        
        
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        
        
        
        
        
        "effectivePeriod": {"class_name": "Period", "is_contained": False},
        
        
        "author": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "editor": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "reviewer": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "endorser": {"class_name": "ContactDetail", "is_contained": False},
        
        
        "summary": {"class_name": "Summary", "is_contained": True},
        
        
        "classification": {"class_name": "Classification", "is_contained": True},
        
        
        "note": {"class_name": "Annotation", "is_contained": False},
        
        
        "currentState": {"class_name": "CodeableConcept", "is_contained": False},
        
        
        "statusDate": {"class_name": "StatusDate", "is_contained": True},
        
        
        "relatedArtifact": {"class_name": "RelatedArtifact", "is_contained": False},
        
        
        "citedArtifact": {"class_name": "CitedArtifact", "is_contained": True},
        
        }
    def __init__(self, resourceType: str = None,  id:  'str'  = None,  meta:  'Meta'  = None,  implicitRules:  'str'  = None,  language:  'str'  = None,  text:  'Narrative'  = None,  contained:  list['Resource']  = None,  extension:  list['Extension']  = None,  modifierExtension:  list['Extension']  = None,  url:  'str'  = None,  identifier:  list['Identifier']  = None,  version:  'str'  = None,  versionAlgorithmString:  'str'  = None,  versionAlgorithmCoding:  'Coding'  = None,  name:  'str'  = None,  title:  'str'  = None,  status:  'str'  = None,  experimental:  'bool'  = None,  date:  'str'  = None,  publisher:  'str'  = None,  contact:  list['ContactDetail']  = None,  description:  'str'  = None,  useContext:  list['UsageContext']  = None,  jurisdiction:  list['CodeableConcept']  = None,  purpose:  'str'  = None,  copyright:  'str'  = None,  copyrightLabel:  'str'  = None,  approvalDate:  'str'  = None,  lastReviewDate:  'str'  = None,  effectivePeriod:  'Period'  = None,  author:  list['ContactDetail']  = None,  editor:  list['ContactDetail']  = None,  reviewer:  list['ContactDetail']  = None,  endorser:  list['ContactDetail']  = None,  summary:  list['Summary']  = None,  classification:  list['Classification']  = None,  note:  list['Annotation']  = None,  currentState:  list['CodeableConcept']  = None,  statusDate:  list['StatusDate']  = None,  relatedArtifact:  list['RelatedArtifact']  = None,  citedArtifact:  'CitedArtifact'  = None, ):
        self.resourceType = resourceType or "Citation"
        self.id = id 
        self.meta = meta 
        self.implicitRules = implicitRules 
        self.language = language 
        self.text = text 
        self.contained = contained or []
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.url = url 
        self.identifier = identifier or []
        self.version = version 
        self.versionAlgorithmString = versionAlgorithmString 
        self.versionAlgorithmCoding = versionAlgorithmCoding 
        self.name = name 
        self.title = title 
        self.status = status 
        self.experimental = experimental 
        self.date = date 
        self.publisher = publisher 
        self.contact = contact or []
        self.description = description 
        self.useContext = useContext or []
        self.jurisdiction = jurisdiction or []
        self.purpose = purpose 
        self.copyright = copyright 
        self.copyrightLabel = copyrightLabel 
        self.approvalDate = approvalDate 
        self.lastReviewDate = lastReviewDate 
        self.effectivePeriod = effectivePeriod 
        self.author = author or []
        self.editor = editor or []
        self.reviewer = reviewer or []
        self.endorser = endorser or []
        self.summary = summary or []
        self.classification = classification or []
        self.note = note or []
        self.currentState = currentState or []
        self.statusDate = statusDate or []
        self.relatedArtifact = relatedArtifact or []
        self.citedArtifact = citedArtifact 
        

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        return super().from_dict(data)
    
    @classmethod
    def from_obj(self, obj: object) -> "Citation":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()