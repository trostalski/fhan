"""
Generated class for DiagnosticReport. 
Time: 2023-09-19 20:34:27
"""
from dataclasses import dataclass
from fhan.models.R5.Meta import *
from fhan.models.R5.BackboneElement import *
from fhan.models.R5.Extension import *
from fhan.models.R5.Annotation import *
from fhan.models.R5.CodeableConcept import *
from fhan.models.R5.Attachment import *
from fhan.models.R5.Resource import *
from fhan.models.R5.Period import *
from fhan.models.R5.Narrative import *
from fhan.models.R5.Identifier import *
from fhan.models.R5.Reference import *


@dataclass
class DiagnosticReport:
    """ The findings and interpretation of diagnostic tests performed on patients, groups of patients, products, substances, devices, and locations, and/or specimens derived from these. The report includes clinical context such as requesting provider information, and some mix of atomic results, images, textual and coded interpretations, and formatted representation of diagnostic reports. The report also includes non-clinical context such as batch analysis and stability reporting of products and substances.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Business identifier for report
    :param Reference basedOn: What was requested
    :param str status: registered | partial | preliminary | modified | final | amended | corrected | appended | cancelled | entered-in-error | unknown
    :param CodeableConcept category: Service category
    :param CodeableConcept code: Name/Code for this diagnostic report
    :param Reference subject: The subject of the report - usually, but not always, the patient
    :param Reference encounter: Health care event when test ordered
    :param str effectivedateTime: Clinically relevant time/time-period for report
    :param Period effectivedateTime: Clinically relevant time/time-period for report
    :param str issued: DateTime this version was made
    :param Reference performer: Responsible Diagnostic Service
    :param Reference resultsInterpreter: Primary result interpreter
    :param Reference specimen: Specimens this report is based on
    :param Reference result: Observations
    :param Annotation note: Comments about the diagnostic report
    :param Reference study: Reference to full details of an analysis associated with the diagnostic report
    :param BackboneElement supportingInfo: Additional information supporting the diagnostic report
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept type: Supporting information role code
    :param Reference reference: Supporting information reference
    :param BackboneElement media: Key images or data associated with this report
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str comment: Comment about the image or data (e.g. explanation)
    :param Reference link: Reference to the image or data source
    :param Reference composition: Reference to a Composition resource for the DiagnosticReport structure
    :param str conclusion: Clinical conclusion (interpretation) of test results
    :param CodeableConcept conclusionCode: Codes for the clinical conclusion of test results
    :param Attachment presentedForm: Entire report as issued
    
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
    
    basedOn: "Reference" = None
    
    status: str = None
    
    category: "CodeableConcept" = None
    
    code: "CodeableConcept" = None
    
    subject: "Reference" = None
    
    encounter: "Reference" = None
    
    effectivedateTime: str = None
    
    effectivedateTime: "Period" = None
    
    issued: str = None
    
    performer: "Reference" = None
    
    resultsInterpreter: "Reference" = None
    
    specimen: "Reference" = None
    
    result: "Reference" = None
    
    note: "Annotation" = None
    
    study: "Reference" = None
    
    supportingInfo: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: "CodeableConcept" = None
    
    reference: "Reference" = None
    
    media: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    comment: str = None
    
    link: "Reference" = None
    
    composition: "Reference" = None
    
    conclusion: str = None
    
    conclusionCode: "CodeableConcept" = None
    
    presentedForm: "Attachment" = None
    