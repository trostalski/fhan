# generated at 2023-09-27 15:10:10.189949 from /Users/tillrostalski/Git/fhan/src/fhan/client/scripts/create_from_template.py

from fhan.models.R4.Account import Account

from fhan.models.R4.ActivityDefinition import ActivityDefinition

from fhan.models.R4.AdverseEvent import AdverseEvent

from fhan.models.R4.AllergyIntolerance import AllergyIntolerance

from fhan.models.R4.Appointment import Appointment

from fhan.models.R4.AppointmentResponse import AppointmentResponse

from fhan.models.R4.AuditEvent import AuditEvent

from fhan.models.R4.Basic import Basic

from fhan.models.R4.Binary import Binary

from fhan.models.R4.BiologicallyDerivedProduct import BiologicallyDerivedProduct

from fhan.models.R4.BodyStructure import BodyStructure

from fhan.models.R4.Bundle import Bundle

from fhan.models.R4.CapabilityStatement import CapabilityStatement

from fhan.models.R4.CarePlan import CarePlan

from fhan.models.R4.CareTeam import CareTeam

from fhan.models.R4.CatalogEntry import CatalogEntry

from fhan.models.R4.ChargeItem import ChargeItem

from fhan.models.R4.ChargeItemDefinition import ChargeItemDefinition

from fhan.models.R4.Claim import Claim

from fhan.models.R4.ClaimResponse import ClaimResponse

from fhan.models.R4.ClinicalImpression import ClinicalImpression

from fhan.models.R4.CodeSystem import CodeSystem

from fhan.models.R4.Communication import Communication

from fhan.models.R4.CommunicationRequest import CommunicationRequest

from fhan.models.R4.CompartmentDefinition import CompartmentDefinition

from fhan.models.R4.Composition import Composition

from fhan.models.R4.ConceptMap import ConceptMap

from fhan.models.R4.Condition import Condition

from fhan.models.R4.Consent import Consent

from fhan.models.R4.Contract import Contract

from fhan.models.R4.Coverage import Coverage

from fhan.models.R4.CoverageEligibilityRequest import CoverageEligibilityRequest

from fhan.models.R4.CoverageEligibilityResponse import CoverageEligibilityResponse

from fhan.models.R4.DetectedIssue import DetectedIssue

from fhan.models.R4.Device import Device

from fhan.models.R4.DeviceDefinition import DeviceDefinition

from fhan.models.R4.DeviceMetric import DeviceMetric

from fhan.models.R4.DeviceRequest import DeviceRequest

from fhan.models.R4.DeviceUseStatement import DeviceUseStatement

from fhan.models.R4.DiagnosticReport import DiagnosticReport

from fhan.models.R4.DocumentManifest import DocumentManifest

from fhan.models.R4.DocumentReference import DocumentReference

from fhan.models.R4.EffectEvidenceSynthesis import EffectEvidenceSynthesis

from fhan.models.R4.Encounter import Encounter

from fhan.models.R4.Endpoint import Endpoint

from fhan.models.R4.EnrollmentRequest import EnrollmentRequest

from fhan.models.R4.EnrollmentResponse import EnrollmentResponse

from fhan.models.R4.EpisodeOfCare import EpisodeOfCare

from fhan.models.R4.EventDefinition import EventDefinition

from fhan.models.R4.Evidence import Evidence

from fhan.models.R4.EvidenceVariable import EvidenceVariable

from fhan.models.R4.ExampleScenario import ExampleScenario

from fhan.models.R4.ExplanationOfBenefit import ExplanationOfBenefit

from fhan.models.R4.FamilyMemberHistory import FamilyMemberHistory

from fhan.models.R4.Flag import Flag

from fhan.models.R4.Goal import Goal

from fhan.models.R4.GraphDefinition import GraphDefinition

from fhan.models.R4.Group import Group

from fhan.models.R4.GuidanceResponse import GuidanceResponse

from fhan.models.R4.HealthcareService import HealthcareService

from fhan.models.R4.ImagingStudy import ImagingStudy

from fhan.models.R4.Immunization import Immunization

