"""
Generated class for DeviceMetric. 
Time: 2023-09-19 22:48:02
"""
from dataclasses import dataclass

from fhan.models.R4.Reference import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Meta import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Extension import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Timing import *
from fhan.models.generator_models import ModelBase


@dataclass
class DeviceMetric(ModelBase):
    """ Describes a measurement, calculation or setting capability of a medical device.
    :param str id: Logical id of this artifact
    :param Meta meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param Narrative text: Text summary of the resource, for human interpretation
    :param Resource contained: Contained, inline Resources
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored
    :param Identifier identifier: Instance identifier
    :param CodeableConcept type: Identity of metric, for example Heart Rate or PEEP Setting
    :param CodeableConcept unit: Unit of Measure for the Metric
    :param Reference source: Describes the link to the source Device
    :param Reference parent: Describes the link to the parent Device
    :param str operationalStatus: on | off | standby | entered-in-error
    :param str color: black | red | green | yellow | blue | magenta | cyan | white
    :param str category: measurement | setting | calculation | unspecified
    :param Timing measurementPeriod: Describes the measurement repetition time
    :param BackboneElement calibration: Describes the calibrations that have been performed or that are required to be performed
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: unspecified | offset | gain | two-point
    :param str state: not-calibrated | calibration-required | calibrated | unspecified
    :param str time: Describes the time last calibration has been performed
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
    
    type: "CodeableConcept" = None
    
    unit: "CodeableConcept" = None
    
    source: "Reference" = None
    
    parent: "Reference" = None
    
    operationalStatus: str = None
    
    color: str = None
    
    category: str = None
    
    measurementPeriod: "Timing" = None
    
    calibration: "BackboneElement" = None
    
    id: str = None
    
    extension: "Extension" = None
    
    modifierExtension: "Extension" = None
    
    type: str = None
    
    state: str = None
    
    time: str = None
    