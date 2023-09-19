"""
Generated class for Citation. 
Time: 2023-09-19 20:23:02
"""
from dataclasses import dataclass
from fhan.models.R4B.Extension import *
from fhan.models.R4B.HumanName import *
from fhan.models.R4B.ContactPoint import *
from fhan.models.R4B.Address import *
from fhan.models.R4B.Meta import *
from fhan.models.R4B.Narrative import *
from fhan.models.R4B.Identifier import *
from fhan.models.R4B.UsageContext import *
from fhan.models.R4B.BackboneElement import *
from fhan.models.R4B.Attachment import *
from fhan.models.R4B.Resource import *
from fhan.models.R4B.Period import *
from fhan.models.R4B.Annotation import *
from fhan.models.R4B.ContactDetail import *
from fhan.models.R4B.CodeableConcept import *
from fhan.models.R4B.Reference import *


@dataclass
class Citation:
    """
    The Citation Resource enables reference to any knowledge artifact for purposes of identification and attribution. The Citation Resource supports existing reference structures and developing publication practices such as versioning, expressing complex contributorship roles, and referencing computable resources.
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    url: str = None
    
    identifier: "Identifier" = None
    
    version: str = None
    
    name: str = None
    
    title: str = None
    
    status: str = None
    
    experimental: bool = None
    
    date: str = None
    
    publisher: str = None
    
    contact: "ContactDetail" = None
    
    description: str = None
    
    useContext: "UsageContext" = None
    
    jurisdiction: "CodeableConcept" = None
    
    purpose: str = None
    
    copyright: str = None
    
    approvalDate: str = None
    
    lastReviewDate: str = None
    
    effectivePeriod: "Period" = None
    
    author: "ContactDetail" = None
    
    editor: "ContactDetail" = None
    
    reviewer: "ContactDetail" = None
    
    endorser: "ContactDetail" = None
    
    summary: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    style: "CodeableConcept" = None
    
    text: str = None
    
    classification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    classifier: "CodeableConcept" = None
    
    note: "Annotation" = None
    
    currentState: "CodeableConcept" = None
    
    statusDate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    activity: "CodeableConcept" = None
    
    actual: bool = None
    
    period: "Period" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationshipType: "CodeableConcept" = None
    
    targetClassifier: "CodeableConcept" = None
    
    targeturi: str = None
    
    targeturi: "Identifier" = None
    
    targeturi: "Reference" = None
    
    targeturi: "Attachment" = None
    
    citedArtifact: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    identifier: "Identifier" = None
    
    relatedIdentifier: "Identifier" = None
    
    dateAccessed: str = None
    
    version: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    value: str = None
    
    baseCitation: "Reference" = None
    
    currentState: "CodeableConcept" = None
    
    statusDate: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    activity: "CodeableConcept" = None
    
    actual: bool = None
    
    period: "Period" = None
    
    title: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    language: "CodeableConcept" = None
    
    text: str = None
    
    abstract: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    language: "CodeableConcept" = None
    
    text: str = None
    
    copyright: str = None
    
    part: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    value: str = None
    
    baseCitation: "Reference" = None
    
    relatesTo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    relationshipType: "CodeableConcept" = None
    
    targetClassifier: "CodeableConcept" = None
    
    targeturi: str = None
    
    targeturi: "Identifier" = None
    
    targeturi: "Reference" = None
    
    targeturi: "Attachment" = None
    
    publicationForm: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    publishedIn: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    identifier: "Identifier" = None
    
    title: str = None
    
    publisher: "Reference" = None
    
    publisherLocation: str = None
    
    periodicRelease: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    citedMedium: "CodeableConcept" = None
    
    volume: str = None
    
    issue: str = None
    
    dateOfPublication: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    date: str = None
    
    year: str = None
    
    month: str = None
    
    day: str = None
    
    season: str = None
    
    text: str = None
    
    articleDate: str = None
    
    lastRevisionDate: str = None
    
    language: "CodeableConcept" = None
    
    accessionNumber: str = None
    
    pageString: str = None
    
    firstPage: str = None
    
    lastPage: str = None
    
    pageCount: str = None
    
    copyright: str = None
    
    webLocation: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    url: str = None
    
    classification: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    classifier: "CodeableConcept" = None
    
    whoClassified: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    person: "Reference" = None
    
    organization: "Reference" = None
    
    publisher: "Reference" = None
    
    classifierCopyright: str = None
    
    freeToShare: bool = None
    
    contributorship: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    complete: bool = None
    
    entry: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    name: "HumanName" = None
    
    initials: str = None
    
    collectiveName: str = None
    
    identifier: "Identifier" = None
    
    affiliationInfo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    affiliation: str = None
    
    role: str = None
    
    identifier: "Identifier" = None
    
    address: "Address" = None
    
    telecom: "ContactPoint" = None
    
    contributionType: "CodeableConcept" = None
    
    role: "CodeableConcept" = None
    
    contributionInstance: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    time: str = None
    
    correspondingContact: bool = None
    
    listOrder: int = None
    
    summary: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    style: "CodeableConcept" = None
    
    source: "CodeableConcept" = None
    
    value: str = None
    
    note: "Annotation" = None
    