"""
Generated class for PaymentReconciliation. 
Time: 2023-09-25 14:53:18
"""
from fhan.models.R4.Reference import *
from fhan.models.R4.Resource import *
from fhan.models.R4.Period import *
from fhan.models.R4.Extension import *
from fhan.models.R4.CodeableConcept import *
from fhan.models.R4.Identifier import *
from fhan.models.R4.Meta import *
from fhan.models.R4.BackboneElement import *
from fhan.models.R4.Narrative import *
from fhan.models.R4.Money import *
from fhan.models.R4.DomainResource import *


    
    

class Detail(ModelBase):
    """ Distribution of the payment amount for a previously acknowledged payable.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param 'Identifier' identifier: Business identifier of the payment detail
    :param 'Identifier' predecessor: Business identifier of the prior payment detail
    :param 'CodeableConcept' type: Category of payment
    :param 'Reference' request: Request giving rise to the payment
    :param 'Reference' submitter: Submitter of the request
    :param 'Reference' response: Response committing to a payment
    :param str date: Date of commitment to pay
    :param 'Reference' responsible: Contact for the response
    :param 'Reference' payee: Recipient of the payment
    :param 'Money' amount: Amount allocated to this payable
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: 'Identifier' = None,  predecessor: 'Identifier' = None,  type: 'CodeableConcept' = None,  request: 'Reference' = None,  submitter: 'Reference' = None,  response: 'Reference' = None,  date: str = None,  responsible: 'Reference' = None,  payee: 'Reference' = None,  amount: 'Money' = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: 'Identifier' = identifier 
        self.predecessor: 'Identifier' = predecessor 
        self.type: 'CodeableConcept' = type 
        self.request: 'Reference' = request 
        self.submitter: 'Reference' = submitter 
        self.response: 'Reference' = response 
        self.date: str = date 
        self.responsible: 'Reference' = responsible 
        self.payee: 'Reference' = payee 
        self.amount: 'Money' = amount 
        

    
    

class ProcessNote(ModelBase):
    """ A note that describes or explains the processing in a human readable form.:param str id: Unique id for inter-element referencing
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored even if unrecognized
    :param str type: display | print | printoper
    :param str text: Note explanatory text
    """
    def __init__(self,  id: str = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  type: str = None,  text: str = None, ):
        self.id: str = id 
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.type: str = type 
        self.text: str = text 
        

class PaymentReconciliation(DomainResource):
    """ This resource provides the details including amount of a payment and allocates the payment items being paid.
    :param str id: Logical id of this artifact
    :param 'Meta' meta: Metadata about the resource
    :param str implicitRules: A set of rules under which this content was created
    :param str language: Language of the resource content
    :param 'Narrative' text: Text summary of the resource, for human interpretation
    :param list['Resource'] contained: Contained, inline Resources
    :param list['Extension'] extension: Additional content defined by implementations
    :param list['Extension'] modifierExtension: Extensions that cannot be ignored
    :param list['Identifier'] identifier: Business Identifier for a payment reconciliation
    :param str status: active | cancelled | draft | entered-in-error
    :param 'Period' period: Period covered
    :param str created: Creation date
    :param 'Reference' paymentIssuer: Party generating payment
    :param 'Reference' request: Reference to requesting resource
    :param 'Reference' requestor: Responsible practitioner
    :param str outcome: queued | complete | error | partial
    :param str disposition: Disposition message
    :param str paymentDate: When payment issued
    :param 'Money' paymentAmount: Total amount of Payment
    :param 'Identifier' paymentIdentifier: Business identifier for the payment
    :param list['Detail'] detail: Settlement particulars
    :param 'CodeableConcept' formCode: Printed form identifier
    :param list['ProcessNote'] processNote: Note concerning processing
    """
    def __init__(self, resourceType: str = "PaymentReconciliation",  id: str = None,  meta: 'Meta' = None,  implicitRules: str = None,  language: str = None,  text: 'Narrative' = None,  contained: list['Resource'] = None,  extension: list['Extension'] = None,  modifierExtension: list['Extension'] = None,  identifier: list['Identifier'] = None,  status: str = None,  period: 'Period' = None,  created: str = None,  paymentIssuer: 'Reference' = None,  request: 'Reference' = None,  requestor: 'Reference' = None,  outcome: str = None,  disposition: str = None,  paymentDate: str = None,  paymentAmount: 'Money' = None,  paymentIdentifier: 'Identifier' = None,  detail: list['Detail'] = None,  formCode: 'CodeableConcept' = None,  processNote: list['ProcessNote'] = None, ):
        self.resourceType: str = resourceType or "PaymentReconciliation"
        self.id: str = id 
        self.meta: 'Meta' = meta 
        self.implicitRules: str = implicitRules 
        self.language: str = language 
        self.text: 'Narrative' = text 
        self.contained: list['Resource'] = contained or []
        self.extension: list['Extension'] = extension or []
        self.modifierExtension: list['Extension'] = modifierExtension or []
        self.identifier: list['Identifier'] = identifier or []
        self.status: str = status 
        self.period: 'Period' = period 
        self.created: str = created 
        self.paymentIssuer: 'Reference' = paymentIssuer 
        self.request: 'Reference' = request 
        self.requestor: 'Reference' = requestor 
        self.outcome: str = outcome 
        self.disposition: str = disposition 
        self.paymentDate: str = paymentDate 
        self.paymentAmount: 'Money' = paymentAmount 
        self.paymentIdentifier: 'Identifier' = paymentIdentifier 
        self.detail: list['Detail'] = detail or []
        self.formCode: 'CodeableConcept' = formCode 
        self.processNote: list['ProcessNote'] = processNote or []
        