from fhan.models.R4.ImmunizationEvaluation import ImmunizationEvaluation

from fhan.models.R4.ImmunizationRecommendation import ImmunizationRecommendation

from fhan.models.R4.ImplementationGuide import ImplementationGuide

from fhan.models.R4.InsurancePlan import InsurancePlan

from fhan.models.R4.Invoice import Invoice

from fhan.models.R4.Library import Library

from fhan.models.R4.Linkage import Linkage

from fhan.models.R4.List import List

from fhan.models.R4.Location import Location

from fhan.models.R4.Measure import Measure

from fhan.models.R4.MeasureReport import MeasureReport

from fhan.models.R4.Media import Media

from fhan.models.R4.Medication import Medication

from fhan.models.R4.MedicationAdministration import MedicationAdministration

from fhan.models.R4.MedicationDispense import MedicationDispense

from fhan.models.R4.MedicationKnowledge import MedicationKnowledge

from fhan.models.R4.MedicationRequest import MedicationRequest

from fhan.models.R4.MedicationStatement import MedicationStatement

from fhan.models.R4.MedicinalProduct import MedicinalProduct

from fhan.models.R4.MedicinalProductAuthorization import MedicinalProductAuthorization

from fhan.models.R4.MedicinalProductContraindication import (
    MedicinalProductContraindication,
)

from fhan.models.R4.MedicinalProductIndication import MedicinalProductIndication

from fhan.models.R4.MedicinalProductIngredient import MedicinalProductIngredient

from fhan.models.R4.MedicinalProductInteraction import MedicinalProductInteraction

from fhan.models.R4.MedicinalProductManufactured import MedicinalProductManufactured

from fhan.models.R4.MedicinalProductPackaged import MedicinalProductPackaged

from fhan.models.R4.MedicinalProductPharmaceutical import MedicinalProductPharmaceutical

from fhan.models.R4.MedicinalProductUndesirableEffect import (
    MedicinalProductUndesirableEffect,
)

from fhan.models.R4.MessageDefinition import MessageDefinition

from fhan.models.R4.MessageHeader import MessageHeader

from fhan.models.R4.MolecularSequence import MolecularSequence

from fhan.models.R4.NamingSystem import NamingSystem

from fhan.models.R4.NutritionOrder import NutritionOrder

from fhan.models.R4.Observation import Observation

from fhan.models.R4.ObservationDefinition import ObservationDefinition

from fhan.models.R4.OperationDefinition import OperationDefinition

from fhan.models.R4.OperationOutcome import OperationOutcome

from fhan.models.R4.Organization import Organization

from fhan.models.R4.OrganizationAffiliation import OrganizationAffiliation

from fhan.models.R4.Patient import Patient

from fhan.models.R4.PaymentNotice import PaymentNotice

from fhan.models.R4.PaymentReconciliation import PaymentReconciliation

from fhan.models.R4.Person import Person

from fhan.models.R4.PlanDefinition import PlanDefinition

from fhan.models.R4.Practitioner import Practitioner

from fhan.models.R4.PractitionerRole import PractitionerRole

from fhan.models.R4.Procedure import Procedure

from fhan.models.R4.Provenance import Provenance

from fhan.models.R4.Questionnaire import Questionnaire

from fhan.models.R4.QuestionnaireResponse import QuestionnaireResponse

from fhan.models.R4.RelatedPerson import RelatedPerson

from fhan.models.R4.RequestGroup import RequestGroup

from fhan.models.R4.ResearchDefinition import ResearchDefinition

from fhan.models.R4.ResearchElementDefinition import ResearchElementDefinition

from fhan.models.R4.ResearchStudy import ResearchStudy

from fhan.models.R4.ResearchSubject import ResearchSubject

from fhan.models.R4.RiskAssessment import RiskAssessment

from fhan.models.R4.RiskEvidenceSynthesis import RiskEvidenceSynthesis

from fhan.models.R4.Schedule import Schedule

from fhan.models.R4.SearchParameter import SearchParameter

from fhan.models.R4.ServiceRequest import ServiceRequest

