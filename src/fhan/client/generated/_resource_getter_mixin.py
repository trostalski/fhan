# generated at 2023-09-26 17:25:20.691662 from /Users/tillrostalski/Git/fhan/src/fhan/client/scripts/create_from_template.py
class ResourceGetterMixin:
    """This mixin class provides the GetHandler with getter methods for each
    resource type. The methods are syntactic sugar for the _get method.
    """
    def __init__(self):
        pass

    def Account(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Account", id, search)

    def ActivityDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ActivityDefinition", id, search)

    def ActorDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ActorDefinition", id, search)

    def AdministrableProductDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("AdministrableProductDefinition", id, search)

    def AdverseEvent(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("AdverseEvent", id, search)

    def AllergyIntolerance(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("AllergyIntolerance", id, search)

    def Appointment(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Appointment", id, search)

    def AppointmentResponse(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("AppointmentResponse", id, search)

    def ArtifactAssessment(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ArtifactAssessment", id, search)

    def AuditEvent(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("AuditEvent", id, search)

    def Basic(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Basic", id, search)

    def Binary(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Binary", id, search)

    def BiologicallyDerivedProduct(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("BiologicallyDerivedProduct", id, search)

    def BiologicallyDerivedProductDispense(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("BiologicallyDerivedProductDispense", id, search)

    def BodyStructure(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("BodyStructure", id, search)

    def Bundle(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Bundle", id, search)

    def CanonicalResource(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CanonicalResource", id, search)

    def CapabilityStatement(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CapabilityStatement", id, search)

    def CarePlan(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CarePlan", id, search)

    def CareTeam(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CareTeam", id, search)

    def ChargeItem(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ChargeItem", id, search)

    def ChargeItemDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ChargeItemDefinition", id, search)

    def Citation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Citation", id, search)

    def Claim(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Claim", id, search)

    def ClaimResponse(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ClaimResponse", id, search)

    def ClinicalImpression(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ClinicalImpression", id, search)

    def ClinicalUseDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ClinicalUseDefinition", id, search)

    def CodeSystem(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CodeSystem", id, search)

    def Communication(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Communication", id, search)

    def CommunicationRequest(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CommunicationRequest", id, search)

    def CompartmentDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CompartmentDefinition", id, search)

    def Composition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Composition", id, search)

    def ConceptMap(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ConceptMap", id, search)

    def Condition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Condition", id, search)

    def ConditionDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ConditionDefinition", id, search)

    def Consent(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Consent", id, search)

    def Contract(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Contract", id, search)

    def Coverage(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Coverage", id, search)

    def CoverageEligibilityRequest(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CoverageEligibilityRequest", id, search)

    def CoverageEligibilityResponse(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("CoverageEligibilityResponse", id, search)

    def DetectedIssue(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DetectedIssue", id, search)

    def Device(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Device", id, search)

    def DeviceAssociation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DeviceAssociation", id, search)

    def DeviceDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DeviceDefinition", id, search)

    def DeviceDispense(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DeviceDispense", id, search)

    def DeviceMetric(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DeviceMetric", id, search)

    def DeviceRequest(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DeviceRequest", id, search)

    def DeviceUsage(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DeviceUsage", id, search)

    def DiagnosticReport(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DiagnosticReport", id, search)

    def DocumentReference(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DocumentReference", id, search)

    def DomainResource(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("DomainResource", id, search)

    def Encounter(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Encounter", id, search)

    def EncounterHistory(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("EncounterHistory", id, search)

    def Endpoint(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Endpoint", id, search)

    def EnrollmentRequest(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("EnrollmentRequest", id, search)

    def EnrollmentResponse(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("EnrollmentResponse", id, search)

    def EpisodeOfCare(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("EpisodeOfCare", id, search)

    def EventDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("EventDefinition", id, search)

    def Evidence(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Evidence", id, search)

    def EvidenceReport(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("EvidenceReport", id, search)

    def EvidenceVariable(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("EvidenceVariable", id, search)

    def ExampleScenario(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ExampleScenario", id, search)

    def ExplanationOfBenefit(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ExplanationOfBenefit", id, search)

    def FamilyMemberHistory(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("FamilyMemberHistory", id, search)

    def Flag(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Flag", id, search)

    def FormularyItem(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("FormularyItem", id, search)

    def GenomicStudy(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("GenomicStudy", id, search)

    def Goal(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Goal", id, search)

    def GraphDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("GraphDefinition", id, search)

    def Group(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Group", id, search)

    def GuidanceResponse(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("GuidanceResponse", id, search)

    def HealthcareService(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("HealthcareService", id, search)

    def ImagingSelection(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ImagingSelection", id, search)

    def ImagingStudy(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ImagingStudy", id, search)

    def Immunization(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Immunization", id, search)

    def ImmunizationEvaluation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ImmunizationEvaluation", id, search)

    def ImmunizationRecommendation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ImmunizationRecommendation", id, search)

    def ImplementationGuide(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ImplementationGuide", id, search)

    def Ingredient(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Ingredient", id, search)

    def InsurancePlan(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("InsurancePlan", id, search)

    def InventoryItem(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("InventoryItem", id, search)

    def InventoryReport(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("InventoryReport", id, search)

    def Invoice(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Invoice", id, search)

    def Library(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Library", id, search)

    def Linkage(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Linkage", id, search)

    def List(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("List", id, search)

    def Location(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Location", id, search)

    def ManufacturedItemDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ManufacturedItemDefinition", id, search)

    def Measure(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Measure", id, search)

    def MeasureReport(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MeasureReport", id, search)

    def Medication(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Medication", id, search)

    def MedicationAdministration(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MedicationAdministration", id, search)

    def MedicationDispense(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MedicationDispense", id, search)

    def MedicationKnowledge(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MedicationKnowledge", id, search)

    def MedicationRequest(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MedicationRequest", id, search)

    def MedicationStatement(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MedicationStatement", id, search)

    def MedicinalProductDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MedicinalProductDefinition", id, search)

    def MessageDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MessageDefinition", id, search)

    def MessageHeader(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MessageHeader", id, search)

    def MetadataResource(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MetadataResource", id, search)

    def MolecularSequence(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("MolecularSequence", id, search)

    def NamingSystem(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("NamingSystem", id, search)

    def NutritionIntake(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("NutritionIntake", id, search)

    def NutritionOrder(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("NutritionOrder", id, search)

    def NutritionProduct(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("NutritionProduct", id, search)

    def Observation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Observation", id, search)

    def ObservationDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ObservationDefinition", id, search)

    def OperationDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("OperationDefinition", id, search)

    def OperationOutcome(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("OperationOutcome", id, search)

    def Organization(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Organization", id, search)

    def OrganizationAffiliation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("OrganizationAffiliation", id, search)

    def PackagedProductDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("PackagedProductDefinition", id, search)

    def Parameters(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Parameters", id, search)

    def Patient(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Patient", id, search)

    def PaymentNotice(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("PaymentNotice", id, search)

    def PaymentReconciliation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("PaymentReconciliation", id, search)

    def Permission(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Permission", id, search)

    def Person(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Person", id, search)

    def PlanDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("PlanDefinition", id, search)

    def Practitioner(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Practitioner", id, search)

    def PractitionerRole(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("PractitionerRole", id, search)

    def Procedure(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Procedure", id, search)

    def Provenance(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Provenance", id, search)

    def Questionnaire(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Questionnaire", id, search)

    def QuestionnaireResponse(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("QuestionnaireResponse", id, search)

    def RegulatedAuthorization(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("RegulatedAuthorization", id, search)

    def RelatedPerson(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("RelatedPerson", id, search)

    def RequestOrchestration(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("RequestOrchestration", id, search)

    def Requirements(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Requirements", id, search)

    def ResearchStudy(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ResearchStudy", id, search)

    def ResearchSubject(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ResearchSubject", id, search)

    def Resource(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Resource", id, search)

    def RiskAssessment(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("RiskAssessment", id, search)

    def Schedule(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Schedule", id, search)

    def SearchParameter(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SearchParameter", id, search)

    def ServiceRequest(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ServiceRequest", id, search)

    def Slot(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Slot", id, search)

    def Specimen(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Specimen", id, search)

    def SpecimenDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SpecimenDefinition", id, search)

    def StructureDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("StructureDefinition", id, search)

    def StructureMap(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("StructureMap", id, search)

    def Subscription(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Subscription", id, search)

    def SubscriptionStatus(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubscriptionStatus", id, search)

    def SubscriptionTopic(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubscriptionTopic", id, search)

    def Substance(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Substance", id, search)

    def SubstanceDefinition(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubstanceDefinition", id, search)

    def SubstanceNucleicAcid(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubstanceNucleicAcid", id, search)

    def SubstancePolymer(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubstancePolymer", id, search)

    def SubstanceProtein(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubstanceProtein", id, search)

    def SubstanceReferenceInformation(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubstanceReferenceInformation", id, search)

    def SubstanceSourceMaterial(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SubstanceSourceMaterial", id, search)

    def SupplyDelivery(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SupplyDelivery", id, search)

    def SupplyRequest(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("SupplyRequest", id, search)

    def Task(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Task", id, search)

    def TerminologyCapabilities(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("TerminologyCapabilities", id, search)

    def TestPlan(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("TestPlan", id, search)

    def TestReport(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("TestReport", id, search)

    def TestScript(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("TestScript", id, search)

    def Transport(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("Transport", id, search)

    def ValueSet(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("ValueSet", id, search)

    def VerificationResult(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("VerificationResult", id, search)

    def VisionPrescription(
        self,
        id: str | list[str] | None = None,
        search: str | None = None,
    ):
        return self._get("VisionPrescription", id, search)
