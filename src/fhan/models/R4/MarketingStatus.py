"""
Generated class for MarketingStatus. 
Time: 2023-09-29 20:34:26
"""
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Extension import *
from fhan.models.R4.Period import *
from fhan.models.generator_models import BaseModel


class MarketingStatus(BaseModel):
    """Base StructureDefinition for MarketingStatus Type: The marketing status describes the date when a medicinal product is actually put on the market or the date as of which it is no longer available.
    :param str id: Unique id for inter-element referencing
    :param Extension extension: Additional content defined by implementations
    :param Extension modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param CodeableConcept country: The country in which the marketing authorisation has been granted shall be specified It should be specified using the ISO 3166 ‑ 1 alpha-2 code elements
    :param CodeableConcept jurisdiction: Where a Medicines Regulatory Agency has granted a marketing authorisation for which specific provisions within a jurisdiction apply, the jurisdiction can be specified using an appropriate controlled terminology The controlled term and the controlled term identifier shall be specified
    :param CodeableConcept status: This attribute provides information on the status of the marketing of the medicinal product See ISO/TS 20443 for more information and examples
    :param Period dateRange: The date when the Medicinal Product is placed on the market by the Marketing Authorisation Holder (or where applicable, the manufacturer/distributor) in a country and/or jurisdiction shall be provided A complete date consisting of day, month and year shall be specified using the ISO 8601 date format NOTE “Placed on the market” refers to the release of the Medicinal Product into the distribution chain
    :param str restoreDate: The date when the Medicinal Product is placed on the market by the Marketing Authorisation Holder (or where applicable, the manufacturer/distributor) in a country and/or jurisdiction shall be provided A complete date consisting of day, month and year shall be specified using the ISO 8601 date format NOTE “Placed on the market” refers to the release of the Medicinal Product into the distribution chain
    """

    # needed for complex properties where the element name is different from the class name
    property_class_info = {
        "extension": {"class_name": "Extension", "is_contained": False},
        "modifierExtension": {"class_name": "Extension", "is_contained": False},
        "country": {"class_name": "CodeableConcept", "is_contained": False},
        "jurisdiction": {"class_name": "CodeableConcept", "is_contained": False},
        "status": {"class_name": "CodeableConcept", "is_contained": False},
        "dateRange": {"class_name": "Period", "is_contained": False},
    }

    def __init__(
        self,
        resourceType: str = None,
        id: "str" = None,
        extension: list["Extension"] = None,
        modifierExtension: list["Extension"] = None,
        country: "CodeableConcept" = None,
        jurisdiction: "CodeableConcept" = None,
        status: "CodeableConcept" = None,
        dateRange: "Period" = None,
        restoreDate: "str" = None,
    ):
        self.resourceType = resourceType or "MarketingStatus"
        self.id = id
        self.extension = extension or []
        self.modifierExtension = modifierExtension or []
        self.country = country
        self.jurisdiction = jurisdiction
        self.status = status
        self.dateRange = dateRange
        self.restoreDate = restoreDate

    @classmethod
    def from_dict(cls, data: dict) -> "MarketingStatus":
        return super().from_dict(data)

    @classmethod
    def from_obj(self, obj: object) -> "MarketingStatus":
        return super().from_obj(obj)

    def as_dict(self) -> dict:
        return super().as_dict()