from fhan.models.R4.Slot import Slot

from fhan.models.R4.Specimen import Specimen

from fhan.models.R4.SpecimenDefinition import SpecimenDefinition

from fhan.models.R4.StructureDefinition import StructureDefinition

from fhan.models.R4.StructureMap import StructureMap

from fhan.models.R4.Subscription import Subscription

from fhan.models.R4.Substance import Substance

from fhan.models.R4.SubstanceNucleicAcid import SubstanceNucleicAcid

from fhan.models.R4.SubstancePolymer import SubstancePolymer

from fhan.models.R4.SubstanceProtein import SubstanceProtein

from fhan.models.R4.SubstanceReferenceInformation import SubstanceReferenceInformation

from fhan.models.R4.SubstanceSourceMaterial import SubstanceSourceMaterial

from fhan.models.R4.SubstanceSpecification import SubstanceSpecification

from fhan.models.R4.SupplyDelivery import SupplyDelivery

from fhan.models.R4.SupplyRequest import SupplyRequest

from fhan.models.R4.Task import Task

from fhan.models.R4.TerminologyCapabilities import TerminologyCapabilities

from fhan.models.R4.TestReport import TestReport

from fhan.models.R4.TestScript import TestScript

from fhan.models.R4.ValueSet import ValueSet

from fhan.models.R4.VerificationResult import VerificationResult

from fhan.models.R4.VisionPrescription import VisionPrescription


