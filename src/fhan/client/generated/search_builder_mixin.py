# generated at 2023-10-10 10:57:20.304823 from /Users/tillrostalski/Git/fhan/src/fhan/client/scripts/create_from_template.py

from fhan.client.generated.search_builder import (
    AccountSearchBuilder, ActivityDefinitionSearchBuilder,
    ActorDefinitionSearchBuilder, AdministrableProductDefinitionSearchBuilder,
    AdverseEventSearchBuilder, AllergyIntoleranceSearchBuilder,
    AppointmentResponseSearchBuilder, AppointmentSearchBuilder,
    ArtifactAssessmentSearchBuilder, AuditEventSearchBuilder,
    BasicSearchBuilder, BinarySearchBuilder,
    BiologicallyDerivedProductDispenseSearchBuilder,
    BiologicallyDerivedProductSearchBuilder, BodyStructureSearchBuilder,
    BundleSearchBuilder, CapabilityStatementSearchBuilder,
    CarePlanSearchBuilder, CareTeamSearchBuilder,
    ChargeItemDefinitionSearchBuilder, ChargeItemSearchBuilder,
    CitationSearchBuilder, ClaimResponseSearchBuilder, ClaimSearchBuilder,
    ClinicalImpressionSearchBuilder, ClinicalUseDefinitionSearchBuilder,
    CodeSystemSearchBuilder, CommunicationRequestSearchBuilder,
    CommunicationSearchBuilder, CompartmentDefinitionSearchBuilder,
    CompositionSearchBuilder, ConceptMapSearchBuilder,
    ConditionDefinitionSearchBuilder, ConditionSearchBuilder,
    ConsentSearchBuilder, ContractSearchBuilder,
    CoverageEligibilityRequestSearchBuilder,
    CoverageEligibilityResponseSearchBuilder, CoverageSearchBuilder,
    DetectedIssueSearchBuilder, DeviceAssociationSearchBuilder,
    DeviceDefinitionSearchBuilder, DeviceDispenseSearchBuilder,
    DeviceMetricSearchBuilder, DeviceRequestSearchBuilder, DeviceSearchBuilder,
    DeviceUsageSearchBuilder, DiagnosticReportSearchBuilder,
    DocumentReferenceSearchBuilder, EncounterHistorySearchBuilder,
    EncounterSearchBuilder, EndpointSearchBuilder,
    EnrollmentRequestSearchBuilder, EnrollmentResponseSearchBuilder,
    EpisodeOfCareSearchBuilder, EventDefinitionSearchBuilder,
    EvidenceReportSearchBuilder, EvidenceSearchBuilder,
    EvidenceVariableSearchBuilder, ExampleScenarioSearchBuilder,
    ExplanationOfBenefitSearchBuilder, FamilyMemberHistorySearchBuilder,
    FlagSearchBuilder, FormularyItemSearchBuilder, GenomicStudySearchBuilder,
    GoalSearchBuilder, GraphDefinitionSearchBuilder, GroupSearchBuilder,
    GuidanceResponseSearchBuilder, HealthcareServiceSearchBuilder,
    ImagingSelectionSearchBuilder, ImagingStudySearchBuilder,
    ImmunizationEvaluationSearchBuilder,
    ImmunizationRecommendationSearchBuilder, ImmunizationSearchBuilder,
    ImplementationGuideSearchBuilder, IngredientSearchBuilder,
    InsurancePlanSearchBuilder, InventoryItemSearchBuilder,
    InventoryReportSearchBuilder, InvoiceSearchBuilder, LibrarySearchBuilder,
    LinkageSearchBuilder, ListSearchBuilder, LocationSearchBuilder,
    ManufacturedItemDefinitionSearchBuilder, MeasureReportSearchBuilder,
    MeasureSearchBuilder, MedicationAdministrationSearchBuilder,
    MedicationDispenseSearchBuilder, MedicationKnowledgeSearchBuilder,
    MedicationRequestSearchBuilder, MedicationSearchBuilder,
    MedicationStatementSearchBuilder, MedicinalProductDefinitionSearchBuilder,
    MessageDefinitionSearchBuilder, MessageHeaderSearchBuilder,
    MolecularSequenceSearchBuilder, NamingSystemSearchBuilder,
    NutritionIntakeSearchBuilder, NutritionOrderSearchBuilder,
    NutritionProductSearchBuilder, ObservationDefinitionSearchBuilder,
    ObservationSearchBuilder, OperationDefinitionSearchBuilder,
    OperationOutcomeSearchBuilder, OrganizationAffiliationSearchBuilder,
    OrganizationSearchBuilder, PackagedProductDefinitionSearchBuilder,
    PatientSearchBuilder, PaymentNoticeSearchBuilder,
    PaymentReconciliationSearchBuilder, PermissionSearchBuilder,
    PersonSearchBuilder, PlanDefinitionSearchBuilder,
    PractitionerRoleSearchBuilder, PractitionerSearchBuilder,
    ProcedureSearchBuilder, ProvenanceSearchBuilder,
    QuestionnaireResponseSearchBuilder, QuestionnaireSearchBuilder,
    RegulatedAuthorizationSearchBuilder, RelatedPersonSearchBuilder,
    RequestOrchestrationSearchBuilder, RequirementsSearchBuilder,
    ResearchStudySearchBuilder, ResearchSubjectSearchBuilder,
    RiskAssessmentSearchBuilder, ScheduleSearchBuilder,
    SearchParameterSearchBuilder, ServiceRequestSearchBuilder,
    SlotSearchBuilder, SpecimenDefinitionSearchBuilder, SpecimenSearchBuilder,
    StructureDefinitionSearchBuilder, StructureMapSearchBuilder,
    SubscriptionSearchBuilder, SubscriptionStatusSearchBuilder,
    SubscriptionTopicSearchBuilder, SubstanceDefinitionSearchBuilder,
    SubstanceNucleicAcidSearchBuilder, SubstancePolymerSearchBuilder,
    SubstanceProteinSearchBuilder, SubstanceReferenceInformationSearchBuilder,
    SubstanceSearchBuilder, SubstanceSourceMaterialSearchBuilder,
    SupplyDeliverySearchBuilder, SupplyRequestSearchBuilder, TaskSearchBuilder,
    TerminologyCapabilitiesSearchBuilder, TestPlanSearchBuilder,
    TestReportSearchBuilder, TestScriptSearchBuilder, TransportSearchBuilder,
    ValueSetSearchBuilder, VerificationResultSearchBuilder,
    VisionPrescriptionSearchBuilder)


