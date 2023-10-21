# generated at 2023-10-05 18:29:10.331759 from /Users/tillrostalski/Git/fhan/src/fhan/client/scripts/create_from_template.py
from typing import Union
from fhan.client.search_bundle import SearchBundle


class SearchResourceMixin:
    """This mixin class provides the SearchHandler with methods for each
    resource type. The methods are syntactic sugar for the _search method.
    """

    def __init__(self):
        pass

    def Account(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Accounts. The search string is passed
        directly to the API."""
        return self._search("Account", search, as_object)

    def ActivityDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ActivityDefinitions. The search string is passed
        directly to the API."""
        return self._search("ActivityDefinition", search, as_object)

    def AdverseEvent(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for AdverseEvents. The search string is passed
        directly to the API."""
        return self._search("AdverseEvent", search, as_object)

    def AllergyIntolerance(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for AllergyIntolerances. The search string is passed
        directly to the API."""
        return self._search("AllergyIntolerance", search, as_object)

    def Appointment(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Appointments. The search string is passed
        directly to the API."""
        return self._search("Appointment", search, as_object)

    def AppointmentResponse(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for AppointmentResponses. The search string is passed
        directly to the API."""
        return self._search("AppointmentResponse", search, as_object)

    def AuditEvent(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for AuditEvents. The search string is passed
        directly to the API."""
        return self._search("AuditEvent", search, as_object)

    def Basic(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Basics. The search string is passed
        directly to the API."""
        return self._search("Basic", search, as_object)

    def Binary(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Binarys. The search string is passed
        directly to the API."""
        return self._search("Binary", search, as_object)

    def BiologicallyDerivedProduct(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for BiologicallyDerivedProducts. The search string is passed
        directly to the API."""
        return self._search("BiologicallyDerivedProduct", search, as_object)

    def BodyStructure(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for BodyStructures. The search string is passed
        directly to the API."""
        return self._search("BodyStructure", search, as_object)

    def Bundle(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Bundles. The search string is passed
        directly to the API."""
        return self._search("Bundle", search, as_object)

    def CapabilityStatement(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CapabilityStatements. The search string is passed
        directly to the API."""
        return self._search("CapabilityStatement", search, as_object)

    def CarePlan(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CarePlans. The search string is passed
        directly to the API."""
        return self._search("CarePlan", search, as_object)

    def CareTeam(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CareTeams. The search string is passed
        directly to the API."""
        return self._search("CareTeam", search, as_object)

    def CatalogEntry(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CatalogEntrys. The search string is passed
        directly to the API."""
        return self._search("CatalogEntry", search, as_object)

    def ChargeItem(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ChargeItems. The search string is passed
        directly to the API."""
        return self._search("ChargeItem", search, as_object)

    def ChargeItemDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ChargeItemDefinitions. The search string is passed
        directly to the API."""
        return self._search("ChargeItemDefinition", search, as_object)

    def Claim(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Claims. The search string is passed
        directly to the API."""
        return self._search("Claim", search, as_object)

    def ClaimResponse(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ClaimResponses. The search string is passed
        directly to the API."""
        return self._search("ClaimResponse", search, as_object)

    def ClinicalImpression(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ClinicalImpressions. The search string is passed
        directly to the API."""
        return self._search("ClinicalImpression", search, as_object)

    def CodeSystem(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CodeSystems. The search string is passed
        directly to the API."""
        return self._search("CodeSystem", search, as_object)

    def Communication(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Communications. The search string is passed
        directly to the API."""
        return self._search("Communication", search, as_object)

    def CommunicationRequest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CommunicationRequests. The search string is passed
        directly to the API."""
        return self._search("CommunicationRequest", search, as_object)

    def CompartmentDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CompartmentDefinitions. The search string is passed
        directly to the API."""
        return self._search("CompartmentDefinition", search, as_object)

    def Composition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Compositions. The search string is passed
        directly to the API."""
        return self._search("Composition", search, as_object)

    def ConceptMap(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ConceptMaps. The search string is passed
        directly to the API."""
        return self._search("ConceptMap", search, as_object)

    def Condition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Conditions. The search string is passed
        directly to the API."""
        return self._search("Condition", search, as_object)

    def Consent(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Consents. The search string is passed
        directly to the API."""
        return self._search("Consent", search, as_object)

    def Contract(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Contracts. The search string is passed
        directly to the API."""
        return self._search("Contract", search, as_object)

    def Coverage(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Coverages. The search string is passed
        directly to the API."""
        return self._search("Coverage", search, as_object)

    def CoverageEligibilityRequest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CoverageEligibilityRequests. The search string is passed
        directly to the API."""
        return self._search("CoverageEligibilityRequest", search, as_object)

    def CoverageEligibilityResponse(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for CoverageEligibilityResponses. The search string is passed
        directly to the API."""
        return self._search("CoverageEligibilityResponse", search, as_object)

    def DetectedIssue(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DetectedIssues. The search string is passed
        directly to the API."""
        return self._search("DetectedIssue", search, as_object)

    def Device(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Devices. The search string is passed
        directly to the API."""
        return self._search("Device", search, as_object)

    def DeviceDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DeviceDefinitions. The search string is passed
        directly to the API."""
        return self._search("DeviceDefinition", search, as_object)

    def DeviceMetric(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DeviceMetrics. The search string is passed
        directly to the API."""
        return self._search("DeviceMetric", search, as_object)

    def DeviceRequest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DeviceRequests. The search string is passed
        directly to the API."""
        return self._search("DeviceRequest", search, as_object)

    def DeviceUseStatement(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DeviceUseStatements. The search string is passed
        directly to the API."""
        return self._search("DeviceUseStatement", search, as_object)

    def DiagnosticReport(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DiagnosticReports. The search string is passed
        directly to the API."""
        return self._search("DiagnosticReport", search, as_object)

    def DocumentManifest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DocumentManifests. The search string is passed
        directly to the API."""
        return self._search("DocumentManifest", search, as_object)

    def DocumentReference(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for DocumentReferences. The search string is passed
        directly to the API."""
        return self._search("DocumentReference", search, as_object)

    def EffectEvidenceSynthesis(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for EffectEvidenceSynthesiss. The search string is passed
        directly to the API."""
        return self._search("EffectEvidenceSynthesis", search, as_object)

    def Encounter(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Encounters. The search string is passed
        directly to the API."""
        return self._search("Encounter", search, as_object)

    def Endpoint(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Endpoints. The search string is passed
        directly to the API."""
        return self._search("Endpoint", search, as_object)

    def EnrollmentRequest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for EnrollmentRequests. The search string is passed
        directly to the API."""
        return self._search("EnrollmentRequest", search, as_object)

    def EnrollmentResponse(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for EnrollmentResponses. The search string is passed
        directly to the API."""
        return self._search("EnrollmentResponse", search, as_object)

    def EpisodeOfCare(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for EpisodeOfCares. The search string is passed
        directly to the API."""
        return self._search("EpisodeOfCare", search, as_object)

    def EventDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for EventDefinitions. The search string is passed
        directly to the API."""
        return self._search("EventDefinition", search, as_object)

    def Evidence(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Evidences. The search string is passed
        directly to the API."""
        return self._search("Evidence", search, as_object)

    def EvidenceVariable(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for EvidenceVariables. The search string is passed
        directly to the API."""
        return self._search("EvidenceVariable", search, as_object)

    def ExampleScenario(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ExampleScenarios. The search string is passed
        directly to the API."""
        return self._search("ExampleScenario", search, as_object)

    def ExplanationOfBenefit(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ExplanationOfBenefits. The search string is passed
        directly to the API."""
        return self._search("ExplanationOfBenefit", search, as_object)

    def FamilyMemberHistory(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for FamilyMemberHistorys. The search string is passed
        directly to the API."""
        return self._search("FamilyMemberHistory", search, as_object)

    def Flag(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Flags. The search string is passed
        directly to the API."""
        return self._search("Flag", search, as_object)

    def Goal(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Goals. The search string is passed
        directly to the API."""
        return self._search("Goal", search, as_object)

    def GraphDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for GraphDefinitions. The search string is passed
        directly to the API."""
        return self._search("GraphDefinition", search, as_object)

    def Group(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Groups. The search string is passed
        directly to the API."""
        return self._search("Group", search, as_object)

    def GuidanceResponse(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for GuidanceResponses. The search string is passed
        directly to the API."""
        return self._search("GuidanceResponse", search, as_object)

    def HealthcareService(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for HealthcareServices. The search string is passed
        directly to the API."""
        return self._search("HealthcareService", search, as_object)

    def ImagingStudy(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ImagingStudys. The search string is passed
        directly to the API."""
        return self._search("ImagingStudy", search, as_object)

    def Immunization(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Immunizations. The search string is passed
        directly to the API."""
        return self._search("Immunization", search, as_object)

    def ImmunizationEvaluation(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ImmunizationEvaluations. The search string is passed
        directly to the API."""
        return self._search("ImmunizationEvaluation", search, as_object)

    def ImmunizationRecommendation(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ImmunizationRecommendations. The search string is passed
        directly to the API."""
        return self._search("ImmunizationRecommendation", search, as_object)

    def ImplementationGuide(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ImplementationGuides. The search string is passed
        directly to the API."""
        return self._search("ImplementationGuide", search, as_object)

    def InsurancePlan(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for InsurancePlans. The search string is passed
        directly to the API."""
        return self._search("InsurancePlan", search, as_object)

    def Invoice(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Invoices. The search string is passed
        directly to the API."""
        return self._search("Invoice", search, as_object)

    def Library(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Librarys. The search string is passed
        directly to the API."""
        return self._search("Library", search, as_object)

    def Linkage(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Linkages. The search string is passed
        directly to the API."""
        return self._search("Linkage", search, as_object)

    def List(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Lists. The search string is passed
        directly to the API."""
        return self._search("List", search, as_object)

    def Location(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Locations. The search string is passed
        directly to the API."""
        return self._search("Location", search, as_object)

    def Measure(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Measures. The search string is passed
        directly to the API."""
        return self._search("Measure", search, as_object)

    def MeasureReport(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MeasureReports. The search string is passed
        directly to the API."""
        return self._search("MeasureReport", search, as_object)

    def Media(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Medias. The search string is passed
        directly to the API."""
        return self._search("Media", search, as_object)

    def Medication(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Medications. The search string is passed
        directly to the API."""
        return self._search("Medication", search, as_object)

    def MedicationAdministration(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicationAdministrations. The search string is passed
        directly to the API."""
        return self._search("MedicationAdministration", search, as_object)

    def MedicationDispense(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicationDispenses. The search string is passed
        directly to the API."""
        return self._search("MedicationDispense", search, as_object)

    def MedicationKnowledge(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicationKnowledges. The search string is passed
        directly to the API."""
        return self._search("MedicationKnowledge", search, as_object)

    def MedicationRequest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicationRequests. The search string is passed
        directly to the API."""
        return self._search("MedicationRequest", search, as_object)

    def MedicationStatement(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicationStatements. The search string is passed
        directly to the API."""
        return self._search("MedicationStatement", search, as_object)

    def MedicinalProduct(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProducts. The search string is passed
        directly to the API."""
        return self._search("MedicinalProduct", search, as_object)

    def MedicinalProductAuthorization(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductAuthorizations. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductAuthorization", search, as_object)

    def MedicinalProductContraindication(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductContraindications. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductContraindication", search, as_object)

    def MedicinalProductIndication(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductIndications. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductIndication", search, as_object)

    def MedicinalProductIngredient(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductIngredients. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductIngredient", search, as_object)

    def MedicinalProductInteraction(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductInteractions. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductInteraction", search, as_object)

    def MedicinalProductManufactured(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductManufactureds. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductManufactured", search, as_object)

    def MedicinalProductPackaged(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductPackageds. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductPackaged", search, as_object)

    def MedicinalProductPharmaceutical(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductPharmaceuticals. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductPharmaceutical", search, as_object)

    def MedicinalProductUndesirableEffect(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MedicinalProductUndesirableEffects. The search string is passed
        directly to the API."""
        return self._search("MedicinalProductUndesirableEffect", search, as_object)

    def MessageDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MessageDefinitions. The search string is passed
        directly to the API."""
        return self._search("MessageDefinition", search, as_object)

    def MessageHeader(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MessageHeaders. The search string is passed
        directly to the API."""
        return self._search("MessageHeader", search, as_object)

    def MolecularSequence(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for MolecularSequences. The search string is passed
        directly to the API."""
        return self._search("MolecularSequence", search, as_object)

    def NamingSystem(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for NamingSystems. The search string is passed
        directly to the API."""
        return self._search("NamingSystem", search, as_object)

    def NutritionOrder(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for NutritionOrders. The search string is passed
        directly to the API."""
        return self._search("NutritionOrder", search, as_object)

    def Observation(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Observations. The search string is passed
        directly to the API."""
        return self._search("Observation", search, as_object)

    def ObservationDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ObservationDefinitions. The search string is passed
        directly to the API."""
        return self._search("ObservationDefinition", search, as_object)

    def OperationDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for OperationDefinitions. The search string is passed
        directly to the API."""
        return self._search("OperationDefinition", search, as_object)

    def OperationOutcome(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for OperationOutcomes. The search string is passed
        directly to the API."""
        return self._search("OperationOutcome", search, as_object)

    def Organization(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Organizations. The search string is passed
        directly to the API."""
        return self._search("Organization", search, as_object)

    def OrganizationAffiliation(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for OrganizationAffiliations. The search string is passed
        directly to the API."""
        return self._search("OrganizationAffiliation", search, as_object)

    def Patient(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Patients. The search string is passed
        directly to the API."""
        return self._search("Patient", search, as_object)

    def PaymentNotice(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for PaymentNotices. The search string is passed
        directly to the API."""
        return self._search("PaymentNotice", search, as_object)

    def PaymentReconciliation(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for PaymentReconciliations. The search string is passed
        directly to the API."""
        return self._search("PaymentReconciliation", search, as_object)

    def Person(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Persons. The search string is passed
        directly to the API."""
        return self._search("Person", search, as_object)

    def PlanDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for PlanDefinitions. The search string is passed
        directly to the API."""
        return self._search("PlanDefinition", search, as_object)

    def Practitioner(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Practitioners. The search string is passed
        directly to the API."""
        return self._search("Practitioner", search, as_object)

    def PractitionerRole(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for PractitionerRoles. The search string is passed
        directly to the API."""
        return self._search("PractitionerRole", search, as_object)

    def Procedure(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Procedures. The search string is passed
        directly to the API."""
        return self._search("Procedure", search, as_object)

    def Provenance(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Provenances. The search string is passed
        directly to the API."""
        return self._search("Provenance", search, as_object)

    def Questionnaire(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Questionnaires. The search string is passed
        directly to the API."""
        return self._search("Questionnaire", search, as_object)

    def QuestionnaireResponse(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for QuestionnaireResponses. The search string is passed
        directly to the API."""
        return self._search("QuestionnaireResponse", search, as_object)

    def RelatedPerson(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for RelatedPersons. The search string is passed
        directly to the API."""
        return self._search("RelatedPerson", search, as_object)

    def RequestGroup(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for RequestGroups. The search string is passed
        directly to the API."""
        return self._search("RequestGroup", search, as_object)

    def ResearchDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ResearchDefinitions. The search string is passed
        directly to the API."""
        return self._search("ResearchDefinition", search, as_object)

    def ResearchElementDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ResearchElementDefinitions. The search string is passed
        directly to the API."""
        return self._search("ResearchElementDefinition", search, as_object)

    def ResearchStudy(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ResearchStudys. The search string is passed
        directly to the API."""
        return self._search("ResearchStudy", search, as_object)

    def ResearchSubject(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ResearchSubjects. The search string is passed
        directly to the API."""
        return self._search("ResearchSubject", search, as_object)

    def RiskAssessment(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for RiskAssessments. The search string is passed
        directly to the API."""
        return self._search("RiskAssessment", search, as_object)

    def RiskEvidenceSynthesis(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for RiskEvidenceSynthesiss. The search string is passed
        directly to the API."""
        return self._search("RiskEvidenceSynthesis", search, as_object)

    def Schedule(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Schedules. The search string is passed
        directly to the API."""
        return self._search("Schedule", search, as_object)

    def SearchParameter(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SearchParameters. The search string is passed
        directly to the API."""
        return self._search("SearchParameter", search, as_object)

    def ServiceRequest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ServiceRequests. The search string is passed
        directly to the API."""
        return self._search("ServiceRequest", search, as_object)

    def Slot(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Slots. The search string is passed
        directly to the API."""
        return self._search("Slot", search, as_object)

    def Specimen(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Specimens. The search string is passed
        directly to the API."""
        return self._search("Specimen", search, as_object)

    def SpecimenDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SpecimenDefinitions. The search string is passed
        directly to the API."""
        return self._search("SpecimenDefinition", search, as_object)

    def StructureDefinition(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for StructureDefinitions. The search string is passed
        directly to the API."""
        return self._search("StructureDefinition", search, as_object)

    def StructureMap(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for StructureMaps. The search string is passed
        directly to the API."""
        return self._search("StructureMap", search, as_object)

    def Subscription(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Subscriptions. The search string is passed
        directly to the API."""
        return self._search("Subscription", search, as_object)

    def Substance(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Substances. The search string is passed
        directly to the API."""
        return self._search("Substance", search, as_object)

    def SubstanceNucleicAcid(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SubstanceNucleicAcids. The search string is passed
        directly to the API."""
        return self._search("SubstanceNucleicAcid", search, as_object)

    def SubstancePolymer(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SubstancePolymers. The search string is passed
        directly to the API."""
        return self._search("SubstancePolymer", search, as_object)

    def SubstanceProtein(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SubstanceProteins. The search string is passed
        directly to the API."""
        return self._search("SubstanceProtein", search, as_object)

    def SubstanceReferenceInformation(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SubstanceReferenceInformations. The search string is passed
        directly to the API."""
        return self._search("SubstanceReferenceInformation", search, as_object)

    def SubstanceSourceMaterial(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SubstanceSourceMaterials. The search string is passed
        directly to the API."""
        return self._search("SubstanceSourceMaterial", search, as_object)

    def SubstanceSpecification(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SubstanceSpecifications. The search string is passed
        directly to the API."""
        return self._search("SubstanceSpecification", search, as_object)

    def SupplyDelivery(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SupplyDeliverys. The search string is passed
        directly to the API."""
        return self._search("SupplyDelivery", search, as_object)

    def SupplyRequest(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for SupplyRequests. The search string is passed
        directly to the API."""
        return self._search("SupplyRequest", search, as_object)

    def Task(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for Tasks. The search string is passed
        directly to the API."""
        return self._search("Task", search, as_object)

    def TerminologyCapabilities(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for TerminologyCapabilitiess. The search string is passed
        directly to the API."""
        return self._search("TerminologyCapabilities", search, as_object)

    def TestReport(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for TestReports. The search string is passed
        directly to the API."""
        return self._search("TestReport", search, as_object)

    def TestScript(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for TestScripts. The search string is passed
        directly to the API."""
        return self._search("TestScript", search, as_object)

    def ValueSet(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for ValueSets. The search string is passed
        directly to the API."""
        return self._search("ValueSet", search, as_object)

    def VerificationResult(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for VerificationResults. The search string is passed
        directly to the API."""
        return self._search("VerificationResult", search, as_object)

    def VisionPrescription(
        self,
        search: str = None,
        as_object: bool = False,
    ) -> Union[dict, SearchBundle]:
        """Search for VisionPrescriptions. The search string is passed
        directly to the API."""
        return self._search("VisionPrescription", search, as_object)