class GetResourceMixin:
    """This mixin class provides the GetHandler with methods for each
    resource type. The methods are syntactic sugar for the _get method.
    """

    def __init__(self):
        pass

    def Account(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Account:
        return self._get("Account", id, as_object)

    def ActivityDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ActivityDefinition:
        return self._get("ActivityDefinition", id, as_object)

    def AdverseEvent(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | AdverseEvent:
        return self._get("AdverseEvent", id, as_object)

    def AllergyIntolerance(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | AllergyIntolerance:
        return self._get("AllergyIntolerance", id, as_object)

    def Appointment(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Appointment:
        return self._get("Appointment", id, as_object)

    def AppointmentResponse(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | AppointmentResponse:
        return self._get("AppointmentResponse", id, as_object)

    def AuditEvent(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | AuditEvent:
        return self._get("AuditEvent", id, as_object)

    def Basic(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Basic:
        return self._get("Basic", id, as_object)

    def Binary(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Binary:
        return self._get("Binary", id, as_object)

    def BiologicallyDerivedProduct(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | BiologicallyDerivedProduct:
        return self._get("BiologicallyDerivedProduct", id, as_object)

    def BodyStructure(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | BodyStructure:
        return self._get("BodyStructure", id, as_object)

    def Bundle(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Bundle:
        return self._get("Bundle", id, as_object)

    def CapabilityStatement(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CapabilityStatement:
        return self._get("CapabilityStatement", id, as_object)

    def CarePlan(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CarePlan:
        return self._get("CarePlan", id, as_object)

    def CareTeam(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CareTeam:
        return self._get("CareTeam", id, as_object)

    def CatalogEntry(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CatalogEntry:
        return self._get("CatalogEntry", id, as_object)

    def ChargeItem(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ChargeItem:
        return self._get("ChargeItem", id, as_object)

    def ChargeItemDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ChargeItemDefinition:
        return self._get("ChargeItemDefinition", id, as_object)

    def Claim(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Claim:
        return self._get("Claim", id, as_object)

    def ClaimResponse(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ClaimResponse:
        return self._get("ClaimResponse", id, as_object)

    def ClinicalImpression(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ClinicalImpression:
        return self._get("ClinicalImpression", id, as_object)

    def CodeSystem(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CodeSystem:
        return self._get("CodeSystem", id, as_object)

    def Communication(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Communication:
        return self._get("Communication", id, as_object)

    def CommunicationRequest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CommunicationRequest:
        return self._get("CommunicationRequest", id, as_object)

    def CompartmentDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CompartmentDefinition:
        return self._get("CompartmentDefinition", id, as_object)

    def Composition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Composition:
        return self._get("Composition", id, as_object)

    def ConceptMap(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ConceptMap:
        return self._get("ConceptMap", id, as_object)

    def Condition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Condition:
        return self._get("Condition", id, as_object)

    def Consent(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Consent:
        return self._get("Consent", id, as_object)

    def Contract(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Contract:
        return self._get("Contract", id, as_object)

    def Coverage(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Coverage:
        return self._get("Coverage", id, as_object)

    def CoverageEligibilityRequest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CoverageEligibilityRequest:
        return self._get("CoverageEligibilityRequest", id, as_object)

    def CoverageEligibilityResponse(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | CoverageEligibilityResponse:
        return self._get("CoverageEligibilityResponse", id, as_object)

    def DetectedIssue(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DetectedIssue:
        return self._get("DetectedIssue", id, as_object)

    def Device(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Device:
        return self._get("Device", id, as_object)

    def DeviceDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DeviceDefinition:
        return self._get("DeviceDefinition", id, as_object)

    def DeviceMetric(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DeviceMetric:
        return self._get("DeviceMetric", id, as_object)

    def DeviceRequest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DeviceRequest:
        return self._get("DeviceRequest", id, as_object)

    def DeviceUseStatement(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DeviceUseStatement:
        return self._get("DeviceUseStatement", id, as_object)

    def DiagnosticReport(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DiagnosticReport:
        return self._get("DiagnosticReport", id, as_object)

    def DocumentManifest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DocumentManifest:
        return self._get("DocumentManifest", id, as_object)

    def DocumentReference(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | DocumentReference:
        return self._get("DocumentReference", id, as_object)

    def EffectEvidenceSynthesis(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | EffectEvidenceSynthesis:
        return self._get("EffectEvidenceSynthesis", id, as_object)

    def Encounter(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Encounter:
        return self._get("Encounter", id, as_object)

    def Endpoint(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Endpoint:
        return self._get("Endpoint", id, as_object)

    def EnrollmentRequest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | EnrollmentRequest:
        return self._get("EnrollmentRequest", id, as_object)

    def EnrollmentResponse(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | EnrollmentResponse:
        return self._get("EnrollmentResponse", id, as_object)

    def EpisodeOfCare(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | EpisodeOfCare:
        return self._get("EpisodeOfCare", id, as_object)

    def EventDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | EventDefinition:
        return self._get("EventDefinition", id, as_object)

    def Evidence(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Evidence:
        return self._get("Evidence", id, as_object)

    def EvidenceVariable(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | EvidenceVariable:
        return self._get("EvidenceVariable", id, as_object)

    def ExampleScenario(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ExampleScenario:
        return self._get("ExampleScenario", id, as_object)

    def ExplanationOfBenefit(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ExplanationOfBenefit:
        return self._get("ExplanationOfBenefit", id, as_object)

    def FamilyMemberHistory(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | FamilyMemberHistory:
        return self._get("FamilyMemberHistory", id, as_object)

    def Flag(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Flag:
        return self._get("Flag", id, as_object)

    def Goal(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Goal:
        return self._get("Goal", id, as_object)

    def GraphDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | GraphDefinition:
        return self._get("GraphDefinition", id, as_object)

    def Group(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Group:
        return self._get("Group", id, as_object)

    def GuidanceResponse(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | GuidanceResponse:
        return self._get("GuidanceResponse", id, as_object)

    def HealthcareService(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | HealthcareService:
        return self._get("HealthcareService", id, as_object)

    def ImagingStudy(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ImagingStudy:
        return self._get("ImagingStudy", id, as_object)

    def Immunization(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Immunization:
        return self._get("Immunization", id, as_object)

    def ImmunizationEvaluation(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ImmunizationEvaluation:
        return self._get("ImmunizationEvaluation", id, as_object)

    def ImmunizationRecommendation(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ImmunizationRecommendation:
        return self._get("ImmunizationRecommendation", id, as_object)

    def ImplementationGuide(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ImplementationGuide:
        return self._get("ImplementationGuide", id, as_object)

    def InsurancePlan(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | InsurancePlan:
        return self._get("InsurancePlan", id, as_object)

    def Invoice(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Invoice:
        return self._get("Invoice", id, as_object)

    def Library(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Library:
        return self._get("Library", id, as_object)

    def Linkage(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Linkage:
        return self._get("Linkage", id, as_object)

    def List(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | List:
        return self._get("List", id, as_object)

    def Location(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Location:
        return self._get("Location", id, as_object)

    def Measure(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Measure:
        return self._get("Measure", id, as_object)

    def MeasureReport(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MeasureReport:
        return self._get("MeasureReport", id, as_object)

    def Media(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Media:
        return self._get("Media", id, as_object)

    def Medication(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Medication:
        return self._get("Medication", id, as_object)

    def MedicationAdministration(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicationAdministration:
        return self._get("MedicationAdministration", id, as_object)

    def MedicationDispense(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicationDispense:
        return self._get("MedicationDispense", id, as_object)

    def MedicationKnowledge(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicationKnowledge:
        return self._get("MedicationKnowledge", id, as_object)

    def MedicationRequest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicationRequest:
        return self._get("MedicationRequest", id, as_object)

    def MedicationStatement(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicationStatement:
        return self._get("MedicationStatement", id, as_object)

    def MedicinalProduct(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProduct:
        return self._get("MedicinalProduct", id, as_object)

    def MedicinalProductAuthorization(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductAuthorization:
        return self._get("MedicinalProductAuthorization", id, as_object)

    def MedicinalProductContraindication(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductContraindication:
        return self._get("MedicinalProductContraindication", id, as_object)

    def MedicinalProductIndication(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductIndication:
        return self._get("MedicinalProductIndication", id, as_object)

    def MedicinalProductIngredient(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductIngredient:
        return self._get("MedicinalProductIngredient", id, as_object)

    def MedicinalProductInteraction(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductInteraction:
        return self._get("MedicinalProductInteraction", id, as_object)

    def MedicinalProductManufactured(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductManufactured:
        return self._get("MedicinalProductManufactured", id, as_object)

    def MedicinalProductPackaged(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductPackaged:
        return self._get("MedicinalProductPackaged", id, as_object)

    def MedicinalProductPharmaceutical(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductPharmaceutical:
        return self._get("MedicinalProductPharmaceutical", id, as_object)

    def MedicinalProductUndesirableEffect(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MedicinalProductUndesirableEffect:
        return self._get("MedicinalProductUndesirableEffect", id, as_object)

    def MessageDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MessageDefinition:
        return self._get("MessageDefinition", id, as_object)

    def MessageHeader(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MessageHeader:
        return self._get("MessageHeader", id, as_object)

    def MolecularSequence(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | MolecularSequence:
        return self._get("MolecularSequence", id, as_object)

    def NamingSystem(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | NamingSystem:
        return self._get("NamingSystem", id, as_object)

    def NutritionOrder(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | NutritionOrder:
        return self._get("NutritionOrder", id, as_object)

    def Observation(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Observation:
        return self._get("Observation", id, as_object)

    def ObservationDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ObservationDefinition:
        return self._get("ObservationDefinition", id, as_object)

    def OperationDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | OperationDefinition:
        return self._get("OperationDefinition", id, as_object)

    def OperationOutcome(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | OperationOutcome:
        return self._get("OperationOutcome", id, as_object)

    def Organization(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Organization:
        return self._get("Organization", id, as_object)

    def OrganizationAffiliation(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | OrganizationAffiliation:
        return self._get("OrganizationAffiliation", id, as_object)

    def Patient(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Patient:
        return self._get("Patient", id, as_object)

    def PaymentNotice(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | PaymentNotice:
        return self._get("PaymentNotice", id, as_object)

    def PaymentReconciliation(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | PaymentReconciliation:
        return self._get("PaymentReconciliation", id, as_object)

    def Person(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Person:
        return self._get("Person", id, as_object)

    def PlanDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | PlanDefinition:
        return self._get("PlanDefinition", id, as_object)

    def Practitioner(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Practitioner:
        return self._get("Practitioner", id, as_object)

    def PractitionerRole(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | PractitionerRole:
        return self._get("PractitionerRole", id, as_object)

    def Procedure(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Procedure:
        return self._get("Procedure", id, as_object)

    def Provenance(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Provenance:
        return self._get("Provenance", id, as_object)

    def Questionnaire(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Questionnaire:
        return self._get("Questionnaire", id, as_object)

    def QuestionnaireResponse(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | QuestionnaireResponse:
        return self._get("QuestionnaireResponse", id, as_object)

    def RelatedPerson(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | RelatedPerson:
        return self._get("RelatedPerson", id, as_object)

    def RequestGroup(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | RequestGroup:
        return self._get("RequestGroup", id, as_object)

    def ResearchDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ResearchDefinition:
        return self._get("ResearchDefinition", id, as_object)

    def ResearchElementDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ResearchElementDefinition:
        return self._get("ResearchElementDefinition", id, as_object)

    def ResearchStudy(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ResearchStudy:
        return self._get("ResearchStudy", id, as_object)

    def ResearchSubject(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ResearchSubject:
        return self._get("ResearchSubject", id, as_object)

    def RiskAssessment(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | RiskAssessment:
        return self._get("RiskAssessment", id, as_object)

    def RiskEvidenceSynthesis(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | RiskEvidenceSynthesis:
        return self._get("RiskEvidenceSynthesis", id, as_object)

    def Schedule(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Schedule:
        return self._get("Schedule", id, as_object)

    def SearchParameter(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SearchParameter:
        return self._get("SearchParameter", id, as_object)

    def ServiceRequest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ServiceRequest:
        return self._get("ServiceRequest", id, as_object)

    def Slot(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Slot:
        return self._get("Slot", id, as_object)

    def Specimen(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Specimen:
        return self._get("Specimen", id, as_object)

    def SpecimenDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SpecimenDefinition:
        return self._get("SpecimenDefinition", id, as_object)

    def StructureDefinition(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | StructureDefinition:
        return self._get("StructureDefinition", id, as_object)

    def StructureMap(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | StructureMap:
        return self._get("StructureMap", id, as_object)

    def Subscription(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Subscription:
        return self._get("Subscription", id, as_object)

    def Substance(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Substance:
        return self._get("Substance", id, as_object)

    def SubstanceNucleicAcid(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SubstanceNucleicAcid:
        return self._get("SubstanceNucleicAcid", id, as_object)

    def SubstancePolymer(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SubstancePolymer:
        return self._get("SubstancePolymer", id, as_object)

    def SubstanceProtein(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SubstanceProtein:
        return self._get("SubstanceProtein", id, as_object)

    def SubstanceReferenceInformation(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SubstanceReferenceInformation:
        return self._get("SubstanceReferenceInformation", id, as_object)

    def SubstanceSourceMaterial(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SubstanceSourceMaterial:
        return self._get("SubstanceSourceMaterial", id, as_object)

    def SubstanceSpecification(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SubstanceSpecification:
        return self._get("SubstanceSpecification", id, as_object)

    def SupplyDelivery(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SupplyDelivery:
        return self._get("SupplyDelivery", id, as_object)

    def SupplyRequest(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | SupplyRequest:
        return self._get("SupplyRequest", id, as_object)

    def Task(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | Task:
        return self._get("Task", id, as_object)

    def TerminologyCapabilities(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | TerminologyCapabilities:
        return self._get("TerminologyCapabilities", id, as_object)

    def TestReport(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | TestReport:
        return self._get("TestReport", id, as_object)

    def TestScript(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | TestScript:
        return self._get("TestScript", id, as_object)

    def ValueSet(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | ValueSet:
        return self._get("ValueSet", id, as_object)

    def VerificationResult(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | VerificationResult:
        return self._get("VerificationResult", id, as_object)

    def VisionPrescription(
        self,
        id: str,
        as_object: bool = False,
    ) -> dict | VisionPrescription:
        return self._get("VisionPrescription", id, as_object)