class SearchBuilderMixin:
    """This mixin class provides the SearchBuilder class
    with getter methods for each resource type.
    """

    def __init__(self):
        pass

    def Account(self):
        return AccountSearchBuilder(search_string="")

    def ActivityDefinition(self):
        return ActivityDefinitionSearchBuilder(search_string="")

    def ActorDefinition(self):
        return ActorDefinitionSearchBuilder(search_string="")

    def AdministrableProductDefinition(self):
        return AdministrableProductDefinitionSearchBuilder(search_string="")

    def AdverseEvent(self):
        return AdverseEventSearchBuilder(search_string="")

    def AllergyIntolerance(self):
        return AllergyIntoleranceSearchBuilder(search_string="")

    def Appointment(self):
        return AppointmentSearchBuilder(search_string="")

    def AppointmentResponse(self):
        return AppointmentResponseSearchBuilder(search_string="")

    def ArtifactAssessment(self):
        return ArtifactAssessmentSearchBuilder(search_string="")

    def AuditEvent(self):
        return AuditEventSearchBuilder(search_string="")

    def Basic(self):
        return BasicSearchBuilder(search_string="")

    def Binary(self):
        return BinarySearchBuilder(search_string="")

    def BiologicallyDerivedProduct(self):
        return BiologicallyDerivedProductSearchBuilder(search_string="")

    def BiologicallyDerivedProductDispense(self):
        return BiologicallyDerivedProductDispenseSearchBuilder(search_string="")

    def BodyStructure(self):
        return BodyStructureSearchBuilder(search_string="")

    def Bundle(self):
        return BundleSearchBuilder(search_string="")

    def CapabilityStatement(self):
        return CapabilityStatementSearchBuilder(search_string="")

    def CarePlan(self):
        return CarePlanSearchBuilder(search_string="")

    def CareTeam(self):
        return CareTeamSearchBuilder(search_string="")

    def ChargeItem(self):
        return ChargeItemSearchBuilder(search_string="")

    def ChargeItemDefinition(self):
        return ChargeItemDefinitionSearchBuilder(search_string="")

    def Citation(self):
        return CitationSearchBuilder(search_string="")

    def Claim(self):
        return ClaimSearchBuilder(search_string="")

    def ClaimResponse(self):
        return ClaimResponseSearchBuilder(search_string="")

    def ClinicalImpression(self):
        return ClinicalImpressionSearchBuilder(search_string="")

    def ClinicalUseDefinition(self):
        return ClinicalUseDefinitionSearchBuilder(search_string="")

    def CodeSystem(self):
        return CodeSystemSearchBuilder(search_string="")

    def Communication(self):
        return CommunicationSearchBuilder(search_string="")

    def CommunicationRequest(self):
        return CommunicationRequestSearchBuilder(search_string="")

    def CompartmentDefinition(self):
        return CompartmentDefinitionSearchBuilder(search_string="")

    def Composition(self):
        return CompositionSearchBuilder(search_string="")

    def ConceptMap(self):
        return ConceptMapSearchBuilder(search_string="")

    def Condition(self):
        return ConditionSearchBuilder(search_string="")

    def ConditionDefinition(self):
        return ConditionDefinitionSearchBuilder(search_string="")

    def Consent(self):
        return ConsentSearchBuilder(search_string="")

    def Contract(self):
        return ContractSearchBuilder(search_string="")

    def Coverage(self):
        return CoverageSearchBuilder(search_string="")

    def CoverageEligibilityRequest(self):
        return CoverageEligibilityRequestSearchBuilder(search_string="")

    def CoverageEligibilityResponse(self):
        return CoverageEligibilityResponseSearchBuilder(search_string="")

    def DetectedIssue(self):
        return DetectedIssueSearchBuilder(search_string="")

    def Device(self):
        return DeviceSearchBuilder(search_string="")

    def DeviceAssociation(self):
        return DeviceAssociationSearchBuilder(search_string="")

    def DeviceDefinition(self):
        return DeviceDefinitionSearchBuilder(search_string="")

    def DeviceDispense(self):
        return DeviceDispenseSearchBuilder(search_string="")

    def DeviceMetric(self):
        return DeviceMetricSearchBuilder(search_string="")

    def DeviceRequest(self):
        return DeviceRequestSearchBuilder(search_string="")

    def DeviceUsage(self):
        return DeviceUsageSearchBuilder(search_string="")

    def DiagnosticReport(self):
        return DiagnosticReportSearchBuilder(search_string="")

    def DocumentReference(self):
        return DocumentReferenceSearchBuilder(search_string="")

    def Encounter(self):
        return EncounterSearchBuilder(search_string="")

    def EncounterHistory(self):
        return EncounterHistorySearchBuilder(search_string="")

    def Endpoint(self):
        return EndpointSearchBuilder(search_string="")

    def EnrollmentRequest(self):
        return EnrollmentRequestSearchBuilder(search_string="")

    def EnrollmentResponse(self):
        return EnrollmentResponseSearchBuilder(search_string="")

    def EpisodeOfCare(self):
        return EpisodeOfCareSearchBuilder(search_string="")

    def EventDefinition(self):
        return EventDefinitionSearchBuilder(search_string="")

    def Evidence(self):
        return EvidenceSearchBuilder(search_string="")

    def EvidenceReport(self):
        return EvidenceReportSearchBuilder(search_string="")

    def EvidenceVariable(self):
        return EvidenceVariableSearchBuilder(search_string="")

    def ExampleScenario(self):
        return ExampleScenarioSearchBuilder(search_string="")

    def ExplanationOfBenefit(self):
        return ExplanationOfBenefitSearchBuilder(search_string="")

    def FamilyMemberHistory(self):
        return FamilyMemberHistorySearchBuilder(search_string="")

    def Flag(self):
        return FlagSearchBuilder(search_string="")

    def FormularyItem(self):
        return FormularyItemSearchBuilder(search_string="")

    def GenomicStudy(self):
        return GenomicStudySearchBuilder(search_string="")

    def Goal(self):
        return GoalSearchBuilder(search_string="")

    def GraphDefinition(self):
        return GraphDefinitionSearchBuilder(search_string="")

    def Group(self):
        return GroupSearchBuilder(search_string="")

    def GuidanceResponse(self):
        return GuidanceResponseSearchBuilder(search_string="")

    def HealthcareService(self):
        return HealthcareServiceSearchBuilder(search_string="")

    def ImagingSelection(self):
        return ImagingSelectionSearchBuilder(search_string="")

    def ImagingStudy(self):
        return ImagingStudySearchBuilder(search_string="")

    def Immunization(self):
        return ImmunizationSearchBuilder(search_string="")

    def ImmunizationEvaluation(self):
        return ImmunizationEvaluationSearchBuilder(search_string="")

    def ImmunizationRecommendation(self):
        return ImmunizationRecommendationSearchBuilder(search_string="")

    def ImplementationGuide(self):
        return ImplementationGuideSearchBuilder(search_string="")

    def Ingredient(self):
        return IngredientSearchBuilder(search_string="")

    def InsurancePlan(self):
        return InsurancePlanSearchBuilder(search_string="")

    def InventoryItem(self):
        return InventoryItemSearchBuilder(search_string="")

    def InventoryReport(self):
        return InventoryReportSearchBuilder(search_string="")

    def Invoice(self):
        return InvoiceSearchBuilder(search_string="")

    def Library(self):
        return LibrarySearchBuilder(search_string="")

    def Linkage(self):
        return LinkageSearchBuilder(search_string="")

    def List(self):
        return ListSearchBuilder(search_string="")

    def Location(self):
        return LocationSearchBuilder(search_string="")

    def ManufacturedItemDefinition(self):
        return ManufacturedItemDefinitionSearchBuilder(search_string="")

    def Measure(self):
        return MeasureSearchBuilder(search_string="")

    def MeasureReport(self):
        return MeasureReportSearchBuilder(search_string="")

    def Medication(self):
        return MedicationSearchBuilder(search_string="")

    def MedicationAdministration(self):
        return MedicationAdministrationSearchBuilder(search_string="")

    def MedicationDispense(self):
        return MedicationDispenseSearchBuilder(search_string="")

    def MedicationKnowledge(self):
        return MedicationKnowledgeSearchBuilder(search_string="")

    def MedicationRequest(self):
        return MedicationRequestSearchBuilder(search_string="")

    def MedicationStatement(self):
        return MedicationStatementSearchBuilder(search_string="")

    def MedicinalProductDefinition(self):
        return MedicinalProductDefinitionSearchBuilder(search_string="")

    def MessageDefinition(self):
        return MessageDefinitionSearchBuilder(search_string="")

    def MessageHeader(self):
        return MessageHeaderSearchBuilder(search_string="")

    def MolecularSequence(self):
        return MolecularSequenceSearchBuilder(search_string="")

    def NamingSystem(self):
        return NamingSystemSearchBuilder(search_string="")

    def NutritionIntake(self):
        return NutritionIntakeSearchBuilder(search_string="")

    def NutritionOrder(self):
        return NutritionOrderSearchBuilder(search_string="")

    def NutritionProduct(self):
        return NutritionProductSearchBuilder(search_string="")

    def Observation(self):
        return ObservationSearchBuilder(search_string="")

    def ObservationDefinition(self):
        return ObservationDefinitionSearchBuilder(search_string="")

    def OperationDefinition(self):
        return OperationDefinitionSearchBuilder(search_string="")

    def OperationOutcome(self):
        return OperationOutcomeSearchBuilder(search_string="")

    def Organization(self):
        return OrganizationSearchBuilder(search_string="")

    def OrganizationAffiliation(self):
        return OrganizationAffiliationSearchBuilder(search_string="")

    def PackagedProductDefinition(self):
        return PackagedProductDefinitionSearchBuilder(search_string="")

    def Patient(self):
        return PatientSearchBuilder(search_string="")

    def PaymentNotice(self):
        return PaymentNoticeSearchBuilder(search_string="")

    def PaymentReconciliation(self):
        return PaymentReconciliationSearchBuilder(search_string="")

    def Permission(self):
        return PermissionSearchBuilder(search_string="")

    def Person(self):
        return PersonSearchBuilder(search_string="")

    def PlanDefinition(self):
        return PlanDefinitionSearchBuilder(search_string="")

    def Practitioner(self):
        return PractitionerSearchBuilder(search_string="")

    def PractitionerRole(self):
        return PractitionerRoleSearchBuilder(search_string="")

    def Procedure(self):
        return ProcedureSearchBuilder(search_string="")

    def Provenance(self):
        return ProvenanceSearchBuilder(search_string="")

    def Questionnaire(self):
        return QuestionnaireSearchBuilder(search_string="")

    def QuestionnaireResponse(self):
        return QuestionnaireResponseSearchBuilder(search_string="")

    def RegulatedAuthorization(self):
        return RegulatedAuthorizationSearchBuilder(search_string="")

    def RelatedPerson(self):
        return RelatedPersonSearchBuilder(search_string="")

    def RequestOrchestration(self):
        return RequestOrchestrationSearchBuilder(search_string="")

    def Requirements(self):
        return RequirementsSearchBuilder(search_string="")

    def ResearchStudy(self):
        return ResearchStudySearchBuilder(search_string="")

    def ResearchSubject(self):
        return ResearchSubjectSearchBuilder(search_string="")

    def RiskAssessment(self):
        return RiskAssessmentSearchBuilder(search_string="")

    def Schedule(self):
        return ScheduleSearchBuilder(search_string="")

    def SearchParameter(self):
        return SearchParameterSearchBuilder(search_string="")

    def ServiceRequest(self):
        return ServiceRequestSearchBuilder(search_string="")

    def Slot(self):
        return SlotSearchBuilder(search_string="")

    def Specimen(self):
        return SpecimenSearchBuilder(search_string="")

    def SpecimenDefinition(self):
        return SpecimenDefinitionSearchBuilder(search_string="")

    def StructureDefinition(self):
        return StructureDefinitionSearchBuilder(search_string="")

    def StructureMap(self):
        return StructureMapSearchBuilder(search_string="")

    def Subscription(self):
        return SubscriptionSearchBuilder(search_string="")

    def SubscriptionStatus(self):
        return SubscriptionStatusSearchBuilder(search_string="")

    def SubscriptionTopic(self):
        return SubscriptionTopicSearchBuilder(search_string="")

    def Substance(self):
        return SubstanceSearchBuilder(search_string="")

    def SubstanceDefinition(self):
        return SubstanceDefinitionSearchBuilder(search_string="")

    def SubstanceNucleicAcid(self):
        return SubstanceNucleicAcidSearchBuilder(search_string="")

    def SubstancePolymer(self):
        return SubstancePolymerSearchBuilder(search_string="")

    def SubstanceProtein(self):
        return SubstanceProteinSearchBuilder(search_string="")

    def SubstanceReferenceInformation(self):
        return SubstanceReferenceInformationSearchBuilder(search_string="")

    def SubstanceSourceMaterial(self):
        return SubstanceSourceMaterialSearchBuilder(search_string="")

    def SupplyDelivery(self):
        return SupplyDeliverySearchBuilder(search_string="")

    def SupplyRequest(self):
        return SupplyRequestSearchBuilder(search_string="")

    def Task(self):
        return TaskSearchBuilder(search_string="")

    def TerminologyCapabilities(self):
        return TerminologyCapabilitiesSearchBuilder(search_string="")

    def TestPlan(self):
        return TestPlanSearchBuilder(search_string="")

    def TestReport(self):
        return TestReportSearchBuilder(search_string="")

    def TestScript(self):
        return TestScriptSearchBuilder(search_string="")

    def Transport(self):
        return TransportSearchBuilder(search_string="")

    def ValueSet(self):
        return ValueSetSearchBuilder(search_string="")

    def VerificationResult(self):
        return VerificationResultSearchBuilder(search_string="")

    def VisionPrescription(self):
        return VisionPrescriptionSearchBuilder(search_string="")
