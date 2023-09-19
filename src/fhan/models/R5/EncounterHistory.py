"""
Generated class for EncounterHistory. 
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
from fhan.models.R5.Duration import *


@dataclass
class EncounterHistory:
    """ A record of significant events/milestones key data throughout the history of an Encounter
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Reference encounter: The Encounter associated with this set of historic values
    :param Identifier identifier: Identifier(s) by which this encounter is known
    :param str status: planned | in-progress | on-hold | discharged | completed | cancelled | discontinued | entered-in-error | unknown
    :param CodeableConcept class: Classification of patient encounter
    :param CodeableConcept type: Specific type of encounter
    :param CodeableReference serviceType: Specific type of service
    :param Reference subject: The patient or group related to this encounter
    :param CodeableConcept subjectStatus: The current status of the subject in relation to the Encounter
    :param Period actualPeriod: The actual start and end time associated with this set of values associated with the encounter
    :param str plannedStartDate: The planned start date/time (or admission date) of the encounter
    :param str plannedEndDate: The planned end date/time (or discharge date) of the encounter
    :param Duration length: Actual quantity of time the encounter lasted (less time absent)
    :param BackboneElement location: Location of the patient at this point in the encounter
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param Reference location: Location the encounter takes place
    :param CodeableConcept form: The physical type of the location (usually the level in the location hierarchy - bed, room, ward, virtual etc.)
    
    """
    id: str = None
    
    meta: "Meta" = None
    
    implicitRules: str = None
    
    language: str = None
    
    text: "Narrative" = None
    
    contained: "Resource" = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    encounter: "Reference" = None
    
    identifier: "Identifier" = None
    
    status: str = None
    
    class: "CodeableConcept" = None
    
    type: "CodeableConcept" = None
    
    serviceType: "CodeableReference" = None
    
    subject: "Reference" = None
    
    subjectStatus: "CodeableConcept" = None
    
    actualPeriod: "Period" = None
    
    plannedStartDate: str = None
    
    plannedEndDate: str = None
    
    length: "Duration" = None
    
    location: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    location: "Reference" = None
    
    form: "CodeableConcept" = None
    